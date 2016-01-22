from source.statement import StatementBlock
from ..header_game_menus import *
from ..module_constants import *


def add_truce(kingdom_a, kingdom_b):
    """
    Sets a truce between two kingdoms
    """
    return StatementBlock(
        (store_add, ":truce_slot", kingdom_a, slot_faction_truce_days_with_factions_begin),
        (val_sub, ":truce_slot", kingdoms_begin),
        (faction_set_slot, kingdom_b, ":truce_slot", dplmc_treaty_truce_days_initial),

        (store_add, ":truce_slot", kingdom_b, slot_faction_truce_days_with_factions_begin),
        (val_sub, ":truce_slot", kingdoms_begin),
        (faction_set_slot, kingdom_a, ":truce_slot", dplmc_treaty_truce_days_initial),

        (store_add, ":slot_war_damage_inflicted_on_b", kingdom_b, slot_faction_war_damage_inflicted_on_factions_begin),
        (val_sub, ":slot_war_damage_inflicted_on_b", kingdoms_begin),
        (faction_set_slot, kingdom_a, ":slot_war_damage_inflicted_on_b", 0),

        (store_add, ":slot_war_damage_inflicted_on_a", kingdom_a, slot_faction_war_damage_inflicted_on_factions_begin),
        (val_sub, ":slot_war_damage_inflicted_on_a", kingdoms_begin),
        (faction_set_slot, kingdom_b, ":slot_war_damage_inflicted_on_a", 0),
    )

scripts = [

    ("randomly_start_war_peace_new", [
        (store_script_param_1, ":initializing_war_peace_cond"),

        # choose kingdom 1
        (store_random_in_range, ":random_offset_1", "fac_kingdom_1", kingdoms_end),
        (val_sub, ":random_offset_1", "fac_kingdom_1"),

        (try_for_range, ":cur_kingdom", "fac_kingdom_1", kingdoms_end),
            (val_add, ":cur_kingdom", ":random_offset_1"),
            (try_begin),
                (ge, ":cur_kingdom", kingdoms_end),
                (val_sub, ":cur_kingdom", kingdoms_end),
                (val_add, ":cur_kingdom", "fac_kingdom_1"),
            (try_end),

            (faction_slot_eq, ":cur_kingdom", slot_faction_state, sfs_active),

            # choose kingdom 2 by trying 50 times to find a kingdom_2
            (assign, ":num_tries", 50),
            (try_for_range, reg0, 0, ":num_tries"),
                (store_random_in_range, ":cur_kingdom_2", kingdoms_begin, kingdoms_end),
                (neq, ":cur_kingdom", ":cur_kingdom_2"),
                (faction_slot_eq, ":cur_kingdom_2", slot_faction_state, sfs_active),
                (assign, ":num_tries", reg0),  # break
            (try_end),

            (try_begin),
                (neq, ":cur_kingdom", ":cur_kingdom_2"),

                (faction_slot_eq, ":cur_kingdom_2", slot_faction_state, sfs_active),

                # select reason to change behaviour
                (call_script, "script_npc_decision_checklist_peace_or_war", ":cur_kingdom", ":cur_kingdom_2", -1),
                (assign, ":kingdom_1_to_kingdom_2", reg0),
                (str_store_string_reg, s57, s14), # save diplomatic explanation string

                # :neighbors -> are they neighbors?
                (store_add, ":slot", slot_faction_neighbors_begin, ":cur_kingdom_2"),
                (val_sub, ":slot", kingdoms_begin),
                (faction_get_slot, ":neighbors", ":cur_kingdom", ":slot"),

                (store_relation, ":cur_relation", ":cur_kingdom", ":cur_kingdom_2"),

                (try_begin),
                    # at war, try to make peace
                    (lt, ":cur_relation", 0),

                    (this_or_next|eq, ":initializing_war_peace_cond", 0),
                    # and trying to improve
                    (ge, ":kingdom_1_to_kingdom_2", 1),

                    (try_begin),
                        (store_current_hours, ":cur_hours"),
                        (faction_get_slot, ":faction_ai_last_decisive_event", ":cur_kingdom", slot_faction_ai_last_decisive_event),
                        (store_sub, ":hours_since_last_decisive_event", ":cur_hours", ":faction_ai_last_decisive_event"),

                        (this_or_next|eq, ":initializing_war_peace_cond", 0),
                        # todo: why is this comment saying 4 days? 400/24 ~ 16 days
                        # wait 4 days until conclude peace after war
                        (ge, ":hours_since_last_decisive_event", 400),

                        (try_begin),
                            # if it is player and goodwill -> offer peace
                            (eq, ":cur_kingdom_2", "fac_player_supporters_faction"),

                            (store_mul, ":goodwill_level", ":kingdom_1_to_kingdom_2", 2),
                            (store_random_in_range, ":random", 0, 20),
                            (try_begin),
                                (lt, ":random", ":goodwill_level"),
                                (call_script, "script_add_notification_menu", "mnu_question_peace_offer", ":cur_kingdom", 0),
                            (try_end),
                        (else_try),
                            # check the other side of the relation and see if both
                            # are willing to make peace
                            (call_script, "script_npc_decision_checklist_peace_or_war", ":cur_kingdom_2", ":cur_kingdom", -1),
                            (assign, ":kingdom_2_to_kingdom_1", reg0),

                            (ge, ":kingdom_2_to_kingdom_1", 1),

                            (store_mul, ":goodwill_level", ":kingdom_1_to_kingdom_2", ":kingdom_2_to_kingdom_1"),

                            (try_begin),
                                (eq, ":initializing_war_peace_cond", 0),
                                (store_add, reg1, ":kingdom_1_to_kingdom_2", 3),
                                (store_add, reg2, ":kingdom_2_to_kingdom_1", 3),
                                (store_mul, ":goodwill_level", reg1, reg2),
                                (val_mul, ":goodwill_level", 3),
                                # fine tuning; results in about 4 peace made start of game w 18 calls
                                (val_div, ":goodwill_level", 4),
                            (try_end),

                            # increase chance of peace (goodwill_level max at 9
                            # -- figure 1/4 chance is once per 120 days)
                            (store_random_in_range, ":random", -1, 19),
                            (lt, ":random", ":goodwill_level"),

                            # make peace
                            (assign, "$g_last_acting_faction", ":cur_kingdom"),
                            (assign, "$g_last_target_faction", ":cur_kingdom_2"),
                            (str_store_string_reg, s64, s57),  #  save diplomatic explanation string

                            (call_script, "script_diplomacy_start_peace_between_kingdoms", ":cur_kingdom", ":cur_kingdom_2", ":initializing_war_peace_cond"),
                        (try_end),
                    (try_end),
                (else_try),
                    # at peace and no truce, try to make war
                    (ge, ":cur_relation", 0),

                    (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":cur_kingdom", ":cur_kingdom_2"),
                    (le, reg0, 0),

                    (assign, ":hostility", ":kingdom_1_to_kingdom_2"),
                    (try_begin),
                        (eq, ":initializing_war_peace_cond", 0),  # start of game
                        # amplify effect if neighbors
                        (val_sub, ":hostility", ":neighbors"),
                    (try_end),
                    (lt, ":hostility", 0),  # non-start in [-1, -3]

                    # :hostility_squared \in [3, 9]
                    (store_mul, ":hostility_squared", ":hostility", -3),
                    (try_begin),
                        # one unprovoked attack once every 600 days, 30 days
                        # for script_npc_decision_checklist_peace_or_war results = -3)
                        (store_random_in_range, ":random", 0, 9),
                    (try_end),

                    # todo: document what this does
                    # reduces hostility when 3rd kingdoms has defence packs?
                    (try_for_range, ":third_kingdom", kingdoms_begin, kingdoms_end),
                        (neq, ":third_kingdom", ":cur_kingdom"),
                        (neq, ":third_kingdom", ":cur_kingdom_2"),
                        (faction_slot_eq, ":third_kingdom", slot_faction_state, sfs_active),

                        (store_relation, ":cur_relation", ":cur_kingdom_2", ":third_kingdom"),
                        # at peace
                        (ge, ":cur_relation", 0),

                        (store_add, ":truce_slot", ":third_kingdom", slot_faction_truce_days_with_factions_begin),
                        (val_sub, ":truce_slot", kingdoms_begin),
                        (faction_get_slot, ":truce_days", ":cur_kingdom_2", ":truce_slot"),

                        # todo: what is this exactly?
                        (gt, ":truce_days", dplmc_treaty_defense_days_expire),

                        (store_div, ":hostility_change", ":truce_days", 20),
                        (val_sub, ":hostility_change", 1),  # adjust to 1-2 points (since random less)
                        (val_sub, ":hostility_squared", ":hostility_change"),
                    (try_end),

                    (lt, ":random", ":hostility_squared"),
                    (assign, "$g_last_acting_faction", ":cur_kingdom"),
                    (assign, "$g_last_target_faction", ":cur_kingdom_2"),
                    (str_store_string_reg, s64, s57),
                    (call_script, "script_diplomacy_start_war_between_kingdoms", ":cur_kingdom", ":cur_kingdom_2", ":initializing_war_peace_cond"),

                    (try_begin),
                        # do initial war damage
                        (eq, ":initializing_war_peace_cond", 0),
                        (store_random_in_range, ":war_damage_inflicted", 10, 120),
                        (store_add, ":slot_war_damage_inflicted", ":cur_kingdom", slot_faction_war_damage_inflicted_on_factions_begin),
                        (val_sub, ":slot_war_damage_inflicted", kingdoms_begin),
                        (faction_set_slot, ":cur_kingdom_2",  ":slot_war_damage_inflicted", ":war_damage_inflicted"),

                        (store_add, ":slot_war_damage_inflicted", ":cur_kingdom_2", slot_faction_war_damage_inflicted_on_factions_begin),
                        (val_sub, ":slot_war_damage_inflicted", kingdoms_begin),
                        (faction_set_slot, ":cur_kingdom", ":slot_war_damage_inflicted", ":war_damage_inflicted"),
                    (try_end),
                (else_try),
                    # at peace and a truce, try to break truce
                    (ge, ":cur_relation", 0),
                    (ge, ":kingdom_1_to_kingdom_2", 1),

                    # consider just nearby factions
                    (assign, ":neighbors_of_neighbors", 0),
                    (assign, ":end_loop", kingdoms_end),
                    (try_for_range, ":third_kingdom", kingdoms_begin, ":end_loop"),
                        (neq, ":third_kingdom", ":cur_kingdom"),
                        (neq, ":third_kingdom", ":cur_kingdom_2"),
                        (assign, ":neighbor_of_1", 0),
                        (assign, ":neighbor_of_2", 0),
                        (assign, ":end_loop_2", kingdoms_end),
                        (try_for_range, ":test_faction", kingdoms_begin, ":end_loop_2"),
                            (store_add, ":slot", slot_faction_neighbors_begin, ":test_faction"),
                            (val_sub, ":slot", kingdoms_begin),
                            (faction_slot_eq, ":third_kingdom", ":slot", 1),

                            (try_begin),
                                (eq, ":test_faction", ":cur_kingdom"),
                                (assign, ":neighbor_of_1", 1),
                            (else_try),
                                (eq, ":test_faction", ":cur_kingdom_2"),
                                (assign, ":neighbor_of_2", 1),
                            (try_end),

                            (eq, ":neighbor_of_1", 1),
                            (eq, ":neighbor_of_2", 1),
                            (assign, ":neighbors_of_neighbors", 1),
                            (assign, ":end_loop_2", ":test_faction"),
                        (try_end),
                        (eq, ":neighbors_of_neighbors", 1),
                        (assign, ":end_loop", ":third_kingdom"),
                    (try_end),

                    (this_or_next|eq, ":neighbors", 1),
                    (eq, ":neighbors_of_neighbors", 1),

                    (try_begin),
                        (eq, ":cur_kingdom_2", "fac_player_supporters_faction"),
                        (assign, ":kingdom_2_to_kingdom_1", 2),
                        (assign, ":shared_history", 50),
                    (else_try),
                        (call_script, "script_npc_decision_checklist_peace_or_war", ":cur_kingdom_2", ":cur_kingdom", -1),
                        (assign, ":kingdom_2_to_kingdom_1", reg0),
                        (store_relation, ":shared_history", ":cur_kingdom_2", ":cur_kingdom"),
                    (try_end),

                    (ge, ":kingdom_2_to_kingdom_1", 1),

                    (store_add, ":goodwill_level", ":kingdom_1_to_kingdom_2", ":kingdom_2_to_kingdom_1"),    #range 2 to 6
                    (val_mul, ":goodwill_level", 3),
                    (val_sub, ":goodwill_level", 5),    #range 1 to 13

                    (val_add, ":shared_history", ":cur_relation"),
                    (val_div, ":shared_history", 20),    #range 0 to 9
                    (val_add, ":goodwill_level", ":shared_history"),

                    (ge, ":goodwill_level", 1),    #both kingdoms like each other, range 1-22
                    (store_random_in_range, ":random", 0, 7),    #if they either really like each other or want each other, this will auto succeed
                    (lt, ":random", ":goodwill_level"),

                    (store_add, ":slot_truce_days", ":cur_kingdom", slot_faction_truce_days_with_factions_begin),
                    (val_sub, ":slot_truce_days", kingdoms_begin),
                    (faction_get_slot, ":truce_days", ":cur_kingdom_2", ":slot_truce_days"),

                    (faction_get_slot, reg0, ":cur_kingdom", slot_faction_leader),
                    (call_script, "script_dplmc_store_troop_personality_caution_level", reg0),
                    (assign, ":troop_caution", reg0),

                    (try_begin),
                        # try to make an offer to player
                        (eq, ":cur_kingdom_2", "fac_player_supporters_faction"),
                        (try_begin),
                            (is_between, ":truce_days", dplmc_treaty_trade_days_expire, dplmc_treaty_defense_days_half_done),
                            (ge, ":cur_relation", 30),
                            (faction_slot_eq, ":cur_kingdom", slot_faction_recognized_player, 1),  #recognized us
                            #  avoid "diplomacy" wars
                            (call_script, "script_count_wars_and_pacts", ":cur_kingdom", ":cur_kingdom_2"),
                            (ge, reg0, 0),
                            (this_or_next|eq, reg1, 0),    # no countervailing pacts OR
                            (eq, ":troop_caution", -1),    #aggressive
                            (call_script, "script_add_notification_menu", "mnu_dplmc_question_alliance_offer", ":cur_kingdom", 0),
                        (else_try),
                            (is_between, ":truce_days", 0, dplmc_treaty_trade_days_half_done),
                            (ge, ":cur_relation", 20),
                            (faction_slot_eq, ":cur_kingdom", slot_faction_recognized_player, 1), #recognized us
                            #MOTO avoid "diplomacy" wars
                            (call_script, "script_count_wars_and_pacts", ":cur_kingdom", ":cur_kingdom_2"),
                            (ge, reg0, 0),
                            (this_or_next|eq, reg1, 0),    #no countervailing pacts OR
                            (eq, ":troop_caution", -1),    #aggressive
                            #MOTO avoid "diplomacy" wars end
                            (call_script, "script_add_notification_menu", "mnu_dplmc_question_defensive_offer", ":cur_kingdom", 0),
                        (else_try),
                            ##nested diplomacy start+ change to use constants chief
                            #(is_between, ":truce_days", 0, 10),
                            (is_between, ":truce_days", 0, dplmc_treaty_truce_days_half_done),
                            ##diplomacy end+
                            (ge, ":cur_relation", 10),
                            (faction_slot_eq, ":cur_kingdom", slot_faction_recognized_player, 1), #recognized us
                            #MOTO avoid "diplomacy" wars
                            (call_script, "script_count_wars_and_pacts", ":cur_kingdom", ":cur_kingdom_2"),
                            (ge, reg0, 0),
                            #MOTO avoid "diplomacy" wars end
                            (call_script, "script_add_notification_menu", "mnu_dplmc_question_trade_offer", ":cur_kingdom", 0),
                        (else_try),
                            (eq, ":truce_days", 0),
                            (ge, ":cur_relation", 5),
                            (call_script, "script_add_notification_menu", "mnu_dplmc_question_nonaggression_offer", ":cur_kingdom", 0),
                        (try_end),
                    (else_try),
                        # try other agreements
                        (try_begin),
                            (is_between, ":truce_days", dplmc_treaty_trade_days_expire, dplmc_treaty_defense_days_half_done),
                            (ge, ":shared_history", 3),
                            (call_script, "script_count_wars_and_pacts", ":cur_kingdom", ":cur_kingdom_2"),
                            (ge, reg0, 0),
                            (this_or_next|eq, reg1, 0),  # no countervailing pacts OR
                            (eq, ":troop_caution", -1),  # aggressive

                            (call_script, "script_dplmc_start_alliance_between_kingdoms", ":cur_kingdom", ":cur_kingdom_2", ":initializing_war_peace_cond"),
                        (else_try),
                            (is_between, ":truce_days", 0, dplmc_treaty_trade_days_half_done),
                            (ge, ":shared_history", 2),
                            (call_script, "script_count_wars_and_pacts", ":cur_kingdom", ":cur_kingdom_2"),
                            (ge, reg0, 0),
                            (this_or_next|eq, reg1, 0),    #no countervailing pacts OR
                            (eq, ":troop_caution", -1),    #aggressive
                            (call_script, "script_dplmc_start_defensive_between_kingdoms", ":cur_kingdom", ":cur_kingdom_2", ":initializing_war_peace_cond"),
                        (else_try),
                            (is_between, ":truce_days", 0, dplmc_treaty_truce_days_half_done),

                            (ge, ":shared_history", 1),
                            (call_script, "script_count_wars_and_pacts", ":cur_kingdom", ":cur_kingdom_2"),
                            (ge, reg0, 0),

                            (call_script, "script_dplmc_start_trade_between_kingdoms", ":cur_kingdom", ":cur_kingdom_2", ":initializing_war_peace_cond"),
                        (else_try),
                            (eq, ":truce_days", 0),
                            (call_script, "script_dplmc_start_nonaggression_between_kingdoms", ":cur_kingdom", ":cur_kingdom_2", ":initializing_war_peace_cond"),
                        (try_end),
                    (try_end),
                (try_end),
            (try_end),
        (try_end),
    ]),

    # arg1: kingdom_a (attacking)
    # arg2: kingdom_b (defending)
    # arg3: war reason:
    #   = 0 means no reason (get it from a script) and the script is being run during initialization.
    #   = 1 means no reason (get it from a script)
    #   = logent to set the reason for the war declaration
    ("diplomacy_start_war_between_kingdoms", [
        (store_script_param, ":kingdom_a", 1),
        (store_script_param, ":kingdom_b", 2),
        (store_script_param, ":initializing_war_peace_cond", 3),

        (try_begin),
            (gt, ":initializing_war_peace_cond", 1),
            (assign, ":reason", ":initializing_war_peace_cond"),
            (assign, ":initializing_war_peace_cond", 1),
        (else_try),
            # if no reason given, get it from script
            (call_script, "script_npc_decision_checklist_peace_or_war", ":kingdom_a", ":kingdom_b", -1),
            (assign, ":explainer_string", reg1),

            (try_begin),
                (eq, ":kingdom_a", "fac_player_supporters_faction"),
                (assign, ":reason", logent_player_faction_declares_war),
            (else_try),
                #for savegame compatibility, this event stands in for the attempt to declare war on all of calradia
                (eq, ":explainer_string", "str_s12s15_declared_war_to_control_calradia"),
                (assign, ":reason", logent_player_faction_declares_war),
            (else_try),
                (eq, ":explainer_string", "str_s12s15_considers_s16_to_be_dangerous_and_untrustworthy_and_shehe_wants_to_bring_s16_down"),
                (assign, ":reason", logent_faction_declares_war_out_of_personal_enmity),
            (else_try),
                (eq, ":explainer_string", "str_s12s15_is_anxious_to_reclaim_old_lands_such_as_s18_now_held_by_s16"),
                (assign, ":reason", logent_faction_declares_war_to_regain_territory),
            (else_try),
                (eq, ":explainer_string", "str_s12s15_faces_too_much_internal_discontent_to_feel_comfortable_ignoring_recent_provocations_by_s16s_subjects"),
                (assign, ":reason", logent_faction_declares_war_to_respond_to_provocation),
            (else_try),
                (eq, ":explainer_string", "str_s12s15_is_alarmed_by_the_growing_power_of_s16"),
                (assign, ":reason", logent_faction_declares_war_to_curb_power),
            (else_try),
                #for savegame compatibility, this event stands in for the attempt to declare war on all of calradia
                (eq, ":explainer_string", "str_s12s15_dominates_its_weaker_neighbor_s16"),
                (assign, ":reason", logent_player_faction_declares_war),
            (else_try),
                (eq, ":explainer_string", "str_s12s15_acts_to_drive_the_people_of_s16_and_their_like_out_of_the_Isles"),
                (assign, ":reason", logent_faction_declares_war_out_of_personal_enmity),
            (try_end),
        (try_end),

        (call_script, "script_add_log_entry", ":reason", ":kingdom_a", 0, 0, ":kingdom_b"),

        # effects of policy only after the start of the game
        (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", ":kingdom_a", ":kingdom_b"),
        (assign, ":current_diplomatic_status", reg0),
        (try_begin),
            (eq, ":reason", logent_faction_declares_war_to_fulfil_pact),
            (call_script, "script_faction_follows_controversial_policy", ":kingdom_a", logent_policy_ruler_declares_war_with_justification),
        (else_try),
            (eq, ":initializing_war_peace_cond", 1),
            (eq, ":current_diplomatic_status", -1),
            (call_script, "script_faction_follows_controversial_policy", ":kingdom_a", logent_policy_ruler_declares_war_with_justification),
        (else_try),
            (eq, ":initializing_war_peace_cond", 1),
            (eq, ":current_diplomatic_status", 0),
            (call_script, "script_faction_follows_controversial_policy", ":kingdom_a", logent_policy_ruler_attacks_without_provocation),
        (else_try),
            (eq, ":current_diplomatic_status", 1),
            (call_script, "script_faction_follows_controversial_policy", ":kingdom_a", logent_policy_ruler_breaks_truce),
        (try_end),

        (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
        (val_min, ":relation", -10),
        (val_add, ":relation", -30),
        (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),

        (try_begin),
            (eq, "$players_kingdom", ":kingdom_a"),
            (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
            (val_min, ":relation", -30),
            (call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
        (else_try),
            (eq, "$players_kingdom", ":kingdom_b"),
            (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
            (val_min, ":relation", -30),
            (call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
        (try_end),

        (try_begin),
            (eq, ":initializing_war_peace_cond", 1),

            (str_store_faction_name_link, s1, ":kingdom_a"),
            (str_store_faction_name_link, s2, ":kingdom_b"),
            (display_log_message, "@{s1} has declared war against {s2}.", color_quest_and_faction_news),

            (store_current_hours, ":hours"),
            (faction_set_slot, ":kingdom_a", slot_faction_ai_last_decisive_event, ":hours"),
            (faction_set_slot, ":kingdom_b", slot_faction_ai_last_decisive_event, ":hours"),

            # set provocation and truce days
            (store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
            (store_add, ":provocation_slot", ":kingdom_b", slot_faction_provocation_days_with_factions_begin),
            (val_sub, ":truce_slot", kingdoms_begin),
            (val_sub, ":provocation_slot", kingdoms_begin),
            (faction_set_slot, ":kingdom_a", ":truce_slot", 0),
            (faction_set_slot, ":kingdom_a", ":provocation_slot", 0),

            (store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
            (store_add, ":provocation_slot", ":kingdom_a", slot_faction_provocation_days_with_factions_begin),
            (val_sub, ":truce_slot", kingdoms_begin),
            (val_sub, ":provocation_slot", kingdoms_begin),
            (faction_set_slot, ":kingdom_b", ":truce_slot", 0),
            (faction_set_slot, ":kingdom_b", ":provocation_slot", 0),

            (call_script, "script_add_notification_menu", "mnu_notification_war_declared", ":kingdom_a", ":kingdom_b"),

            (call_script, "script_update_faction_notes", ":kingdom_a"),
            (call_script, "script_update_faction_notes", ":kingdom_b"),
            (assign, "$g_recalculate_ais", 1),
        (try_end),

        (try_begin),
            (check_quest_active, "qst_cause_provocation"),
            (neg|check_quest_succeeded, "qst_cause_provocation"),
            (this_or_next|eq, "$players_kingdom", ":kingdom_a"),
            (eq, "$players_kingdom", ":kingdom_b"),
            (call_script, "script_abort_quest", "qst_cause_provocation", 0),
        (try_end),

        # active defensive pacts (against kindom_a)
        (try_begin),
            # war was not caused by defensive pact or alliance
            (neq, ":reason", logent_faction_declares_war_to_fulfil_pact),

            (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
                (neq, ":cur_kingdom", ":kingdom_a"),
                (neq, ":cur_kingdom", ":kingdom_b"),

                # is at peace
                (store_relation, ":cur_relation", ":cur_kingdom", ":kingdom_a"),
                (ge, ":cur_relation", 0),

                # not in a truce
                (store_add, ":truce_slot", ":kingdom_b", slot_faction_truce_days_with_factions_begin),
                (val_sub, ":truce_slot", kingdoms_begin),
                (faction_get_slot, ":truce_days", ":cur_kingdom", ":truce_slot"),
                (gt, ":truce_days", dplmc_treaty_defense_days_expire),

                (assign, "$g_last_acting_faction", ":cur_kingdom"),
                (assign, "$g_last_target_faction", ":kingdom_a"),
                (str_store_faction_name, s15, ":cur_kingdom"),
                (str_store_faction_name, s16, ":kingdom_a"),
                (str_store_faction_name, s17, ":kingdom_b"),
                (str_store_string, s64, "@{s15} complies with its defensive pact with {s17} by attacking {s16}."),

                (call_script, "script_diplomacy_start_war_between_kingdoms", ":cur_kingdom", ":kingdom_a", logent_faction_declares_war_to_fulfil_pact),
            (try_end),
        (try_end),

        # activate alliances (against kindom_b)
        (try_for_range, ":cur_kingdom", kingdoms_begin, kingdoms_end),
            (neq, ":cur_kingdom", ":kingdom_a"),
            (neq, ":cur_kingdom", ":kingdom_b"),

            # is at peace
            (store_relation, ":cur_relation", ":cur_kingdom", ":kingdom_b"),
            (ge, ":cur_relation", 0),

            # not in a truce
            (store_add, ":truce_slot", ":kingdom_a", slot_faction_truce_days_with_factions_begin),
            (val_sub, ":truce_slot", kingdoms_begin),
            (faction_get_slot, ":truce_days", ":cur_kingdom", ":truce_slot"),
            (gt, ":truce_days", dplmc_treaty_alliance_days_expire),

            # todo: is this required?
            # build explanation string chief
            (assign, "$g_last_acting_faction", ":cur_kingdom"),
            (assign, "$g_last_target_faction", ":kingdom_b"),
            (str_store_faction_name, s15, ":cur_kingdom"),
            (str_store_faction_name, s16, ":kingdom_b"),
            (str_store_faction_name, s17, ":kingdom_a"),
            (str_store_string, s64, "@{s15} complies with its alliance with {s17} by attacking {s16}."),

            (call_script, "script_diplomacy_start_war_between_kingdoms", ":cur_kingdom", ":kingdom_b", logent_faction_declares_war_to_fulfil_pact),
        (try_end),
    ]),

    # Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
    # Output: none
    ("diplomacy_start_peace_between_kingdoms", [
        (store_script_param, ":kingdom_a", 1),
        (store_script_param, ":kingdom_b", 2),
        (store_script_param, ":initializing_war_peace_cond", 3), #set to 1 if not the start of the game

        (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
        (val_max, ":relation", 0),
        (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
        (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

        (try_begin),
            (eq, "$players_kingdom", ":kingdom_a"),
            (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
            (val_max, ":relation", 0),
            (call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
            (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", "fac_player_supporters_faction"), #event cancels certain quests
        (else_try),
            (eq, "$players_kingdom", ":kingdom_b"),
            (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
            (val_max, ":relation", 0),
            (call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
            (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", "fac_player_supporters_faction"), #event cancels certain quests
        (try_end),

        (try_for_range, ":cur_center", centers_begin, centers_end),
            (store_faction_of_party, ":faction_no", ":cur_center"),
            (this_or_next|eq, ":faction_no", ":kingdom_a"),
            (eq, ":faction_no", ":kingdom_b"),
            (party_get_slot, ":besieger_party", ":cur_center", slot_center_is_besieged_by),
            (ge, ":besieger_party", 0), #town is under siege
            (party_is_active, ":besieger_party"),
            (store_faction_of_party, ":besieger_party_faction_no", ":besieger_party"),
            (this_or_next|eq, ":besieger_party_faction_no", ":kingdom_a"),
            (eq, ":besieger_party_faction_no", ":kingdom_b"),
            (call_script, "script_lift_siege", ":cur_center", 0),
        (try_end),

        (try_begin),
            (this_or_next|eq, "$players_kingdom", ":kingdom_a"),
            (eq, "$players_kingdom", ":kingdom_b"),

            (ge, "$g_player_besiege_town", 0),
            (party_is_active, "$g_player_besiege_town"),

            (store_faction_of_party, ":besieged_center_faction_no", "$g_player_besiege_town"),

            (this_or_next|eq, ":besieged_center_faction_no", ":kingdom_a"),
            (eq, ":besieged_center_faction_no", ":kingdom_b"),

            (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
            (assign, "$g_player_besiege_town", -1),
        (try_end),

        (try_begin),
            (eq, ":initializing_war_peace_cond", 1),
            (str_store_faction_name_link, s1, ":kingdom_a"),
            (str_store_faction_name_link, s2, ":kingdom_b"),
            (display_log_message, "@{s1} and {s2} have made peace with each other.", color_quest_and_faction_news),
            (call_script, "script_add_notification_menu", "mnu_notification_peace_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu        
            (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
            (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
            (assign, "$g_recalculate_ais", 1),
        (try_end),

        add_truce(":kingdom_a", ":kingdom_b"),
    ]),

    # Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
    # Output: none
    ("dplmc_start_alliance_between_kingdoms", [
        (store_script_param, ":kingdom_a", 1),
        (store_script_param, ":kingdom_b", 2),
        (store_script_param, ":initializing_war_peace_cond", 3),

        (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
        (val_add, ":relation", 15),
        (val_max, ":relation", 40),
        (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
        (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

        (try_begin),
            (eq, "$players_kingdom", ":kingdom_a"),
            (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
            (val_add, ":relation", 15),
            (val_max, ":relation", 40),
            (call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
        (else_try),
            (eq, "$players_kingdom", ":kingdom_b"),
            (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
            (val_add, ":relation", 15),
            (val_max, ":relation", 40),
            (call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
        (try_end),

        (try_begin),
            (eq, ":initializing_war_peace_cond", 1),
            (str_store_faction_name_link, s1, ":kingdom_a"),
            (str_store_faction_name_link, s2, ":kingdom_b"),
            (display_log_message, "@{s1} and {s2} have entered into an alliance with each other."),

            (call_script, "script_add_notification_menu", "mnu_dplmc_notification_alliance_declared", ":kingdom_a", ":kingdom_b"), #stability penalty for early peace is in the menu

            (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
            (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
            (assign, "$g_recalculate_ais", 1),
        (try_end),

        add_truce(":kingdom_a", ":kingdom_b"),

        # share wars
        (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
            (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
            (neq, ":kingdom_a", ":faction_no"),
            (neq, ":kingdom_b", ":faction_no"),
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_a", ":faction_no"),
            #result: -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
            (eq, reg0, -2),
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_b", ":faction_no"),
            (ge, reg0, -1),

            # todo: is this block needed?
            # MOTO build explanation string chief
            (assign, "$g_last_acting_faction", ":kingdom_b"),
            (assign, "$g_last_target_faction", ":faction_no"),
            (str_store_faction_name, s15, ":kingdom_b"),
            (str_store_faction_name, s16, ":faction_no"),
            (str_store_string, s64, "@{s15} complies with the new alliance by attacking {s16}."),
            # MOTO build explanation string end
            (call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_b", ":faction_no", logent_faction_declares_war_to_fulfil_pact),
        (try_end),

        # todo: this block is a code of the previous; make it a Python function
        (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
            (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
            (neq, ":kingdom_a", ":faction_no"),
            (neq, ":kingdom_b", ":faction_no"),
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_b", ":faction_no"),
            #result: -1 faction_1 has a casus belli against faction_2. 1, faction_1 has a truce with faction_2, -2, the two factions are at war
            (eq, reg0, -2),
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction",":kingdom_a", ":faction_no"),
            (ge, reg0, -1),
            # MOTO build explanation string chief
            (assign, "$g_last_acting_faction", ":kingdom_a"),
            (assign, "$g_last_target_faction", ":faction_no"),
            (str_store_faction_name, s15, ":kingdom_a"),
            (str_store_faction_name, s16, ":faction_no"),
            (str_store_string, s64, "@{s15} complies with the new alliance by attacking {s16}."),
            # MOTO build explanation string end
            (call_script, "script_diplomacy_start_war_between_kingdoms", ":kingdom_a", ":faction_no", logent_faction_declares_war_to_fulfil_pact),
        (try_end),
    ]),

    # Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
    # Output: none
    ("dplmc_start_defensive_between_kingdoms", [
        (store_script_param, ":kingdom_a", 1),
        (store_script_param, ":kingdom_b", 2),
        (store_script_param, ":initializing_war_peace_cond", 3),

        (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
        (val_add, ":relation", 10),
        (val_max, ":relation", 30),
        (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
        (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

        (try_begin),
            (eq, "$players_kingdom", ":kingdom_a"),
            (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
            (val_add, ":relation", 10),
            (val_max, ":relation", 30),
            (call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
        (else_try),
            (eq, "$players_kingdom", ":kingdom_b"),
            (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
            (val_add, ":relation", 10),
            (val_max, ":relation", 30),
            (call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
        (try_end),

        (try_begin),
            (eq, ":initializing_war_peace_cond", 1),
            (str_store_faction_name_link, s1, ":kingdom_a"),
            (str_store_faction_name_link, s2, ":kingdom_b"),
            (display_log_message, "@{s1} and {s2} have concluded a defensive pact with each other."),

            #stability penalty for early peace is in the menu
            #(call_script, "script_add_notification_menu", "mnu_dplmc_notification_defensive_declared", ":kingdom_a", ":kingdom_b"),

            (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
            (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
            (assign, "$g_recalculate_ais", 1),
        (try_end),

        add_truce(":kingdom_a", ":kingdom_b"),
    ]),

    # Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
    # Output: none
    ("dplmc_start_trade_between_kingdoms", [
        (store_script_param, ":kingdom_a", 1),
        (store_script_param, ":kingdom_b", 2),
        (store_script_param, ":initializing_war_peace_cond", 3),

        (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
        (val_add, ":relation", 5),
        (val_max, ":relation", 20),
        (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
        (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

        (try_begin),
            (eq, "$players_kingdom", ":kingdom_a"),
            (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
            (val_add, ":relation", 5),
            (val_max, ":relation", 20),
            (call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
        (else_try),
            (eq, "$players_kingdom", ":kingdom_b"),
            (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
            (val_add, ":relation", 5),
            (val_max, ":relation", 20),
            (call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
        (try_end),

        (try_begin),
            (eq, ":initializing_war_peace_cond", 1),
            (str_store_faction_name_link, s1, ":kingdom_a"),
            (str_store_faction_name_link, s2, ":kingdom_b"),
            (display_log_message, "@{s1} and {s2} have concluded a trade agreement with each other."),

            #stability penalty for early peace is in the menu
            #(call_script, "script_add_notification_menu", "mnu_dplmc_notification_trade_declared", ":kingdom_a", ":kingdom_b"),
            (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
            (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
            (assign, "$g_recalculate_ais", 1),
        (try_end),

        add_truce(":kingdom_a", ":kingdom_b"),
    ]),

    # Input: arg1 = kingdom_1, arg2 = kingdom_2, arg3 = initializing_war_peace_cond
    # Output: none
    ("dplmc_start_nonaggression_between_kingdoms", [
        (store_script_param, ":kingdom_a", 1),
        (store_script_param, ":kingdom_b", 2),
        (store_script_param, ":initializing_war_peace_cond", 3),

        (store_relation, ":relation", ":kingdom_a", ":kingdom_b"),
        (val_add, ":relation", 3),
        (val_max, ":relation", 10),
        (set_relation, ":kingdom_a", ":kingdom_b", ":relation"),
        (call_script, "script_exchange_prisoners_between_factions", ":kingdom_a", ":kingdom_b"),

        (try_begin),
            (eq, "$players_kingdom", ":kingdom_a"),
            (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_b"),
            (val_add, ":relation", 3),
            (val_max, ":relation", 10),
            (call_script, "script_set_player_relation_with_faction", ":kingdom_b", ":relation"),
        (else_try),
            (eq, "$players_kingdom", ":kingdom_b"),
            (store_relation, ":relation", "fac_player_supporters_faction", ":kingdom_a"),
            (val_add, ":relation", 3),
            (val_max, ":relation", 10),
            (call_script, "script_set_player_relation_with_faction", ":kingdom_a", ":relation"),
        (try_end),

        (try_begin),
            (eq, ":initializing_war_peace_cond", 1),
            (str_store_faction_name_link, s1, ":kingdom_a"),
            (str_store_faction_name_link, s2, ":kingdom_b"),
            (display_log_message, "@{s1} and {s2} have agreed to a non-aggression pact."),

            #(call_script, "script_add_notification_menu", "mnu_dplmc_notification_nonaggression_declared", ":kingdom_a", ":kingdom_b"),
            (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_a", ":kingdom_b"), #cancels quests
            (call_script, "script_event_kingdom_make_peace_with_kingdom", ":kingdom_b", ":kingdom_a"), #cancels quests
            (assign, "$g_recalculate_ais", 1),
        (try_end),

        add_truce(":kingdom_a", ":kingdom_b"),
    ]),
]
