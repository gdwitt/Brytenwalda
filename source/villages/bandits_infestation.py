from source.header_operations import *
from source.header_common import *

from source.header_game_menus import mnf_disable_all_keys

from source.header_items import num_equipment_kinds, max_inventory_items

from source.module_constants import slot_village_infested_by_bandits, \
    slot_village_raid_progress, slot_village_recover_progress, slot_quest_target_center, \
    slot_town_elder, svs_looted


menus = [
    ("village_infest_bandits_result", 0, "{s9}", "none", [
        (try_begin),
            (eq, "$g_battle_result", 1),
            (jump_to_menu, "mnu_village_infestation_removed"),
        (else_try),
            (str_store_string, s9, "@Try as you might, you could not defeat "
                                   "the bandits. Infuriated, they raze the "
                                   "village to the ground to punish the peasants, "
                                   "and then leave the burning wasteland behind "
                                   "to find greener pastures to plunder."),
            (set_background_mesh, "mesh_pic_looted_village1"),
        (try_end),
        ], [
        ("continue",[],"Continue...", [
            (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
            (call_script, "script_village_set_state",  "$current_town", svs_looted),
            (party_set_slot, "$current_town", slot_village_raid_progress, 0),
            (party_set_slot, "$current_town", slot_village_recover_progress, 0),
            (try_begin),
                (check_quest_active, "qst_eliminate_bandits_infesting_village"),
                (quest_slot_eq, "qst_eliminate_bandits_infesting_village", slot_quest_target_center, "$g_encountered_party"),
                (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -10),
                (call_script, "script_fail_quest", "qst_eliminate_bandits_infesting_village"),
                (call_script, "script_end_quest", "qst_eliminate_bandits_infesting_village"),
            (else_try),
                (check_quest_active, "qst_deal_with_bandits_at_lords_village"),
                (quest_slot_eq, "qst_deal_with_bandits_at_lords_village", slot_quest_target_center, "$g_encountered_party"),
                (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -8), #chief cambiado
                (call_script, "script_fail_quest", "qst_deal_with_bandits_at_lords_village"),
                (call_script, "script_end_quest", "qst_deal_with_bandits_at_lords_village"),
            (else_try),
                (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -6), #chief cambiado
            (try_end),
            (jump_to_menu, "mnu_village")
        ]),
    ]),

    ("village_infestation_removed", mnf_disable_all_keys,
     "In a battle worthy of song, you and your men drive the bandits out of the "
     "village, making it safe once more. The villagers have little left in the "
     "way of wealth after their ordeal, but they offer you all they can find.", "none", [

        (party_get_slot, ":bandit_troop", "$g_encountered_party", slot_village_infested_by_bandits),
        (party_set_slot, "$g_encountered_party", slot_village_infested_by_bandits, 0),
        (party_clear, "p_temp_party"),
        (party_add_members, "p_temp_party", ":bandit_troop", "$qst_eliminate_bandits_infesting_village_num_bandits"),
        (assign, "$g_strength_contribution_of_player", 50),
        (call_script, "script_party_give_xp_and_gold", "p_temp_party"),
        (try_begin),
            (check_quest_active, "qst_eliminate_bandits_infesting_village"),
            (quest_slot_eq, "qst_eliminate_bandits_infesting_village", slot_quest_target_center, "$g_encountered_party"),
            (call_script, "script_end_quest", "qst_eliminate_bandits_infesting_village"),
            # Add quest reward
            (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 6),
            (call_script, "script_change_player_relation_with_faction", "fac_commoners", 5),
        (else_try),
            (check_quest_active, "qst_deal_with_bandits_at_lords_village"),
            (quest_slot_eq, "qst_deal_with_bandits_at_lords_village", slot_quest_target_center, "$g_encountered_party"),
            (call_script, "script_succeed_quest", "qst_deal_with_bandits_at_lords_village"),
            (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 6),
            (call_script, "script_change_player_relation_with_faction", "fac_commoners", 4),
        (else_try),
            # Add normal reward
            (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 6),
            (call_script, "script_change_player_relation_with_faction", "fac_commoners", 5),
        (try_end),

        (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
        (try_for_range, ":slot_no", num_equipment_kinds, max_inventory_items + num_equipment_kinds),
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", 70),
            (troop_set_inventory_slot, ":merchant_troop", ":slot_no", -1),
        (try_end),
        ], [

        ("village_bandits_defeated_accept", [], "Take it as your just due.", [
            (jump_to_menu, "mnu_village"),
            (party_get_slot, ":merchant_troop", "$current_town", slot_town_elder),
            (troop_sort_inventory, ":merchant_troop"),
            (change_screen_loot, ":merchant_troop"),
        ]),

        ("village_bandits_defeated_cont", [], "Refuse, stating that they need these items more than you do.", [
            (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
            (call_script, "script_change_player_honor", 1),
            (jump_to_menu, "mnu_village")
        ]),
    ]),
]
