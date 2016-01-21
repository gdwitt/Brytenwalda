from source.header_game_menus import *
from source.header_items import *
from source.module_constants import *


menus = [

    ("village_start_attack", mnf_disable_all_keys | mnf_scale_picture,
     "Some of the angry villagers grab their tools and prepare to resist you. "
     "It looks like you'll have a fight on your hands if you continue.", "none", [

        (set_background_mesh, "mesh_pic_villageriot"),
        (call_script, "script_party_count_members_with_full_health", "p_main_party"),
        (assign, ":player_party_size", reg0),
        (call_script, "script_party_count_members_with_full_health", "$current_town"),
        (assign, ":villagers_party_size", reg0),

        (try_begin),
            (store_random_in_range, ":random_no", 55, 120),
            (gt, ":player_party_size", ":random_no"),
            (jump_to_menu, "mnu_village_loot_no_resist"),
        (else_try),
            (this_or_next | eq, ":villagers_party_size", 0),
            (eq, "$g_battle_result", 1),
            (try_begin),
                (eq, "$g_battle_result", 1),
                (store_random_in_range, ":enmity", -30, -15),
                (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
                (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
                (gt, ":town_lord", 0),
                (call_script, "script_change_player_relation_with_troop", ":town_lord", -15),
                (store_faction_of_party, ":faction_no", "$current_town"),
                (call_script, "script_change_player_relation_with_faction", ":faction_no", -20),
                (call_script, "script_change_player_relation_with_faction", "fac_commoners", -3),
            (try_end),
            (jump_to_menu, "mnu_village_loot_no_resist"),
        (else_try),
            (eq, "$g_battle_result", -1),
            (jump_to_menu, "mnu_village_loot_defeat"),
        (try_end),
        ], [

        ("village_raid_attack", [], "Charge them.", [

            (store_random_in_range, ":enmity", -15, -10),
            (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
            (try_begin),
                (party_get_slot, ":town_lord", "$current_town", slot_town_lord),
                (gt, ":town_lord", 0),
                (call_script, "script_change_player_relation_with_troop", ":town_lord", -15),
                (store_faction_of_party, ":faction_no", "$current_town"),
                (call_script, "script_change_player_relation_with_faction", ":faction_no", -20),
                (call_script, "script_change_player_relation_with_faction", "fac_commoners", -3),
            (try_end),

            (call_script, "script_calculate_battle_advantage"),
            (set_battle_advantage, reg0),
            (set_party_battle_mode),
            (assign, "$g_battle_result", 0),
            (assign, "$g_village_raid_evil", 1),
            (set_jump_mission, "mt_village_raid"),
            (party_get_slot, ":scene_to_use", "$current_town", slot_castle_exterior),
            (jump_to_scene, ":scene_to_use"),
            (assign, "$g_next_menu", "mnu_village_start_attack"),

            (call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$g_encountered_party"),
            (call_script, "script_objectionable_action", tmt_humanitarian, "str_loot_village"),

            (jump_to_menu, "mnu_battle_debrief"),
            (change_screen_mission),
        ]),

        ("village_raid_leave", [], "Leave this village alone.",
            [(change_screen_return)]),
     ]),


    ("village_loot_no_resist", 0,
     "The villagers here are few and frightened, and they quickly scatter and "
     "run before you. The village is at your mercy.", "none", [], [

        ("village_loot", [], "Plunder the village, then raze it.", [
            (call_script, "script_village_set_state", "$current_town", svs_being_raided),
            (party_set_slot, "$current_town", slot_village_raided_by, "p_main_party"),
            (assign, "$g_player_raiding_village", "$current_town"),

            (try_begin),
                (store_faction_of_party, ":village_faction", "$current_town"),
                (store_relation, ":relation", "$players_kingdom", ":village_faction"),
                (ge, ":relation", 0),
                (call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$current_town"),
            (try_end),
            (rest_for_hours_interactive, 1, 5, 1),
            (change_screen_return),
        ]),

        ("village_raid_leave", [], "Leave this village alone." , [(change_screen_return)]),
    ]),

    ("village_loot_complete", mnf_disable_all_keys,
     "On your orders your troops sack the village, pillaging everything of "
     "any value, and then put the buildings to the torch. From the coins and "
     "valuables that are found, you get your share of {reg1} scillingas.", "none", [

        (try_begin),
            (get_achievement_stat, ":number_of_village_raids", ACHIEVEMENT_THE_BANDIT, 0),
            (get_achievement_stat, ":number_of_caravan_raids", ACHIEVEMENT_THE_BANDIT, 1),
            (val_add, ":number_of_village_raids", 1),
            (set_achievement_stat, ACHIEVEMENT_THE_BANDIT, 0, ":number_of_village_raids"),

            (ge, ":number_of_village_raids", 3),
            (ge, ":number_of_caravan_raids", 3),
            (unlock_achievement, ACHIEVEMENT_THE_BANDIT),
        (try_end),

        (party_get_slot, ":village_lord", "$current_town", slot_town_lord),
        (try_begin),
            (gt,  ":village_lord", 0),
            (call_script, "script_change_player_relation_with_troop", ":village_lord", -5),
        (try_end),

        (store_random_in_range, ":enmity", -35, -25),
        (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
        (call_script, "script_change_player_relation_with_faction", "fac_commoners", -3),

        (store_faction_of_party, ":village_faction", "$current_town"),
        (store_relation, ":relation", ":village_faction", "fac_player_supporters_faction"),
        (try_begin),
            (lt, ":relation", 0),
            (call_script, "script_change_player_relation_with_faction", ":village_faction", -3),
        (try_end),

        # money_gained = 50 + 5*prosperity
        (assign, ":money_gained", 50),
        (party_get_slot, ":prosperity", "$current_town", slot_town_prosperity),
        (store_mul, ":prosperity_of_village_mul_5", ":prosperity", 5),
        (val_add, ":money_gained", ":prosperity_of_village_mul_5"),
        (call_script, "script_troop_add_gold", "trp_player", ":money_gained"),

        (assign, ":morale_increase", 3),
        (store_div, ":money_gained_div_100", ":money_gained", 100),
        (val_add, ":morale_increase", ":money_gained_div_100"),
        (call_script, "script_change_player_party_morale", ":morale_increase"),

        (faction_get_slot, ":faction_morale", ":village_faction", slot_faction_morale_of_player_troops),
        (store_mul, ":morale_increase_mul_2", ":morale_increase", 200),
        (val_sub, ":faction_morale", ":morale_increase_mul_2"),
        (faction_set_slot, ":village_faction",  slot_faction_morale_of_player_troops, ":faction_morale"),

        (call_script, "script_objectionable_action", tmt_humanitarian, "str_loot_village"),

        (assign, reg1, ":money_gained"),
      ], [
        ("continue", [], "Continue...", [
            (jump_to_menu, "mnu_close"),

            # steal cattle
            (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
            (assign, ":max_value", reg0),
            # +1 so random_in_range below includes the max value.
            (val_add, ":max_value", 1),

            (store_random_in_range, ":heads_stolen", 0, ":max_value"),
            (try_begin),
                (gt, ":heads_stolen", 0),

                # add cattle to map
                (call_script, "script_create_cattle_herd1", "$current_town", ":heads_stolen"),

                # remove cattle from village
                (party_get_slot, ":num_cattle", "$current_town", slot_village_number_of_cattle),
                (val_sub, ":num_cattle", ":heads_stolen"),
                (party_set_slot, "$current_town", slot_village_number_of_cattle, ":num_cattle"),
            (try_end),

            (call_script, "script_set_merchandise_after_village_loot", "$current_town", "trp_temp_troop"),
            (change_screen_loot, "trp_temp_troop"),
        ]),
    ]),

    ("village_loot_defeat", mnf_scale_picture,
     "Fighting with courage and determination, the villagers manage to hold "
     "together and drive off your forces.", "none", [
        (set_background_mesh, "mesh_pic_villageriot"),
     ], [
      ("continue", [], "Continue...", [(change_screen_return)]),
    ]),

    ("village_loot_continue", 0,
     "Do you wish to continue looting this village?", "none", [], [

        ("disembark_yes", [], "Yes.", [
            (rest_for_hours_interactive, 3, 5, 1),
            (change_screen_return),
        ]),

        ("yono_no", [], "No.", [
            (call_script, "script_village_set_state", "$current_town", 0),
            (party_set_slot, "$current_town", slot_village_raided_by, -1),
            (assign, "$g_player_raiding_village", 0),
            (change_screen_return),
        ]),
    ]),
]


scripts = [
    ("set_merchandise_after_village_loot", [
        (store_script_param, ":village", 1),
        (store_script_param, ":troop_for_merchandise", 2),

        # Select items produced in bound town to be stolen.
        (party_get_slot, ":bound_town", ":village", slot_village_bound_center),
        (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
        (reset_item_probabilities, 100),

        (assign, ":total_probability", 0),
        (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
            (store_add, ":cur_price_slot", ":cur_goods", ":item_to_price_slot"),
            (party_get_slot, ":cur_price", ":bound_town", ":cur_price_slot"),
            (gt, ":cur_price", 0),

            # cur_prob = 4*(prod + consump/3)*average_price_factor/item_price
            (call_script, "script_center_get_production", ":bound_town", ":cur_goods"),
            (assign, ":cur_probability", reg0),
            (call_script, "script_center_get_consumption", ":bound_town", ":cur_goods"),
            (val_div, reg0, 3),
            (val_add, ":cur_probability", reg0),
            (val_mul, ":cur_probability", 4),
            (val_mul, ":cur_probability", average_price_factor),
            (val_div, ":cur_probability", ":cur_price"),

            (val_add, ":total_probability", ":cur_probability"),
        (try_end),

        (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
            (store_add, ":cur_price_slot", ":cur_goods", ":item_to_price_slot"),
            (party_get_slot, ":cur_price", ":bound_town", ":cur_price_slot"),
            (gt, ":cur_price", 0),

            # cur_prob = 4*(prod + consump/3)*average_price_factor/item_price
            (call_script, "script_center_get_production", ":bound_town", ":cur_goods"),
            (assign, ":cur_probability", reg0),
            (call_script, "script_center_get_consumption", ":bound_town", ":cur_goods"),
            (val_div, reg0, 3),
            (val_add, ":cur_probability", reg0),
            (gt, ":cur_probability", 0),  # todo: why this line is here but not above?
            (val_mul, ":cur_probability", 4),
            (val_mul, ":cur_probability", average_price_factor),
            (val_div, ":cur_probability", ":cur_price"),

            # compute relative to the total probability computed above
            (val_div, ":cur_probability", ":total_probability"),

            # ":cur_probability" is per slot; we want total probability
            (val_mul, ":cur_probability", num_merchandise_goods),

            # probabilities must be percentages
            (val_mul, ":cur_probability", 100),
            (set_item_probability_in_merchandise, ":cur_goods", ":cur_probability"),
        (try_end),

        (troop_clear_inventory, ":troop_for_merchandise"),
        # todo: above uses 40 (num_merchandise_goods), but this uses 30.
        (troop_add_merchandise, ":troop_for_merchandise", itp_type_goods, 30),
        (troop_sort_inventory, ":troop_for_merchandise"),
    ])
]
