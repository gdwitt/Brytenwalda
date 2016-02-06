from source.header_operations import *
from source.header_common import *
from source.header_triggers import *
from source.header_mission_templates import *

from source.module_constants import *


###########################formations chief empieza####################
# Formations triggers v3 by motomataru, Warband port

formations_triggers = [
    (ti_before_mission_start, 0, 0, [], [
        (assign, "$gk_order", 0),
        (assign, "$gk_order_hold_over_there", 0),
        (assign, "$last_player_trigger", Far_Away),
        (assign, "$native_display", 0),
        (assign, "$rethink_on_formation", 0),
        (try_for_range, ":team", 0, 4),
            (try_for_range, ":division", 0, 9),
                (store_add, ":slot", "slot_team_d0_type", ":division"),
                (team_set_slot, ":team", ":slot", sdt_unknown),
                (store_add, ":slot", "slot_team_d0_speed_limit", ":division"),
                (team_set_slot, ":team", ":slot", 10),
                (store_add, ":slot", "slot_team_d0_target_team", ":division"),
                (team_set_slot, ":team", ":slot", -1),
                (store_add, ":slot", "slot_team_d0_fclock", ":division"),
                (team_set_slot, ":team", ":slot", 1),
            (try_end),
        (try_end),
        #should it be getitemscorewithimod?
        (call_script, "script_init_item_score"),
        # # Autoloot improved by rubik end

    ]),

    # Start troops in formation
    (ti_after_mission_start, 0, ti_once, [(neg|game_in_multiplayer_mode)], [
        (get_player_agent_no, "$fplayer_agent_no"),
        (agent_get_group, "$fplayer_team_no", "$fplayer_agent_no"),
        (call_script, "script_store_battlegroup_data"),

        #get modal team faction
        (store_sub, ":num_kingdoms", kingdoms_end, kingdoms_begin),
        (store_mul, ":end", 4, ":num_kingdoms"),
        (try_for_range, ":slot", 0, ":end"),
            (team_set_slot, scratch_team, ":slot", 0),
        (try_end),
        (try_for_agents, ":cur_agent"),
            (agent_is_human, ":cur_agent"),
            (agent_get_group, ":cur_team", ":cur_agent"),
            (agent_get_troop_id, ":cur_troop", ":cur_agent"),
            (store_troop_faction, ":cur_faction", ":cur_troop"),
            (is_between, ":cur_faction", kingdoms_begin, kingdoms_end),
            (store_mul, ":slot", ":cur_team", ":num_kingdoms"),
            (val_sub, ":cur_faction", kingdoms_begin),
            (val_add, ":slot", ":cur_faction"),
            (team_get_slot, ":count", scratch_team, ":slot"),
            (val_add, ":count", 1),
            (team_set_slot, scratch_team, ":slot", ":count"),
        (try_end),

        (try_for_range, ":team", 0, 4),
            (team_slot_ge, ":team", "slot_team_size", 1),
            (team_get_leader, ":fleader", ":team"),
            (try_begin),
                (ge, ":fleader", 0),
                (agent_get_troop_id, ":fleader_troop", ":fleader"),
                (store_troop_faction, ":team_faction", ":fleader_troop"),
            (else_try),
                (assign, ":team_faction", 0),
                (assign, ":modal_count", 0),
                (store_mul, ":begin", ":team", ":num_kingdoms"),
                (store_add, ":end", ":begin", ":num_kingdoms"),
                (try_for_range, ":slot", ":begin", ":end"),
                    (team_get_slot, ":count", scratch_team, ":slot"),
                    (gt, ":count", ":modal_count"),
                    (assign, ":modal_count", ":count"),
                    (store_sub, ":team_faction", ":begin", ":slot"),
                    (val_add, ":team_faction", kingdoms_begin),
                (try_end),
            (try_end),
            (team_set_slot, ":team", "slot_team_faction", ":team_faction"),
        (try_end),

        (assign, ":depth_cavalry", 0),
        (try_begin),
            (eq, "$formation_off", 0),
            (display_message, "@Forming ranks."),
            #keep cavalry on the map
            (assign, ":largest_mounted_division_size", 0),
            (try_for_range, ":division", 0, 9),
                (store_add, ":slot", "slot_team_d0_type", ":division"),
                (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
                (team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
                (store_add, ":slot", "slot_team_d0_size", ":division"),
                (team_get_slot, reg0, "$fplayer_team_no", ":slot"),
                (lt, ":largest_mounted_division_size", reg0),
                (assign, ":largest_mounted_division_size", reg0),
            (try_end),

            (try_begin),
                (gt, ":largest_mounted_division_size", 0),
                (val_mul, ":largest_mounted_division_size", 2),
                (convert_to_fixed_point, ":largest_mounted_division_size"),
                (store_sqrt, ":depth_cavalry", ":largest_mounted_division_size"),
                (convert_from_fixed_point, ":depth_cavalry"),
                (val_sub, ":depth_cavalry", 1),

                (store_mul, reg0, formation_start_spread_out, 50),
                (val_add, reg0, formation_minimum_spacing_horse_length),
                (val_mul, ":depth_cavalry", reg0),

                (store_mul, ":depth_infantry", formation_start_spread_out, 50),
                (val_add, ":depth_infantry", formation_minimum_spacing),
                (val_mul, ":depth_infantry", 2),
                (val_sub, ":depth_cavalry", ":depth_infantry"),

                (try_begin),
                    (gt, ":depth_cavalry", 0),
                    (agent_get_position, pos49, "$fplayer_agent_no"),
                    (copy_position, pos2, pos49),
                    (call_script, "script_team_get_position_of_enemies", Enemy_Team_Pos, "$fplayer_team_no", grc_everyone),
                    (call_script, "script_point_y_toward_position", pos2, Enemy_Team_Pos),
                    (position_move_y, pos2, ":depth_cavalry"),
                    (agent_set_position, "$fplayer_agent_no", pos2),    #fake out script_battlegroup_place_around_leader
                (try_end),
            (try_end),
        (try_end),

        #initial formations
        (call_script, "script_division_reset_places"),
        (try_for_range, ":division", 0, 9),
            (store_add, ":slot", "slot_team_d0_size", ":division"),
            (team_slot_ge, "$fplayer_team_no", ":slot", 1),
            (store_add, ":slot", "slot_faction_d0_mem_relative_x_flag", ":division"),
            (faction_get_slot, ":formation_is_memorized", "fac_player_faction", ":slot"),
            (try_begin),
                (neq, ":formation_is_memorized", 0),
                (store_add, ":slot", "slot_faction_d0_mem_formation", ":division"),
                (faction_get_slot, ":mem_formation", "fac_player_faction", ":slot"),
                (store_add, ":slot", "slot_team_d0_formation", ":division"),
                (team_set_slot, "$fplayer_team_no", ":slot", ":mem_formation"),    #do this here to prevent script_player_attempt_formation from resetting spacing

                (store_add, ":slot", "slot_faction_d0_mem_formation_space", ":division"),
                (faction_get_slot, ":value", "fac_player_faction", ":slot"),
                #bring unformed divisions into sync with formations' minimum
                (set_show_messages, 0),
                (try_begin),
                    (ge, ":value", 0),
                    (try_for_range, reg0, 0, ":value"),
                        (team_give_order, "$fplayer_team_no", ":division", mordr_spread_out),
                    (try_end),
                (else_try),
                    (try_for_range, reg0, ":value", 0),
                        (team_give_order, "$fplayer_team_no", ":division", mordr_stand_closer),
                    (try_end),
                (try_end),
                (set_show_messages, 1),
                (store_add, ":slot", "slot_team_d0_formation_space", ":division"),
                (team_set_slot, "$fplayer_team_no", ":slot", ":value"),

                (call_script, "script_player_attempt_formation", ":division", ":mem_formation", 0),
            (else_try),
                (neq, "$formation_off", 0),
                (team_give_order, "$fplayer_team_no", ":division", mordr_hold),
            (else_try),
                (store_add, ":slot", "slot_team_d0_type", ":division"),
                (team_slot_eq, "$fplayer_team_no", ":slot", sdt_archer),
                (call_script, "script_player_attempt_formation", ":division", formation_default, 0),
            (else_try),
                (this_or_next|team_slot_eq, "$fplayer_team_no", ":slot", sdt_cavalry),
                (team_slot_eq, "$fplayer_team_no", ":slot", sdt_harcher),
                (call_script, "script_player_attempt_formation", ":division", formation_wedge, 0),
            (else_try),
                (call_script, "script_get_default_formation", "$fplayer_team_no"),
                (call_script, "script_player_attempt_formation", ":division", reg0, 0),
            (try_end),
        (try_end),

        (try_begin),
            (gt, ":depth_cavalry", 0),
            (agent_set_position, "$fplayer_agent_no", pos49),
        (try_end),

        (val_add, "$last_player_trigger", 1),    #signal .5 sec trigger to start
    ]),

    (.1, 0, 0, [
        (neq, "$when_f1_first_detected", 0),
        (store_mission_timer_c_msec, reg0),
        (val_sub, reg0, "$when_f1_first_detected"),
        (ge, reg0, 250),    #check around .3 seconds later (Native trigger delay does not work right)
        (eq, "$gk_order", gk_order_1),    #next trigger set MOVE menu?
    ], [
        (assign, "$when_f1_first_detected", 0),

        (try_begin),
            (game_key_is_down, gk_order_1),    #BUT player is holding down key?
            (assign, "$gk_order_hold_over_there", 2),
            (assign, "$gk_order", 0),
        (else_try),
            (eq, "$gk_order_hold_over_there", 1),
            (assign, "$gk_order_hold_over_there", 0),
            (assign, "$gk_order", 0),
            (call_script, "script_player_order_formations", mordr_hold),
        (try_end),
    ]),

    (0, 0, 0, [
        (game_key_clicked, gk_order_1),
        (neg|main_hero_fallen)
    ], [
        (store_mission_timer_c_msec, "$when_f1_first_detected"),
        (try_begin),
            #(eq, "$gk_order", 0),
            (neq, "$gk_order", gk_order_1),
            (neq, "$gk_order", gk_order_2),
            (neq, "$gk_order", gk_order_3),
            (assign, "$gk_order", gk_order_1),
            (assign, "$native_display", 0),
            (assign, "$gk_order_hold_over_there", 0),
        (else_try),
            (eq, "$gk_order", gk_order_1),    #HOLD
            (assign, "$gk_order_hold_over_there", 1),
            # (assign, "$fclock", 1),    #sent to delayed trigger above to override Native for unformed divisions
            # (call_script, "script_player_order_formations", mordr_hold),
            # (assign, "$gk_order", 0),
        (else_try),
            (eq, "$gk_order", gk_order_2),    #ADVANCE
            (assign, "$gk_order", 0),
            (presentation_set_duration, 0),    #clear F2 menu additions
            (call_script, "script_player_order_formations", mordr_advance),
        (else_try),
            (eq, "$gk_order", gk_order_3),    #HOLD FIRE
            (assign, "$gk_order", 0),
        (try_end),
    ]),

    (0, 0, 0, [
        (game_key_clicked, gk_order_2),
        (neg|main_hero_fallen)
    ], [
        (try_begin),
            #(eq, "$gk_order", 0),
            (neq, "$gk_order", gk_order_1),
            (neq, "$gk_order", gk_order_2),
            (neq, "$gk_order", gk_order_3),
            (assign, "$gk_order", gk_order_2),
            (assign, "$native_display", 0),
            (start_presentation, "prsnt_order_display"),
        (else_try),
            (eq, "$gk_order", gk_order_1),    #FOLLOW
            (assign, "$gk_order", 0),
            (call_script, "script_player_order_formations", mordr_follow),
        (else_try),
            (eq, "$gk_order", gk_order_2),    #FALL BACK
            (assign, "$gk_order", 0),
            (presentation_set_duration, 0),    #clear F2 menu additions
            (call_script, "script_player_order_formations", mordr_fall_back),
        (else_try),
            (eq, "$gk_order", gk_order_3),    #FIRE AT WILL
            (assign, "$gk_order", 0),
        (try_end),
    ]),

    (0, 0, 0, [
        (game_key_clicked, gk_order_3),
        (neg|main_hero_fallen)
    ], [
        (try_begin),
            #(eq, "$gk_order", 0),
            (neq, "$gk_order", gk_order_1),
            (neq, "$gk_order", gk_order_2),
            (neq, "$gk_order", gk_order_3),
            (assign, "$gk_order", gk_order_3),
            (assign, "$native_display", 0),
        (else_try),
            (eq, "$gk_order", gk_order_1),    #CHARGE
            (assign, "$gk_order", 0),
            (call_script, "script_player_order_formations", mordr_charge),
        (else_try),
            (eq, "$gk_order", gk_order_2),    #SPREAD OUT
            (assign, "$gk_order", 0),
            (presentation_set_duration, 0),    #clear F2 menu additions
            (call_script, "script_player_order_formations", mordr_spread_out),
        (else_try),
            (eq, "$gk_order", gk_order_3),    #BLUNT WEAPONS
            (assign, "$gk_order", 0),
        (try_end),
    ]),

    (0, 0, 0, [
        (game_key_clicked, gk_order_4),
        (neg|main_hero_fallen)
    ], [
        (try_begin),
            (eq, "$gk_order", 0),
            (try_begin),
                (eq, "$formation_off", 0),
                (assign, "$gk_order", gk_order_4),
                (start_presentation, "prsnt_order_display"),
            (else_try),
                (display_message, "@Formations turned OFF in options menu"),
            (try_end),
        (else_try),
            (eq, "$gk_order", gk_order_1),    #STAND GROUND
            (assign, "$gk_order", 0),
            (call_script, "script_player_order_formations", mordr_stand_ground),
        (else_try),
            (eq, "$gk_order", gk_order_2),    #STAND CLOSER
            (assign, "$gk_order", 0),
            (presentation_set_duration, 0),    #clear F2 menu additions
            (call_script, "script_player_order_formations", mordr_stand_closer),
        (else_try),
            (eq, "$gk_order", gk_order_3),    #ANY WEAPON
            (assign, "$gk_order", 0),
        (else_try),
            (eq, "$gk_order", gk_order_4),    #FORMATION - RANKS
            (assign, "$gk_order", 0),
            (call_script, "script_division_reset_places"),
            (try_for_range, ":division", 0, 9),
                (class_is_listening_order, "$fplayer_team_no", ":division"),
                (store_add, ":slot", "slot_team_d0_target_team", ":division"),
                (team_set_slot, "$fplayer_team_no", ":slot", -1),
                (store_add, ":slot", "slot_team_d0_size", ":division"),
                (team_slot_ge, "$fplayer_team_no", ":slot", 1),
                (store_add, ":slot", "slot_team_d0_fclock", ":division"),
                (team_set_slot, "$fplayer_team_no", ":slot", 1),
                (call_script, "script_player_attempt_formation", ":division", formation_ranks, 1),
            (try_end),
            (eq, "$native_display", 1),
            (start_presentation, "prsnt_order_display"),
        (try_end),
    ]),

    (0, 0, 0, [
        (game_key_clicked, gk_order_5),
        (neg|main_hero_fallen)
    ], [
        (try_begin),
            (eq, "$gk_order", 0),
            (assign, "$gk_order", gk_order_5),
            (start_presentation, "prsnt_order_display"),
       (else_try),
            (eq, "$gk_order", gk_order_1),    #RETREAT
            (assign, "$gk_order", 0),
            (call_script, "script_player_order_formations", mordr_retreat),
        (else_try),
            (eq, "$gk_order", gk_order_2),    #MOUNT
            (assign, "$gk_order", 0),
            (presentation_set_duration, 0),    #clear F2 menu additions
        (else_try),
            (eq, "$gk_order", gk_order_4), #FORMATION - SHIELDWALL
            (assign, "$gk_order", 0),
            (call_script, "script_division_reset_places"),
            (try_for_range, ":division", 0, 9),
                (class_is_listening_order, "$fplayer_team_no", ":division"),
                (store_add, ":slot", "slot_team_d0_target_team", ":division"),
                (team_set_slot, "$fplayer_team_no", ":slot", -1),
                (store_add, ":slot", "slot_team_d0_size", ":division"),
                (team_slot_ge, "$fplayer_team_no", ":slot", 1),
                (store_add, ":slot", "slot_team_d0_fclock", ":division"),
                (team_set_slot, "$fplayer_team_no", ":slot", 1),
                (call_script, "script_player_attempt_formation", ":division", formation_shield, 1),
            (try_end),
            (eq, "$native_display", 1),
            (start_presentation, "prsnt_order_display"),
        (else_try),
            (eq, "$gk_order", gk_order_5),    #One-Hander
            (call_script, "script_order_weapon_type_switch", onehand),
            (assign, "$gk_order", 0),
            (eq, "$native_display", 1),
            (start_presentation, "prsnt_order_display"),
        (else_try),
            (eq, "$gk_order", gk_order_6),    #Begin Skirmish
            (call_script, "script_order_skirmish_begin_end"),
            (assign, "$gk_order", 0),
            (eq, "$native_display", 1),
            (start_presentation, "prsnt_order_display"),
        (try_end),
    ]),

    (0, 0, 0, [
        (game_key_clicked, gk_order_6),
        (neg|main_hero_fallen)
    ], [
        (try_begin),
            (eq, "$gk_order", 0),
            (assign, "$gk_order", gk_order_6),
            (start_presentation, "prsnt_order_display"),
        (else_try),
            (eq, "$gk_order", gk_order_2),    #DISMOUNT
            (assign, "$gk_order", 0),
            (presentation_set_duration, 0),    #clear F2 menu additions
            (call_script, "script_player_order_formations", mordr_dismount),
        (else_try),
            (eq, "$gk_order", gk_order_4), #FORMATION - WEDGE
            (assign, "$gk_order", 0),
            (call_script, "script_division_reset_places"),
            (try_for_range, ":division", 0, 9),
                (class_is_listening_order, "$fplayer_team_no", ":division"),
                (store_add, ":slot", "slot_team_d0_target_team", ":division"),
                (team_set_slot, "$fplayer_team_no", ":slot", -1),
                (store_add, ":slot", "slot_team_d0_size", ":division"),
                (team_slot_ge, "$fplayer_team_no", ":slot", 1),
                (store_add, ":slot", "slot_team_d0_fclock", ":division"),
                (team_set_slot, "$fplayer_team_no", ":slot", 1),
                (call_script, "script_player_attempt_formation", ":division", formation_wedge, 1),
            (try_end),
            (eq, "$native_display", 1),
            (start_presentation, "prsnt_order_display"),
        (else_try),
            (eq, "$gk_order", gk_order_5),    #Two-Handers & Polearms
            (call_script, "script_order_weapon_type_switch", bothhands),
            (assign, "$gk_order", 0),
            (eq, "$native_display", 1),
            (start_presentation, "prsnt_order_display"),
        (else_try),
            (eq, "$gk_order", gk_order_6),    #Skirmish
            (call_script, "script_order_skirmish_begin_end"),
            (assign, "$gk_order", 0),
            (eq, "$native_display", 1),
            (start_presentation, "prsnt_order_display"),
        (try_end),
    ]),

    (0, 0, 0, [
        (key_clicked, key_f7),
        (neg|main_hero_fallen)
    ], [
        (try_begin),
            (eq, "$gk_order", gk_order_2),    #MEMORIZE DIVISION PLACEMENTS
            (try_for_range, ":division", 0, 9),
                (class_is_listening_order, "$fplayer_team_no", ":division"),
                (store_add, ":slot", "slot_team_d0_size", ":division"),
                (team_slot_ge, "$fplayer_team_no", ":slot", 1),

                (store_add, ":slot", "slot_team_d0_formation", ":division"),
                (team_get_slot, ":value", "$fplayer_team_no", ":slot"),
                (store_add, ":slot", "slot_faction_d0_mem_formation", ":division"),
                (faction_set_slot, "fac_player_faction", ":slot", ":value"),

                (store_add, ":slot", "slot_team_d0_formation_space", ":division"),
                (team_get_slot, ":value", "$fplayer_team_no", ":slot"),
                (store_add, ":slot", "slot_faction_d0_mem_formation_space", ":division"),
                (faction_set_slot, "fac_player_faction", ":slot", ":value"),

                (agent_get_position, pos1, "$fplayer_agent_no"),
                (try_begin),
                    (call_script, "script_team_get_position_of_enemies", Enemy_Team_Pos, "$fplayer_team_no", grc_everyone),
                    (neq, reg0, 0),    #more than 0 enemies still alive?
                    (call_script, "script_point_y_toward_position", pos1, Enemy_Team_Pos),
                (try_end),
               # (call_script, "script_get_formation_destination", Current_Pos, "$fplayer_team_no", ":division"),
                      (team_get_order_position, Current_Pos, "$fplayer_team_no", ":division"),    #use this to capture Native      Advance and Fall Back positioning
                (position_transform_position_to_local, Temp_Pos, pos1, Current_Pos), #Temp_Pos = vector to division w.r.t. leader facing enemy

                (position_get_x, ":value", Temp_Pos),
                (store_add, ":slot", "slot_faction_d0_mem_relative_x_flag", ":division"),
                (faction_set_slot, "fac_player_faction", ":slot", ":value"),

                (position_get_y, ":value", Temp_Pos),
                (store_add, ":slot", "slot_faction_d0_mem_relative_y", ":division"),
                (faction_set_slot, "fac_player_faction", ":slot", ":value"),

                (store_add, ":slot", "slot_team_d0_type", ":division"),
                (team_get_slot, ":value", "$fplayer_team_no", ":slot"),
                (call_script, "script_str_store_division_type_name", s1, ":value"),
                (store_add, reg0, ":division", 1),
                (display_message, "@The placement of {s1} division {reg0} memorized."),
            (try_end),

        (else_try),
            (eq, "$gk_order", gk_order_4), #FORMATION - SQUARE
            (assign, "$gk_order", 0),
            (call_script, "script_division_reset_places"),
            (try_for_range, ":division", 0, 9),
                (class_is_listening_order, "$fplayer_team_no", ":division"),
                (store_add, ":slot", "slot_team_d0_target_team", ":division"),
                (team_set_slot, "$fplayer_team_no", ":slot", -1),
                (store_add, ":slot", "slot_team_d0_size", ":division"),
                (team_slot_ge, "$fplayer_team_no", ":slot", 1),
                (store_add, ":slot", "slot_team_d0_fclock", ":division"),
                (team_set_slot, "$fplayer_team_no", ":slot", 1),
                (call_script, "script_player_attempt_formation", ":division", formation_square, 1),
            (try_end),
            (eq, "$native_display", 1),
            (start_presentation, "prsnt_order_display"),
        (else_try),
            (eq, "$gk_order", gk_order_5),    #Ranged
            (call_script, "script_order_weapon_type_switch", ranged),
            (assign, "$gk_order", 0),
            (eq, "$native_display", 1),
            (start_presentation, "prsnt_order_display"),
        (try_end),
    ]),

    (0, 0, 0, [
        (key_clicked, key_f8),
        (neg|main_hero_fallen)
    ], [
        (try_begin),
            (eq, "$gk_order", gk_order_2),    #FORGET DIVISION PLACEMENTS (WILL USE DEFAULT)
            (try_for_range, ":division", 0, 9),
                (class_is_listening_order, "$fplayer_team_no", ":division"),
                (store_add, ":slot", "slot_faction_d0_mem_relative_x_flag", ":division"),    #use as flag
                (faction_set_slot, "fac_player_faction", ":slot", 0),

                (store_add, ":slot", "slot_team_d0_size", ":division"),
                (team_slot_ge, "$fplayer_team_no", ":slot", 1),
                (store_add, ":slot", "slot_team_d0_type", ":division"),
                (team_get_slot, ":value", "$fplayer_team_no", ":slot"),
                (call_script, "script_str_store_division_type_name", s1, ":value"),
                (store_add, reg0, ":division", 1),
                (display_message, "@The placement of {s1} division {reg0} set to default."),
            (try_end),
        (else_try),
            (eq, "$gk_order", gk_order_4), #FORMATION - CANCEL
            (assign, "$gk_order", 0),
            (call_script, "script_player_order_formations", mordr_charge),
            (eq, "$native_display", 1),
            (start_presentation, "prsnt_order_display"),
        (else_try),
            (eq, "$gk_order", gk_order_5),    #Shields
            (call_script, "script_order_weapon_type_switch", shield),
            (assign, "$gk_order", 0),
            (eq, "$native_display", 1),
            (start_presentation, "prsnt_order_display"),
        (try_end),
    ]),

    (0, 0, 0, [
        (this_or_next|game_key_clicked, gk_group0_hear),
        (this_or_next|game_key_clicked, gk_group1_hear),
        (this_or_next|game_key_clicked, gk_group2_hear),
        (this_or_next|game_key_clicked, gk_group3_hear),
        (this_or_next|game_key_clicked, gk_group4_hear),
        (this_or_next|game_key_clicked, gk_group5_hear),
        (this_or_next|game_key_clicked, gk_group6_hear),
        (this_or_next|game_key_clicked, gk_group7_hear),
        (this_or_next|game_key_clicked, gk_group8_hear),
        (this_or_next|game_key_clicked, gk_reverse_order_group),    #shows up as "unknown 6" on Native screen
        (this_or_next|game_key_clicked, gk_everyone_around_hear),
        (game_key_clicked, gk_everyone_hear),
        (neg|main_hero_fallen)
    ], [
        (assign, "$gk_order", 0),
        (start_presentation, "prsnt_order_display"),
        (assign, "$native_display", 1),
    ]),

    (0, 0, 0, [
        (key_is_down, key_escape),
        (is_presentation_active, "prsnt_order_display"),
    ], [
        (assign, "$gk_order", 0),
        (assign, "$native_display", 0),
        (presentation_set_duration, 0),
    ]),

    (.5, 0, 0, [
        (neq, "$last_player_trigger", Far_Away),
        (neg|main_hero_fallen)
    ], [
        (set_fixed_point_multiplier, 100),
        (store_mission_timer_c_msec, "$last_player_trigger"),

        (try_begin),    #set up revertible types for type check
            (try_for_range, ":team", 0, 4),
                (try_for_range, ":division", 0, 9),
                    (store_add, ":slot", "slot_team_d0_type", ":division"),
                    (this_or_next|team_slot_eq, ":team", ":slot", sdt_skirmisher),
                    (team_slot_eq, ":team", ":slot", sdt_harcher),
                    (team_set_slot, ":team", ":slot", sdt_unknown),
                (try_end),
            (try_end),
        (try_end),

        (call_script, "script_store_battlegroup_data"),
        (call_script, "script_team_get_position_of_enemies", Enemy_Team_Pos, "$fplayer_team_no", grc_everyone),
        (assign, ":num_enemies", reg0),

        (try_begin),
            (eq, ":num_enemies", 0),    #no more enemies?
            (try_for_range, ":division", 0, 9),
                (call_script, "script_formation_end", "$fplayer_team_no", ":division"),
            (try_end),
        (try_end),

        (gt, ":num_enemies", 0),
        (call_script, "script_division_reset_places"),

        #implement HOLD OVER THERE when player lets go of key
        (try_begin),
            (eq, "$gk_order_hold_over_there", 2),
            (neg|game_key_is_down, gk_order_1),

            (assign, ":num_bgroups", 0),
            (try_for_range, ":division", 0, 9),
                (class_is_listening_order, "$fplayer_team_no", ":division"),
                (store_add, ":slot", "slot_team_d0_target_team", ":division"),
                (team_set_slot, "$fplayer_team_no", ":slot", -1),
                (store_add, ":slot", "slot_team_d0_size", ":division"),
                (team_slot_ge, "$fplayer_team_no", ":slot", 1),
                (store_add, ":slot", "slot_team_d0_fclock", ":division"),
                (team_set_slot, "$fplayer_team_no", ":slot", 1),
                (team_get_order_position, pos1, "$fplayer_team_no", ":division"),
                (val_add, ":num_bgroups", 1),
            (try_end),

            (gt, ":num_bgroups", 0),
            (copy_position, Target_Pos, pos1),    #kludge around team_get_order_position rotation problems

            #player designating target battlegroup?
            (assign, ":distance_to_enemy", Far_Away),
            (try_for_range, ":team", 0, 4),
                (teams_are_enemies, ":team", "$fplayer_team_no"),
                (team_slot_ge, ":team", "slot_team_size", 1),
                (try_for_range, ":division", 0, 9),
                    (store_add, ":slot", "slot_team_d0_size", ":division"),
                    (team_slot_ge, ":team", ":slot", 1),
                    (call_script, "script_battlegroup_get_position", Temp_Pos, ":team", ":division"),
                    (get_distance_between_positions, reg0, Target_Pos, Temp_Pos),
                    (gt, ":distance_to_enemy", reg0),
                    (assign, ":distance_to_enemy", reg0),
                    (assign, ":closest_enemy_team", ":team"),
                    (assign, ":closest_enemy_division", ":division"),
                (try_end),
            (try_end),

            (call_script, "script_battlegroup_get_action_radius", ":closest_enemy_team", ":closest_enemy_division"),
            (assign, ":radius_enemy_battlegroup", reg0),

            (try_begin),
                (le, ":distance_to_enemy", ":radius_enemy_battlegroup"),    #target position within radius of an enemy battlegroup?
                (le, ":distance_to_enemy", AI_charge_distance),    #limit so player can place divisions near large enemy battlegroups without selecting them
                (call_script, "script_battlegroup_get_position", Target_Pos, ":closest_enemy_team", ":closest_enemy_division"),
                (gt, ":num_bgroups", 1),
                (store_add, ":slot", "slot_team_d0_type", ":closest_enemy_division"),
                (team_get_slot, reg0, ":closest_enemy_team", ":slot"),
                (call_script, "script_str_store_division_type_name", s1, reg0),
                (display_message, "@...and attack enemy {s1} division!"),
            (try_end),

            (call_script, "script_point_y_toward_position", Target_Pos, Enemy_Team_Pos),

            #place player divisions
            (agent_get_position, pos49, "$fplayer_agent_no"),
            (try_for_range, ":division", 0, 9),
                (class_is_listening_order, "$fplayer_team_no", ":division"),
                (store_add, ":slot", "slot_team_d0_size", ":division"),
                (team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
                (gt, ":troop_count", 0),

                (try_begin),
                    (le, ":distance_to_enemy", ":radius_enemy_battlegroup"),    #target position within radius of an enemy battlegroup?
                    (store_add, ":slot", "slot_team_d0_target_team", ":division"),
                    (team_set_slot, "$fplayer_team_no", ":slot", ":closest_enemy_team"),
                    (store_add, ":slot", "slot_team_d0_target_division", ":division"),
                    (team_set_slot, "$fplayer_team_no", ":slot", ":closest_enemy_division"),
                (try_end),

                (store_add, ":slot", "slot_team_d0_formation", ":division"),
                (team_get_slot, ":fformation", "$fplayer_team_no", ":slot"),

                (try_begin),
                    (gt, ":num_bgroups", 1),
                    (agent_set_position, "$fplayer_agent_no", Target_Pos),    #fake out script_battlegroup_place_around_leader
                    (call_script, "script_player_attempt_formation", ":division", ":fformation", 0),
                (else_try),
                    (try_begin),
                        (le, ":distance_to_enemy", ":radius_enemy_battlegroup"),    #target position within radius of an enemy battlegroup?
                        (call_script, "script_battlegroup_get_attack_destination", Target_Pos, "$fplayer_team_no", ":division", ":closest_enemy_team", ":closest_enemy_division"),
                        (store_add, ":slot", "slot_team_d0_type", ":closest_enemy_division"),
                        (team_get_slot, reg0, ":closest_enemy_team", ":slot"),
                        (call_script, "script_str_store_division_type_name", s1, reg0),
                        (display_message, "@...and attack enemy {s1} division!"),
                    (try_end),


                        (call_script, "script_set_formation_destination", "$fplayer_team_no", ":division", Target_Pos),

                                        (neq, ":fformation", formation_none),
                    (store_add, ":slot", "slot_team_d0_formation_space", ":division"),
                    (team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
                    (try_begin),
                        (store_add, ":slot", "slot_team_d0_type", ":division"),
                        (team_get_slot, ":sd_type", "$fplayer_team_no", ":slot"),
                        (neq, ":sd_type", sdt_cavalry),
                        (neq, ":sd_type", sdt_harcher),
                        (try_begin),
                            (eq, ":sd_type", sdt_archer),
                            (call_script, "script_get_centering_amount", formation_default, ":troop_count", ":div_spacing"),
                            (val_mul, reg0, -1),
                            (assign, ":script", "script_form_archers"),
                        (else_try),
                            (call_script, "script_get_centering_amount", ":fformation", ":troop_count", ":div_spacing"),
                            (assign, ":script", "script_form_infantry"),
                        (try_end),
                        (position_move_x, Target_Pos, reg0),
                    (else_try),
                        (assign, ":script", "script_form_cavalry"),
                    (try_end),
                    (copy_position, pos1, Target_Pos),
                    (call_script, ":script", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", 0, ":fformation"),
                (try_end),
                (store_add, ":slot", "slot_team_d0_move_order", ":division"),
                (team_set_slot, "$fplayer_team_no", ":slot", mordr_hold),
            (try_end), #division loop
            (agent_set_position, "$fplayer_agent_no", pos49),
            (assign, "$gk_order_hold_over_there", 0),
        (try_end),    #HOLD OVER THERE

        #periodic functions
        (try_begin),    #rethink after reform
            (gt, "$rethink_on_formation", 0),
##            (try_for_agents, ":agent"),    #MOTO this needs to be smarter: got troops walking backwards & turning back on player (but perhaps that's Native?)
##                (agent_force_rethink, ":agent"),
##            (try_end),
            (assign, "$rethink_on_formation", 0),
        (try_end),

        (assign, ":save_autorotate", "$formation_autorotate"),
        (assign, "$formation_autorotate", 0),
        (try_for_range, ":division", 0, 9),
            (store_add, ":slot", "slot_team_d0_size", ":division"),
            (team_get_slot, ":troop_count", "$fplayer_team_no", ":slot"),
            (gt, ":troop_count", 0),

            (store_add, ":slot", "slot_team_d0_target_team", ":division"),
            (team_get_slot, ":target_team", "$fplayer_team_no", ":slot"),
            (store_add, ":slot", "slot_team_d0_target_division", ":division"),
            (team_get_slot, ":target_division", "$fplayer_team_no", ":slot"),
            (try_begin),
                (ge, ":target_team", 0),    #enemy battlegroup targeted?
                (store_add, ":slot", "slot_team_d0_size", ":target_division"),
                (team_get_slot, reg0, ":target_team", ":slot"),

                (le, reg0, 0),    #target destroyed?
                (store_add, ":slot", "slot_team_d0_target_team", ":division"),
                (team_set_slot, "$fplayer_team_no", ":slot", -1),

                (store_add, ":slot", "slot_team_d0_type", ":target_division"),
                (team_get_slot, reg0, ":target_team", ":slot"),
                (call_script, "script_str_store_division_type_name", s1, reg0),

                (store_add, reg0, ":division", 1),
                (display_message, "@Division {reg0}: returning after destroying enemy {s1} division."),
                (store_add, ":slot", "slot_team_d0_move_order", ":division"),
                (team_set_slot, "$fplayer_team_no", ":slot", mordr_follow),
            (try_end),

            (store_add, ":slot", "slot_team_d0_fclock", ":division"),
            (team_get_slot, ":fclock", "$fplayer_team_no", ":slot"),
            (store_mod, ":time_slice", ":fclock", Reform_Trigger_Modulus),
            (val_add, ":fclock", 1),
            (team_set_slot, "$fplayer_team_no", ":slot", ":fclock"),

            (try_begin),
                (store_add, ":slot", "slot_team_d0_move_order", ":division"),
                (team_slot_eq, "$fplayer_team_no", ":slot", mordr_follow),
                (call_script, "script_battlegroup_place_around_leader", "$fplayer_team_no", ":division"),
                (team_set_slot, "$fplayer_team_no", ":slot", mordr_follow),    #override script_battlegroup_place_around_leader

            #periodically reform
            (else_try),
                (eq, ":time_slice", 0),
                (team_get_movement_order, reg0, "$fplayer_team_no", ":division"),
                (neq, reg0, mordr_stand_ground),
                (store_add, ":slot", "slot_team_d0_formation", ":division"),
                (team_get_slot, ":fformation", "$fplayer_team_no", ":slot"),
                (try_begin),
                    (neq, ":fformation", formation_none),
                    (store_add, ":slot", "slot_team_d0_formation_space", ":division"),
                    (team_get_slot, ":div_spacing", "$fplayer_team_no", ":slot"),
                    (store_add, ":slot", "slot_team_d0_type", ":division"),
                    (team_get_slot, ":sd_type", "$fplayer_team_no", ":slot"),

                    (try_begin),
                        (store_add, ":slot", "slot_team_d0_first_member", ":division"),
                        (team_slot_eq, "$fplayer_team_no", ":slot", "$fplayer_agent_no"),
                        (assign, ":first_member_is_player", 1),
                    (else_try),
                        (assign, ":first_member_is_player", 0),
                    (try_end),

                    (try_begin),
                        (ge, ":target_team", 0),    #enemy battlegroup targeted?
                        (try_begin),
                            (this_or_next|eq, ":sd_type", sdt_archer),
                            (this_or_next|eq, ":sd_type", sdt_harcher),
                            (eq, ":sd_type", sdt_skirmisher),
                            (store_add, ":slot", "slot_team_d0_in_melee", ":division"),
                            (team_slot_ge, "$fplayer_team_no", ":slot", 1),    #ranged are firing?
                            (call_script, "script_formation_current_position", pos1, "$fplayer_team_no", ":division"),    #stop advancing
                        (else_try),
                            (call_script, "script_battlegroup_get_attack_destination", pos1, "$fplayer_team_no", ":division", ":target_team", ":target_division"),
                        (try_end),

                    (else_try),
                        (call_script, "script_get_formation_destination", pos1, "$fplayer_team_no", ":division"),
                        (try_begin),
                            (neq, ":sd_type", sdt_cavalry),
                            (neq, ":sd_type", sdt_harcher),
                            (eq, ":first_member_is_player", 0),
                            (position_move_y, pos1, -2000),
                        (try_end),
                        (call_script, "script_point_y_toward_position", pos1, Enemy_Team_Pos),
                        (try_begin),
                            (neq, ":sd_type", sdt_cavalry),
                            (neq, ":sd_type", sdt_harcher),
                            (eq, ":first_member_is_player", 0),
                            (position_move_y, pos1, 2000),
                        (try_end),
                    (try_end),

                    (call_script, "script_set_formation_destination", "$fplayer_team_no", ":division", pos1),

                    (try_begin),
                        (eq, ":sd_type", sdt_archer),
                        (call_script, "script_get_centering_amount", formation_default, ":troop_count", ":div_spacing"),
                        (val_mul, reg0, -1),
                        (position_move_x, pos1, reg0),
                    (else_try),
                        (neq, ":sd_type", sdt_cavalry),
                        (neq, ":sd_type", sdt_harcher),
                        (call_script, "script_get_centering_amount", ":fformation", ":troop_count", ":div_spacing"),
                        (position_move_x, pos1, reg0),
                    (try_end),

                    (try_begin),
                        (eq, ":sd_type", sdt_archer),
                        (call_script, "script_form_archers", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":first_member_is_player", ":fformation"),
                    (else_try),
                        (this_or_next|eq, ":sd_type", sdt_cavalry),
                        (eq, ":sd_type", sdt_harcher),
                        (try_begin),
                            (ge, ":target_team", 0),    #enemy battlegroup targeted?
                            (call_script, "script_formation_current_position", pos29, "$fplayer_team_no", ":division"),
                            (call_script, "script_battlegroup_get_position", Enemy_Team_Pos, ":target_team", ":target_division"),
                            (get_distance_between_positions, ":distance_to_enemy", pos29, Enemy_Team_Pos),

                            (call_script, "script_battlegroup_get_action_radius", "$fplayer_team_no", ":division"),
                            (assign, ":combined_radius", reg0),
                            (call_script, "script_battlegroup_get_action_radius", ":target_team", ":target_division"),
                            (val_add, ":combined_radius", reg0),

                            (le, ":distance_to_enemy", ":combined_radius"),
                            (call_script, "script_formation_end", "$fplayer_team_no", ":division"),
                            (store_add, reg0, ":division", 1),
                            (display_message, "@Division {reg0}: cavalry formation disassembled."),
                            (set_show_messages, 0),
                            (team_give_order, "$fplayer_team_no", ":division", mordr_charge),
                            (set_show_messages, 1),
                        (else_try),
                            (call_script, "script_form_cavalry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":first_member_is_player"),
                        (try_end),
                    (else_try),
                        (call_script, "script_form_infantry", "$fplayer_team_no", ":division", "$fplayer_agent_no", ":div_spacing", ":first_member_is_player", ":fformation"),
                    (try_end),

                    (val_add, "$rethink_on_formation", 1),

                (else_try),    #divisions not in formation
                    (ge, ":target_team", 0),    #enemy battlegroup targeted?
                    (store_add, ":slot", "slot_team_d0_target_division", ":division"),
                    (team_get_slot, ":target_division", "$fplayer_team_no", ":slot"),
                    (try_begin),
                        (this_or_next|eq, ":sd_type", sdt_archer),
                        (this_or_next|eq, ":sd_type", sdt_harcher),
                        (eq, ":sd_type", sdt_skirmisher),
                        (store_add, ":slot", "slot_team_d0_in_melee", ":division"),
                        (team_slot_ge, "$fplayer_team_no", ":slot", 1),    #ranged are firing?
                        (call_script, "script_battlegroup_get_position", pos1, "$fplayer_team_no", ":division"),    #stop advancing
                    (else_try),
                        (call_script, "script_battlegroup_get_attack_destination", pos1, "$fplayer_team_no", ":division", ":target_team", ":target_division"),
                    (try_end),
                    (call_script, "script_set_formation_destination", "$fplayer_team_no", ":division", pos1),
                    (team_get_movement_order, ":existing_order", "$fplayer_team_no", ":division"),
                    (try_begin),
                        (ge, ":target_team", 0),    #enemy battlegroup targeted?
                        (call_script, "script_battlegroup_get_position", pos29, "$fplayer_team_no", ":division"),
                        (call_script, "script_battlegroup_get_position", Enemy_Team_Pos, ":target_team", ":target_division"),
                        (get_distance_between_positions, ":distance_to_enemy", pos29, Enemy_Team_Pos),

                        (call_script, "script_battlegroup_get_action_radius", "$fplayer_team_no", ":division"),
                        (assign, ":combined_radius", reg0),
                        (call_script, "script_battlegroup_get_action_radius", ":target_team", ":target_division"),
                        (val_add, ":combined_radius", reg0),

                        (le, ":distance_to_enemy", ":combined_radius"),
                        (try_begin),
                            (neq, ":existing_order", mordr_charge),
                            (set_show_messages, 0),
                            (team_give_order, "$fplayer_team_no", ":division", mordr_charge),
                            (set_show_messages, 1),
                        (try_end),
                    (else_try),
                        (neq, ":existing_order", mordr_hold),
                        (set_show_messages, 0),
                        (team_give_order, "$fplayer_team_no", ":division", mordr_hold),
                        (set_show_messages, 1),
                    (try_end),
                (try_end),
            (try_end),    #Periodic Reform
        (try_end),    #Division Loop

        (assign, "$formation_autorotate", ":save_autorotate"),
    ]),

    (ti_on_agent_spawn, 0, 0, [], [
        (store_trigger_param_1, ":agent"),
        (agent_is_human, ":agent"),
        (try_begin),
            (multiplayer_get_my_player, ":player"),
            (player_is_active, ":player"),
            (player_get_agent_id, ":player_agent", ":player"),
            (eq, ":agent", ":player_agent"),
            (assign, "$fplayer_agent_no", ":player_agent"),
            (player_get_team_no,  "$fplayer_team_no", ":player"),
        (else_try),
            (agent_is_non_player, ":agent"),
            (agent_get_group, ":team", ":agent"),
            (gt, ":team", -1),    #not a MP spectator
            (call_script, "script_agent_fix_division", ":agent"), #Division fix
            (agent_get_class, reg0, ":agent"),
            (eq, reg0, grc_infantry),    #set up for possible shield wall
            (agent_get_division, ":division", ":agent"),
            (team_get_hold_fire_order, ":fire_order", ":team", ":division"),
            (call_script, "script_equip_best_melee_weapon", ":agent", 1, 0, ":fire_order"),    #best weapon, force shield
        (try_end),
    ]),

    # (ti_on_agent_killed_or_wounded, 0, 0, [], [    #prevent      leaving noswing weapons around for player to pick up
    #           (store_trigger_param_1, ":dead_agent_no"),
    #           (call_script, "script_switch_from_noswing_weapons", ":dead_agent_no"),
    #       ]),
]
#end formations triggers

#AI triggers v3 for WB by motomataru
AI_triggers = [
    (ti_before_mission_start, 0, 0, [], [
        (assign, "$ranged_clock", 1),
        (assign, "$battle_phase", BP_Setup),
        (assign, "$clock_reset", 0),
        (init_position, Team0_Cavalry_Destination),
        (init_position, Team1_Cavalry_Destination),
        (init_position, Team2_Cavalry_Destination),
        (init_position, Team3_Cavalry_Destination),
    ]),

    (0, 0, ti_once, [(gt, "$last_player_trigger", Far_Away)], [    #delay 'til AFTER Formations trigger fires
        (try_for_agents, ":cur_agent"),
            (agent_set_slot, ":cur_agent",  "slot_agent_is_running_away", 0),
        (try_end),
        (set_fixed_point_multiplier, 100),
        # (call_script, "script_store_battlegroup_data"),    done in formations trigger
        (try_for_range, ":team", 0, 4),
            (call_script, "script_battlegroup_get_position", pos0, ":team", grc_everyone),
            (position_get_x, reg0, pos0),
            (team_set_slot, ":team", "slot_team_starting_x", reg0),
            (position_get_y, reg0, pos0),
            (team_set_slot, ":team", "slot_team_starting_y", reg0),

            #prevent confusion over AI not using formations for archers
            (neq, ":team", "$fplayer_team_no"),
            (store_add, ":slot", "slot_team_d0_formation", grc_archers),
            (team_set_slot, ":team", ":slot", formation_none),
        (try_end),
        (call_script, "script_field_tactics", 1)
    ]),

    (.1, 0, 0, [], [
        (store_mission_timer_c_msec, reg0),
        (val_sub, reg0, "$last_player_trigger"),
        (ge, reg0, 250),    #delay to offset from formations trigger (trigger delay does not work right)
        (val_add, "$last_player_trigger", 500),

        (try_begin),    #catch moment fighting starts
            (eq, "$clock_reset", 0),
            (call_script, "script_cf_any_fighting"),
            (call_script, "script_cf_count_casualties"),
            (assign, "$battle_phase", BP_Fight),
(set_show_messages, 1),
#(display_message, "@Trigger: BP_Fight, fighting and casualties"),
(display_message, "@ "),
        (try_end),

        (set_fixed_point_multiplier, 100),
        (call_script, "script_store_battlegroup_data"),

        (try_begin),    #reassess ranged position when fighting starts
            (ge, "$battle_phase", BP_Fight),    #we have to do it this way because BP_Fight may be set in ways other than casualties
            (eq, "$clock_reset", 0),
            (call_script, "script_field_tactics", 1),
            (assign, "$ranged_clock", 0),
            (assign, "$clock_reset", 1),

        (else_try),    #at longer intervals after setup...
            (ge, "$battle_phase", BP_Jockey),
            # (store_mul, ":five_sec_modulus", 5, Reform_Trigger_Modulus),    #MOTO uncomment this section if archers too fidgety
            # (val_div, ":five_sec_modulus", formation_reform_interval),
            # (store_mod, reg0, "$ranged_clock", ":five_sec_modulus"),
            # (eq, reg0, 0),

            #reassess archer position
            (call_script, "script_field_tactics", 1),

            #catch reinforcements and set divisions to be retyped with new troops
            (try_begin),
                (neg|team_slot_eq, 0, "slot_team_reinforcement_stage", "$defender_reinforcement_stage"),
                (team_set_slot, 0, "slot_team_reinforcement_stage", "$defender_reinforcement_stage"),
                (try_for_range, ":division", 0, 9),
                    (store_add, ":slot", "slot_team_d0_type", ":division"),
                    (team_set_slot, 0, ":slot", sdt_unknown),
                    (team_set_slot, 2, ":slot", sdt_unknown),
                (try_end),
            (try_end),
            (try_begin),
                (neg|team_slot_eq, 1, "slot_team_reinforcement_stage", "$attacker_reinforcement_stage"),
                (team_set_slot, 1, "slot_team_reinforcement_stage", "$attacker_reinforcement_stage"),
                (try_for_range, ":division", 0, 9),
                    (store_add, ":slot", "slot_team_d0_type", ":division"),
                    (team_set_slot, 1, ":slot", sdt_unknown),
                    (team_set_slot, 3, ":slot", sdt_unknown),
                (try_end),
            (try_end),

        (else_try),
            (call_script, "script_field_tactics", 0),
        (try_end),

        (try_begin),
            (eq, "$battle_phase", BP_Setup),
            (assign, ":not_in_setup_position", 0),
            (try_for_range, ":bgteam", 0, 4),
                (neq, ":bgteam", "$fplayer_team_no"),
                (team_slot_ge, ":bgteam", "slot_team_size", 1),
                (call_script, "script_battlegroup_get_position", pos1, ":bgteam", grc_archers),
                (team_get_order_position, pos0, ":bgteam", grc_archers),
                (get_distance_between_positions, reg0, pos0, pos1),
                (gt, reg0, 500),
                (assign, ":not_in_setup_position", 1),
            (try_end),
            (eq, ":not_in_setup_position", 0),    #all AI reached setup position?
            (assign, "$battle_phase", BP_Jockey),
        (try_end),

        (val_add, "$ranged_clock", 1),
    ]),

    (0, 0, ti_once, [
        (main_hero_fallen),    #if AI to take over for mods with post-player battle action
        (eq, AI_Replace_Dead_Player, 1),
    ], [
        (try_for_agents, ":agent"),    #reassign agents to the divisions AI uses
            (agent_is_alive, ":agent"),
            (call_script, "script_agent_fix_division", ":agent"),
        (try_end),

        (set_show_messages, 0),    #undo special player commands for divisions AI uses
        (try_for_range, ":division", 0, 3),
            (team_give_order, "$fplayer_team_no", ":division", mordr_use_any_weapon),
            (team_give_order, "$fplayer_team_no", ":division", mordr_fire_at_will),
        (try_end),
        (set_show_messages, 1),
    ]),
]
#end AI triggers
