from source.header_operations import *
from source.header_common import *

from source.header_game_menus import mnf_disable_all_keys

from source.module_constants import logent_player_stole_cattles_from_village, ACHIEVEMENT_GOT_MILK, \
    slot_village_number_of_cattle, slot_town_lord, slot_village_player_can_not_steal_cattle


menus = [

    ("village_steal_cattle_confirm", 0,
     "As the party member with the highest looting skill ({reg2}), {reg3?you "
     "reckon:{s1} reckons} that you can steal as many as {reg4} heads of "
     "village's cattle.", "none", [

        (call_script, "script_get_max_skill_of_player_party", "skl_looting"),
        (assign, reg2, reg0),
        (assign, ":max_skill_owner", reg1),
        (try_begin),
            (eq, ":max_skill_owner", "trp_player"),
            (assign, reg3, 1),
        (else_try),
            (assign, reg3, 0),
            (str_store_troop_name, s1, ":max_skill_owner"),
        (try_end),

        (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
        (assign, reg4, reg0),
      ], [

      ("village_steal_cattle_confirm", [], "Go on.", [
         (rest_for_hours_interactive, 3, 5, 1),
         (assign, "$auto_menu", "mnu_village_steal_cattle"),
         (change_screen_return),
       ]),

      ("forget_it", [], "Forget it.", [(change_screen_return)]),
    ]),

    ("village_steal_cattle", mnf_disable_all_keys, "{s1}", "none", [
        (store_faction_of_party, ":faction_no", "$current_town"),

        (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
        (assign, ":max_value", reg0),
        # +1 so random_in_range below includes the max value.
        (val_add, ":max_value", 1),

        (store_random_in_range, ":heads_stolen", 0, ":max_value"),

        # avoids the player repeating this action every second
        (party_set_slot, "$current_town", slot_village_player_can_not_steal_cattle, 1),

        (try_begin),
            (le, ":heads_stolen", 0),
            (call_script, "script_change_player_relation_with_center", "$current_town", -20),
            (call_script, "script_change_player_relation_with_faction", ":faction_no", -10),
            (str_store_string, s1, "@You fail to steal any cattle."),
        (else_try),
            (assign, reg17, ":heads_stolen"),
            (store_sub, reg12, ":heads_stolen", 1),

            (try_begin),
                (party_get_slot, ":lord", "$current_town", slot_town_lord),
                (gt, ":lord", 0),
                (call_script, "script_change_player_relation_with_troop", ":lord", -25),
                (call_script, "script_add_log_entry", logent_player_stole_cattles_from_village, "trp_player",  "$current_town", ":lord", "$g_encountered_party_faction"),
            (try_end),

            (call_script, "script_change_player_relation_with_center", "$current_town", -40),
            (call_script, "script_change_player_relation_with_faction" ,":faction_no", -20),
            (call_script, "script_change_player_honor", -5),

            (str_store_string, s1, "@You drive away {reg17} {reg12?heads:head} of cattle from the village's herd."),

            (try_begin),
                (ge, ":heads_stolen", 3),
                (unlock_achievement, ACHIEVEMENT_GOT_MILK),
            (try_end),

            # add cattle to map
            (call_script, "script_create_cattle_herd1", "$current_town", ":heads_stolen"),

            # remove cattle from village
            (party_get_slot, ":num_cattle", "$current_town", slot_village_number_of_cattle),
            (val_sub, ":num_cattle", ":heads_stolen"),
            (party_set_slot, "$current_town", slot_village_number_of_cattle, ":num_cattle"),
        (try_end),
        ], [
        ("continue", [], "Continue...", [(change_screen_return)])
    ]),
]

scripts = [

    # Input: arg1 = village_no
    # Output: reg0 = amount
    # amount = min[total_cattle, 2*looting + (1 + men_fit/10)]
    ("calculate_amount_of_cattle_can_be_stolen", [
        (store_script_param, ":village_no", 1),

        (call_script, "script_get_max_skill_of_player_party", "skl_looting"),
        (assign, ":max_skill", reg0),
        (store_mul, ":can_steal", ":max_skill", 2),

        (call_script, "script_party_count_fit_for_battle", "p_main_party"),

        (store_add, ":num_men_effect", reg0, 10),
        (val_div, ":num_men_effect", 10),
        (val_add, ":can_steal", ":num_men_effect"),
        (party_get_slot, ":num_cattle", ":village_no", slot_village_number_of_cattle),
        (val_min, ":can_steal", ":num_cattle"),

        (assign, reg0, ":can_steal"),
    ]),
]
