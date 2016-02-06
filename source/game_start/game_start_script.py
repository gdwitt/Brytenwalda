from source.header_operations import *
from source.header_common import s5, reg0, reg1

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
            (party_set_slot, ":center_no", slot_town_sacked, 0),
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
