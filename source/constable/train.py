from source.header_operations import *
from source.header_common import *

from source.header_dialogs import *
from source.header_skills import skl_trainer

from source.module_constants import walled_centers_begin, walled_centers_end, \
    slot_party_type, spt_town, spt_castle, slot_town_lord


dialog_option = \
    [anyone | plyr, "dplmc_constable_recruits_and_training", [
        (neg | is_between, "$g_constable_training_center", walled_centers_begin, walled_centers_end),
        ], "I require soldiers to be trained.", "dplmc_constable_train_ask", []
    ]

dialogs = [

    [anyone, "dplmc_constable_train_ask", [],
     "Of course, where should I train them?", "dplmc_constable_train_select", []
    ],

    [anyone | plyr | repeat_for_parties, "dplmc_constable_train_select", [
        (store_repeat_object, ":party_no"),
        (this_or_next | party_slot_eq, ":party_no", slot_party_type, spt_town),
        (party_slot_eq, ":party_no", slot_party_type, spt_castle),
        (party_slot_eq, ":party_no", slot_town_lord, "trp_player"),
        (str_store_party_name, s11, ":party_no"),
        ], "{!}{s11}.", "dplmc_constable_train_type_ask", [
        (store_repeat_object, "$diplomacy_var"),
    ]],

    # todo: allow to choose unit type instead of branch number
    [anyone, "dplmc_constable_train_type_ask", [
        (str_store_party_name, s11, "$diplomacy_var"),
        ], "Do you prefer the alternate promotion, if there is one?", "dplmc_constable_train_type", []
    ],

    [anyone | plyr, "dplmc_constable_train_type", [],
     "No.", "dplmc_constable_train_improved_ask", [
         (assign, "$g_constable_training_type", 0)
    ]],

    [anyone | plyr, "dplmc_constable_train_type", [],
     "Ranged and Cavalry.", "dplmc_constable_train_improved_ask", [
         (assign, "$g_constable_training_type", 1)
    ]],

    [anyone, "dplmc_constable_train_improved_ask", [],
     "If you want I can hire additional trainers so we can train the recruits "
     "faster. This will cost 10% more, but train the troops 50% faster.", "dplmc_constable_train_improved", []
    ],

    [anyone | plyr, "dplmc_constable_train_improved", [],
     "Yes, very well, hire additional trainers.", "dplmc_constable_train_center", [
         (assign, "$g_constable_training_improved", 1)
    ]],

    [anyone | plyr, "dplmc_constable_train_improved", [],
     "No, you have to train them alone.", "dplmc_constable_train_center", [
         (assign, "$g_constable_training_improved", 0)
    ]],

    [anyone, "dplmc_constable_train_center", [
        (str_store_party_name, s11, "$diplomacy_var"),
        (try_begin),
            (eq, "$g_constable_training_type", 0),
            (str_store_string, s12, "@You are preferring melee units."),
        (else_try),
            (str_store_string, s12, "@You are preferring ranged and cavalry units."),
        (try_end),

        (str_clear, s13),
        (try_begin),
            (eq, "$g_constable_training_improved", 1),
            (str_store_string, s13, "@ and the additional trainers"),
        (try_end),
        ], "Alright, I will train the recruits in {s11}. {s12} Please, make sure we "
           "have enough money in the treasury to pay the equipment{s13}. "
           "Make sure to place the troops you prefer to have trained at the bottom of "
           "the garrison list.", "dplmc_constable_pretalk", [
        (assign, "$g_constable_training_center", "$diplomacy_var")
    ]],

    [anyone | plyr, "dplmc_constable_train_select", [],
     "I changed my mind, maybe you shouldn't train them.", "dplmc_constable_pretalk", []
    ],

    [anyone | plyr, "dplmc_constable_recruits_and_training", [
        (is_between, "$g_constable_training_center", walled_centers_begin, walled_centers_end),
        (str_store_party_name, s11, "$g_constable_training_center"),
        ], "Please stop training the recruits in {s11}.", "dplmc_constable_train_stop", []
    ],

    [anyone, "dplmc_constable_train_stop", [
        (is_between, "$g_constable_training_center", walled_centers_begin, walled_centers_end),
        ], "As you wish.", "dplmc_constable_pretalk", [
        (assign, "$g_constable_training_center", -1)
    ]],
]


simple_triggers = [

    (24, [
        (eq, "$g_player_constable", "trp_dplmc_constable"),
        (is_between, "$g_constable_training_center", walled_centers_begin, walled_centers_end),
        (party_slot_eq, "$g_constable_training_center", slot_town_lord, "trp_player"),

        # Base of 100 + 10 per level of the player's base trainer skill, max of 200 points at 10 skill.
        (store_skill_level, ":training_points", skl_trainer, "trp_player"),
        (val_mul, ":training_points", 10),
        (val_add, ":training_points", 100),

        # 50% extra training points if you are using improved training.
        (try_begin),
            (eq, "$g_constable_training_improved", 1),
            (val_mul, ":training_points", 3),
            (val_div, ":training_points", 2),
        (try_end),

        (party_get_num_companion_stacks, ":num_stacks", "$g_constable_training_center"),

        (assign, ":trained", 0),
        (try_for_range, ":i_stack", 0, ":num_stacks"),
            (eq, ":trained", 0),
            (party_stack_get_troop_id, ":troop_id", "$g_constable_training_center", ":i_stack"),
            (neg | troop_is_hero, ":troop_id"),

            (troop_get_upgrade_troop, ":upgrade_troop", ":troop_id" , "$g_constable_training_type"),
            (try_begin),
                (le, ":upgrade_troop", 0),
                (troop_get_upgrade_troop, ":upgrade_troop", ":troop_id", 0),
            (try_end),

            # proceed if troop is upgradable
            (gt, ":upgrade_troop", 0),

            # tiers cost different amount of points to train.
            (store_character_level, ":troop_level", ":troop_id"),
            (assign, ":point_cost", 0),
            (try_begin),
                (is_between, ":troop_level", 0, 16),
                (assign, ":point_cost", 10),  # 10-30
            (else_try),
                (is_between, ":troop_level", 16, 20),
                (assign, ":point_cost", 12),  # 8-25
            (else_try),
                (is_between, ":troop_level", 20, 24),
                (assign, ":point_cost", 20),  # 5-15
            (else_try),
                (is_between, ":troop_level", 24, 30),
                (assign, ":point_cost", 50),  # 2-6
                (try_begin),
                    (eq, "$g_realism_upgrade", 0),
                    (assign, ":point_cost", 75),
                (try_end),
            (else_try),
                # for anything else
                (assign, ":point_cost", 100),
            (try_end),

            (store_div, ":num_trained", ":training_points", ":point_cost"),

            (party_count_members_of_type, ":cur_number", "$g_constable_training_center", ":troop_id"),
            (val_min, ":num_trained", ":cur_number"),

            (call_script, "script_game_get_upgrade_cost", ":troop_id"),
            (assign, ":upgrade_cost", reg0),

            # +10% cost if using improved training.
            (try_begin),
                (eq, "$g_constable_training_improved", 1),
                (val_mul, ":upgrade_cost", 11),
                (val_div, ":upgrade_cost", 10),
            (try_end),

            (store_mul, ":total_upgrade_cost", ":num_trained", ":upgrade_cost"),

            (store_troop_gold, ":gold", "trp_household_possessions"),
            (try_begin),
                (lt, ":gold", ":total_upgrade_cost"),
                (store_div, ":money_limit", ":gold", ":upgrade_cost"),
                (val_min, ":num_trained", ":money_limit"),
                (store_mul, ":total_upgrade_cost", ":num_trained", ":upgrade_cost"),
                (display_message, "@Not enough money in treasury to upgrade troops."),
            (try_end),

            # upgrade troops
            (party_remove_members, "$g_constable_training_center", ":troop_id", ":num_trained"),
            (party_add_members, "$g_constable_training_center", ":upgrade_troop", ":num_trained"),

            # remove money
            (call_script, "script_dplmc_withdraw_from_treasury", ":total_upgrade_cost"),

            (assign, reg5, ":num_trained"),
            (str_store_troop_name, s6, ":troop_id"),
            (str_store_troop_name, s7, ":upgrade_troop"),
            (str_store_party_name, s8, "$g_constable_training_center"),
            (display_message, "@Your constable upgraded {reg5} {s6} to {s7} in {s8}"),

            # todo: constable only upgrades one stack, even if it has points for more than one. Fix it.
            (assign, ":trained", 1),
        (try_end),
    ]),
]
