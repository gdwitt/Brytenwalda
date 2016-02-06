from source.header_operations import *
from source.header_common import *

from source.header_dialogs import *

from source.module_constants import walled_centers_begin, walled_centers_end, \
    slot_troop_occupation, slto_kingdom_hero, spt_town, \
    slot_troop_prisoner_of_party, spt_castle, spt_patrol, \
    slot_troop_leaded_party, spt_kingdom_hero_party


kingdom_option = \
    [anyone | plyr, "dplmc_constable_reports", [
        (eq, "$players_kingdom", "fac_player_supporters_faction"),
        ], "Give me a report about the kingdom's forces.", "dplmc_constable_kingdom_overview", []
    ]

dialogs = [
    [anyone, "dplmc_constable_kingdom_overview", [
        (assign, ":garrison_size", 0),
        (assign, ":field_size", 0),
        (assign, ":castle_count", 0),
        (assign, ":town_count", 0),

        (try_for_parties, ":selected_party"),
            (try_begin),
                (this_or_next|party_slot_eq, ":selected_party", "slot_party_type", spt_town),
                (party_slot_eq, ":selected_party", "slot_party_type", spt_castle),
                (store_faction_of_party, ":party_faction", ":selected_party"),
                (eq, ":party_faction", "fac_player_supporters_faction"),

                (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
                (try_for_range, ":i_stack", 0, ":num_stacks"),
                    (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
                    (val_add, ":garrison_size", ":stack_size"),
                (try_end),

                (try_begin),
                    (party_slot_eq, ":selected_party", "slot_party_type", spt_castle),
                    (val_add, ":castle_count", 1),
                (else_try),
                    (val_add, ":town_count", 1),
                (try_end),
            (else_try),
                (party_slot_eq, ":selected_party", "slot_party_type", spt_kingdom_hero_party),
                (store_faction_of_party, ":party_faction", ":selected_party"),
                (eq, ":party_faction", "fac_player_supporters_faction"),
                (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
                (try_for_range, ":i_stack", 0, ":num_stacks"),
                    (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
                    (val_add, ":field_size", ":stack_size"),
                (try_end),
            (else_try),
                (eq, ":selected_party", "p_main_party"),
                (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
                (try_for_range, ":i_stack", 0, ":num_stacks"),
                    (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
                    (val_add, ":field_size", ":stack_size"),
                (try_end),
            (try_end),
        (try_end),

        (assign, reg2, ":garrison_size"),
        (str_store_string, s6, "@Our kingdom currently has {reg2} soldiers"),
        (assign, reg2, ":town_count"),
        (str_store_string, s6, "@{s6} garrisoned in {reg2} towns"),
        (assign, reg2, ":castle_count"),
        (str_store_string, s6, "@{s6} and {reg2} castles."),
        (try_begin),
            (gt, ":field_size", 0),
            (assign, reg2, ":field_size"),
            (str_store_string, s6, "@{s6} In addition we have {reg2} soldiers in the field."),
        (try_end),
        ], "{!}{s6}", "dplmc_constable_reports_ask", []
    ],
]

army_option = \
    [anyone | plyr, "dplmc_constable_reports", [],
     "Give me a report about my army.", "dplmc_constable_overview", []
    ]

dialogs += [

    [anyone, "dplmc_constable_overview", [
        (assign, ":garrison_size", 0),
        (assign, ":field_size", 0),
        (assign, ":patrol_size", 0),
        (assign, ":castle_count", 0),
        (assign, ":town_count", 0),
        (try_for_parties, ":selected_party"),

            (try_begin),
                (this_or_next|party_slot_eq, ":selected_party", "slot_party_type", spt_town),
                (party_slot_eq, ":selected_party", "slot_party_type", spt_castle),
                (party_slot_eq, ":selected_party", "slot_town_lord", "trp_player"),

                (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
                (try_for_range, ":i_stack", 0, ":num_stacks"),
                    (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
                    (val_add, ":garrison_size", ":stack_size"),
                (try_end),

                (try_begin),
                    (party_slot_eq, ":selected_party", "slot_party_type", spt_castle),
                    (val_add, ":castle_count", 1),
                (else_try),
                    (val_add, ":town_count", 1),
                (try_end),
            (else_try),
                (eq, ":selected_party", "p_main_party"),
                (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
                (try_for_range, ":i_stack", 0, ":num_stacks"),
                    (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
                    (val_add, ":field_size", ":stack_size"),
                (try_end),
            (else_try),
                (party_slot_eq, ":selected_party", "slot_party_type", spt_patrol),
                (party_slot_eq, ":selected_party", "slot_party_mission_diplomacy", "trp_player"),
                (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),
                (try_for_range, ":i_stack", 0, ":num_stacks"),
                    (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
                    (val_add, ":patrol_size", ":stack_size"),
                (try_end),
            (try_end),
        (try_end),

        (assign, reg2, ":garrison_size"),
        (str_store_string, s6, "@We currently have {reg2} soldiers"),
        (assign, reg2, ":town_count"),
        (str_store_string, s6, "@{s6} garrisoned in {reg2} towns"),
        (assign, reg2, ":castle_count"),
        (str_store_string, s6, "@{s6} and {reg2} castles."),
        (try_begin),
            (gt, ":field_size", 0),
            (assign, reg2, ":field_size"),
            (assign, reg3, ":patrol_size"),
            (str_store_string, s6, "@{s6} In addition you have {reg2} soldiers in "
                                   "your convoy and {reg3} soldiers in patrols."),
        (try_end),
        ], "{!}{s6}", "dplmc_constable_reports_ask", []
    ],
]

lord_convoy_option = \
    [anyone | plyr, "dplmc_constable_reports", [],
     "Give me a status report about the convoy of a lord.", "dplmc_constable_lord", []
    ]

dialogs += [

    [anyone, "dplmc_constable_lord", [],
     "About which lord do you like to be informed?", "dplmc_constable_status_lord_select", []
    ],

    [anyone | plyr | repeat_for_troops, "dplmc_constable_status_lord_select", [
        (store_repeat_object, ":troop_no"),
        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (neq, "trp_player", ":troop_no"),
        (troop_slot_ge, ":troop_no", slot_troop_leaded_party, 0),
        (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
        (store_troop_faction, ":faction_no", ":troop_no"),
        (eq, ":faction_no", "fac_player_supporters_faction"),
        (str_store_troop_name, s11, ":troop_no"),
        ], "{!}{s11}.", "dplmc_constable_status_lord_info", [

        (store_repeat_object, "$diplomacy_var"),
    ]],

    [anyone | plyr, "dplmc_constable_status_lord_select", [],
     "Never mind.", "dplmc_constable_reports_ask", []
    ],

    [anyone, "dplmc_constable_status_lord_info", [
        (assign, ":selected_troop", "$diplomacy_var"),
        (str_store_troop_name, s60, ":selected_troop"),

        (call_script, "script_update_troop_location_notes", ":selected_troop", 1),
        (call_script, "script_get_information_about_troops_position", ":selected_troop", 0),

        (assign, ":party_size", 0),
        (troop_get_slot, ":selected_party", ":selected_troop", slot_troop_leaded_party),
        (str_store_string, s52, "str_empty_string"),
        (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),

        (le, ":num_stacks", 20),

        (try_for_range, ":i_stack", 1, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", ":selected_party", ":i_stack"),
            (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
            (val_add, ":party_size", ":stack_size"),
            (assign, reg2, ":stack_size"),
            (str_store_troop_name, s53, ":stack_troop"),
            (str_store_string, s52, "@{!}{s52} {reg2} {s53}."),
        (try_end),

        (assign, reg2, ":party_size"),
        (str_store_string, s51, "@He fields {reg2} soldiers."),
        ], "{!}{s1} {s51} {s52}", "dplmc_constable_lord", []
    ],

    [anyone, "dplmc_constable_status_lord_info", [

        (assign, ":selected_troop", "$diplomacy_var"),
        (str_store_troop_name, s60, ":selected_troop"),

        (call_script, "script_update_troop_location_notes", ":selected_troop", 1),
        (call_script, "script_get_information_about_troops_position", ":selected_troop", 0),

        (assign, ":party_size", 0),
        (troop_get_slot, ":selected_party", ":selected_troop", slot_troop_leaded_party),
        (str_store_string, s52, "str_empty_string"),
        (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),

        (try_for_range, ":i_stack", 1, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", ":selected_party", ":i_stack"),
            (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
            (val_add, ":party_size", ":stack_size"),
            (try_begin),
                (le, ":i_stack", 20),
                (assign, reg2, ":stack_size"),
                (str_store_troop_name, s53, ":stack_troop"),
                (str_store_string, s52, "@{!}{s52} {reg2} {s53}."),
            (try_end),
        (try_end),

        (assign, reg2, ":party_size"),
        (str_store_string, s51, "@He fields {reg2} soldiers."),
        ], "{!}{s1} {s51} {s52}", "dplmc_constable_status_lord_info_6", []
    ],

    [anyone, "dplmc_constable_status_lord_info_6", [
        (assign, ":selected_troop", "$diplomacy_var"),
        (str_store_troop_name, s60, ":selected_troop"),

        (assign, ":party_size", 0),
        (troop_get_slot, ":selected_party", ":selected_troop", slot_troop_leaded_party),
        (str_store_string, s52, "str_empty_string"),
        (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),

        (try_for_range, ":i_stack", 20, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", ":selected_party", ":i_stack"),
            (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
            (val_add, ":party_size", ":stack_size"),
            (assign, reg2, ":stack_size"),
            (str_store_troop_name, s53, ":stack_troop"),
            (str_store_string, s52, "@{!}{s52} {reg2} {s53}."),
        (try_end),
        (assign, reg2, ":party_size"),
        ], "{!}{s52}", "dplmc_constable_lord", []
    ],
]

# garrison status

garrison_option = \
    [anyone | plyr, "dplmc_constable_reports", [],
     "I require a status report about the garrison of a fief.", "dplmc_constable_status", []
    ]

dialogs += [

    [anyone, "dplmc_constable_status", [],
     "About which fief do you like to be informed?", "dplmc_constable_status_select_fief", []
    ],

    [anyone | plyr | repeat_for_parties, "dplmc_constable_status_select_fief", [
        (store_repeat_object, ":party_no"),
        (is_between, ":party_no", walled_centers_begin, walled_centers_end),
        (store_faction_of_party, ":party_faction", ":party_no"),
        (this_or_next|party_slot_eq, ":party_no", "slot_town_lord", "trp_player"),
        (eq, ":party_faction", "fac_player_supporters_faction"),
        (str_store_party_name, s60, ":party_no"),
        ], "{!}{s60}.", "dplmc_constable_status_info", [
        (store_repeat_object, "$diplomacy_var"),
    ]],

    [anyone, "dplmc_constable_status_info", [
        (assign, ":selected_party", "$diplomacy_var"),
        (str_store_party_name, s60, ":selected_party"),
        (assign, ":garrison_size", 0),
        (str_store_string, s52, "str_empty_string"),
        (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),

        (le, ":num_stacks", 20),

        (try_for_range, ":i_stack", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", ":selected_party", ":i_stack"),
            (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
            (val_add, ":garrison_size", ":stack_size"),
            (assign, reg2, ":stack_size"),
            (str_store_troop_name, s53, ":stack_troop"),
            (str_store_string, s52, "@{!}{s52} {reg2} {s53}."),
        (try_end),

        (assign, reg2, ":garrison_size"),
        (str_store_string, s51, "@We currently have {reg2} soldiers garrisoned in {s60}."),
        ], "{!}{s51} {s52}", "dplmc_constable_status", []
    ],

    [anyone, "dplmc_constable_status_info", [
        (assign, ":selected_party", "$diplomacy_var"),
        (str_store_party_name, s60, ":selected_party"),

        (assign, ":garrison_size", 0),

        (str_store_string, s52, "str_empty_string"),
        (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),

        (try_for_range, ":i_stack", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", ":selected_party", ":i_stack"),
            (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
            (val_add, ":garrison_size", ":stack_size"),
            (try_begin),
                (le, ":i_stack", 20),
                (assign, reg2, ":stack_size"),
                (str_store_troop_name, s53, ":stack_troop"),
                (str_store_string, s52, "@{!}{s52} {reg2} {s53}."),
            (try_end),
        (try_end),

        (assign, reg2, ":garrison_size"),
        (str_store_string, s51, "@We currently have {reg2} soldiers garrisoned in {s60}."),
        ], "{!}{s51} {s52}", "dplmc_constable_status_info_6", []
    ],

    [anyone, "dplmc_constable_status_info_6", [
        (assign, ":selected_party", "$diplomacy_var"),
        (str_store_party_name, s60, ":selected_party"),

        (str_store_string, s52, "str_empty_string"),
        (party_get_num_companion_stacks, ":num_stacks", ":selected_party"),

        (try_for_range, ":i_stack", 20, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", ":selected_party", ":i_stack"),
            (party_stack_get_size, ":stack_size", ":selected_party", ":i_stack"),
            (assign, reg2, ":stack_size"),
            (str_store_troop_name, s53, ":stack_troop"),
            (str_store_string, s52, "@{!}{s52} {reg2} {s53}."),
        (try_end),
        ], "{!}{s52}", "dplmc_constable_status", []
    ],

    [anyone | plyr, "dplmc_constable_status_select_fief", [], "Never mind.",
     "dplmc_constable_reports_ask", []
    ],
]
