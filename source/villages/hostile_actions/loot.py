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
            (call_script, "script_village_set_state", "$current_town", svs_normal),
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
    ]),
]


simple_triggers = [
    # This trigger will check if player's raid has been completed and will
    # lead control to village menu.
    (1, [
        (ge, "$g_player_raiding_village", 1),
        (try_begin),
            (neq, "$g_player_is_captive", 0),
            (assign, "$g_player_raiding_village", 0),
        (else_try),
            (map_free),  # we have been attacked during raid
            (assign, "$g_player_raiding_village", 0),
        (else_try),
            # continue raiding
            (this_or_next | party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_looted),
            (party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_deserted),
            (start_encounter, "$g_player_raiding_village"),
            (rest_for_hours, 0),
            (assign, "$g_player_raiding_village", 0),
            (assign, "$g_player_raid_complete", 1),
        (else_try),
            # continue raiding
            (party_slot_eq, "$g_player_raiding_village", slot_village_state, svs_being_raided),
            (rest_for_hours, 3, 5, 1),  # rest while attackable
        (else_try),
            (rest_for_hours, 0, 0, 0),  # stop resting - abort
            (assign, "$g_player_raiding_village", 0),
            (assign, "$g_player_raid_complete", 0),
        (try_end),
    ]),

    # Tests if player is too far from the village that the raid stops
    # at more than half a distance, a game menu opens asking if the player wants to continue it.
    # ref: http://forums.taleworlds.com/index.php/topic,148290.msg3568597.html#msg3568597
    (0.25, [
        (ge, "$g_player_raiding_village", 1),
        (store_distance_to_party_from_party, ":distance", "$g_player_raiding_village", "p_main_party"),
        (try_begin),
            (gt, ":distance", raid_distance),
            (str_store_party_name_link, s1, "$g_player_raiding_village"),
            (display_message, "@You have broken off your raid of {s1}."),
            (call_script, "script_village_set_state", "$current_town", svs_normal),
            (party_set_slot, "$current_town", slot_village_raided_by, -1),
            (assign, "$g_player_raiding_village", 0),
            (rest_for_hours, 0, 0, 0),  # stop resting - abort
        (else_try),
            (ge, ":distance", raid_distance / 2),
            (map_free),
            (jump_to_menu, "mnu_village_loot_continue"),
        (try_end),
    ]),

    # Process village raids
    (2, [
        (try_for_range, ":village_no", villages_begin, villages_end),

            # get icons for
            # :normal_village_icon
            # :burnt_village_icon
            # :deserted_village
            (try_begin),
                (this_or_next|is_between, ":village_no", "p_village_61", "p_village_62"), #Shapeshte through Shulus (up to Ilvia)
                (this_or_next|is_between, ":village_no", "p_village_69", "p_village_72"), #Tismirr and Karindi
                (this_or_next|eq, ":village_no", "p_village_82"), #Bhulaban
                (this_or_next|eq, ":village_no", "p_village_138"),
                (this_or_next|eq, ":village_no", "p_village_92"),
                (this_or_next|eq, ":village_no", "p_village_96"),
                (this_or_next|is_between, ":village_no", "p_village_104", "p_village_108"), #Tismirr and Karindi
                (is_between, ":village_no", "p_village_166", "p_village_212"),
                (assign, ":normal_village_icon", "icon_kolba_village"),
                (assign, ":burnt_village_icon", "icon_village_burnt_a"),
                (assign, ":deserted_village_icon", "icon_village_deserted_b"),
            (else_try),
                (assign, ":normal_village_icon", "icon_village_a"),
                (assign, ":burnt_village_icon", "icon_village_burnt_a"),
                (assign, ":deserted_village_icon", "icon_village_deserted_b"),
            (try_end),

            (party_get_slot, ":village_raid_progress", ":village_no", slot_village_raid_progress),

            (try_begin),
                # village is normal
                (party_slot_eq, ":village_no", slot_village_state, svs_normal),
                (val_sub, ":village_raid_progress", 5),
                (val_max, ":village_raid_progress", 0),
                (party_set_slot, ":village_no", slot_village_raid_progress, ":village_raid_progress"),
                (try_begin),
                    (lt, ":village_raid_progress", 50),

                    (try_begin),
                        (party_get_icon, ":village_icon", ":village_no"),
                        (neq, ":village_icon", ":normal_village_icon"),
                        (party_set_icon, ":village_no", ":normal_village_icon"),
                    (try_end),

                    (party_slot_ge, ":village_no", slot_village_smoke_added, 1),
                    (party_set_slot, ":village_no", slot_village_smoke_added, 0),
                    (party_clear_particle_systems, ":village_no"),
                (try_end),
            (else_try),
                # village is being raided
                (party_slot_eq, ":village_no", slot_village_state, svs_being_raided),
                # end raid unless there is an enemy party nearby
                (assign, ":raid_ended", 1),
                (party_get_slot, ":raider_party", ":village_no", slot_village_raided_by),

                (try_begin),
                    (ge, ":raider_party", 0),
                    (party_is_active, ":raider_party"),
                    (this_or_next|neq, ":raider_party", "p_main_party"),
                    (eq, "$g_player_is_captive", 0),
                    (store_distance_to_party_from_party, ":distance", ":village_no", ":raider_party"),
                    (lt, ":distance", raid_distance),
                    (assign, ":raid_ended", 0),
                (try_end),

                (try_begin),
                    (eq, ":raid_ended", 1),
                    (call_script, "script_village_set_state", ":village_no", svs_normal), #clear raid flag
                    (party_set_slot, ":village_no", slot_village_smoke_added, 0),
                    (party_clear_particle_systems, ":village_no"),
                (else_try),
                    (assign, ":raid_progress_increase", 11),
                    (party_get_slot, ":looter_party", ":village_no", slot_village_raided_by),

                    # increase progress by looting skill
                    (try_begin),
                        (party_get_skill_level, ":looting_skill", ":looter_party", "skl_looting"),
                        (val_add, ":raid_progress_increase", ":looting_skill"),
                    (try_end),

                    # reduce progress by watch tower
                    (try_begin),
                        (party_slot_eq, ":village_no", slot_center_has_watch_tower, 1),
                        (val_mul, ":raid_progress_increase", 4),
                        (val_div, ":raid_progress_increase", 7),
                    (try_end),

                    (val_add, ":village_raid_progress", ":raid_progress_increase"),
                    (party_set_slot, ":village_no", slot_village_raid_progress, ":village_raid_progress"),

                    (try_begin),
                        # half progress: add smoke
                        (ge, ":village_raid_progress", 50),
                        (party_slot_eq, ":village_no", slot_village_smoke_added, 0),
                        (party_add_particle_system, ":village_no", "psys_map_village_fire"),
                        (party_add_particle_system, ":village_no", "psys_map_village_fire_smoke"),
                        (party_set_icon, ":village_no", ":burnt_village_icon"),
                        (party_set_slot, ":village_no", slot_village_smoke_added, 1),
                    (try_end),

                    (try_begin),
                        # full progress: loot it
                        (gt, ":village_raid_progress", 100),
                        (str_store_party_name_link, s1, ":village_no"),
                        (party_stack_get_troop_id, ":raid_leader", ":looter_party", 0),
                        (ge, ":raid_leader", 0),
                        (str_store_party_name, s2, ":looter_party"),
                        (store_faction_of_party, ":village_faction", ":village_no"),
                        (faction_get_color, ":faction_color", ":village_faction"),
                        (display_log_message, "@The village of {s1} has been looted by {s2}.", ":faction_color"),

                        (try_begin),
                            (party_get_slot, ":village_lord", ":village_no", slot_town_lord),
                            (is_between, ":village_lord", active_npcs_begin, active_npcs_end),
                            (call_script, "script_troop_change_relation_with_troop", ":raid_leader", ":village_lord", -1),
                            (val_add, "$total_battle_enemy_changes", -1),
                        (try_end),

                        # give loot gold to raid leader
                        (troop_get_slot, ":raid_leader_gold", ":raid_leader", slot_troop_wealth),
                        (party_get_slot, ":village_prosperity", ":village_no"),
                        (store_mul, ":value_of_loot", ":village_prosperity", 60), #average is 3000
                        (val_add, ":raid_leader_gold", ":value_of_loot"),
                        (troop_set_slot, ":raid_leader", slot_troop_wealth, ":raid_leader_gold"),

                        # take loot gold from village lord
                        (try_begin),
                            (is_between, ":village_lord", active_npcs_begin, active_npcs_end),
                            (troop_get_slot, ":village_lord_gold", ":village_lord", slot_troop_wealth),
                            (val_sub, ":village_lord_gold", ":value_of_loot"),
                            (val_max, ":village_lord_gold", 0),
                            (troop_set_slot, ":village_lord", slot_troop_wealth, ":village_lord_gold"),
                        (try_end),

                        # set it looted, init recover progress
                        (call_script, "script_village_set_state",  ":village_no", svs_looted),
                        (party_set_slot, ":village_no", slot_center_accumulated_rents, 0),
                        (party_set_slot, ":village_no", slot_center_accumulated_tariffs, 0),

                        (party_set_slot, ":village_no", slot_village_raid_progress, 0),
                        (party_set_slot, ":village_no", slot_village_recover_progress, 0),
                        (try_begin),
                            (store_faction_of_party, ":village_faction", ":village_no"),
                            (this_or_next|party_slot_eq, ":village_no", slot_town_lord, "trp_player"),
                            (eq, ":village_faction", "fac_player_supporters_faction"),
                            (call_script, "script_add_notification_menu", "mnu_notification_village_raided", ":village_no", ":raid_leader"),
                        (try_end),
                        (call_script, "script_add_log_entry", logent_village_raided, ":raid_leader",  ":village_no", -1, -1),
                        (store_faction_of_party, ":looter_faction", ":looter_party"),
                        (call_script, "script_faction_inflict_war_damage_on_faction", ":looter_faction", ":village_faction", 5),
                    (try_end),  # loot
                (try_end),
            (else_try),  # recover
                (party_slot_eq, ":village_no", slot_village_state, svs_looted),
                (party_get_slot, ":recover_progress", ":village_no", slot_village_recover_progress),
                (val_add, ":recover_progress", 1),
                (party_set_slot, ":village_no", slot_village_recover_progress, ":recover_progress"),

                (try_begin),
                    (ge, ":recover_progress", 10),
                    (party_slot_eq, ":village_no", slot_village_smoke_added, 1),
                    (party_clear_particle_systems, ":village_no"),
                    (party_add_particle_system, ":village_no", "psys_map_village_looted_smoke"),
                    (party_set_slot, ":village_no", slot_village_smoke_added, 2),
                (try_end),

                (try_begin),
                    (gt, ":recover_progress", 50),
                    (party_slot_eq, ":village_no", slot_village_smoke_added, 2),
                    (party_clear_particle_systems, ":village_no"),
                    (party_set_slot, ":village_no", slot_village_smoke_added, 3),
                    (party_set_icon, ":village_no", ":deserted_village_icon"),
                (try_end),

                (try_begin),
                    # village back to normal
                    (gt, ":recover_progress", 100),
                    (call_script, "script_village_set_state", ":village_no", svs_normal),
                    (party_set_slot, ":village_no", slot_village_recover_progress, 0),

                    (party_clear_particle_systems, ":village_no"),
                    (party_set_slot, ":village_no", slot_village_smoke_added, 0),
                    (party_set_icon, ":village_no", ":normal_village_icon"),
                (try_end),
            (try_end),
        (try_end),
    ]),
]
