from source.header_game_menus import *
from source.header_items import *
from source.module_constants import *


menus = [
    ("make_prisoners", 0, "{s18}", "none", [

        (call_script, "script_party_count_members_with_full_health", "p_main_party"),
        (assign, ":player_party_size", reg0),
        (call_script, "script_party_count_members_with_full_health", "$current_town"),
        (assign, ":villagers_party_size", reg0),
        (try_begin),
            (lt, ":player_party_size", 50),
            (ge, ":villagers_party_size", 40),
            (neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
            (jump_to_menu, "mnu_village_start_attack"),
        (try_end),

        (party_get_free_prisoners_capacity, ":prisoner_capacity", "p_main_party"),
        (party_get_slot, ":lord", "$current_town", slot_town_lord),

        (call_script, "script_get_max_skill_of_player_party", "skl_looting"),
        (assign, ":looting_lvl", reg0),

        (try_begin),
            (gt, ":prisoner_capacity", 0),

            (party_get_slot, ":mod_troop", "$current_town", slot_center_volunteer_troop_type),
            # todo: make max prisoners depend on village population

            # prisoners = min[U(0, 20) + 2*looting, capacity]
            # where U(0, 20) is a random number between 0 and 20
            (store_random_in_range, ":prisoners", 0, 20),

            (store_mul, ":bonus_loot", ":looting_lvl", 2),
            (store_add, ":prisoners", ":bonus_loot", ":prisoners"),

            (val_min, ":prisoners", ":prisoner_capacity"),

            (try_begin),
                (gt, ":prisoners", 0),
                (assign, reg4, 0),  # 0 -> made prisoners

                # profit = prisoners*[U(1, 10) + looting/2]
                (store_random_in_range, ":random_profit", 1, 10),
                (val_div, ":looting_lvl", 2),
                (store_add, ":random_profit", ":random_profit", ":looting_lvl"),
                (store_mul, ":profit", ":prisoners", ":random_profit"),

                # reputation_change = 5*prisoners - 2*prisoners/persuasion
                # todo: reputation change should decrease with persuasion.
                (party_get_skill_level, ":player_persuasion", "p_main_party", "skl_persuasion"),
                (val_div, ":player_persuasion", 2),

                (store_random_in_range, ":random_replossmut", -1, -5),
                (store_mul, ":reputation_change", ":prisoners", ":random_replossmut"),

                (store_div, ":tempholder", ":prisoners", ":player_persuasion"),
                (val_add, ":reputation_change", ":tempholder"),

                # store stuff to the menu option
                (assign, reg1, ":prisoners"),
                (assign, reg2, ":profit"),
                (assign, reg3, ":reputation_change"),
                (assign, reg12, ":lord"),
                (assign, reg13, ":mod_troop"),

                # store strings
                (str_store_party_name, s2, "$current_town"),
                (store_faction_of_party, ":center_faction", "$current_town"),
                (str_store_faction_name, s9, ":center_faction"),

                (try_begin),
                    (ge, ":lord", 0),
                    (str_store_troop_name, s8, ":lord"),
                    (str_store_troop_name, s9, ":mod_troop"),
                (try_end),

                (str_store_string, s18, "@You will get {reg1} {s9} as prisoners "
                                        "and robb them {reg2} scillingas. "
                                        "It will cost you {reg3} reputation "
                                        "with {s2}. You also lose reputation with "
                                        "{s8}. You will lose honour and "
                                        "reputation with villages."),
            (else_try),
                (str_store_string, s18, "@You didnt manage to capture any prisoners "),
                (assign, reg4, 1),  # 1 -> made no prisoners
            (try_end),
        (else_try),
            (str_store_string, s18, "@You have no free prisoner capacity and thus "
                                    "can not forciable take prisoners "),
            (assign, reg4, 2),  # 2 -> no space for prisoners
        (try_end),
        (set_background_mesh, "mesh_pic_payment1"),
    ], [

        ("no_prisoners_capacity", [
            (eq, reg4, 2),
            ], "You have no free prisoners space.", [
            (jump_to_menu, "mnu_village"),
        ]),

        ("continue_no_prisoners_captured", [
            (eq, reg4, 1),
            ], "You didnt manage to capture any prisoners...", [
            (jump_to_menu,"mnu_village"),
        ]),

        ("capture_prisoners", [
            (eq, reg4, 0),
            ], "Capture Prisoners.", [

            (assign, ":prisoners", reg1),
            (assign, ":profit", reg2),
            (assign, ":reputation_change", reg3),
            (assign, ":lord", reg12),
            (assign, ":mod_troop", reg13),
            (rest_for_hours_interactive, 3, 5, 1),
            (call_script, "script_change_player_relation_with_center", "$current_town", ":reputation_change"),
            (call_script, "script_change_player_relation_with_troop", ":lord", -10),

            (try_for_range, ":center", centers_begin, centers_end),
                (call_script, "script_change_player_relation_with_center", ":center", -2),
            (try_end),

            (call_script, "script_change_player_honor", -13),

            # prisoners and money
            (party_add_prisoners, "p_main_party", ":mod_troop", ":prisoners"),
            (troop_add_gold, "trp_player", ":profit"),

            # todo: some companions should be upset by this action

            (try_begin),
                (store_faction_of_party, ":village_faction", "$current_town"),
                (store_relation, ":relation", "$players_kingdom", ":village_faction"),
                (ge, ":relation", 0),
                (call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$current_town"),
            (try_end),

            (call_script, "script_add_log_entry", logent_village_extorted, "trp_player",  "$current_town", ":lord", "$g_encountered_party_faction"),
            (party_set_slot, "$current_town", slot_village_raided_by, -1),
            (change_screen_return),
        ]),

        ("forget_it", [
            (eq, reg4, 0),
            ], "Forget it.", [
            (jump_to_menu,"mnu_village"),
        ]),
    ]),
]
