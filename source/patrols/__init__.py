from source.header_operations import *
from source.header_common import *
from source.header_dialogs import anyone, plyr, repeat_for_parties
from source.header_parties import ai_bhvr_travel_to_party, ai_bhvr_patrol_location

from source.module_constants import spt_patrol, slot_party_type, slot_party_ai_object, \
    centers_begin, centers_end, slot_party_ai_state, spai_patrolling_around_center, \
    dplmc_slot_party_mission_diplomacy, spai_retreating_to_center, npc_kingdoms_begin, \
    npc_kingdoms_end, towns_begin, towns_end, slot_faction_leader, slot_party_home_center, \
    slot_center_original_faction, slot_faction_reinforcements_a, slot_town_lord, \
    slot_troop_original_faction, slot_faction_reinforcements_b, slot_faction_reinforcements_c


dialogs = [

    [anyone, "start", [
        (party_slot_eq, "$g_encountered_party", slot_party_type, spt_patrol),
        (party_slot_eq, "$g_encountered_party", dplmc_slot_party_mission_diplomacy, "trp_player"),
        (party_get_slot, ":target_party", "$g_encountered_party", slot_party_ai_object),
        (str_store_party_name, s6, ":target_party"),
        ], "Greetings, Sire. We are still patrolling {s6}. Do you have new orders?", "patrol_talk", []
    ],

    [anyone, "patrol_pretalk", [], "Greetings, Sire. Do you have new orders?", "patrol_talk", []],

    # patrol new area
    [anyone | plyr, "patrol_talk", [],
     "Please patrol a new area.", "patrol_orders_area_ask", []
    ],

    [anyone, "patrol_orders_area_ask", [], "Where should we go?",
     "patrol_orders_area", []
    ],

    [anyone | plyr | repeat_for_parties, "patrol_orders_area", [
        (store_repeat_object, ":party_no"),
        (is_between, ":party_no", centers_begin, centers_end),
        (store_faction_of_party, ":party_faction", ":party_no"),
        (eq, ":party_faction", "$players_kingdom"),
        (str_store_party_name, s11, ":party_no"),
        ], "{s11}.", "patrol_confirm_ask", [
        (store_repeat_object, "$diplomacy_var"),
    ]],

    [anyone | plyr, "patrol_orders_area", [], "Nevermind.", "patrol_pretalk", []],

    [anyone, "patrol_confirm_ask", [
        (str_store_party_name, s5, "$diplomacy_var")
        ], "As you wish, we will patrol {s5}.", "patrol_confirm", []
    ],

    [anyone | plyr, "patrol_confirm", [
        (str_store_party_name, s5, "$diplomacy_var")
    ], "Thank you.", "close_window", [
        (party_set_name, "$g_encountered_party", "@{s5} patrol"),
        (party_set_slot, "$g_encountered_party", slot_party_ai_object, "$diplomacy_var"),
        (party_set_slot, "$g_encountered_party", slot_party_ai_state, spai_patrolling_around_center),
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_travel_to_party),
        (party_set_ai_object, "$g_encountered_party", "$diplomacy_var"),
        (assign, "$g_leave_encounter", 1),
     ]],

    [anyone | plyr, "patrol_confirm", [], "Wait, I changed my mind.", "patrol_pretalk", []],

    # reinforce garrison
    [anyone | plyr, "patrol_talk", [], "I need you to reinforce a garrison.",
     "patrol_orders_garrison_ask", []],

    [anyone, "patrol_orders_garrison_ask", [],
     "Where should we go?", "patrol_garrison_target", []],

    [anyone | plyr | repeat_for_parties, "patrol_garrison_target", [
        (store_repeat_object, ":party_no"),
        (is_between, ":party_no", centers_begin, centers_end),
        (store_faction_of_party, ":party_faction", ":party_no"),
        (eq, ":party_faction", "$players_kingdom"),
        (str_store_party_name, s11, ":party_no"),
        ], "{!}{s11}.", "patrol_garrison_confirm_ask", [
        (store_repeat_object, "$diplomacy_var"),
    ]],

    [anyone | plyr, "patrol_garrison_target", [], "Nevermind.", "patrol_pretalk", []],

    [anyone, "patrol_garrison_confirm_ask", [
        (str_store_party_name, s5, "$diplomacy_var")
        ], "As you wish, we will reinforce {s5}.", "patrol_garrison_confirm", []
    ],

    [anyone | plyr, "patrol_garrison_confirm", [
        (str_store_party_name, s5, "$diplomacy_var")
        ], "Thank you.", "close_window", [
        (party_set_name, "$g_encountered_party", "@{s5} patrol"),
        (party_set_slot, "$g_encountered_party", slot_party_ai_object, "$diplomacy_var"),
        (party_set_slot, "$g_encountered_party", slot_party_ai_state, spai_retreating_to_center),
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_travel_to_party),
        (party_set_ai_object, "$g_encountered_party", "$diplomacy_var"),
        (assign, "$g_leave_encounter", 1),
    ]],

    [anyone | plyr, "patrol_garrison_confirm", [],
     "Wait, I changed my mind.", "patrol_pretalk", []],

    # give troops
    [anyone | plyr, "patrol_talk", [],
     "I want to hand over some men to the patrol.", "patrol_give_troops", []],

    [anyone, "patrol_give_troops", [],
     "Well, I could use some good soldiers. Thank you.", "patrol_pretalk", [
        (change_screen_give_members, "$g_talk_troop_party"),
        (change_screen_exchange_members, 0),
    ]],

    # disband
    [anyone | plyr, "patrol_talk", [],
     "I do not need you any longer. I command you to disband.", "close_window", [
        (remove_party, "$g_encountered_party"),
        (assign, "$g_leave_encounter", 1),
    ]],

    [anyone | plyr, "patrol_talk", [], "Please continue.", "close_window", [
        (assign, "$g_leave_encounter", 1)
    ]],
]

simple_triggers = [

    # Patrol wages
    # todo: why aren't patrol wages equal to NPC patrols?
    (24 * 7, [
        (try_for_parties, ":party_no"),
            (party_slot_eq, ":party_no", slot_party_type, spt_patrol),

            (party_get_slot, ":ai_state", ":party_no", slot_party_ai_state),
            (eq, ":ai_state", spai_patrolling_around_center),

            (try_begin),
                (party_slot_eq, ":party_no", dplmc_slot_party_mission_diplomacy, "trp_player"),
                (assign, ":total_wage", 0),
                (party_get_num_companion_stacks, ":num_stacks", ":party_no"),
                (try_for_range, ":i_stack", 0, ":num_stacks"),
                    (party_stack_get_troop_id, ":stack_troop", ":party_no", ":i_stack"),
                    (party_stack_get_size, ":stack_size", ":party_no", ":i_stack"),
                    (call_script, "script_game_get_troop_wage", ":stack_troop", 0),
                    (val_mul, reg0, ":stack_size"),
                    (val_add, ":total_wage", reg0),
                (try_end),
                (store_troop_gold, ":gold", "trp_household_possessions"),

                (try_begin),
                    (lt, ":gold", ":total_wage"),
                    (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),
                    (str_store_party_name, s6, ":target_party"),
                    (display_log_message, "@Your soldiers patrolling {s6} disbanded because you can't pay the wages!", 0xFF0000),
                    (remove_party, ":party_no"),
                (try_end),
            (try_end),
        (try_end),
    ]),

    # create patrols for npc factions
    (24 * 7, [
        (try_for_range, ":kingdom", npc_kingdoms_begin, npc_kingdoms_end),

            # max patrols = number of towns
            (assign, ":max_patrols", 0),
            (try_for_range, ":center", towns_begin, towns_end),
                (store_faction_of_party, ":center_faction", ":center"),
                (eq, ":center_faction", ":kingdom"),
                (val_add, ":max_patrols", 1),
            (try_end),

            (assign, ":count", 0),
            (try_for_parties, ":party_no"),
                # Remove patrols above the maximum number allowed.
                (party_slot_eq, ":party_no", slot_party_type, spt_patrol),
                (store_faction_of_party, ":party_faction", ":party_no"),
                (eq, ":party_faction", ":kingdom"),
                (neg | party_slot_eq, ":party_no", dplmc_slot_party_mission_diplomacy, "trp_player"),  # not player ordered
                (try_begin),
                    (ge, ":count", ":max_patrols"),

                    (try_begin),
                        (ge, "$cheat_mode", 1),
                        (str_store_faction_name, s4, ":kingdom"),
                        (str_store_party_name, s5, ":party_no"),
                        (display_message, "@{!}DEBUG - Removed {s5} because {s4} cannot support that many patrols"),
                    (try_end),

                    (remove_party, ":party_no"),
                (else_try),
                    (val_add, ":count", 1),
                (try_end),
            (try_end),

            # create patrol
            (try_begin),
                (lt, ":count", ":max_patrols"),

                (store_random_in_range, ":random", 0, 10),
                (le, ":random", 3),

                (assign, ":start_center", -1),
                (assign, ":target_center", -1),

                (try_for_range, ":center", towns_begin, towns_end),
                    (store_faction_of_party, ":center_faction", ":center"),
                    (eq, ":center_faction", ":kingdom"),

                    (eq, ":start_center", -1),
                    (eq, ":target_center", -1),

                    (assign, ":continue", 1),
                    (try_for_parties, ":party_no"),
                        (party_slot_eq, ":party_no", slot_party_type, spt_patrol),
                        (store_faction_of_party, ":party_faction", ":party_no"),
                        (eq, ":party_faction", ":kingdom"),
                        (party_get_slot, ":target_patrol", ":party_no", slot_party_ai_object),  # chief cambia
                        (eq, ":target_patrol", ":center"),  # chief cambia
                        (assign, ":continue", 0),
                    (try_end),
                    (eq, ":continue", 1),

                    (call_script, "script_cf_select_random_town_with_faction", ":kingdom"),
                    (neq, reg0, -1),

                    (assign, ":start_center", reg0),
                    (assign, ":target_center", ":center"),
                (try_end),

                (try_begin),
                    (neq, ":start_center", -1),
                    (neq, ":target_center", -1),
                    (store_random_in_range, ":random_size", 0, 3),
                    (faction_get_slot, ":faction_leader", ":kingdom", slot_faction_leader),
                    (call_script, "script_send_patrol", ":start_center", ":target_center", ":random_size", ":kingdom", ":faction_leader"),
                (try_end),
            (try_end),
        (try_end),
    ]),

    # Patrol ai
    (2, [
        (try_for_parties, ":party_no"),
            (party_slot_eq, ":party_no", slot_party_type, spt_patrol),

            # todo: patrols don't keep prisoners, why?
            (call_script, "script_party_remove_all_prisoners", ":party_no"),

            (try_begin),
                (get_party_ai_behavior, ":ai_behavior", ":party_no"),
                (eq, ":ai_behavior", ai_bhvr_travel_to_party),
                (party_get_slot, ":target_party", ":party_no", slot_party_ai_object),

                (try_begin),
                    (gt, ":target_party", 0),
                    (store_distance_to_party_from_party, ":distance_to_target", ":party_no", ":target_party"),
                    (le, ":distance_to_target", 5),
                    (try_begin),
                        # patrol returned to town, merge it.
                        (party_get_slot, ":ai_state", ":party_no", slot_party_ai_state),
                        (eq, ":ai_state", spai_retreating_to_center),
                        (try_begin),
                            (le, ":distance_to_target", 1),
                            # todo: when a patrol is created, it is not removed from the town party
                            # this is therefore creating units in the town.
                            (call_script, "script_party_add_party", ":target_party", ":party_no"),
                            (remove_party, ":party_no"),
                        (try_end),
                    (else_try),
                        # else, continue patrol
                        (party_get_position, pos1, ":target_party"),
                        (party_set_ai_behavior, ":party_no", ai_bhvr_patrol_location),
                        (party_set_ai_patrol_radius, ":party_no", 1),
                        (party_set_ai_target_position, ":party_no", pos1),
                    (try_end),
                # (else_try),
                # remove party?
                (try_end),
            (try_end),
        (try_end),
    ]),
]

scripts = [
    ("send_patrol", [
        (store_script_param, ":start_party", 1),
        (store_script_param, ":target_party", 2),
        (store_script_param, ":size", 3),  # 0 small, 1 medium, 2 big, 3 elite
        (store_script_param, ":faction", 4),  # the faction that sent it
        (store_script_param, ":order_troop", 5),  # who gave the order

        (set_spawn_radius, 1),
        (spawn_around_party, ":start_party", "pt_patrol_party"),
        (assign, ":spawned_party", reg0),
        (party_set_faction, ":spawned_party", ":faction"),
        (party_set_slot, ":spawned_party", slot_party_type, spt_patrol),
        (party_set_slot, ":spawned_party", slot_party_home_center, ":start_party"),
        (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":order_troop"),
        (str_store_party_name, s5, ":target_party"),
        (party_set_name, ":spawned_party", "@{s5} patrol"),

        (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
        (party_set_ai_object, ":spawned_party", ":target_party"),
        (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
        (party_set_slot, ":spawned_party", slot_party_ai_state, spai_patrolling_around_center),

        (try_begin),
            # own patrols cost money.
            (neg | is_between, ":faction", npc_kingdoms_begin, npc_kingdoms_end),

            (party_get_slot, ":faction", ":start_party", slot_center_original_faction),
            (try_begin),
                (is_between, "$g_player_culture", npc_kingdoms_begin, npc_kingdoms_end),
                (assign, ":faction", "$g_player_culture"),
            (else_try),
                (party_get_slot, ":town_lord", ":start_party", slot_town_lord),
                (gt, ":town_lord", 0),
                (troop_get_slot, ":faction", ":town_lord", slot_troop_original_faction),
            (try_end),

            (try_begin),
                (eq, ":size", 0),
                (call_script, "script_dplmc_withdraw_from_treasury", 1000),
            (else_try),
                (this_or_next | eq, ":size", 1),
                (eq, ":size", 3),
                (call_script, "script_dplmc_withdraw_from_treasury", 2000),
            (else_try),
                (eq, ":size", 2),
                (call_script, "script_dplmc_withdraw_from_treasury", 3000),
            (try_end),
        (try_end),

        (faction_get_slot, ":party_template_a", ":faction", slot_faction_reinforcements_a),
        (faction_get_slot, ":party_template_b", ":faction", slot_faction_reinforcements_b),
        (faction_get_slot, ":party_template_c", ":faction", slot_faction_reinforcements_c),

        (try_begin),
            (eq, ":size", 3),
            (party_add_template, ":spawned_party", ":party_template_c"),
        (else_try),
            (val_add, ":size", 1),
            (val_mul, ":size", 2),
            (try_for_range, ":cur_i", 0, ":size"),
                (store_random_in_range, ":random", 0, 3),
                (try_begin),
                    (eq, ":random", 0),
                    (party_add_template, ":spawned_party", ":party_template_a"),
                (else_try),
                    (eq, ":random", 1),
                    (party_add_template, ":spawned_party", ":party_template_b"),
                (else_try),
                    (party_add_template, ":spawned_party", ":party_template_c"),
                (try_end),

                (try_begin),  # debug
                    (eq, "$cheat_mode", 1),
                    (assign, reg0, ":cur_i"),
                    (str_store_faction_name, s7, ":faction"),
                    (display_message, "@{!}DEBUG - Added {reg0}.template of faction {s7} to patrol."),
                (try_end),
            (try_end),
        (try_end),

        (try_begin),  # debug
            (eq, "$cheat_mode", 1),
            (str_store_party_name, s13, ":target_party"),
            (str_store_faction_name, s14, ":faction"),
            (str_store_party_name, s15, ":start_party"),
            (display_message, "@{!}DEBUG - Send {s14} patrol from {s15} to {s13}"),
        (try_end),
    ]),

    # sends `patrol_party` template to patrol, constructed from party `:party_no`.
    ("send_patrol_party", [
        (store_script_param, ":start_party", 1),
        (store_script_param, ":target_party", 2),
        (store_script_param, ":party_no", 3),
        (store_script_param, ":faction", 4),
        (store_script_param, ":order_troop", 5),

        (set_spawn_radius, 1),
        (spawn_around_party, ":start_party", "pt_patrol_party"),
        (assign, ":spawned_party", reg0),

        (party_set_faction, ":spawned_party", ":faction"),
        (party_set_slot, ":spawned_party", slot_party_type, spt_patrol),
        (party_set_slot, ":spawned_party", slot_party_home_center, ":start_party"),
        (party_set_slot, ":spawned_party", dplmc_slot_party_mission_diplomacy, ":order_troop"),

        (str_store_party_name, s5, ":target_party"),
        (party_set_name, ":spawned_party", "@{s5} patrol"),

        (party_set_ai_behavior, ":spawned_party", ai_bhvr_travel_to_party),
        (party_set_ai_object, ":spawned_party", ":target_party"),
        (party_set_slot, ":spawned_party", slot_party_ai_object, ":target_party"),
        (party_set_slot, ":spawned_party", slot_party_ai_state, spai_patrolling_around_center),

        (call_script, "script_party_add_party", ":spawned_party", ":party_no"),
    ]),
]
