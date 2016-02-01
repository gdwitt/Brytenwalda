from source.header_operations import *
from source.header_common import *

from source.header_dialogs import *

from source.module_constants import dplmc_slot_faction_patrol_time, centers_begin, centers_end, \
    slot_party_type, spt_patrol, spai_undefined, dplmc_slot_party_mission_diplomacy, \
    spai_patrolling_around_center, spai_retreating_to_center


create_option = \
    [anyone | plyr, "dplmc_constable_security", [],
     "I want to enlist a patrol.", "dplmc_constable_patrol_size_ask", []
    ]

dialogs = [
    [anyone, "dplmc_constable_patrol_size_ask", [
        (store_current_hours, ":current_hours"),
        (val_sub, ":current_hours", 24 * 7),
        (faction_get_slot, ":policy_time", "fac_player_faction", dplmc_slot_faction_patrol_time),
        (ge, ":current_hours", ":policy_time"),
        ], "You can take some men from your garrison or enlist fresh ones. "
           "In the latter case you can enlist a small patrol for 1000 scillingas, "
           "a medium patrol for 2000 scillingas or a big patrol for 3000 scillingas. "
           "You can also enlist a small elite patrol for 2000 scillingas. "
           "We have to pay weekly wages for the soldiers so make sure you have "
           "enough money in the treasury.", "dplmc_constable_patrol_size",
        []
    ],

    [anyone, "dplmc_constable_patrol_size_ask", [

        (store_current_hours, ":current_hours"),
        (val_sub, ":current_hours", 24 * 7),
        (faction_get_slot, ":policy_time", "fac_player_faction", dplmc_slot_faction_patrol_time),
        (store_sub, ":wait_hours" , ":policy_time", ":current_hours"),
        (store_div, ":wait_days", ":wait_hours", 24),
        (store_mod, ":wait_mod", ":wait_hours", 24),
        (try_begin),
            (lt, ":wait_mod", 0),
            (val_add, ":wait_days", 1),
        (try_end),
        (assign, reg0, ":wait_days"),
        ], "There are no fresh recruits available at the moment. We have to wait {reg0} days. "
           "But you can take soldiers from your garrison.", "dplmc_constable_patrol_size", []
    ],

    [anyone | plyr, "dplmc_constable_patrol_size", [],
     "Take troops out of the garrison.", "dplmc_constable_patrol_garrison", [

        (store_party_size_wo_prisoners, ":garrison_size", "$current_town"),
        (gt, ":garrison_size", 0),
        (party_clear, "p_temp_party"),
        (assign, "$g_move_heroes", 1),
        (call_script, "script_party_add_party", "p_temp_party", "p_main_party"),
        (party_clear, "p_main_party"),
        (party_remove_members, "p_main_party", "trp_player", 1),

        (change_screen_exchange_members, 1),
    ]],

    [anyone, "dplmc_constable_patrol_garrison", [
        (store_party_size_wo_prisoners, ":garrison_size", "$current_town"),
        (le, ":garrison_size", 0),
        ], "We do not have any troops in the garrison.", "dplmc_constable_patrol_size", []
    ],

    [anyone, "dplmc_constable_patrol_garrison", [],
     "My {lord/lady}, are you done with the patrol troops.", "dplmc_constable_patrol_garrison_2", []
    ],

    [anyone, "dplmc_constable_patrol_garrison_2", [
        (store_party_size_wo_prisoners, ":garrison_size", "p_main_party"),
        (le, ":garrison_size", 0),
        # todo: why this?
        (party_add_members, "p_main_party", "trp_briton_footmant2", 1), #zerilius included otherwise gives errors
        ], "You didn't choose any soldiers. Seems like you changed your mind.",
        "dplmc_constable_pretalk", [
        (party_remove_members, "p_main_party", "trp_briton_footmant2", 1),
        (call_script, "script_party_add_party", "p_main_party", "p_temp_party"),
        (assign, "$g_move_heroes", 0),
    ]],

    # todo: patrol choices do not correspond to the patrol script options. Fix that.
    #[anyone, "dplmc_constable_patrol_garrison",                            #zerilius changes
    [anyone, "dplmc_constable_patrol_garrison_2", [],
     "Where do you want to send the patrol?", "dplmc_constable_patrol_garrison_location", []
    ],

    [anyone | plyr | repeat_for_parties, "dplmc_constable_patrol_garrison_location", [
        (store_repeat_object, ":party_no"),
        (is_between, ":party_no", centers_begin, centers_end),
        (store_faction_of_party, ":party_faction", ":party_no"),
        (eq, ":party_faction", "$players_kingdom"),
        (str_store_party_name, s11, ":party_no"),
        ], "{!}{s11}.", "dplmc_constable_patrol_garrison_confirm_ask", [
        (store_repeat_object, "$diplomacy_var"),
        (party_clear, "p_temp_party_2"),
        (call_script, "script_party_add_party", "p_temp_party_2", "p_main_party"),
        (party_clear, "p_main_party"),
        (party_stack_get_troop_id, ":troop_id", "p_main_party", 0),
        (try_begin),
            (ge, ":troop_id", 0),
            (party_stack_get_size, ":troop_size", "p_main_party", 0),
            (party_remove_members, "p_main_party", ":troop_id", ":troop_size"),
        (try_end),
        (party_stack_get_troop_id, ":troop_id", "p_main_party", 1),
        (try_begin),
            (ge, ":troop_id", 0),
            (party_stack_get_size, ":troop_size", "p_main_party", 1),
            (party_remove_members, "p_main_party", ":troop_id", ":troop_size"),
        (try_end),

        (call_script, "script_party_add_party", "p_main_party", "p_temp_party"),
        (assign, "$g_move_heroes", 0),
    ]],

    [anyone, "dplmc_constable_patrol_garrison_confirm_ask", [
        (store_party_size, ":party_size", "p_temp_party_2"),

        (assign, ":prisoner_size", 0),
        (party_get_num_prisoner_stacks, ":num_prisoner_stacks", "p_temp_party_2"),
        (try_for_range_backwards, ":stack_no", 0, ":num_prisoner_stacks"),
            (party_prisoner_stack_get_size, ":stack_size", "p_temp_party_2", ":stack_no"),
            (val_add, ":prisoner_size", ":stack_size"),
        (try_end),
        (le, ":party_size", ":prisoner_size"),
        ], "You didn't choose any soldiers. Seems like you changed your mind.", "dplmc_constable_pretalk", []
    ],

    [anyone, "dplmc_constable_patrol_garrison_confirm_ask", [
        (str_store_party_name, s9, "$diplomacy_var"),
        ], "Do you really want to send the patrol to {s9}?", "dplmc_constable_patrol_garrison_confirm", []
    ],

    [anyone | plyr, "dplmc_constable_patrol_garrison_confirm", [],
     "Yes.", "dplmc_constable_pretalk", [
        (call_script, "script_send_patrol_party", "$current_town", "$diplomacy_var", "p_temp_party_2", "fac_player_faction", "trp_player"),
        (party_clear, "p_temp_party_2"),
    ]],

    [anyone | plyr, "dplmc_constable_patrol_garrison_confirm", [],
     "No.", "dplmc_constable_pretalk", [
        (call_script, "script_party_add_party", "$current_town", "p_temp_party_2"),
        (party_clear, "p_temp_party_2"),
    ]],

    [anyone | plyr, "dplmc_constable_patrol_size", [
        (store_current_hours, ":current_hours"),
        (val_sub, ":current_hours", 24 * 7),
        (faction_get_slot, ":policy_time", "fac_player_faction", dplmc_slot_faction_patrol_time),
        (ge, ":current_hours", ":policy_time"),

        (store_troop_gold, ":gold", "trp_household_possessions"),
        (ge, ":gold", 1000),
        ], "A small one.", "dplmc_constable_patrol_location_ask", [
        (assign, "$temp", 0),
    ]],

    [anyone | plyr, "dplmc_constable_patrol_size", [
        (store_current_hours, ":current_hours"),
        (val_sub, ":current_hours", 24 * 7),
        (faction_get_slot, ":policy_time", "fac_player_faction", dplmc_slot_faction_patrol_time),
        (ge, ":current_hours", ":policy_time"),

        (store_troop_gold, ":gold", "trp_household_possessions"),
        (ge, ":gold", 2000),
        ], "A medium one.", "dplmc_constable_patrol_location_ask", [
        (assign, "$temp", 1),
    ]],

    [anyone | plyr, "dplmc_constable_patrol_size", [
        (store_current_hours, ":current_hours"),
        (val_sub, ":current_hours", 24 * 7),
        (faction_get_slot, ":policy_time", "fac_player_faction", dplmc_slot_faction_patrol_time),
        (ge, ":current_hours", ":policy_time"),

        (store_troop_gold, ":gold", "trp_household_possessions"),
        (ge, ":gold", 3000),
        ], "A big one.", "dplmc_constable_patrol_location_ask", [
        (assign, "$temp", 2),
    ]],

    [anyone | plyr, "dplmc_constable_patrol_size", [
        (store_current_hours, ":current_hours"),
        (val_sub, ":current_hours", 24 * 7),
        (faction_get_slot, ":policy_time", "fac_player_faction", dplmc_slot_faction_patrol_time),
        (ge, ":current_hours", ":policy_time"),

        (store_troop_gold, ":gold", "trp_household_possessions"),
        (ge, ":gold",2000)
        ], "Get the best troops around.", "dplmc_constable_patrol_location_ask", [
        (assign, "$temp", 3),
    ]],

    [anyone | plyr, "dplmc_constable_patrol_size", [],
     "None.", "dplmc_constable_pretalk", []
    ],

    [anyone, "dplmc_constable_patrol_location_ask", [],
     "Where do you want to send the patrol?", "dplmc_constable_patrol_location", []
    ],

    [anyone | plyr | repeat_for_parties, "dplmc_constable_patrol_location", [
        (store_repeat_object, ":party_no"),
        (is_between, ":party_no", centers_begin, centers_end),
        (store_faction_of_party, ":party_faction", ":party_no"),
        (eq, ":party_faction", "$players_kingdom"),
        (str_store_party_name, s11, ":party_no"),
        ], "{!}{s11}.", "dplmc_constable_patrol_confirm_ask", [
        (store_repeat_object, "$diplomacy_var"),
    ]],

    [anyone | plyr, "dplmc_constable_patrol_location", [],
     "Nowhere.", "dplmc_constable_pretalk", []
    ],

    [anyone, "dplmc_constable_patrol_confirm_ask", [
        (assign, ":size", "str_dplmc_small"),
        (val_add, ":size", "$temp"),
        (str_store_string, s8, ":size"),
        (str_store_party_name, s9, "$diplomacy_var"),
        ], "Do you really want to send a {s8} patrol to {s9}?", "dplmc_constable_patrol_confirm", []
    ],

    [anyone | plyr, "dplmc_constable_patrol_confirm", [],
     "Yes.", "dplmc_constable_pretalk", [
        (store_current_hours, ":current_hours"),
        (faction_set_slot, "fac_player_faction", dplmc_slot_faction_patrol_time, ":current_hours"),
        (call_script, "script_send_patrol", "$current_town", "$diplomacy_var", "$temp", "$players_kingdom", "trp_player"),
    ]],

    [anyone | plyr, "dplmc_constable_patrol_confirm", [], "No.", "dplmc_constable_pretalk", []],
]

############# change patrol target

change_target_option = \
    [anyone | plyr, "dplmc_constable_security", [],
     "I want to change the target of a patrol.", "dplmc_constable_patrol_change_ask", []
    ]

dialogs += [
    [anyone, "dplmc_constable_patrol_change_ask", [],
     "Which patrol should change the target?", "dplmc_constable_patrol_change", []
    ],

    [anyone | plyr | repeat_for_parties, "dplmc_constable_patrol_change", [
        (store_repeat_object, ":party_no"),
        (party_slot_eq, ":party_no", slot_party_type, spt_patrol),
        (party_slot_eq, ":party_no", dplmc_slot_party_mission_diplomacy, "trp_player"),
        (str_store_party_name, s11, ":party_no"),
        ], "{!}{s11}.", "dplmc_constable_patrol_change_target_ask", [
        (store_repeat_object, "$diplomacy_var"),
    ]],

    [anyone | plyr, "dplmc_constable_patrol_change", [], "None.", "dplmc_constable_security_ask", []],

    [anyone, "dplmc_constable_patrol_change_target_ask", [],
     "Where do you want to send it?", "dplmc_constable_patrol_change_target", []],

    [anyone | plyr | repeat_for_parties, "dplmc_constable_patrol_change_target", [
        (store_repeat_object, ":party_no"),
        (is_between, ":party_no", centers_begin, centers_end),
        (store_faction_of_party, ":party_faction", ":party_no"),
        (eq, ":party_faction", "$players_kingdom"),
        (str_store_party_name, s11, ":party_no"),
        ], "{!}{s11}.", "dplmc_constable_patrol_change_target_confirm_ask", [
        (store_repeat_object, "$temp"),
    ]],

    [anyone | plyr, "dplmc_constable_patrol_change_target", [],
     "Nowhere.", "dplmc_constable_security_ask", []
    ],

    [anyone, "dplmc_constable_patrol_change_target_confirm_ask", [
        (str_store_party_name, s5, "$diplomacy_var"),
        (str_store_party_name, s6, "$temp"),
        ], "As you wish, I will send a messenger carrying the orders to "
           "patrol {s6} to the {s5}.", "dplmc_constable_patrol_change_target_confirm", []
    ],

    [anyone | plyr, "dplmc_constable_patrol_change_target_confirm", [],
     "Thank you.", "dplmc_constable_security_ask", [
        (call_script, "script_dplmc_send_messenger_to_party", "$diplomacy_var", spai_patrolling_around_center, "$temp"),
    ]],

    [anyone | plyr, "dplmc_constable_patrol_change_target_confirm", [],
     "Oh maybe not.", "dplmc_constable_security_ask", []
    ],
]

############# move patrol to center

return_to_center_option = \
    [anyone | plyr, "dplmc_constable_security", [],
     "I want a patrol to return to a center.", "dplmc_constable_patrol_to_center_ask", []
    ]

dialogs += [
    [anyone, "dplmc_constable_patrol_to_center_ask", [],
     "Which patrol should move to a center?", "dplmc_constable_patrol_to_center", []
    ],

    [anyone | plyr | repeat_for_parties, "dplmc_constable_patrol_to_center", [
        (store_repeat_object, ":party_no"),
        (party_slot_eq, ":party_no", slot_party_type, spt_patrol),
        (party_slot_eq, ":party_no", dplmc_slot_party_mission_diplomacy, "trp_player"),
        (str_store_party_name, s11, ":party_no"),
        ], "{!}{s11}.", "dplmc_constable_patrol_to_center_target_ask", [
        (store_repeat_object, "$diplomacy_var"),
    ]],

    [anyone | plyr, "dplmc_constable_patrol_to_center", [],
     "None.", "dplmc_constable_security_ask", []
    ],

    [anyone, "dplmc_constable_patrol_to_center_target_ask", [],
     "Where do you want to send it?", "dplmc_constable_patrol_to_center_target", []
    ],

    [anyone | plyr | repeat_for_parties, "dplmc_constable_patrol_to_center_target", [
        (store_repeat_object, ":party_no"),
        (is_between, ":party_no", centers_begin, centers_end),
        (store_faction_of_party, ":party_faction", ":party_no"),
        (eq, ":party_faction", "$players_kingdom"),
        (str_store_party_name, s11, ":party_no"),
        ], "{!}{s11}.", "dplmc_constable_patrol_change_to_center_confirm_ask", [
        (store_repeat_object, "$temp"),
    ]],

    [anyone | plyr, "dplmc_constable_patrol_to_center_target", [],
     "Nowhere.", "dplmc_constable_security_ask", []
    ],

    [anyone, "dplmc_constable_patrol_change_to_center_confirm_ask", [
        (str_store_party_name, s5, "$diplomacy_var"),
        (str_store_party_name, s6, "$temp"),
        ], "As you wish, I will send a messenger carrying the orders to move "
           "to {s6} to the {s5}.", "dplmc_constable_patrol_to_center_confirm", []
    ],

    [anyone | plyr, "dplmc_constable_patrol_to_center_confirm", [],
     "Thank you.", "dplmc_constable_security_ask", [
        (call_script, "script_dplmc_send_messenger_to_party", "$diplomacy_var", spai_retreating_to_center, "$temp"),
    ]],

    [anyone | plyr, "dplmc_constable_patrol_to_center_confirm", [],
     "Oh maybe not.", "dplmc_constable_security_ask", []
    ],
]


############# disband patrol


disband_option = \
    [anyone | plyr, "dplmc_constable_security", [],
     "I want to disband a patrol.", "dplmc_constable_patrol_disband_ask", []
    ]


dialogs += [
    [anyone, "dplmc_constable_patrol_disband_ask", [],
     "Which patrol do you want to disband?", "dplmc_constable_patrol_disband", []
    ],

    [anyone | plyr | repeat_for_parties, "dplmc_constable_patrol_disband", [
        (store_repeat_object, ":party_no"),
        (party_slot_eq, ":party_no", slot_party_type, spt_patrol),
        (party_slot_eq, ":party_no", dplmc_slot_party_mission_diplomacy, "trp_player"),
        (str_store_party_name, s11, ":party_no"),
        ], "{!}{s11}.", "dplmc_constable_patrol_disband_confirm_ask", [
        (store_repeat_object, "$diplomacy_var"),
    ]],

    [anyone | plyr, "dplmc_constable_patrol_disband", [], "None.", "dplmc_constable_pretalk", []],

    [anyone, "dplmc_constable_patrol_disband_confirm_ask", [
        (str_store_party_name, s5, "$diplomacy_var"),
        ], "As you wish, I will send a messenger who will tell {s5} to disband.",
     "dplmc_constable_patrol_disband_confirm", []
    ],

    [anyone | plyr, "dplmc_constable_patrol_disband_confirm", [],
     "Thank you.", "dplmc_constable_security_ask", [
        (call_script, "script_dplmc_send_messenger_to_party", "$diplomacy_var", spai_undefined, -1),
    ]],

    [anyone | plyr, "dplmc_constable_patrol_disband_confirm", [],
     "No.", "dplmc_constable_security_ask", []
    ],
]
