from ..header_game_menus import *
from ..header_items import *
from ..module_constants import *


scripts = [
    ("game_start", [
        (troop_set_slot, "trp_hero1", slot_troop_occupation, "trp_briton_cavalry"),
        (troop_set_slot, "trp_hero2", slot_troop_occupation, "trp_saxon_infantryt5"),
        (troop_set_slot, "trp_hero3", slot_troop_occupation, "trp_pict_infantryt5"),
        (troop_set_slot, "trp_hero4", slot_troop_occupation, "trp_engle_infantryt5"),
        (troop_set_slot, "trp_hero5", slot_troop_occupation, "trp_irish_noblecavalry"),
        (troop_set_slot, "trp_hero6", slot_troop_occupation, "trp_jute_infantryelitet5"),
        (troop_set_slot, "trp_hero7", slot_troop_occupation, "trp_sea_raider_leader2"),
        (troop_set_slot, "trp_hero8", slot_troop_occupation, "trp_looter_leader2"),
        (troop_set_slot, "trp_hero9", slot_troop_occupation, "trp_slaver_chief"),
        (troop_set_slot, "trp_hero10", slot_troop_occupation, "trp_fresna_infantryt3"),
        (troop_set_slot, "trp_hero11", slot_troop_occupation, "trp_mercenary_leader"),
        (troop_set_slot, "trp_hero12", slot_troop_occupation, "trp_cantaber_iuventus"),
        (assign, "$g_upgrade_time", 336),  # 2 weeks for 1st upgrade call

        (call_script, "script_coop_set_default_admin_settings"),

        (assign, "$g_report_extra_xp", 1),
        (assign, "$g_rand_rain_limit", 30),
        (assign, "$g_report_shot_distance", 1),
        (assign, "$g_speed_ai_battles", 1),
        (assign, "$g_dplmc_terrain_advantage", DPLMC_TERRAIN_ADVANTAGE_ENABLE),
        (assign, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
        (assign, "$g_pintar_cuerpo", 0),
        (assign, "$g_historia2", 0),  # romanruins
        (assign, "$g_historia21", 0),  # odin'scave
        (assign, "$sp_alturas", 1),
        (assign, "$g_realistic_casualties", 0),
        (assign, "$g_weapon_breaking", 1),
        (assign, "$g_armor_penalties", 1),
        (assign, "$g_morale_rest", 1),
        (assign, "$g_encumbrance_penalty", 1),
        (assign, "$g_siege_realism", 1),
        (assign, "$g_avdificultad", 0),
        (assign, "$sp_shield_bash", 1),
        (assign, "$sp_shield_bash_ai", 1),
        (assign, "$sp_decapitation", 0),
        (assign, "$sp_fatigas", 1),
        (assign, "$g_heridas_chel", 1),
        (assign, "$drowning", 1),  # toggles drowning in mission templates
        (assign, "$sp_caer_andar", 1),
        (assign, "$sp_criticos", 1),
        (assign, "$g_realism_upgrade", 1),
        (assign, "$freelancer_state", 0),  # freelancer chief
        # Version for TML Submod. Will use it to do savegame compatibility updates in the future if required. F123 - Submod -> 1.41 (Yay new versions!)
        (assign, "$tml_version", 122),

        #
        (assign, "$g_presentation_center_faction", "fac_kingdom_1"),
        (assign, "$g_presentations_next_presentation", -1),
        (assign, "$camp_supply", 1),  # used for camp over run supply loss
        (assign, "$current_camp_party", -1),
        # used for camp entrenchment, value is -1 or entrenchment party id
        (assign, "$target", -1),
        (assign, "$target_2", -1),
        (assign, "$message_party_target", -1),
        (assign, "$message_target", -1),
        (assign, "$duel_encounter", -1),  # used for wilderness duels, 1 for normal duel, 2 for treachery battle
        (assign, "$unable_to_duel", -1),  # used in messaging system to notify player that party is unable to duel at this time
        (assign, "$unable_to_pay", -1),  # used in messaging system to check if player has enough gold to hire party
        (assign, "$attack_party_question", -1),  # used in messaging system to let player agree or not before hiring
        (assign, "$skirmish_party_no", -1),  # party number of active skirmish party
        (assign, "$spy_target", -1),  # used for sending spy to a town
        (assign, "$attack_party_answer", -1),  # used to tell script_build_reply what answer was given by player regarding paying for attack
        (assign, "$commoner_trust", -30),  # how well farmer parties like the player
        (troop_set_auto_equip, "trp_loot_wagon_storage_1", 0),  # don't allow storage troop to equip items

        # fire arrow
        (troop_set_slot, "trp_global_value", slot_gloval_show_fire_arrow_particle, 0),
        (troop_set_slot, "trp_global_value", slot_gloval_fire_arrow_key, 0x14),
        (troop_set_slot, "trp_global_value", slot_gloval_max_fire_arrow, 100),
        (troop_set_slot, "trp_global_value", slot_gloval_max_flame_slot, 40),

        (try_for_range, ":center_no", centers_begin, centers_end),
            (party_set_slot, ":center_no", slot_saqueo_state, 0),
        (try_end),

        # wound system
        (assign, "$wound_type", 0), # 0-8 (0=not wounded, 1-8=type of wound) chief
        (assign, "$heal_day", 0),   # day that wound heals chief

        # tax system
        (assign, "$g_sod_tax", 0),

        (call_script, "script_initialize_religion"),

        (faction_set_slot, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
        (assign, "$g_player_luck", 200),
        (troop_set_slot, "trp_player", slot_troop_occupation, slto_kingdom_hero),
        (store_random_in_range, ":starting_training_ground", training_grounds_begin, training_grounds_end),
        (party_relocate_near_party, "p_main_party", ":starting_training_ground", 3),
        (str_store_troop_name, s5, "trp_player"),
        (party_set_name, "p_main_party", s5),
        (call_script, "script_update_party_creation_random_limits"),
        (assign, "$g_player_party_icon", -1),
        (party_set_slot, "p_main_party", slot_party_loot_wagon, -1),  # stores party id of loot wagon
        (party_set_slot, "p_main_party", slot_party_wagon_leader, -1),  # stores the troop id of the wagon leader
        (party_set_slot, "p_main_party", slot_loot_wagon_target, 1),

        (try_for_range, ":npc", 0, kingdom_ladies_end),
            (this_or_next|eq, ":npc", "trp_player"),
            (is_between, ":npc", active_npcs_begin, kingdom_ladies_end),
            (troop_set_slot, ":npc", slot_troop_father, -1),
            (troop_set_slot, ":npc", slot_troop_mother, -1),
            (troop_set_slot, ":npc", slot_troop_guardian, -1),
            (troop_set_slot, ":npc", slot_troop_spouse, -1),
            (troop_set_slot, ":npc", slot_troop_betrothed, -1),
            (troop_set_slot, ":npc", slot_troop_prisoner_of_party, -1),
            (troop_set_slot, ":npc", slot_lady_last_suitor, -1),
            (troop_set_slot, ":npc", slot_troop_stance_on_faction_issue, -1),

            (store_random_in_range, ":decision_seed", 0, 10000),
            (troop_set_slot, ":npc", slot_troop_set_decision_seed, ":decision_seed"),    #currently not used
            (troop_set_slot, ":npc", slot_troop_temp_decision_seed, ":decision_seed"),    #currently not used, holds for at least 24 hours
        (try_end),

        (assign, "$g_lord_long_term_count", 0),
        (call_script, "script_initialize_banner_info"),
        
        (try_for_range, ":cur_troop", active_npcs_begin, kingdom_ladies_end),
            (troop_set_slot, ":cur_troop", slot_troop_duel_challenger, -1),
            (troop_set_slot, ":cur_troop", slot_troop_duel_challenged, -1),
            (troop_set_slot, ":cur_troop", slot_troop_poisoned, -1),
        (try_end),

        # items slots
        (call_script, "script_initialize_item_info"),

        # npcs relations, ages, etc.
        (call_script, "script_initialize_aristocracy"),

        (call_script, "script_initialize_companions"),

        (call_script, "script_initialize_pretenders"),

        # Set random feast time
        (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
            (store_random_in_range, ":last_feast_time", 0, 312),  # 240 + 72
            (val_mul, ":last_feast_time", -1),
            (faction_set_slot, ":faction_no", slot_faction_last_feast_start_time, ":last_feast_time"),
        (try_end),

        # Set random town sequence
        # todo: what does this do exactly?
        (store_sub, ":num_towns", towns_end, towns_begin),
        (assign, ":num_iterations", ":num_towns"),
        (try_for_range, ":cur_town_no", 0, ":num_towns"),
            (troop_set_slot, "trp_random_town_sequence", ":cur_town_no", -1),
        (try_end),

        (assign, ":cur_town_no", 0),
        (try_for_range, ":unused", 0, ":num_iterations"),
            (store_random_in_range, ":random_no", 0, ":num_towns"),
            (assign, ":is_unique", 1),
            (try_for_range, ":cur_town_no_2", 0, ":num_towns"),
                (troop_slot_eq, "trp_random_town_sequence", ":cur_town_no_2", ":random_no"),
                (assign, ":is_unique", 0),
            (try_end),
            (try_begin),
                (eq, ":is_unique", 1),
                (troop_set_slot, "trp_random_town_sequence", ":cur_town_no", ":random_no"),
                (val_add, ":cur_town_no", 1),
            (else_try),
                (val_add, ":num_iterations", 1),
            (try_end),
        (try_end),

        (call_script, "script_initialize_cultures"),

        # initialize marshall
        (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
            (faction_set_slot, ":faction_no", slot_faction_marshall, -1),
        (try_end),
        (faction_set_slot, "fac_player_supporters_faction", slot_faction_marshall, "trp_player"),

        (call_script, "script_initialize_faction_troop_types"),

        (call_script, "script_dplmc_init_domestic_policy"),

        # Initial prices of goods
        (try_for_range, ":item_no", trade_goods_begin, trade_goods_end),
            (store_sub, ":offset", ":item_no", trade_goods_begin),
            (val_add, ":offset", slot_town_trade_good_prices_begin),
            (try_for_range, ":center_no", centers_begin, centers_end),
                (party_set_slot, ":center_no", ":offset", average_price_factor),
            (try_end),
        (try_end),

        (try_for_range, ":center_no", centers_begin, centers_end),
            (party_set_slot, ":center_no", slot_center_last_spotted_enemy, -1),
            (party_set_slot, ":center_no", slot_center_is_besieged_by, -1),
            (party_set_slot, ":center_no", slot_center_last_taken_by_troop, -1),
        (try_end),

        (call_script, "script_initialize_trade_routes"),
        (call_script, "script_initialize_sea_trade_routes"),
        (call_script, "script_initialize_town_arena_info"),
        (call_script, "script_initialize_tournaments"),

        # Villages
        # pass 1: Give one village to each castle
        (try_for_range, ":cur_center", castles_begin, castles_end),
            (assign, ":min_dist", 999999),
            (assign, ":min_dist_village", -1),
            (try_for_range, ":cur_village", villages_begin, villages_end),
                (neg|party_slot_ge, ":cur_village", slot_village_bound_center, 1), #skip villages which are already bound.
                (store_distance_to_party_from_party, ":cur_dist", ":cur_village", ":cur_center"),
                (lt, ":cur_dist", ":min_dist"),
                (assign, ":min_dist", ":cur_dist"),
                (assign, ":min_dist_village", ":cur_village"),
            (try_end),
            (party_set_slot, ":min_dist_village", slot_village_bound_center, ":cur_center"),
            (store_faction_of_party, ":town_faction", ":cur_center"),
            (call_script, "script_give_center_to_faction_aux", ":min_dist_village", ":town_faction"),
        (try_end),

        # pass 2: Give other villages to closest town.
        (try_for_range, ":cur_village", villages_begin, villages_end),
            (neg|party_slot_ge, ":cur_village", slot_village_bound_center, 1), #skip villages which are already bound.
            (assign, ":min_dist", 999999),
            (assign, ":min_dist_town", -1),
            (try_for_range, ":cur_town", towns_begin, towns_end),
                (store_distance_to_party_from_party, ":cur_dist", ":cur_village", ":cur_town"),
                (lt, ":cur_dist", ":min_dist"),
                (assign, ":min_dist", ":cur_dist"),
                (assign, ":min_dist_town", ":cur_town"),
            (try_end),
            (party_set_slot, ":cur_village", slot_village_bound_center, ":min_dist_town"),
            (store_faction_of_party, ":town_faction", ":min_dist_town"),
            (call_script, "script_give_center_to_faction_aux", ":cur_village", ":town_faction"),
        (try_end),

        # Assign npcs and buildings to towns
        (try_for_range, ":town_no", towns_begin, towns_end),
            (store_sub, ":offset", ":town_no", towns_begin),
            (party_set_slot, ":town_no", slot_party_type, spt_town),
            (store_add, ":cur_object_no", "scn_town_1_center", ":offset"),
            (party_set_slot, ":town_no", slot_town_center, ":cur_object_no"),
            (store_add, ":cur_object_no", "scn_town_1_castle", ":offset"),
            (party_set_slot, ":town_no", slot_town_castle, ":cur_object_no"),
            (store_add, ":cur_object_no", "scn_town_1_prison", ":offset"),
            (party_set_slot, ":town_no", slot_town_prison, ":cur_object_no"),
            (store_add, ":cur_object_no", "scn_town_1_walls", ":offset"),
            (party_set_slot, ":town_no", slot_town_walls, ":cur_object_no"),
            (store_add, ":cur_object_no", "scn_town_1_tavern", ":offset"),
            (party_set_slot, ":town_no", slot_town_tavern, ":cur_object_no"),
            (store_add, ":cur_object_no", "scn_town_1_store", ":offset"),
            (party_set_slot, ":town_no", slot_town_store, ":cur_object_no"),
            (store_add, ":cur_object_no", "scn_town_1_arena", ":offset"),
            (party_set_slot, ":town_no", slot_town_arena, ":cur_object_no"),
            (store_add, ":cur_object_no", "scn_town_1_alley", ":offset"),
            (party_set_slot, ":town_no", slot_town_alley, ":cur_object_no"),
            (store_add, ":cur_object_no", "trp_town_1_mayor", ":offset"),
            (party_set_slot, ":town_no", slot_town_elder, ":cur_object_no"),
            (store_add, ":cur_object_no", "trp_town_1_tavernkeeper", ":offset"),
            (party_set_slot, ":town_no", slot_town_tavernkeeper, ":cur_object_no"),
            (store_add, ":cur_object_no", "trp_town_1_weaponsmith", ":offset"),
            (party_set_slot, ":town_no", slot_town_weaponsmith, ":cur_object_no"),
            (store_add, ":cur_object_no", "trp_town_1_armorer", ":offset"),
            (party_set_slot, ":town_no", slot_town_armorer, ":cur_object_no"),
            (store_add, ":cur_object_no", "trp_town_1_merchant", ":offset"),
            (party_set_slot, ":town_no", slot_town_merchant, ":cur_object_no"),
            (store_add, ":cur_object_no", "trp_town_1_horse_merchant", ":offset"),
            (party_set_slot, ":town_no", slot_town_horse_merchant, ":cur_object_no"),
            (store_add, ":cur_object_no", "scn_town_1_center", ":offset"),
            (party_set_slot, ":town_no", slot_town_center, ":cur_object_no"),
            (party_set_slot, ":town_no", slot_town_reinforcement_party_template, "pt_center_reinforcements"),
        (try_end),

        # Ports
        # (party_set_slot, "p_town_6", slot_town_port, 1),  # alt cult
        (party_set_slot, "p_town_2", slot_town_port, 1),  # Seals-ey
        (party_set_slot, "p_town_7", slot_town_port, 1),  # Caer Liwelydd
        (party_set_slot, "p_town_13", slot_town_port, 1),  # Caer Segeint
        (party_set_slot, "p_town_17", slot_town_port, 1),   # Caer Uisc
        # (party_set_slot, "p_town_19", slot_town_port, 1),  # Dun At
        (party_set_slot, "p_town_27", slot_town_port, 1),  # Bebbanburh
        (party_set_slot, "p_town_32", slot_town_port, 1),  # Dun Keltair
        (party_set_slot, "p_town_33", slot_town_port, 1),  # Aileach
        (party_set_slot, "p_town_37", slot_town_port, 1),  # Duin Foither
        # (party_set_slot, "p_town_42", slot_town_port, 1),  # Din Cado
        (party_set_slot, "p_castle_42", slot_town_port, 1),  # Caer Manaw

        # Castles
        (try_for_range, ":castle_no", castles_begin, castles_end),
            (store_sub, ":offset", ":castle_no", castles_begin),
            (val_mul, ":offset", 3),

            (store_add, ":exterior_scene_no", "scn_castle_1_exterior", ":offset"),
            (party_set_slot, ":castle_no", slot_castle_exterior, ":exterior_scene_no"),
            (store_add, ":interior_scene_no", "scn_castle_1_interior", ":offset"),
            (party_set_slot, ":castle_no", slot_town_castle, ":interior_scene_no"),
            (store_add, ":interior_scene_no", "scn_castle_1_prison", ":offset"),
            (party_set_slot, ":castle_no", slot_town_prison, ":interior_scene_no"),

            (party_set_slot, ":castle_no", slot_town_reinforcement_party_template, "pt_center_reinforcements"),
            (party_set_slot, ":castle_no", slot_party_type, spt_castle),
            (party_set_slot, ":castle_no", slot_center_is_besieged_by, -1),
        (try_end),

        # Set which castles need to be attacked with siege towers.
        #(party_set_slot, "p_town_19", slot_center_siege_with_belfry, 1),
        #(party_set_slot, "p_town_30", slot_center_siege_with_belfry, 1),
        #(party_set_slot, "p_town_32", slot_center_siege_with_belfry, 1),
        #(party_set_slot, "p_town_36", slot_center_siege_with_belfry, 1),
        #(party_set_slot, "p_town_40", slot_center_siege_with_belfry, 1),
        (party_set_slot, "p_castle_9", slot_center_siege_with_belfry, 1),
        #(party_set_slot, "p_castle_13", slot_center_siege_with_belfry, 1),
        #(party_set_slot, "p_castle_27", slot_center_siege_with_belfry, 1),
        #(party_set_slot, "p_castle_49", slot_center_siege_with_belfry, 1),
        (party_set_slot, "p_castle_59", slot_center_siege_with_belfry, 1),
        #(party_set_slot, "p_castle_69", slot_center_siege_with_belfry, 1),
        #(party_set_slot, "p_castle_72", slot_center_siege_with_belfry, 1),

        (party_set_slot, "p_castle_21", slot_center_siege_with_ram, 1),
        #(party_set_slot, "p_castle_23", slot_center_siege_with_ram, 1),
        #(party_set_slot, "p_castle_38", slot_center_siege_with_ram, 1),
        (party_set_slot, "p_castle_42", slot_center_siege_with_ram, 1),
        (party_set_slot, "p_castle_60", slot_center_siege_with_ram, 1),
        (party_set_slot, "p_castle_61", slot_center_siege_with_ram, 1),
        #(party_set_slot, "p_town_30", slot_center_siege_with_ram,      1),
        #(party_set_slot, "p_town_36", slot_center_siege_with_ram,      1),
        #(party_set_slot, "p_town_40", slot_center_siege_with_ram,      1),

        # Villages characters
        (try_for_range, ":village_no", villages_begin, villages_end),
            (store_sub, ":offset", ":village_no", villages_begin),

            (store_add, ":exterior_scene_no", "scn_village_1", ":offset"),
            (party_set_slot, ":village_no", slot_castle_exterior, ":exterior_scene_no"),

            (store_add, ":store_troop_no", "trp_village_1_elder", ":offset"),
            (party_set_slot, ":village_no", slot_town_elder, ":store_troop_no"),

            (party_set_slot, ":village_no", slot_party_type, spt_village),
            (party_set_slot, ":village_no", slot_village_raided_by, -1),

            (call_script, "script_refresh_village_defenders", ":village_no"),
            (call_script, "script_refresh_village_defenders", ":village_no"),
            (call_script, "script_refresh_village_defenders", ":village_no"),
            (call_script, "script_refresh_village_defenders", ":village_no"),
        (try_end),

        (call_script, "script_initialize_banners"),

        (call_script, "script_initialize_town_factions"),

        # Initialize walkers (must be after initialize_cultures)
        (try_for_range, ":center_no", centers_begin, centers_end),
            (try_for_range, ":walker_no", 0, num_town_walkers),
                (call_script, "script_center_set_walker_to_type", ":center_no", ":walker_no", walkert_default),
            (try_end),
        (try_end),

        # This needs to be after `initialize_town_factions`
        (call_script, "script_initialize_economic_information"),

        (call_script, "script_initialize_notes"),

        (call_script, "script_game_start_dynamic"),
    ]),

    ("initialize_religion", [
        (assign, "$g_sod_faith", 0),
        (assign, "$g_pueblos_religion", 0),
        (assign, "$g_sod_global_faith", 0),
        (party_set_slot, "p_town_8", center_religion_pagana, 1),  # grantebrydge
        (party_set_slot, "p_town_11", center_religion_pagana, 1),  # Aegelesburh
        (party_set_slot, "p_town_18", center_religion_pagana, 1),  # Searoburh
        (party_set_slot, "p_town_23", center_religion_pagana, 1),  # Licidfelth
        (party_set_slot, "p_town_24", center_religion_pagana, 1),  # Linnuis

        (party_set_slot, "p_village_1", center_religion_pagana, 1),
        (party_set_slot, "p_village_2", center_religion_pagana, 1),
        (party_set_slot, "p_village_4", center_religion_pagana, 1),
        (party_set_slot, "p_village_8", center_religion_pagana, 1),
        (party_set_slot, "p_village_10", center_religion_pagana, 1),
        (party_set_slot, "p_village_14", center_religion_pagana, 1),
        (party_set_slot, "p_village_74", center_religion_pagana, 1),
        (party_set_slot, "p_village_51", center_religion_pagana, 1),
        (party_set_slot, "p_village_16", center_religion_pagana, 1),
        (party_set_slot, "p_village_41", center_religion_pagana, 1),
        (party_set_slot, "p_village_49", center_religion_pagana, 1),
        (party_set_slot, "p_village_12", center_religion_pagana, 1),
        (party_set_slot, "p_village_21", center_religion_pagana, 1),
        (party_set_slot, "p_village_76", center_religion_pagana, 1),
        (party_set_slot, "p_village_87", center_religion_pagana, 1),
        (party_set_slot, "p_village_75", center_religion_pagana, 1),
        (party_set_slot, "p_village_38", center_religion_pagana, 1),
        (party_set_slot, "p_village_88", center_religion_pagana, 1),
        (party_set_slot, "p_village_89", center_religion_pagana, 1),
        (party_set_slot, "p_village_44", center_religion_pagana, 1),
        (party_set_slot, "p_village_93", center_religion_pagana, 1),
        (party_set_slot, "p_village_52", center_religion_pagana, 1),
        (party_set_slot, "p_village_98", center_religion_pagana, 1),
        (party_set_slot, "p_village_17", center_religion_pagana, 1),
        (party_set_slot, "p_village_48", center_religion_pagana, 1),
        (party_set_slot, "p_village_36", center_religion_pagana, 1),
        (party_set_slot, "p_village_67", center_religion_pagana, 1),
        (party_set_slot, "p_village_103", center_religion_pagana, 1),
        (party_set_slot, "p_village_129", center_religion_pagana, 1),
        (party_set_slot, "p_village_122", center_religion_pagana, 1),
        (party_set_slot, "p_village_55", center_religion_pagana, 1),
        (party_set_slot, "p_village_54", center_religion_pagana, 1),
        (party_set_slot, "p_village_124", center_religion_pagana, 1),
        (party_set_slot, "p_village_42", center_religion_pagana, 1),
        (party_set_slot, "p_village_90", center_religion_pagana, 1),
        (party_set_slot, "p_village_91", center_religion_pagana, 1),
        (party_set_slot, "p_village_151", center_religion_pagana, 1),
        (party_set_slot, "p_village_95", center_religion_pagana, 1),
        (party_set_slot, "p_village_99", center_religion_pagana, 1),
        (party_set_slot, "p_village_20", center_religion_pagana, 1),
        (party_set_slot, "p_village_3", center_religion_pagana, 1),
        (party_set_slot, "p_village_28", center_religion_pagana, 1),
        (party_set_slot, "p_village_47", center_religion_pagana, 1),
        (party_set_slot, "p_village_46", center_religion_pagana, 1),

        (party_set_slot, "p_village_170", center_religion_pagana, 1),
        (party_set_slot, "p_village_71", center_religion_pagana, 1),
        (party_set_slot, "p_village_116", center_religion_pagana, 1),
        (party_set_slot, "p_village_57", center_religion_pagana, 1),
        (party_set_slot, "p_village_20", center_religion_pagana, 1),
        (party_set_slot, "p_village_99", center_religion_pagana, 1),
        (party_set_slot, "p_village_43", center_religion_pagana, 1),
        (party_set_slot, "p_village_21", center_religion_pagana, 1),
        (party_set_slot, "p_village_16", center_religion_pagana, 1),
        (party_set_slot, "p_village_38", center_religion_pagana, 1),
        (party_set_slot, "p_village_65", center_religion_pagana, 1),
        (party_set_slot, "p_village_35", center_religion_pagana, 1),

        #gente cristiana
        (try_for_range, ":center_no", centers_begin, centers_end),
            (neg|party_slot_ge, ":center_no", center_religion_pagana, 1), #skip villages which are pagan.
            (neg|party_slot_eq, ":center_no", slot_party_type, spt_castle),
            (assign, "$g_pueblos_religion", 4),
            (store_random_in_range, ":rand", 30, 90),
            (party_set_slot, ":center_no", slot_center_sod_local_faith, ":rand"),
        (try_end),
            (try_for_range, ":center_no", centers_begin, centers_end),
            (neg|party_slot_eq, ":center_no", slot_party_type, spt_castle),
            (party_slot_eq, ":center_no", center_religion_pagana, 1), #anade fe a las villas paganas
            (store_random_in_range, ":rand", -90, -30),
            (party_set_slot, ":center_no", slot_center_sod_local_faith, ":rand"),
        (try_end),
    ]),

    ("initialize_cultures",[
        # player culture
        (assign, ":player_faction_culture", "fac_culture_1"),
        (faction_set_slot, "fac_player_supporters_faction", slot_faction_culture, ":player_faction_culture"),
        (faction_set_slot, "fac_player_faction", slot_faction_culture, ":player_faction_culture"),

        # others culture
        (faction_set_slot, "fac_culture_1", slot_faction_tier_1_troop, "trp_jute_recruit"),
        (faction_set_slot, "fac_culture_1", slot_faction_tier_2_troop, "trp_jute_footmant2"),
        (faction_set_slot, "fac_culture_1", slot_faction_tier_3_troop, "trp_jute_skirmishert3"),
        (faction_set_slot, "fac_culture_1", slot_faction_tier_4_troop, "trp_jute_infantryt3"),
        (faction_set_slot, "fac_culture_1", slot_faction_tier_5_troop, "trp_jute_horsemant4"),

        (faction_set_slot, "fac_culture_2", slot_faction_tier_1_troop, "trp_saxon_recruit"),
        (faction_set_slot, "fac_culture_2", slot_faction_tier_2_troop, "trp_saxon_footmant2"),
        (faction_set_slot, "fac_culture_2", slot_faction_tier_3_troop, "trp_saxon_skirmishert3"),
        (faction_set_slot, "fac_culture_2", slot_faction_tier_4_troop, "trp_saxon_infantryt3"),
        (faction_set_slot, "fac_culture_2", slot_faction_tier_5_troop, "trp_saxon_horseman1"),

        (faction_set_slot, "fac_culture_3", slot_faction_tier_1_troop, "trp_saxon_recruit"),
        (faction_set_slot, "fac_culture_3", slot_faction_tier_2_troop, "trp_saxon_footmant2"),
        (faction_set_slot, "fac_culture_3", slot_faction_tier_3_troop, "trp_saxon_skirmishert3"),
        (faction_set_slot, "fac_culture_3", slot_faction_tier_4_troop, "trp_saxon_infantryt3"),
        (faction_set_slot, "fac_culture_3", slot_faction_tier_5_troop, "trp_saxon_horseman1"),

        (faction_set_slot, "fac_culture_4", slot_faction_tier_1_troop, "trp_engle_recruit"),
        (faction_set_slot, "fac_culture_4", slot_faction_tier_2_troop, "trp_engle_footmant2"),
        (faction_set_slot, "fac_culture_4", slot_faction_tier_3_troop, "trp_engle_skirmishert3"),
        (faction_set_slot, "fac_culture_4", slot_faction_tier_4_troop, "trp_engle_infantryt3"),
        (faction_set_slot, "fac_culture_4", slot_faction_tier_5_troop, "trp_engle_horseman"),

        (faction_set_slot, "fac_culture_5", slot_faction_tier_1_troop, "trp_saxon_recruit"),
        (faction_set_slot, "fac_culture_5", slot_faction_tier_2_troop, "trp_saxon_footmant2"),
        (faction_set_slot, "fac_culture_5", slot_faction_tier_3_troop, "trp_saxon_skirmishert3"),
        (faction_set_slot, "fac_culture_5", slot_faction_tier_4_troop, "trp_saxon_infantryt3"),
        (faction_set_slot, "fac_culture_5", slot_faction_tier_5_troop, "trp_saxon_horseman1"),

        (faction_set_slot, "fac_culture_6", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_6", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_6", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_6", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_6", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_7", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_7", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_7", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_7", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_7", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_8", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_8", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_8", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_8", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_8", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_9", slot_faction_tier_1_troop, "trp_engle_recruit"),
        (faction_set_slot, "fac_culture_9", slot_faction_tier_2_troop, "trp_engle_footmant2"),
        (faction_set_slot, "fac_culture_9", slot_faction_tier_3_troop, "trp_engle_skirmishert3"),
        (faction_set_slot, "fac_culture_9", slot_faction_tier_4_troop, "trp_engle_infantryt3"),
        (faction_set_slot, "fac_culture_9", slot_faction_tier_5_troop, "trp_engle_horseman"),

        (faction_set_slot, "fac_culture_10", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_10", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_10", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_10", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_10", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_11", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_11", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_11", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_11", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_11", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_12", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_12", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_12", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_12", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_12", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_13", slot_faction_tier_1_troop, "trp_engle_recruit"),
        (faction_set_slot, "fac_culture_13", slot_faction_tier_2_troop, "trp_engle_footmant2"),
        (faction_set_slot, "fac_culture_13", slot_faction_tier_3_troop, "trp_engle_skirmishert3"),
        (faction_set_slot, "fac_culture_13", slot_faction_tier_4_troop, "trp_engle_infantryt3"),
        (faction_set_slot, "fac_culture_13", slot_faction_tier_5_troop, "trp_engle_horseman"),

        (faction_set_slot, "fac_culture_14", slot_faction_tier_1_troop, "trp_engle_recruit"),
        (faction_set_slot, "fac_culture_14", slot_faction_tier_2_troop, "trp_engle_footmant2"),
        (faction_set_slot, "fac_culture_14", slot_faction_tier_3_troop, "trp_engle_skirmishert3"),
        (faction_set_slot, "fac_culture_14", slot_faction_tier_4_troop, "trp_engle_infantryt3"),
        (faction_set_slot, "fac_culture_14", slot_faction_tier_5_troop, "trp_engle_horseman"),

        (faction_set_slot, "fac_culture_15", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_15", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_15", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_15", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_15", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_16", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_16", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_16", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_16", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_16", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_17", slot_faction_tier_1_troop, "trp_irish_recruit"),
        (faction_set_slot, "fac_culture_17", slot_faction_tier_2_troop, "trp_irish_footmant2"),
        (faction_set_slot, "fac_culture_17", slot_faction_tier_3_troop, "trp_irish_infantryt3"),
        (faction_set_slot, "fac_culture_17", slot_faction_tier_4_troop, "trp_irish_skirmishert3"),
        (faction_set_slot, "fac_culture_17", slot_faction_tier_5_troop, "trp_irish_infantryt5"),

        (faction_set_slot, "fac_culture_18", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_18", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_18", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_18", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_18", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_19", slot_faction_tier_1_troop, "trp_irish_recruit"),
        (faction_set_slot, "fac_culture_19", slot_faction_tier_2_troop, "trp_irish_footmant2"),
        (faction_set_slot, "fac_culture_19", slot_faction_tier_3_troop, "trp_irish_infantryt3"),
        (faction_set_slot, "fac_culture_19", slot_faction_tier_4_troop, "trp_irish_skirmishert3"),
        (faction_set_slot, "fac_culture_19", slot_faction_tier_5_troop, "trp_irish_infantryt5"),

        (faction_set_slot, "fac_culture_20", slot_faction_tier_1_troop, "trp_pict_recruit"),
        (faction_set_slot, "fac_culture_20", slot_faction_tier_2_troop, "trp_pict_footmant2"),
        (faction_set_slot, "fac_culture_20", slot_faction_tier_3_troop, "trp_pict_skirmishert3"),
        (faction_set_slot, "fac_culture_20", slot_faction_tier_4_troop, "trp_pict_horsesquiret3"),
        (faction_set_slot, "fac_culture_20", slot_faction_tier_5_troop, "trp_pict_skirmishert4"),

        (faction_set_slot, "fac_culture_21", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_21", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_21", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_21", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_21", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_22", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_22", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_22", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_22", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_22", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_23", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_23", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_23", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_23", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_23", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_24", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_24", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_24", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_24", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_24", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_25", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_25", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_25", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_25", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_25", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_26", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_26", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_26", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_26", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_26", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_27", slot_faction_tier_1_troop, "trp_irish_recruit"),
        (faction_set_slot, "fac_culture_27", slot_faction_tier_2_troop, "trp_irish_footmant2"),
        (faction_set_slot, "fac_culture_27", slot_faction_tier_3_troop, "trp_irish_infantryt3"),
        (faction_set_slot, "fac_culture_27", slot_faction_tier_4_troop, "trp_irish_skirmishert3"),
        (faction_set_slot, "fac_culture_27", slot_faction_tier_5_troop, "trp_irish_infantryt5"),

        (faction_set_slot, "fac_culture_28", slot_faction_tier_1_troop, "trp_irish_recruit"),
        (faction_set_slot, "fac_culture_28", slot_faction_tier_2_troop, "trp_irish_footmant2"),
        (faction_set_slot, "fac_culture_28", slot_faction_tier_3_troop, "trp_irish_infantryt3"),
        (faction_set_slot, "fac_culture_28", slot_faction_tier_4_troop, "trp_irish_skirmishert3"),
        (faction_set_slot, "fac_culture_28", slot_faction_tier_5_troop, "trp_irish_infantryt5"),

        (faction_set_slot, "fac_culture_29", slot_faction_tier_1_troop, "trp_irish_recruit"),
        (faction_set_slot, "fac_culture_29", slot_faction_tier_2_troop, "trp_irish_footmant2"),
        (faction_set_slot, "fac_culture_29", slot_faction_tier_3_troop, "trp_irish_infantryt3"),
        (faction_set_slot, "fac_culture_29", slot_faction_tier_4_troop, "trp_irish_skirmishert3"),
        (faction_set_slot, "fac_culture_29", slot_faction_tier_5_troop, "trp_irish_infantryt5"),

        (faction_set_slot, "fac_culture_30", slot_faction_tier_1_troop, "trp_irish_recruit"),
        (faction_set_slot, "fac_culture_30", slot_faction_tier_2_troop, "trp_irish_footmant2"),
        (faction_set_slot, "fac_culture_30", slot_faction_tier_3_troop, "trp_irish_infantryt3"),
        (faction_set_slot, "fac_culture_30", slot_faction_tier_4_troop, "trp_irish_skirmishert3"),
        (faction_set_slot, "fac_culture_30", slot_faction_tier_5_troop, "trp_irish_infantryt5"),

        (faction_set_slot, "fac_culture_31", slot_faction_tier_1_troop, "trp_irish_recruit"),
        (faction_set_slot, "fac_culture_31", slot_faction_tier_2_troop, "trp_irish_footmant2"),
        (faction_set_slot, "fac_culture_31", slot_faction_tier_3_troop, "trp_irish_infantryt3"),
        (faction_set_slot, "fac_culture_31", slot_faction_tier_4_troop, "trp_irish_skirmishert3"),
        (faction_set_slot, "fac_culture_31", slot_faction_tier_5_troop, "trp_irish_infantryt5"),

        (faction_set_slot, "fac_culture_1", slot_faction_town_walker_male_troop, "trp_town_walker_5"),
        (faction_set_slot, "fac_culture_1", slot_faction_town_walker_female_troop, "trp_town_walker_6"),
        (faction_set_slot, "fac_culture_1", slot_faction_village_walker_male_troop, "trp_village_walker_5"),
        (faction_set_slot, "fac_culture_1", slot_faction_village_walker_female_troop, "trp_village_walker_6"),
        (faction_set_slot, "fac_culture_1", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_1", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_2", slot_faction_town_walker_male_troop, "trp_town_walker_5"),
        (faction_set_slot, "fac_culture_2", slot_faction_town_walker_female_troop, "trp_town_walker_6"),
        (faction_set_slot, "fac_culture_2", slot_faction_village_walker_male_troop, "trp_village_walker_5"),
        (faction_set_slot, "fac_culture_2", slot_faction_village_walker_female_troop, "trp_village_walker_6"),
        (faction_set_slot, "fac_culture_2", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_2", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_3", slot_faction_town_walker_male_troop, "trp_town_walker_5"),
        (faction_set_slot, "fac_culture_3", slot_faction_town_walker_female_troop, "trp_town_walker_6"),
        (faction_set_slot, "fac_culture_3", slot_faction_village_walker_male_troop, "trp_village_walker_5"),
        (faction_set_slot, "fac_culture_3", slot_faction_village_walker_female_troop, "trp_village_walker_6"),
        (faction_set_slot, "fac_culture_3", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_3", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_4", slot_faction_town_walker_male_troop, "trp_town_walker_5"),
        (faction_set_slot, "fac_culture_4", slot_faction_town_walker_female_troop, "trp_town_walker_6"),
        (faction_set_slot, "fac_culture_4", slot_faction_village_walker_male_troop, "trp_village_walker_5"),
        (faction_set_slot, "fac_culture_4", slot_faction_village_walker_female_troop, "trp_village_walker_6"),
        (faction_set_slot, "fac_culture_4", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_4", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_5", slot_faction_town_walker_male_troop, "trp_town_walker_5"),
        (faction_set_slot, "fac_culture_5", slot_faction_town_walker_female_troop, "trp_town_walker_6"),
        (faction_set_slot, "fac_culture_5", slot_faction_village_walker_male_troop, "trp_village_walker_5"),
        (faction_set_slot, "fac_culture_5", slot_faction_village_walker_female_troop, "trp_village_walker_6"),
        (faction_set_slot, "fac_culture_5", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_5", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_6", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_6", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_6", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_6", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_6", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_6", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_7", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_7", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_7", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_7", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_7", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_7", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_8", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_8", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_8", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_8", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_8", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_8", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_9", slot_faction_town_walker_male_troop, "trp_town_walker_5"),
        (faction_set_slot, "fac_culture_9", slot_faction_town_walker_female_troop, "trp_town_walker_6"),
        (faction_set_slot, "fac_culture_9", slot_faction_village_walker_male_troop, "trp_village_walker_5"),
        (faction_set_slot, "fac_culture_9", slot_faction_village_walker_female_troop, "trp_village_walker_6"),
        (faction_set_slot, "fac_culture_9", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_9", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_10", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_10", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_10", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_10", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_10", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_10", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_11", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_11", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_11", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_11", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_11", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_11", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_12", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_12", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_12", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_12", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_12", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_12", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_13", slot_faction_town_walker_male_troop, "trp_town_walker_5"),
        (faction_set_slot, "fac_culture_13", slot_faction_town_walker_female_troop, "trp_town_walker_6"),
        (faction_set_slot, "fac_culture_13", slot_faction_village_walker_male_troop, "trp_village_walker_5"),
        (faction_set_slot, "fac_culture_13", slot_faction_village_walker_female_troop, "trp_village_walker_6"),
        (faction_set_slot, "fac_culture_13", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_13", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_14", slot_faction_town_walker_male_troop, "trp_town_walker_5"),
        (faction_set_slot, "fac_culture_14", slot_faction_town_walker_female_troop, "trp_town_walker_6"),
        (faction_set_slot, "fac_culture_14", slot_faction_village_walker_male_troop, "trp_village_walker_5"),
        (faction_set_slot, "fac_culture_14", slot_faction_village_walker_female_troop, "trp_village_walker_6"),
        (faction_set_slot, "fac_culture_14", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_14", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_15", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_15", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_15", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_15", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_15", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_15", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_16", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_16", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_16", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_16", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_16", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_16", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_17", slot_faction_town_walker_male_troop, "trp_town_walker_3"),
        (faction_set_slot, "fac_culture_17", slot_faction_town_walker_female_troop, "trp_town_walker_4"),
        (faction_set_slot, "fac_culture_17", slot_faction_village_walker_male_troop, "trp_village_walker_3"),
        (faction_set_slot, "fac_culture_17", slot_faction_village_walker_female_troop, "trp_village_walker_4"),
        (faction_set_slot, "fac_culture_17", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_17", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_18", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_18", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_18", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_18", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_18", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_18", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_19", slot_faction_town_walker_male_troop, "trp_town_walker_3"),
        (faction_set_slot, "fac_culture_19", slot_faction_town_walker_female_troop, "trp_town_walker_4"),
        (faction_set_slot, "fac_culture_19", slot_faction_village_walker_male_troop, "trp_village_walker_3"),
        (faction_set_slot, "fac_culture_19", slot_faction_village_walker_female_troop, "trp_village_walker_4"),
        (faction_set_slot, "fac_culture_19", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_19", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_20", slot_faction_town_walker_male_troop, "trp_town_walker_3"),
        (faction_set_slot, "fac_culture_20", slot_faction_town_walker_female_troop, "trp_town_walker_4"),
        (faction_set_slot, "fac_culture_20", slot_faction_village_walker_male_troop, "trp_village_walker_3"),
        (faction_set_slot, "fac_culture_20", slot_faction_village_walker_female_troop, "trp_village_walker_4"),
        (faction_set_slot, "fac_culture_20", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_20", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_21", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_21", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_21", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_21", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_21", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_21", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_22", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_22", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_22", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_22", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_22", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_22", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_23", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_23", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_23", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_23", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_23", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_23", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_24", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_24", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_24", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_24", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_24", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_24", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_25", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_25", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_25", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_25", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_25", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_25", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_26", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_26", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_26", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_26", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_26", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_26", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_27", slot_faction_town_walker_male_troop, "trp_town_walker_3"),
        (faction_set_slot, "fac_culture_27", slot_faction_town_walker_female_troop, "trp_town_walker_4"),
        (faction_set_slot, "fac_culture_27", slot_faction_village_walker_male_troop, "trp_village_walker_3"),
        (faction_set_slot, "fac_culture_27", slot_faction_village_walker_female_troop, "trp_village_walker_4"),
        (faction_set_slot, "fac_culture_27", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_27", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_28", slot_faction_town_walker_male_troop, "trp_town_walker_3"),
        (faction_set_slot, "fac_culture_28", slot_faction_town_walker_female_troop, "trp_town_walker_4"),
        (faction_set_slot, "fac_culture_28", slot_faction_village_walker_male_troop, "trp_village_walker_3"),
        (faction_set_slot, "fac_culture_28", slot_faction_village_walker_female_troop, "trp_village_walker_4"),
        (faction_set_slot, "fac_culture_28", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_28", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_29", slot_faction_town_walker_male_troop, "trp_town_walker_3"),
        (faction_set_slot, "fac_culture_29", slot_faction_town_walker_female_troop, "trp_town_walker_4"),
        (faction_set_slot, "fac_culture_29", slot_faction_village_walker_male_troop, "trp_village_walker_3"),
        (faction_set_slot, "fac_culture_29", slot_faction_village_walker_female_troop, "trp_village_walker_4"),
        (faction_set_slot, "fac_culture_29", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_29", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_30", slot_faction_town_walker_male_troop, "trp_town_walker_3"),
        (faction_set_slot, "fac_culture_30", slot_faction_town_walker_female_troop, "trp_town_walker_4"),
        (faction_set_slot, "fac_culture_30", slot_faction_village_walker_male_troop, "trp_village_walker_3"),
        (faction_set_slot, "fac_culture_30", slot_faction_village_walker_female_troop, "trp_village_walker_4"),
        (faction_set_slot, "fac_culture_30", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_30", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_31", slot_faction_town_walker_male_troop, "trp_town_walker_3"),
        (faction_set_slot, "fac_culture_31", slot_faction_town_walker_female_troop, "trp_town_walker_4"),
        (faction_set_slot, "fac_culture_31", slot_faction_village_walker_male_troop, "trp_village_walker_3"),
        (faction_set_slot, "fac_culture_31", slot_faction_village_walker_female_troop, "trp_village_walker_4"),
        (faction_set_slot, "fac_culture_31", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_31", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        # Factions:
        (faction_set_slot, "fac_kingdom_1", slot_faction_culture, "fac_culture_1"),
        (faction_set_slot, "fac_kingdom_1", slot_faction_leader, "trp_kingdom_1_lord"),
        (troop_set_slot, "trp_kingdom_1_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_2", slot_faction_culture, "fac_culture_2"),
        (faction_set_slot, "fac_kingdom_2", slot_faction_leader, "trp_kingdom_2_lord"),
        (troop_set_slot, "trp_kingdom_2_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_3", slot_faction_culture, "fac_culture_3"),
        (faction_set_slot, "fac_kingdom_3", slot_faction_leader, "trp_kingdom_3_lord"),
        (troop_set_slot, "trp_kingdom_3_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_4", slot_faction_culture, "fac_culture_4"),
        (faction_set_slot, "fac_kingdom_4", slot_faction_leader, "trp_kingdom_4_lord"),
        (troop_set_slot, "trp_kingdom_4_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_5", slot_faction_culture, "fac_culture_5"),
        (faction_set_slot, "fac_kingdom_5", slot_faction_leader, "trp_kingdom_5_lord"),
        (troop_set_slot, "trp_kingdom_5_lord", slot_troop_renown, 1600),

        (faction_set_slot, "fac_kingdom_6", slot_faction_culture, "fac_culture_6"),
        (faction_set_slot, "fac_kingdom_6", slot_faction_leader, "trp_kingdom_6_lord"),
        (troop_set_slot, "trp_kingdom_6_lord", slot_troop_renown, 1000),

        (faction_set_slot, "fac_kingdom_7", slot_faction_culture, "fac_culture_7"),
        (faction_set_slot, "fac_kingdom_7", slot_faction_leader, "trp_kingdom_7_lord"),
        (troop_set_slot, "trp_kingdom_7_lord", slot_troop_renown, 900),

        (faction_set_slot, "fac_kingdom_8", slot_faction_culture, "fac_culture_8"),
        (faction_set_slot, "fac_kingdom_8", slot_faction_leader, "trp_kingdom_8_lord"),
        (troop_set_slot, "trp_kingdom_8_lord", slot_troop_renown, 1400),

        (faction_set_slot, "fac_kingdom_9", slot_faction_culture, "fac_culture_9"),
        (faction_set_slot, "fac_kingdom_9", slot_faction_leader, "trp_kingdom_9_lord"),
        (troop_set_slot, "trp_kingdom_9_lord", slot_troop_renown, 2000),

        (faction_set_slot, "fac_kingdom_10", slot_faction_culture, "fac_culture_10"),
        (faction_set_slot, "fac_kingdom_10", slot_faction_leader, "trp_kingdom_10_lord"),
        (troop_set_slot, "trp_kingdom_10_lord", slot_troop_renown, 800),

        (faction_set_slot, "fac_kingdom_11", slot_faction_culture, "fac_culture_11"),
        (faction_set_slot, "fac_kingdom_11", slot_faction_leader, "trp_kingdom_11_lord"),
        (troop_set_slot, "trp_kingdom_11_lord", slot_troop_renown, 1600),

        (faction_set_slot, "fac_kingdom_12", slot_faction_culture, "fac_culture_12"),
        (faction_set_slot, "fac_kingdom_12", slot_faction_leader, "trp_kingdom_12_lord"),
        (troop_set_slot, "trp_kingdom_12_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_13", slot_faction_culture, "fac_culture_13"),
        (faction_set_slot, "fac_kingdom_13", slot_faction_leader, "trp_kingdom_13_lord"),
        (troop_set_slot, "trp_kingdom_13_lord", slot_troop_renown, 2200),

        (faction_set_slot, "fac_kingdom_14", slot_faction_culture, "fac_culture_14"),
        (faction_set_slot, "fac_kingdom_14", slot_faction_leader, "trp_kingdom_14_lord"),
        (troop_set_slot, "trp_kingdom_14_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_15", slot_faction_culture, "fac_culture_15"),
        (faction_set_slot, "fac_kingdom_15", slot_faction_leader, "trp_kingdom_15_lord"),
        (troop_set_slot, "trp_kingdom_15_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_16", slot_faction_culture, "fac_culture_16"),
        (faction_set_slot, "fac_kingdom_16", slot_faction_leader, "trp_kingdom_16_lord"),
        (troop_set_slot, "trp_kingdom_16_lord", slot_troop_renown, 1000),

        (faction_set_slot, "fac_kingdom_17", slot_faction_culture, "fac_culture_17"),
        (faction_set_slot, "fac_kingdom_17", slot_faction_leader, "trp_kingdom_17_lord"),
        (troop_set_slot, "trp_kingdom_17_lord", slot_troop_renown, 1600),

        (faction_set_slot, "fac_kingdom_18", slot_faction_culture, "fac_culture_18"),
        (faction_set_slot, "fac_kingdom_18", slot_faction_leader, "trp_kingdom_18_lord"),
        (troop_set_slot, "trp_kingdom_18_lord", slot_troop_renown, 1600),

        (faction_set_slot, "fac_kingdom_19", slot_faction_culture, "fac_culture_19"),
        (faction_set_slot, "fac_kingdom_19", slot_faction_leader, "trp_kingdom_19_lord"),
        (troop_set_slot, "trp_kingdom_19_lord", slot_troop_renown, 1600),

        (faction_set_slot, "fac_kingdom_20", slot_faction_culture, "fac_culture_20"),
        (faction_set_slot, "fac_kingdom_20", slot_faction_leader, "trp_kingdom_20_lord"),
        (troop_set_slot, "trp_kingdom_20_lord", slot_troop_renown, 1800),

        (faction_set_slot, "fac_kingdom_21", slot_faction_culture, "fac_culture_21"),
        (faction_set_slot, "fac_kingdom_21", slot_faction_leader, "trp_kingdom_21_lord"),
        (troop_set_slot, "trp_kingdom_21_lord", slot_troop_renown, 900),

        (faction_set_slot, "fac_kingdom_22", slot_faction_culture, "fac_culture_22"),
        (faction_set_slot, "fac_kingdom_22", slot_faction_leader, "trp_kingdom_22_lord"),
        (troop_set_slot, "trp_kingdom_22_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_23", slot_faction_culture, "fac_culture_23"),
        (faction_set_slot, "fac_kingdom_23", slot_faction_leader, "trp_kingdom_23_lord"),
        (troop_set_slot, "trp_kingdom_23_lord", slot_troop_renown, 1400),

        (faction_set_slot, "fac_kingdom_24", slot_faction_culture, "fac_culture_24"),
        (faction_set_slot, "fac_kingdom_24", slot_faction_leader, "trp_kingdom_24_lord"),
        (troop_set_slot, "trp_kingdom_24_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_25", slot_faction_culture, "fac_culture_25"),
        (faction_set_slot, "fac_kingdom_25", slot_faction_leader, "trp_kingdom_25_lord"),
        (troop_set_slot, "trp_kingdom_25_lord", slot_troop_renown, 900),

        (faction_set_slot, "fac_kingdom_26", slot_faction_culture, "fac_culture_26"),
        (faction_set_slot, "fac_kingdom_26", slot_faction_leader, "trp_kingdom_26_lord"),
        (troop_set_slot, "trp_kingdom_26_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_27", slot_faction_culture, "fac_culture_27"),
        (faction_set_slot, "fac_kingdom_27", slot_faction_leader, "trp_kingdom_27_lord"),
        (troop_set_slot, "trp_kingdom_27_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_28", slot_faction_culture, "fac_culture_28"),
        (faction_set_slot, "fac_kingdom_28", slot_faction_leader, "trp_kingdom_28_lord"),
        (troop_set_slot, "trp_kingdom_28_lord", slot_troop_renown, 1600),

        (faction_set_slot, "fac_kingdom_29", slot_faction_culture, "fac_culture_29"),
        (faction_set_slot, "fac_kingdom_29", slot_faction_leader, "trp_kingdom_29_lord"),
        (troop_set_slot, "trp_kingdom_29_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_30", slot_faction_culture, "fac_culture_30"),
        (faction_set_slot, "fac_kingdom_30", slot_faction_leader, "trp_kingdom_30_lord"),
        (troop_set_slot, "trp_kingdom_30_lord", slot_troop_renown, 1800),

        (faction_set_slot, "fac_kingdom_31", slot_faction_culture, "fac_culture_31"),
        (faction_set_slot, "fac_kingdom_31", slot_faction_leader, "trp_kingdom_31_lord"),
        (troop_set_slot, "trp_kingdom_31_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_1", slot_faction_adjective, "str_kingdom_1_adjective"),
        (faction_set_slot, "fac_kingdom_2", slot_faction_adjective, "str_kingdom_2_adjective"),
        (faction_set_slot, "fac_kingdom_3", slot_faction_adjective, "str_kingdom_3_adjective"),
        (faction_set_slot, "fac_kingdom_4", slot_faction_adjective, "str_kingdom_4_adjective"),
        (faction_set_slot, "fac_kingdom_5", slot_faction_adjective, "str_kingdom_5_adjective"),
        (faction_set_slot, "fac_kingdom_6", slot_faction_adjective, "str_kingdom_6_adjective"),
        (faction_set_slot, "fac_kingdom_7", slot_faction_adjective, "str_kingdom_7_adjective"),
        (faction_set_slot, "fac_kingdom_8", slot_faction_adjective, "str_kingdom_8_adjective"),
        (faction_set_slot, "fac_kingdom_9", slot_faction_adjective, "str_kingdom_9_adjective"),
        (faction_set_slot, "fac_kingdom_10", slot_faction_adjective, "str_kingdom_10_adjective"),
        (faction_set_slot, "fac_kingdom_11", slot_faction_adjective, "str_kingdom_11_adjective"),
        (faction_set_slot, "fac_kingdom_12", slot_faction_adjective, "str_kingdom_12_adjective"),
        (faction_set_slot, "fac_kingdom_13", slot_faction_adjective, "str_kingdom_13_adjective"),
        (faction_set_slot, "fac_kingdom_14", slot_faction_adjective, "str_kingdom_14_adjective"),
        (faction_set_slot, "fac_kingdom_15", slot_faction_adjective, "str_kingdom_15_adjective"),
        (faction_set_slot, "fac_kingdom_16", slot_faction_adjective, "str_kingdom_16_adjective"),
        (faction_set_slot, "fac_kingdom_17", slot_faction_adjective, "str_kingdom_17_adjective"),
        (faction_set_slot, "fac_kingdom_18", slot_faction_adjective, "str_kingdom_18_adjective"),
        (faction_set_slot, "fac_kingdom_19", slot_faction_adjective, "str_kingdom_19_adjective"),
        (faction_set_slot, "fac_kingdom_20", slot_faction_adjective, "str_kingdom_20_adjective"),
        (faction_set_slot, "fac_kingdom_21", slot_faction_adjective, "str_kingdom_21_adjective"),
        (faction_set_slot, "fac_kingdom_22", slot_faction_adjective, "str_kingdom_22_adjective"),
        (faction_set_slot, "fac_kingdom_23", slot_faction_adjective, "str_kingdom_23_adjective"),
        (faction_set_slot, "fac_kingdom_24", slot_faction_adjective, "str_kingdom_24_adjective"),
        (faction_set_slot, "fac_kingdom_25", slot_faction_adjective, "str_kingdom_25_adjective"),
        (faction_set_slot, "fac_kingdom_26", slot_faction_adjective, "str_kingdom_26_adjective"),
        (faction_set_slot, "fac_kingdom_27", slot_faction_adjective, "str_kingdom_27_adjective"),
        (faction_set_slot, "fac_kingdom_28", slot_faction_adjective, "str_kingdom_28_adjective"),
        (faction_set_slot, "fac_kingdom_29", slot_faction_adjective, "str_kingdom_29_adjective"),
        (faction_set_slot, "fac_kingdom_30", slot_faction_adjective, "str_kingdom_30_adjective"),
        (faction_set_slot, "fac_kingdom_31", slot_faction_adjective, "str_kingdom_31_adjective"),
    ]),

    ("initialize_banners", [
        (faction_set_slot, "fac_kingdom_1", slot_faction_banner, "mesh_banner_kingdom_a"),
        (faction_set_slot, "fac_kingdom_2", slot_faction_banner, "mesh_banner_kingdom_b"),
        (faction_set_slot, "fac_kingdom_3", slot_faction_banner, "mesh_banner_kingdom_c"),
        (faction_set_slot, "fac_kingdom_4", slot_faction_banner, "mesh_banner_kingdom_d"),
        (faction_set_slot, "fac_kingdom_5", slot_faction_banner, "mesh_banner_kingdom_e"),
        (faction_set_slot, "fac_kingdom_6", slot_faction_banner, "mesh_banner_kingdom_f"),
        (faction_set_slot, "fac_kingdom_7", slot_faction_banner, "mesh_banner_kingdom_g"),
        (faction_set_slot, "fac_kingdom_8", slot_faction_banner, "mesh_banner_kingdom_h"),
        (faction_set_slot, "fac_kingdom_9", slot_faction_banner, "mesh_banner_kingdom_i"),
        (faction_set_slot, "fac_kingdom_10", slot_faction_banner, "mesh_banner_kingdom_j"),
        (faction_set_slot, "fac_kingdom_11", slot_faction_banner, "mesh_banner_kingdom_k"),
        (faction_set_slot, "fac_kingdom_12", slot_faction_banner, "mesh_banner_kingdom_l"),
        (faction_set_slot, "fac_kingdom_13", slot_faction_banner, "mesh_banner_kingdom_ll"),
        (faction_set_slot, "fac_kingdom_14", slot_faction_banner, "mesh_banner_kingdom_m"),
        (faction_set_slot, "fac_kingdom_15", slot_faction_banner, "mesh_banner_kingdom_n"),
        (faction_set_slot, "fac_kingdom_16", slot_faction_banner, "mesh_banner_kingdom_o"),
        (faction_set_slot, "fac_kingdom_17", slot_faction_banner, "mesh_banner_kingdom_p"),
        (faction_set_slot, "fac_kingdom_18", slot_faction_banner, "mesh_banner_kingdom_q"),
        (faction_set_slot, "fac_kingdom_19", slot_faction_banner, "mesh_banner_kingdom_r"),
        (faction_set_slot, "fac_kingdom_20", slot_faction_banner, "mesh_banner_kingdom_s"),
        (faction_set_slot, "fac_kingdom_21", slot_faction_banner, "mesh_banner_kingdom_t"),
        (faction_set_slot, "fac_kingdom_22", slot_faction_banner, "mesh_banner_kingdom_u"),
        (faction_set_slot, "fac_kingdom_23", slot_faction_banner, "mesh_banner_kingdom_v"),
        (faction_set_slot, "fac_kingdom_24", slot_faction_banner, "mesh_banner_kingdom_w"),
        (faction_set_slot, "fac_kingdom_25", slot_faction_banner, "mesh_banner_kingdom_x"),
        (faction_set_slot, "fac_kingdom_26", slot_faction_banner, "mesh_banner_kingdom_y"),
        (faction_set_slot, "fac_kingdom_27", slot_faction_banner, "mesh_banner_kingdom_z"),
        (faction_set_slot, "fac_kingdom_28", slot_faction_banner, "mesh_banner_kingdom_2a"),
        (faction_set_slot, "fac_kingdom_29", slot_faction_banner, "mesh_banner_kingdom_2b"),
        (faction_set_slot, "fac_kingdom_30", slot_faction_banner, "mesh_banner_kingdom_2c"),
        (faction_set_slot, "fac_kingdom_31", slot_faction_banner, "mesh_banner_kingdom_2d"),

        (try_for_range, ":cur_faction", npc_kingdoms_begin, npc_kingdoms_end),
            (faction_get_slot, ":cur_faction_king", ":cur_faction", slot_faction_leader),
            (faction_get_slot, ":cur_faction_banner", ":cur_faction", slot_faction_banner),
            (val_sub, ":cur_faction_banner", banner_meshes_begin),
            (val_add, ":cur_faction_banner", banner_scene_props_begin),
            (troop_set_slot, ":cur_faction_king", slot_troop_banner_scene_prop, ":cur_faction_banner"),
        (try_end),

        (try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
            (this_or_next|troop_slot_eq, ":kingdom_hero", slot_troop_occupation, slto_kingdom_hero),
            (troop_slot_eq, ":kingdom_hero", slot_troop_occupation, slto_inactive_pretender),

            (store_troop_faction, ":kingdom_hero_faction", ":kingdom_hero"),
            (neg|faction_slot_eq, ":kingdom_hero_faction", slot_faction_leader, ":kingdom_hero"),
            (try_begin),
                (eq, ":kingdom_hero_faction", "fac_kingdom_1"),
                (troop_set_slot, "trp_knight_1_1", slot_troop_banner_scene_prop, "spr_banner_cj"),
                (troop_set_slot, "trp_knight_1_2", slot_troop_banner_scene_prop, "spr_banner_ck"),
                (troop_set_slot, "trp_knight_1_3", slot_troop_banner_scene_prop, "spr_banner_cl"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_2"),
                (troop_set_slot, "trp_knight_2_1", slot_troop_banner_scene_prop, "spr_banner_cm"),
                (troop_set_slot, "trp_knight_2_2", slot_troop_banner_scene_prop, "spr_banner_cn"),
                (troop_set_slot, "trp_knight_2_3", slot_troop_banner_scene_prop, "spr_banner_co"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_3"),
                (troop_set_slot, "trp_knight_3_1", slot_troop_banner_scene_prop, "spr_banner_cp"),
                (troop_set_slot, "trp_knight_3_2", slot_troop_banner_scene_prop, "spr_banner_cq"),
                (troop_set_slot, "trp_knight_3_3", slot_troop_banner_scene_prop, "spr_banner_cr"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_4"),
                (troop_set_slot, "trp_knight_4_1", slot_troop_banner_scene_prop, "spr_banner_cs"),
                (troop_set_slot, "trp_knight_4_2", slot_troop_banner_scene_prop, "spr_banner_ct"),
                (troop_set_slot, "trp_knight_4_3", slot_troop_banner_scene_prop, "spr_banner_cu"),
                (troop_set_slot, "trp_knight_4_4", slot_troop_banner_scene_prop, "spr_banner_da"),
                (troop_set_slot, "trp_knight_4_5", slot_troop_banner_scene_prop, "spr_banner_db"),
                (troop_set_slot, "trp_knight_4_6", slot_troop_banner_scene_prop, "spr_banner_dc"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_5"),
                (troop_set_slot, "trp_knight_5_1", slot_troop_banner_scene_prop, "spr_banner_dd"),
                (troop_set_slot, "trp_knight_5_2", slot_troop_banner_scene_prop, "spr_banner_de"),
                (troop_set_slot, "trp_knight_5_3", slot_troop_banner_scene_prop, "spr_banner_df"),
                (troop_set_slot, "trp_knight_5_4", slot_troop_banner_scene_prop, "spr_banner_dg"),
                (troop_set_slot, "trp_knight_5_5", slot_troop_banner_scene_prop, "spr_banner_dh"),
                (troop_set_slot, "trp_knight_5_6", slot_troop_banner_scene_prop, "spr_banner_di"),
                (troop_set_slot, "trp_knight_5_7", slot_troop_banner_scene_prop, "spr_banner_dj"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_6"),
                (troop_set_slot, "trp_knight_6_1", slot_troop_banner_scene_prop, "spr_banner_dk"),
                (troop_set_slot, "trp_knight_6_2", slot_troop_banner_scene_prop, "spr_banner_dl"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_7"),
                (troop_set_slot, "trp_knight_7_1", slot_troop_banner_scene_prop, "spr_banner_dm"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_8"),
                (troop_set_slot, "trp_knight_8_1", slot_troop_banner_scene_prop, "spr_banner_dn"),
                (troop_set_slot, "trp_knight_8_2", slot_troop_banner_scene_prop, "spr_banner_do"),
                (troop_set_slot, "trp_knight_8_3", slot_troop_banner_scene_prop, "spr_banner_dp"),
                (troop_set_slot, "trp_knight_8_4", slot_troop_banner_scene_prop, "spr_banner_dq"),
                (troop_set_slot, "trp_knight_8_5", slot_troop_banner_scene_prop, "spr_banner_dr"),
                (troop_set_slot, "trp_knight_8_6", slot_troop_banner_scene_prop, "spr_banner_ds"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_9"),
                (troop_set_slot, "trp_knight_9_1", slot_troop_banner_scene_prop, "spr_banner_dt"),
                (troop_set_slot, "trp_knight_9_2", slot_troop_banner_scene_prop, "spr_banner_du"),
                (troop_set_slot, "trp_knight_9_3", slot_troop_banner_scene_prop, "spr_banner_ea"),
                (troop_set_slot, "trp_knight_9_4", slot_troop_banner_scene_prop, "spr_banner_eb"),
                (troop_set_slot, "trp_knight_9_5", slot_troop_banner_scene_prop, "spr_banner_ec"),
                (troop_set_slot, "trp_knight_9_6", slot_troop_banner_scene_prop, "spr_banner_ed"),
                (troop_set_slot, "trp_knight_9_7", slot_troop_banner_scene_prop, "spr_banner_ee"),
                (troop_set_slot, "trp_knight_9_8", slot_troop_banner_scene_prop, "spr_banner_ef"),
                (troop_set_slot, "trp_knight_9_9", slot_troop_banner_scene_prop, "spr_banner_eg"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_10"),
                (troop_set_slot, "trp_knight_10_1", slot_troop_banner_scene_prop, "spr_banner_eh"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_11"),
                (troop_set_slot, "trp_knight_11_1", slot_troop_banner_scene_prop, "spr_banner_ei"),
                (troop_set_slot, "trp_knight_11_2", slot_troop_banner_scene_prop, "spr_banner_ej"),
                (troop_set_slot, "trp_knight_11_3", slot_troop_banner_scene_prop, "spr_banner_ek"),
                (troop_set_slot, "trp_knight_11_4", slot_troop_banner_scene_prop, "spr_banner_el"),
                (troop_set_slot, "trp_knight_11_5", slot_troop_banner_scene_prop, "spr_banner_em"),
                (troop_set_slot, "trp_knight_11_6", slot_troop_banner_scene_prop, "spr_banner_en"),
                (troop_set_slot, "trp_knight_11_7", slot_troop_banner_scene_prop, "spr_banner_eo"),
                (troop_set_slot, "trp_knight_11_8", slot_troop_banner_scene_prop, "spr_banner_ep"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_12"),
                (troop_set_slot, "trp_knight_12_1", slot_troop_banner_scene_prop, "spr_banner_eq"),
                (troop_set_slot, "trp_knight_12_2", slot_troop_banner_scene_prop, "spr_banner_er"),
                (troop_set_slot, "trp_knight_12_3", slot_troop_banner_scene_prop, "spr_banner_es"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_13"),
                (troop_set_slot, "trp_knight_13_1", slot_troop_banner_scene_prop, "spr_banner_et"),
                (troop_set_slot, "trp_knight_13_2", slot_troop_banner_scene_prop, "spr_banner_eu"),
                (troop_set_slot, "trp_knight_13_3", slot_troop_banner_scene_prop, "spr_banner_f01"),
                (troop_set_slot, "trp_knight_13_4", slot_troop_banner_scene_prop, "spr_banner_f02"),
                (troop_set_slot, "trp_knight_13_5", slot_troop_banner_scene_prop, "spr_banner_f03"),
                (troop_set_slot, "trp_knight_13_6", slot_troop_banner_scene_prop, "spr_banner_f04"),
                (troop_set_slot, "trp_knight_13_7", slot_troop_banner_scene_prop, "spr_banner_f05"),
                (troop_set_slot, "trp_knight_13_8", slot_troop_banner_scene_prop, "spr_banner_f06"),
                (troop_set_slot, "trp_knight_13_9", slot_troop_banner_scene_prop, "spr_banner_f07"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_14"),
                (troop_set_slot, "trp_knight_14_1", slot_troop_banner_scene_prop, "spr_banner_f08"),
                (troop_set_slot, "trp_knight_14_2", slot_troop_banner_scene_prop, "spr_banner_f09"),
                (troop_set_slot, "trp_knight_14_3", slot_troop_banner_scene_prop, "spr_banner_f10"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_15"),
                (troop_set_slot, "trp_knight_15_1", slot_troop_banner_scene_prop, "spr_banner_f11"),
                (troop_set_slot, "trp_knight_15_2", slot_troop_banner_scene_prop, "spr_banner_f12"),
                (troop_set_slot, "trp_knight_15_3", slot_troop_banner_scene_prop, "spr_banner_f13"),
                (troop_set_slot, "trp_knight_15_4", slot_troop_banner_scene_prop, "spr_banner_f14"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_16"),
                (troop_set_slot, "trp_knight_16_1", slot_troop_banner_scene_prop, "spr_banner_f15"),
                (troop_set_slot, "trp_knight_16_2", slot_troop_banner_scene_prop, "spr_banner_f16"),
                (troop_set_slot, "trp_knight_16_3", slot_troop_banner_scene_prop, "spr_banner_f17"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_17"),
                (troop_set_slot, "trp_knight_17_1", slot_troop_banner_scene_prop, "spr_banner_f18"),
                (troop_set_slot, "trp_knight_17_2", slot_troop_banner_scene_prop, "spr_banner_f19"),
                (troop_set_slot, "trp_knight_17_3", slot_troop_banner_scene_prop, "spr_banner_f20"),
                (troop_set_slot, "trp_knight_17_4", slot_troop_banner_scene_prop, "spr_banner_g01"),
                (troop_set_slot, "trp_knight_17_5", slot_troop_banner_scene_prop, "spr_banner_h01"),
                (troop_set_slot, "trp_knight_17_6", slot_troop_banner_scene_prop, "spr_banner_h02"),
                (troop_set_slot, "trp_knight_17_7", slot_troop_banner_scene_prop, "spr_banner_h03"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_18"),
                (troop_set_slot, "trp_knight_18_1", slot_troop_banner_scene_prop, "spr_banner_h04"),
                (troop_set_slot, "trp_knight_18_2", slot_troop_banner_scene_prop, "spr_banner_h05"),
                (troop_set_slot, "trp_knight_18_3", slot_troop_banner_scene_prop, "spr_banner_h06"),
                (troop_set_slot, "trp_knight_18_4", slot_troop_banner_scene_prop, "spr_banner_h07"),
                (troop_set_slot, "trp_knight_18_5", slot_troop_banner_scene_prop, "spr_banner_h08"),
                (troop_set_slot, "trp_knight_18_6", slot_troop_banner_scene_prop, "spr_banner_h09"),
                (troop_set_slot, "trp_knight_18_7", slot_troop_banner_scene_prop, "spr_banner_h10"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_19"),
                (troop_set_slot, "trp_knight_19_1", slot_troop_banner_scene_prop, "spr_banner_h11"),
                (troop_set_slot, "trp_knight_19_2", slot_troop_banner_scene_prop, "spr_banner_h12"),
                (troop_set_slot, "trp_knight_19_3", slot_troop_banner_scene_prop, "spr_banner_h13"),
                (troop_set_slot, "trp_knight_19_4", slot_troop_banner_scene_prop, "spr_banner_h14"),
                (troop_set_slot, "trp_knight_19_5", slot_troop_banner_scene_prop, "spr_banner_h15"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_20"),
                (troop_set_slot, "trp_knight_20_1", slot_troop_banner_scene_prop, "spr_banner_h16"),
                (troop_set_slot, "trp_knight_20_2", slot_troop_banner_scene_prop, "spr_banner_h17"),
                (troop_set_slot, "trp_knight_20_3", slot_troop_banner_scene_prop, "spr_banner_h18"),
                (troop_set_slot, "trp_knight_20_4", slot_troop_banner_scene_prop, "spr_banner_h19"),
                (troop_set_slot, "trp_knight_20_5", slot_troop_banner_scene_prop, "spr_banner_h20"),
                (troop_set_slot, "trp_knight_20_6", slot_troop_banner_scene_prop, "spr_banner_h21"),
                (troop_set_slot, "trp_knight_20_7", slot_troop_banner_scene_prop, "spr_banner_i01"),
                (troop_set_slot, "trp_knight_20_8", slot_troop_banner_scene_prop, "spr_banner_i02"),
                (troop_set_slot, "trp_knight_20_9", slot_troop_banner_scene_prop, "spr_banner_i03"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_21"),
                (troop_set_slot, "trp_knight_21_1", slot_troop_banner_scene_prop, "spr_banner_i04"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_22"),
                (troop_set_slot, "trp_knight_22_1", slot_troop_banner_scene_prop, "spr_banner_i05"),
                (troop_set_slot, "trp_knight_22_2", slot_troop_banner_scene_prop, "spr_banner_i06"),
                (troop_set_slot, "trp_knight_22_3", slot_troop_banner_scene_prop, "spr_banner_i07"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_23"),
                (troop_set_slot, "trp_knight_23_1", slot_troop_banner_scene_prop, "spr_banner_i08"),
                (troop_set_slot, "trp_knight_23_2", slot_troop_banner_scene_prop, "spr_banner_i09"),
                (troop_set_slot, "trp_knight_23_3", slot_troop_banner_scene_prop, "spr_banner_i10"),
                (troop_set_slot, "trp_knight_23_4", slot_troop_banner_scene_prop, "spr_banner_i11"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_24"),
                (troop_set_slot, "trp_knight_24_1", slot_troop_banner_scene_prop, "spr_banner_i12"),
                (troop_set_slot, "trp_knight_24_2", slot_troop_banner_scene_prop, "spr_banner_i13"),
                (troop_set_slot, "trp_knight_24_3", slot_troop_banner_scene_prop, "spr_banner_i14"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_25"),
                (troop_set_slot, "trp_knight_25_1", slot_troop_banner_scene_prop, "spr_banner_i15"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_26"),
                (troop_set_slot, "trp_knight_26_1", slot_troop_banner_scene_prop, "spr_banner_i16"),
                (troop_set_slot, "trp_knight_26_2", slot_troop_banner_scene_prop, "spr_banner_i17"),
                (troop_set_slot, "trp_knight_26_3", slot_troop_banner_scene_prop, "spr_banner_i18"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_27"),
                (troop_set_slot, "trp_knight_27_1", slot_troop_banner_scene_prop, "spr_banner_i19"),
                (troop_set_slot, "trp_knight_27_2", slot_troop_banner_scene_prop, "spr_banner_i20"),
                (troop_set_slot, "trp_knight_27_3", slot_troop_banner_scene_prop, "spr_banner_i21"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_28"),
                (troop_set_slot, "trp_knight_28_1", slot_troop_banner_scene_prop, "spr_banner_k01"),
                (troop_set_slot, "trp_knight_28_2", slot_troop_banner_scene_prop, "spr_banner_k02"),
                (troop_set_slot, "trp_knight_28_3", slot_troop_banner_scene_prop, "spr_banner_k03"),
                (troop_set_slot, "trp_knight_28_4", slot_troop_banner_scene_prop, "spr_banner_k04"),
                (troop_set_slot, "trp_knight_28_5", slot_troop_banner_scene_prop, "spr_banner_k05"),
                (troop_set_slot, "trp_knight_28_6", slot_troop_banner_scene_prop, "spr_banner_k06"),
                (troop_set_slot, "trp_knight_28_7", slot_troop_banner_scene_prop, "spr_banner_k07"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_29"),
                (troop_set_slot, "trp_knight_29_1", slot_troop_banner_scene_prop, "spr_banner_k08"),
                (troop_set_slot, "trp_knight_29_2", slot_troop_banner_scene_prop, "spr_banner_k09"),
                (troop_set_slot, "trp_knight_29_3", slot_troop_banner_scene_prop, "spr_banner_k10"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_30"),
                (troop_set_slot, "trp_knight_30_1", slot_troop_banner_scene_prop, "spr_banner_k11"),
                (troop_set_slot, "trp_knight_30_2", slot_troop_banner_scene_prop, "spr_banner_k12"),
                (troop_set_slot, "trp_knight_30_3", slot_troop_banner_scene_prop, "spr_banner_k13"),
                (troop_set_slot, "trp_knight_30_4", slot_troop_banner_scene_prop, "spr_banner_k14"),
                (troop_set_slot, "trp_knight_30_5", slot_troop_banner_scene_prop, "spr_banner_k15"),
                (troop_set_slot, "trp_knight_30_6", slot_troop_banner_scene_prop, "spr_banner_k16"),
                (troop_set_slot, "trp_knight_30_7", slot_troop_banner_scene_prop, "spr_banner_k17"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_31"),
                (troop_set_slot, "trp_knight_31_1", slot_troop_banner_scene_prop, "spr_banner_k18"),
                (troop_set_slot, "trp_knight_31_2", slot_troop_banner_scene_prop, "spr_banner_k19"),
                (troop_set_slot, "trp_knight_31_3", slot_troop_banner_scene_prop, "spr_banner_k20"),
            (else_try),
                (troop_set_slot, "trp_kingdom_1_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_y"),
                (troop_set_slot, "trp_kingdom_2_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_r"),
                (troop_set_slot, "trp_kingdom_3_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_u"),
                (troop_set_slot, "trp_kingdom_4_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_ll"),
                (troop_set_slot, "trp_kingdom_5_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_i"),
                (troop_set_slot, "trp_kingdom_6_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_f"),
                (troop_set_slot, "trp_kingdom_7_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_l"),
                (troop_set_slot, "trp_kingdom_8_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_o"),
                (troop_set_slot, "trp_kingdom_9_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_q"),
                (troop_set_slot, "trp_kingdom_10_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_s"),
                (troop_set_slot, "trp_kingdom_11_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_v"),
            (try_end),
        (try_end),
    ]),

    ("initialize_town_factions",[
        # Give centers to factions
        (call_script, "script_give_center_to_faction_aux", "p_town_1", "fac_kingdom_1"),
        (call_script, "script_give_center_to_faction_aux", "p_town_2", "fac_kingdom_2"),
        (call_script, "script_give_center_to_faction_aux", "p_town_3", "fac_kingdom_12"),
        (call_script, "script_give_center_to_faction_aux", "p_town_4", "fac_kingdom_9"),
        (call_script, "script_give_center_to_faction_aux", "p_town_5", "fac_kingdom_16"),
        (call_script, "script_give_center_to_faction_aux", "p_town_6", "fac_kingdom_18"),
        (call_script, "script_give_center_to_faction_aux", "p_town_7", "fac_kingdom_15"),
        (call_script, "script_give_center_to_faction_aux", "p_town_8", "fac_kingdom_4"),
        (call_script, "script_give_center_to_faction_aux", "p_town_9", "fac_kingdom_26"),
        (call_script, "script_give_center_to_faction_aux", "p_town_10", "fac_kingdom_13"),
        (call_script, "script_give_center_to_faction_aux", "p_town_11", "fac_kingdom_9"),
        (call_script, "script_give_center_to_faction_aux", "p_town_12", "fac_kingdom_3"),
        (call_script, "script_give_center_to_faction_aux", "p_town_13", "fac_kingdom_23"),
        (call_script, "script_give_center_to_faction_aux", "p_town_14", "fac_kingdom_4"),
        (call_script, "script_give_center_to_faction_aux", "p_town_15", "fac_kingdom_11"),
        (call_script, "script_give_center_to_faction_aux", "p_town_16", "fac_kingdom_5"),
        (call_script, "script_give_center_to_faction_aux", "p_town_17", "fac_kingdom_8"),
        (call_script, "script_give_center_to_faction_aux", "p_town_18", "fac_kingdom_5"),
        (call_script, "script_give_center_to_faction_aux", "p_town_19", "fac_kingdom_19"),
        (call_script, "script_give_center_to_faction_aux", "p_town_20", "fac_kingdom_13"),
        (call_script, "script_give_center_to_faction_aux", "p_town_21", "fac_kingdom_27"),
        (call_script, "script_give_center_to_faction_aux", "p_town_22", "fac_kingdom_22"),

        (call_script, "script_give_center_to_faction_aux", "p_town_23", "fac_kingdom_9"),
        (call_script, "script_give_center_to_faction_aux", "p_town_24", "fac_kingdom_14"),
        (call_script, "script_give_center_to_faction_aux", "p_town_25", "fac_kingdom_21"),
        (call_script, "script_give_center_to_faction_aux", "p_town_26", "fac_kingdom_25"),
        (call_script, "script_give_center_to_faction_aux", "p_town_27", "fac_kingdom_13"),
        (call_script, "script_give_center_to_faction_aux", "p_town_28", "fac_kingdom_11"),
        (call_script, "script_give_center_to_faction_aux", "p_town_29", "fac_kingdom_24"),
        (call_script, "script_give_center_to_faction_aux", "p_town_30", "fac_kingdom_17"),
        (call_script, "script_give_center_to_faction_aux", "p_town_31", "fac_kingdom_30"),
        (call_script, "script_give_center_to_faction_aux", "p_town_32", "fac_kingdom_29"),
        (call_script, "script_give_center_to_faction_aux", "p_town_33", "fac_kingdom_30"),
        (call_script, "script_give_center_to_faction_aux", "p_town_34", "fac_kingdom_20"),
        (call_script, "script_give_center_to_faction_aux", "p_town_35", "fac_kingdom_28"),
        (call_script, "script_give_center_to_faction_aux", "p_town_36", "fac_kingdom_28"),
        (call_script, "script_give_center_to_faction_aux", "p_town_37", "fac_kingdom_20"),
        (call_script, "script_give_center_to_faction_aux", "p_town_38", "fac_kingdom_18"),
        (call_script, "script_give_center_to_faction_aux", "p_town_39", "fac_kingdom_20"),
        (call_script, "script_give_center_to_faction_aux", "p_town_40", "fac_kingdom_31"),
        (call_script, "script_give_center_to_faction_aux", "p_town_41", "fac_kingdom_6"),
        (call_script, "script_give_center_to_faction_aux", "p_town_42", "fac_kingdom_7"),


        (call_script, "script_give_center_to_faction_aux", "p_castle_1", "fac_kingdom_9"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_2", "fac_kingdom_13"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_3", "fac_kingdom_6"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_4", "fac_kingdom_2"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_5", "fac_kingdom_30"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_6", "fac_kingdom_30"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_7", "fac_kingdom_26"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_8", "fac_kingdom_4"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_9", "fac_kingdom_30"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_10", "fac_kingdom_2"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_11", "fac_kingdom_3"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_12", "fac_kingdom_1"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_13", "fac_kingdom_24"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_14", "fac_kingdom_3"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_15", "fac_kingdom_8"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_16", "fac_kingdom_8"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_17", "fac_kingdom_16"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_18", "fac_kingdom_11"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_19", "fac_kingdom_5"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_20", "fac_kingdom_1"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_21", "fac_kingdom_28"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_22", "fac_kingdom_13"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_23", "fac_kingdom_14"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_24", "fac_kingdom_27"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_25", "fac_kingdom_23"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_26", "fac_kingdom_26"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_27", "fac_kingdom_11"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_28", "fac_kingdom_28"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_29", "fac_kingdom_17"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_30", "fac_kingdom_8"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_31", "fac_kingdom_5"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_32", "fac_kingdom_4"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_33", "fac_kingdom_9"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_34", "fac_kingdom_22"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_35", "fac_kingdom_23"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_36", "fac_kingdom_11"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_37", "fac_kingdom_6"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_38", "fac_kingdom_24"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_39", "fac_kingdom_5"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_40", "fac_kingdom_4"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_41", "fac_kingdom_17"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_42", "fac_kingdom_10"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_43", "fac_kingdom_18"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_44", "fac_kingdom_12"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_45", "fac_kingdom_28"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_46", "fac_kingdom_15"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_47", "fac_kingdom_28"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_48", "fac_kingdom_15"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_49", "fac_kingdom_22"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_50", "fac_kingdom_19"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_51", "fac_kingdom_9"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_52", "fac_kingdom_9"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_53", "fac_kingdom_13"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_54", "fac_kingdom_18"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_55", "fac_kingdom_18"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_56", "fac_kingdom_18"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_57", "fac_kingdom_13"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_58", "fac_kingdom_30"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_59", "fac_kingdom_17"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_60", "fac_kingdom_31"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_61", "fac_kingdom_12"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_62", "fac_kingdom_20"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_63", "fac_kingdom_20"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_64", "fac_kingdom_20"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_65", "fac_kingdom_13"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_66", "fac_kingdom_20"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_67", "fac_kingdom_29"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_68", "fac_kingdom_19"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_69", "fac_kingdom_17"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_70", "fac_kingdom_27"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_71", "fac_kingdom_20"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_72", "fac_kingdom_19"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_73", "fac_kingdom_17"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_74", "fac_kingdom_29"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_75", "fac_kingdom_31"),

        # give towns to great lords
        (call_script, "script_give_center_to_lord", "p_town_1",  "trp_kingdom_1_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_2",  "trp_kingdom_2_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_3",  "trp_kingdom_12_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_4",  "trp_knight_9_1", 0),
        (call_script, "script_give_center_to_lord", "p_town_5",  "trp_kingdom_16_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_6",  "trp_kingdom_18_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_7",  "trp_kingdom_15_lord", 0),

        (call_script, "script_give_center_to_lord", "p_town_8",  "trp_knight_4_1", 0),
        (call_script, "script_give_center_to_lord", "p_town_9",  "trp_kingdom_26_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_10", "trp_knight_13_1", 0),
        (call_script, "script_give_center_to_lord", "p_town_11", "trp_knight_9_2", 0),
        (call_script, "script_give_center_to_lord", "p_town_12", "trp_kingdom_3_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_13", "trp_kingdom_23_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_14", "trp_kingdom_4_lord", 0),

        (call_script, "script_give_center_to_lord", "p_town_15", "trp_knight_11_1", 0),
        (call_script, "script_give_center_to_lord", "p_town_16", "trp_knight_5_1", 0),
        (call_script, "script_give_center_to_lord", "p_town_17", "trp_kingdom_8_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_18", "trp_kingdom_5_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_19", "trp_kingdom_19_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_20",  "trp_knight_13_2", 0),
        (call_script, "script_give_center_to_lord", "p_town_21",  "trp_kingdom_27_lord", 0),

        (call_script, "script_give_center_to_lord", "p_town_22",  "trp_kingdom_22_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_23",  "trp_kingdom_9_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_24",  "trp_kingdom_14_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_25",  "trp_kingdom_21_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_26",  "trp_kingdom_25_lord", 0),

        (call_script, "script_give_center_to_lord", "p_town_27",  "trp_kingdom_13_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_28",  "trp_kingdom_11_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_29", "trp_kingdom_24_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_30", "trp_kingdom_17_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_31", "trp_kingdom_30_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_32", "trp_kingdom_29_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_33", "trp_knight_30_1", 0),

        (call_script, "script_give_center_to_lord", "p_town_34", "trp_kingdom_20_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_35", "trp_knight_28_1", 0),
        (call_script, "script_give_center_to_lord", "p_town_36", "trp_kingdom_28_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_37", "trp_knight_20_2", 0),
        (call_script, "script_give_center_to_lord", "p_town_38", "trp_knight_18_1", 0),
        (call_script, "script_give_center_to_lord", "p_town_39", "trp_knight_20_1", 0),
        (call_script, "script_give_center_to_lord", "p_town_40", "trp_kingdom_31_lord", 0),

        (call_script, "script_give_center_to_lord", "p_town_41", "trp_kingdom_6_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_42", "trp_kingdom_7_lord", 0),

        (call_script, "script_assign_lords_to_empty_centers"),

        # set original factions
        (try_for_range, ":center_no", centers_begin, centers_end),
            (store_faction_of_party, ":original_faction", ":center_no"),
            (faction_get_slot, ":culture", ":original_faction", slot_faction_culture),
            (party_set_slot, ":center_no", slot_center_culture,  ":culture"),
            (party_set_slot, ":center_no", slot_center_original_faction,  ":original_faction"),
            (party_set_slot, ":center_no", slot_center_ex_faction,  ":original_faction"),
        (try_end),

        # set territorial disputes
        (party_set_slot, "p_castle_10", slot_center_ex_faction, "fac_kingdom_5"), # gewissae quiere Hlew ceaster de suth seaxna
        (party_set_slot, "p_castle_37", slot_center_ex_faction, "fac_kingdom_5"), # gewissae quiere caer baddan de Hwice
        (party_set_slot, "p_castle_30", slot_center_ex_faction, "fac_kingdom_5"), # gewissae quiere caer durnac de Dumnonia
        (party_set_slot, "p_town_16", slot_center_ex_faction, "fac_kingdom_9"), # Mierce quiere Dorce Ceaster de gewissae
        (party_set_slot, "p_town_10", slot_center_ex_faction, "fac_kingdom_9"), #Mierce quiere Eorfewic de Bernaccia
        (party_set_slot, "p_town_23", slot_center_ex_faction, "fac_kingdom_13"), #Bernacia quiere Licidfeld de Mierce
        (party_set_slot, "p_town_24", slot_center_ex_faction, "fac_kingdom_13"), #Bernaccia quiere Linnuis de Lindisware
        (party_set_slot, "p_castle_61", slot_center_ex_faction, "fac_kingdom_13"), #Bernaccia quiere Din Baer de Goddodin
        (party_set_slot, "p_castle_48",   slot_center_ex_faction, "fac_kingdom_18"), #Alt Clut atacara reghed
        (party_set_slot, "p_town_34",   slot_center_ex_faction, "fac_kingdom_19"), #Dal Riata quiere Dun Duirn de los pictos
        (party_set_slot, "p_castle_50",   slot_center_ex_faction, "fac_kingdom_20"), #pictos atacaran a dal riata
        (party_set_slot, "p_castle_43",   slot_center_ex_faction, "fac_kingdom_20"), #pictos atacaran a alt cult
        (party_set_slot, "p_castle_24",   slot_center_ex_faction, "fac_kingdom_28"), #Desmumu quiere Ard de Laigin
        (party_set_slot, "p_town_40",   slot_center_ex_faction, "fac_kingdom_29"), #Ulaid quiere Emain Mancha de Airgialla
        (party_set_slot, "p_castle_72",   slot_center_ex_faction, "fac_kingdom_30"), #Ui Neill quiere Sebuirge de Dal Riata
        (party_set_slot, "p_castle_74",   slot_center_ex_faction, "fac_kingdom_30"), #Ui Neill quiere Magh rath de Ulaid
        (party_set_slot, "p_castle_17",   slot_center_ex_faction, "fac_kingdom_11"), #Pengwern quiere Caer Legionis de Crafu
        (party_set_slot, "p_castle_33",   slot_center_ex_faction, "fac_kingdom_4"), #Anglia quiere Ligor Ceaster de Mercia

        # todo: what this does?
        # they seem to depend on which faction has which town
        (call_script, "script_update_village_market_towns"),
        # todo: what this does?
        (call_script, "script_find_neighbors"),
    ]),

    # sets the default availability of notes
    ("initialize_notes", [
        # tableaus
        (try_for_range, ":troop_no", "trp_player", "trp_merchants_end"),
            (add_troop_note_tableau_mesh, ":troop_no", "tableau_troop_note_mesh"),
        (try_end),

        (try_for_range, ":center_no", centers_begin, centers_end),
            (add_party_note_tableau_mesh, ":center_no", "tableau_center_note_mesh"),
        (try_end),

        (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
            (is_between, ":faction_no", "fac_kingdom_1", kingdoms_end), #Exclude player kingdom
            (add_faction_note_tableau_mesh, ":faction_no", "tableau_faction_note_mesh"),
        (else_try),
            (add_faction_note_tableau_mesh, ":faction_no", "tableau_faction_note_mesh_banner"),
        (try_end),

        # notes
        (troop_set_note_available, "trp_player", 1),
        (troop_set_note_available, "trp_especiales_3", 1),
        (troop_set_note_available, "trp_npcneko", 1),
        (troop_set_note_available, "trp_iniau", 1),
        (troop_set_note_available, "trp_thyr", 1),
        (troop_set_note_available, "trp_npc_tradecompanion", 1),

        (try_for_range, ":troop_no", kings_begin, kings_end),
            (troop_set_note_available, ":troop_no", 1),
        (try_end),

        (try_for_range, ":troop_no", lords_begin, lords_end),
            (troop_set_note_available, ":troop_no", 1),
        (try_end),

        (try_for_range, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
            (troop_set_note_available, ":troop_no", 1),
        (try_end),
        (troop_set_note_available, "trp_knight_1_1_wife", 0),

        (try_for_range, ":troop_no", pretenders_begin, pretenders_end),
            (troop_set_note_available, ":troop_no", 1),
        (try_end),

        #Lady and companion notes become available as you meet/recruit them

        (try_for_range, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
            (faction_set_note_available, ":faction_no", 1),
        (try_end),
        (faction_set_note_available, "fac_neutral", 0),

        (try_for_range, ":party_no", centers_begin, centers_end),
            (party_set_note_available, ":party_no", 1),
        (try_end),
    ]),

    ("initialize_pretenders", [
        (troop_set_slot, "trp_kingdom_1_pretender", slot_troop_original_faction2, "fac_kingdom_1"),
        (troop_set_slot, "trp_kingdom_2_pretender", slot_troop_original_faction2, "fac_kingdom_2"),
        (troop_set_slot, "trp_kingdom_3_pretender", slot_troop_original_faction2, "fac_kingdom_3"),
        (troop_set_slot, "trp_kingdom_4_pretender", slot_troop_original_faction2, "fac_kingdom_4"),
        (troop_set_slot, "trp_kingdom_5_pretender", slot_troop_original_faction2, "fac_kingdom_5"),
        (troop_set_slot, "trp_kingdom_6_pretender", slot_troop_original_faction2, "fac_kingdom_6"),
        (troop_set_slot, "trp_kingdom_7_pretender", slot_troop_original_faction2, "fac_kingdom_7"),
        (troop_set_slot, "trp_kingdom_8_pretender", slot_troop_original_faction2, "fac_kingdom_8"),
        (troop_set_slot, "trp_kingdom_9_pretender", slot_troop_original_faction2, "fac_kingdom_9"),
        (troop_set_slot, "trp_kingdom_10_pretender", slot_troop_original_faction2, "fac_kingdom_10"),
        (troop_set_slot, "trp_kingdom_11_pretender", slot_troop_original_faction2, "fac_kingdom_11"),

        (troop_set_slot, "trp_kingdom_1_pretender", slot_troop_original_faction, "fac_kingdom_26"),
        (troop_set_slot, "trp_kingdom_2_pretender", slot_troop_original_faction, "fac_kingdom_19"),
        (troop_set_slot, "trp_kingdom_3_pretender", slot_troop_original_faction, "fac_kingdom_22"),
        (troop_set_slot, "trp_kingdom_4_pretender", slot_troop_original_faction, "fac_kingdom_13"),
        (troop_set_slot, "trp_kingdom_5_pretender", slot_troop_original_faction, "fac_kingdom_9"),
        (troop_set_slot, "trp_kingdom_6_pretender", slot_troop_original_faction, "fac_kingdom_6"),
        (troop_set_slot, "trp_kingdom_7_pretender", slot_troop_original_faction, "fac_kingdom_12"),
        (troop_set_slot, "trp_kingdom_8_pretender", slot_troop_original_faction, "fac_kingdom_16"),
        (troop_set_slot, "trp_kingdom_9_pretender", slot_troop_original_faction, "fac_kingdom_18"),
        (troop_set_slot, "trp_kingdom_10_pretender", slot_troop_original_faction, "fac_kingdom_20"),
        (troop_set_slot, "trp_kingdom_11_pretender", slot_troop_original_faction, "fac_kingdom_23"),

        (try_for_range, ":pretender", pretenders_begin, pretenders_end),
            (troop_set_slot, ":pretender", slot_lord_reputation_type, lrep_none),
        (try_end),
    ]),

    # initializes quantities that are dynamic in the game
    ("game_start_dynamic", [
        (assign, "$is_game_start", 1),

        # npcs renown
        (try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
            (this_or_next|troop_slot_eq, ":kingdom_hero", slot_troop_occupation, slto_kingdom_hero),
            (troop_slot_eq, ":kingdom_hero", slot_troop_occupation, slto_inactive_pretender),

            (store_troop_faction, ":kingdom_hero_faction", ":kingdom_hero"),
            (neg|faction_slot_eq, ":kingdom_hero_faction", slot_faction_leader, ":kingdom_hero"),

            (store_character_level, ":level", ":kingdom_hero"),
            (store_mul, ":renown", ":level", ":level"),
            (val_div, ":renown", 4), #for top lord, it is about 400

            (troop_get_slot, ":age", ":kingdom_hero", slot_troop_age),
            (store_mul, ":age_addition", ":age", ":age"),
            (val_div, ":age_addition", 8),
            (val_add, ":renown", ":age_addition"),

            (try_begin),
                (faction_slot_eq, ":kingdom_hero_faction", slot_faction_leader, ":kingdom_hero"),
                (store_random_in_range, ":random_renown", 350, 500),
            (else_try),
                (store_random_in_range, ":random_renown", 100, 300),
            (try_end),

            (val_add, ":renown", ":random_renown"),
            (troop_set_slot, ":kingdom_hero", slot_troop_renown, ":renown"),
        (try_end),

        # start random wars
        (try_for_range, ":unused", 0, 18),
            (call_script, "script_randomly_start_war_peace_new"),
        (try_end),

        # initialize random truces
        (try_for_range, ":kingdom_a", kingdoms_begin, kingdoms_end),
            (store_add, ":already_done", ":kingdom_a", 1),    #hit every relationship just ONCE
            (try_for_range, ":kingdom_b", ":already_done", kingdoms_end),
                (store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
                (val_sub, ":truce_slot", kingdoms_begin),
                (faction_get_slot, ":truce_days", ":kingdom_b", ":truce_slot"),
                (ge, ":truce_days", dplmc_treaty_truce_days_initial),

                (store_random_in_range, reg0, 1, dplmc_treaty_truce_days_initial),
                (val_sub, ":truce_days", reg0),
                (val_add, ":truce_days", 1),    #leave a minimum of 2 days
                (faction_set_slot, ":kingdom_b", ":truce_slot", ":truce_days"),
                (store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
                (val_sub, ":truce_slot", kingdoms_begin),
                (faction_set_slot, ":kingdom_a", ":truce_slot", ":truce_days"),
            (try_end),
        (try_end),

        (try_for_range, ":village_no", villages_begin, villages_end),
            (call_script, "script_refresh_village_merchant_inventory", ":village_no"),
        (try_end),

        (call_script, "script_refresh_center_inventories"),
        (call_script, "script_refresh_center_armories"),
        (call_script, "script_refresh_center_weaponsmiths"),
        (call_script, "script_refresh_center_stables"),
        (call_script, "script_refresh_special_merchants"),

        # Set original faction
        (try_for_range, ":troop_id", original_kingdom_heroes_begin, active_npcs_end),
            (try_begin),
                (store_troop_faction, ":faction_id", ":troop_id"),
                (is_between, ":faction_id", kingdoms_begin, kingdoms_end),
                (troop_set_slot, ":troop_id", slot_troop_original_faction, ":faction_id"),
                (try_begin),
                    (is_between, ":troop_id", pretenders_begin, pretenders_end),
                    (faction_set_slot, ":faction_id", slot_faction_has_rebellion_chance, 1),
                (try_end),
            (try_end),

            (store_random_in_range, ":random_gold", 8000, 20000),
            (assign, ":initial_wealth", ":random_gold"),
            (store_div, ":travel_money", ":initial_wealth", 10),
            (troop_add_gold, ":troop_id", ":travel_money"),
            (val_sub, ":initial_wealth", ":travel_money"),
            (val_abs, ":initial_wealth"),

            (try_begin),
                (store_troop_faction, ":faction", ":troop_id"),
                (faction_slot_eq, ":faction", slot_faction_leader, ":troop_id"),
                (assign, ":initial_wealth", 30000),
            (try_end),
            (troop_set_slot, ":troop_id", slot_troop_wealth, ":initial_wealth"),
        (try_end),

        # Add initial wealth, garrisons and garrison upgrades
        (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
            (assign, ":initial_wealth", 2500),
            (try_begin),
                (is_between, ":center_no", towns_begin, towns_end),
                (val_mul, ":initial_wealth", 2),
            (try_end),
            (party_set_slot, ":center_no", slot_town_wealth, ":initial_wealth"),

            (assign, ":garrison_strength", 15),
            (try_begin),
                (party_slot_eq, ":center_no", slot_party_type, spt_town),
                (assign, ":garrison_strength", 40),
            (try_end),

            (try_for_range, ":unused", 0, ":garrison_strength"),
                (call_script, "script_cf_reinforce_party", ":center_no"),
            (try_end),
            (store_div, ":xp_rounds", ":garrison_strength", 5),
            (val_add, ":xp_rounds", 2),

            (options_get_campaign_ai, ":reduce_campaign_ai"),

            (try_begin), #hard
                (eq, ":reduce_campaign_ai", 0),
                (assign, ":xp_addition_for_centers", 9500),
            (else_try), #moderate
                (eq, ":reduce_campaign_ai", 1),
                (assign, ":xp_addition_for_centers", 7000),
            (else_try), #easy
                (eq, ":reduce_campaign_ai", 2),
                (assign, ":xp_addition_for_centers", 4500),
            (try_end),

            (try_for_range, ":unused", 0, ":xp_rounds"),
                (party_upgrade_with_xp, ":center_no", ":xp_addition_for_centers", 0),
            (try_end),

            # Fill town food stores up to half the limit
            (call_script, "script_center_get_food_store_limit", ":center_no"),
            (assign, ":food_store_limit", reg0),
            (val_div, ":food_store_limit", 2),
            (party_set_slot, ":center_no", slot_party_food_store, ":food_store_limit"),

            # create lord parties
            (party_get_slot, ":center_lord", ":center_no", slot_town_lord),
            (ge, ":center_lord", 1),
            (troop_slot_eq, ":center_lord", slot_troop_leaded_party, 0),
            (assign, "$g_there_is_no_avaliable_centers", 0),
            (call_script, "script_create_kingdom_hero_party", ":center_lord", ":center_no"),
            (assign, ":lords_party", "$pout_party"),
            (party_attach_to_party, ":lords_party", ":center_no"),
            (party_set_slot, ":center_no", slot_town_player_odds, 1000),
        (try_end),

        # initial relations
        # todo: make this an N(N-1)/2 script instead of N^2
        (try_for_range, ":lord", original_kingdom_heroes_begin, active_npcs_end),
            (troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
            (troop_get_slot, ":lord_faction", ":lord", slot_troop_original_faction),

            (try_for_range, ":other_hero", original_kingdom_heroes_begin, active_npcs_end),
                (this_or_next|troop_slot_eq, ":other_hero", slot_troop_occupation, slto_kingdom_hero),
                (troop_slot_eq, ":other_hero", slot_troop_occupation, slto_inactive_pretender),
                (troop_get_slot, ":other_hero_faction", ":other_hero", slot_troop_original_faction),
                (eq, ":other_hero_faction", ":lord_faction"),

                (call_script, "script_troop_get_family_relation_to_troop", ":lord", ":other_hero"),
                (call_script, "script_troop_change_relation_with_troop", ":lord", ":other_hero", reg0),

                (store_random_in_range, ":random", 0, 11), #this will be scored twice between two kingdom heroes, so starting relation will average 10. Between lords and pretenders it will average 7.5
                (call_script, "script_troop_change_relation_with_troop", ":lord", ":other_hero", ":random"),
            (try_end),
        (try_end),

        # do about 5 years' worth of political history (assuming 3 random checks a day)
        (try_for_range, ":unused", 0, 5000),
            (call_script, "script_cf_random_political_event"),
        (try_end),

        # measure stability of the realm
        (try_for_range, ":kingdom", kingdoms_begin, kingdoms_end),
            (call_script, "script_evaluate_realm_stability", ":kingdom"),
        (try_end),

        # assign love interests to unmarried male lords
        (try_for_range, ":cur_troop", lords_begin, lords_end),
            (troop_slot_eq, ":cur_troop", slot_troop_spouse, -1),
            (neg|is_between, ":cur_troop", kings_begin, kings_end),
            (neg|is_between, ":cur_troop", pretenders_begin, pretenders_end),

            (call_script, "script_assign_troop_love_interests", ":cur_troop"),
        (try_end),

        (store_random_in_range, "$romantic_attraction_seed", 0, 5),

        (try_for_range, ":unused", 0, 10),
            (call_script, "script_spawn_bandits"),
        (try_end),

        # add looters around each village with 1/5 probability.
        (set_spawn_radius, 5),
        (try_for_range, ":cur_village", villages_begin, villages_end),
            (store_random_in_range, ":random_value", 0, 5),
            (eq, ":random_value", 0),
            (spawn_around_party, ":cur_village", "pt_looters"),
        (try_end),

        (call_script, "script_update_mercenary_units_of_towns"),
        (call_script, "script_update_ransom_brokers"),
        (call_script, "script_update_tavern_travellers"),
        (call_script, "script_update_tavern_minstrels"),
        (call_script, "script_update_booksellers"),

        (try_for_range, ":village_no", villages_begin, villages_end),
            (call_script, "script_update_volunteer_troops_in_village", ":village_no"),
        (try_end),

        (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
            (call_script, "script_update_faction_notes", ":cur_kingdom"),
            (store_random_in_range, ":random_no", -60, 0),
            (faction_set_slot, ":cur_kingdom", slot_faction_last_offensive_concluded, ":random_no"),
        (try_end),

        (try_for_range, ":cur_troop", original_kingdom_heroes_begin, active_npcs_end),
            (call_script, "script_update_troop_notes", ":cur_troop"),
        (try_end),

        (try_for_range, ":cur_center", centers_begin, centers_end),
            (call_script, "script_update_center_notes", ":cur_center"),
        (try_end),

        (call_script, "script_update_troop_notes", "trp_player"),

        # Place kingdom ladies
        (try_for_range, ":troop_id", kingdom_ladies_begin, kingdom_ladies_end),
            (call_script, "script_get_kingdom_lady_social_determinants", ":troop_id"),
            (troop_set_slot, ":troop_id", slot_troop_cur_center, reg1),
        (try_end),

        (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
            (call_script, "script_faction_recalculate_strength", ":faction_no"),
        (try_end),

        (party_set_slot, "p_main_party", slot_party_unrested_morale_penalty, 0),
        (call_script, "script_get_player_party_morale_values"),
        (party_set_morale, "p_main_party", reg0),

        (call_script, "script_initialize_acres"),

        # todo: this should not be needed, but issue #6 makes it required.
        (try_for_range, ":cur_center", centers_begin, centers_end),
            (party_set_slot, ":cur_center", slot_spy_in_town, 0),
        (try_end),
        (assign, "$is_game_start", 0),
    ]),
]
