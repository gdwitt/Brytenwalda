from source.header_operations import *
from source.header_common import *

from source.header_items import max_inventory_items, num_equipment_kinds

from source.module_constants import slot_town_lord, slot_center_player_relation, \
    slot_town_elder, tmt_humanitarian, logent_village_extorted


menus = [
    ("village_take_food_confirm", 0,
     "It will be difficult to force and threaten the peasants into giving their "
     "precious supplies. You think you will need at least one hour.", "none", [], [

        ("village_take_food_confirm", [], "Go ahead.", [
            (rest_for_hours_interactive, 1, 5, 0), #rest while not attackable
            (assign, "$auto_enter_town", "$current_town"),
            (assign, "$g_town_visit_after_rest", 1),
            (assign, "$auto_enter_menu_in_center", "mnu_village_take_food"),
            (change_screen_return),
        ]),

        ("forget_it", [], "Forget it.", [
            (jump_to_menu, "mnu_village_hostile_action")
        ]),
    ]),

    ("village_take_food", 0,
     "The villagers grudgingly bring out what they have for you.", "none", [

        # possibility of an attack
        (call_script, "script_party_count_members_with_full_health","p_main_party"),
        (assign, ":player_party_size", reg0),
        (call_script, "script_party_count_members_with_full_health","$current_town"),
        (assign, ":villagers_party_size", reg0),
        (try_begin),
            (lt, ":player_party_size", 20),
            (ge, ":villagers_party_size", 40),
            (neg|party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
            (jump_to_menu, "mnu_village_start_attack"),
        (try_end),
        ], [

        ("take_supplies", [], "Take the supplies.", [
            (try_begin),
                (party_slot_ge, "$current_town", slot_center_player_relation, -55),
                (store_faction_of_party, ":faction_no", "$current_town"),
                (try_begin),
                    (party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
                    (call_script, "script_change_player_relation_with_center", "$current_town", -5),
                    (call_script, "script_change_player_relation_with_faction", ":faction_no", -20),
                (else_try),
                    (call_script, "script_change_player_relation_with_center", "$current_town", -10),
                    (call_script, "script_change_player_relation_with_faction", ":faction_no", -20),
                (try_end),
            (try_end),

            (try_begin),
                (party_get_slot, ":village_lord", "$current_town", slot_town_lord),
                (gt, ":village_lord", 1),
                (call_script, "script_change_player_relation_with_troop", ":village_lord", -15),
            (try_end),

            (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
            (party_get_skill_level, ":player_party_looting", "p_main_party", "skl_looting"),

            (val_mul, ":player_party_looting", 3),
            (store_sub, ":random_chance", 70, ":player_party_looting"),

            # Increases the chance of looting by 3% per skill level
            (try_for_range, ":slot_no", num_equipment_kinds, max_inventory_items + num_equipment_kinds),
                (store_random_in_range, ":rand", 0, 100),
                (lt, ":rand", ":random_chance"),
                (troop_set_inventory_slot, ":merchant_troop", ":slot_no", -1),
            (try_end),

            (call_script, "script_objectionable_action", tmt_humanitarian, "str_steal_from_villagers"),

            (call_script, "script_add_log_entry", logent_village_extorted, "trp_player",  "$current_town", -1, -1),
            (store_faction_of_party,":village_faction",  "$current_town"),
            (call_script, "script_faction_inflict_war_damage_on_faction", "$players_kingdom", ":village_faction", 5),

            (jump_to_menu, "mnu_village"),
            (troop_sort_inventory, ":merchant_troop"),
            (change_screen_loot, ":merchant_troop"),
        ]),

        ("let_them_keep_it_2", [], "Let them keep it.", [
            (jump_to_menu, "mnu_village")
        ]),
    ]),
]
