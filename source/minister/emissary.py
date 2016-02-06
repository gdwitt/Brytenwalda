from source.header_operations import *
from source.header_common import *

from source.header_dialogs import *
from source.module_constants import *


dialog_option = \
    [anyone | plyr, "minister_talk", [
        (is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),
        ], "I wish to dispatch an emissary.", "minister_diplomatic_kingdoms", []
    ]

dialogs = [
    [anyone, "minister_diplomatic_kingdoms", [
        # this condition avoids the player selecting the mission and find later that there are no emissaries available.
        (assign, ":companion_found", 0),
        (try_for_range, ":emissary", companions_begin, companions_end),
            (main_party_has_troop, ":emissary"),
            (troop_slot_eq, ":emissary", slot_troop_prisoner_of_party, -1),
            (assign, ":companion_found", 1),
        (try_end),
        (eq, ":companion_found", 1),
        ], "To whom do you wish to send this emissary?", "minister_diplomatic_kingdoms_select", []
    ],

    [anyone, "minister_diplomatic_kingdoms", [],
     "Unfortunately, there is no one eligible to be an emissary.", "minister_pretalk", []
    ],

    [anyone | plyr | repeat_for_factions, "minister_diplomatic_kingdoms_select", [
        (store_repeat_object, ":faction_no"),
        (is_between, ":faction_no", kingdoms_begin, kingdoms_end),
        (neg | faction_slot_eq, ":faction_no", "slot_faction_leader", "trp_player"),
        (neq, ":faction_no", "$players_kingdom"),
        (neq, ":faction_no", "fac_player_supporters_faction"),
        (faction_slot_eq, ":faction_no", "slot_faction_state", sfs_active),
        (faction_get_slot, ":leader_no", ":faction_no", "slot_faction_leader"),
        (str_store_troop_name, s10, ":leader_no"),
        (str_store_faction_name, s11, ":faction_no"),
        (call_script, "script_change_diplomatic_action_ruler_kingdom_strings", ":leader_no", ":faction_no"),
        # todo: clear string implies {s14} is not needed below
        (str_clear, s14),
        # Has/has not recognized us a monarch
        ], "{s10} of the {s11}{s14}", "minister_diplomatic_initiative_type", [
        (store_repeat_object, "$g_faction_selected"),
    ]],

    [anyone | plyr, "minister_diplomatic_kingdoms_select", [],
     "Never mind", "minister_pretalk", []
    ],

]

dialogs += [

    [anyone, "minister_diplomatic_initiative_type", [],
     "What do you wish to tell him?", "minister_diplomatic_initiative_type_select", []
    ],

    [anyone | plyr, "minister_diplomatic_initiative_type_select", [
        (store_relation, ":relation", "fac_player_supporters_faction", "$g_faction_selected"),
        (lt, ":relation", 0)
        ], "That our two kingdoms should enter into truce.", "minister_diplomatic_emissary", [
        (assign, "$g_initiative_selected", npc_mission_peace_request)
    ]],

    [anyone | plyr, "minister_diplomatic_initiative_type_select", [],
     "That I wish to put myself under his protection, as his vassal.", "minister_diplomatic_emissary", [
         (assign, "$g_initiative_selected", npc_mission_pledge_vassal)
    ]],

    [anyone | plyr, "minister_diplomatic_initiative_type_select", [
        (store_relation, ":relation", "fac_player_supporters_faction", "$g_faction_selected"),
        (faction_slot_eq, "$g_faction_selected", "slot_faction_recognized_player", 0),
        (ge, ":relation", 0)
        ], "That I wish to express my goodwill, as one monarch to another.", "minister_diplomatic_emissary", [
        (assign, "$g_initiative_selected", npc_mission_seek_recognition)
    ]],

    [anyone | plyr, "minister_diplomatic_initiative_type_select", [
        (store_relation, ":relation", "fac_player_supporters_faction", "$g_faction_selected"),
        (ge, ":relation", 0)
        ], "That I declare war upon him.", "minister_declare_war", []
    ],

    [anyone | plyr, "minister_diplomatic_initiative_type_select", [], "Never mind", "close_window", []],
]

# select emissary
dialogs += [

    [anyone, "minister_diplomatic_emissary", [],
     "Who shall be your emissary? You should choose one whom you trust, but who "
     "is also persuasive -- one who can negotiate without giving offense.",
     "minister_emissary_select", []
    ],

    [anyone | plyr | repeat_for_troops, "minister_emissary_select", [
        (store_repeat_object, ":emissary"),
        (main_party_has_troop, ":emissary"),
        (is_between, ":emissary", companions_begin, companions_end),
        (troop_slot_eq, ":emissary", slot_troop_prisoner_of_party, -1),
        (call_script, "script_set_diplomatic_emissary_skill_level_string", ":emissary", "skl_persuasion", 0),
        ], "{s11}", "minister_emissary_dispatch", [
        (store_repeat_object, "$g_emissary_selected"),
    ]],

    [anyone | plyr, "minister_emissary_select", [], "Actually, I can't think of anyone.", "minister_pretalk", []],
]

# dispatch emissary
dialogs += [

    [anyone, "minister_emissary_dispatch", [
        (str_store_troop_name, s11, "$g_emissary_selected"),
        (str_store_faction_name, s12, "$g_faction_selected"),

        (try_begin),
            (eq, "$g_initiative_selected", npc_mission_seek_recognition),
            (str_store_string, s14, "str_seek_recognition"),
        (else_try),
            (eq, "$g_initiative_selected", npc_mission_pledge_vassal),
            (str_store_string, s14, "str_seek_vassalhood"),
        (else_try),
            (eq, "$g_initiative_selected", npc_mission_peace_request),
            (str_store_string, s14, "str_seek_a_truce"),
        (else_try),
            (eq, "$g_initiative_selected", dplmc_npc_mission_nonaggression_request),
            (str_store_string, s14, "str_dplmc_conclude_non_agression"),
        (try_end),
        ], "Very well -- I shall send {s11} to the {s12} to {s14}.", "minister_diplomatic_dispatch_confirm", []
    ],

    [anyone | plyr, "minister_diplomatic_dispatch_confirm", [], "Yes, do that", "minister_pretalk", [
        (troop_set_slot, "$g_emissary_selected", slot_troop_days_on_mission, 3),
        (troop_set_slot, "$g_emissary_selected", slot_troop_current_mission, "$g_initiative_selected"),
        (troop_set_slot, "$g_emissary_selected", slot_troop_mission_object, "$g_faction_selected"),
        (try_begin),
            (eq, "$g_initiative_selected", dplmc_npc_mission_gift_horses_request),
            (call_script, "script_dplmc_withdraw_from_treasury", "$diplomacy_var"),
        (try_end),
        (troop_set_slot, "$g_emissary_selected", slot_troop_mission_diplomacy, "$diplomacy_var"),
        (troop_set_slot, "$g_emissary_selected", slot_troop_mission_diplomacy2, "$diplomacy_var2"),

        (remove_member_from_party, "$g_emissary_selected", "p_main_party"),
    ]],

    [anyone | plyr, "minister_diplomatic_dispatch_confirm", [], "Actually, hold off on that", "minister_pretalk", []],
]


# declare war (does not require emissary; it is immediate)
dialogs += [

    [anyone, "minister_declare_war", [
        (try_begin),
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_player_supporters_faction", "$g_faction_selected"),
            (eq, reg0, 1),
            (str_store_string, s12, "str_in_doing_so_you_will_be_in_violation_of_your_truce_is_that_what_you_want"),
        (else_try),
            (call_script, "script_diplomacy_faction_get_diplomatic_status_with_faction", "fac_player_supporters_faction", "$g_faction_selected"),
            (neq, reg0, -1),
            (str_store_string, s12, "str_if_you_attack_without_provocation_some_of_your_vassals_may_consider_you_to_be_too_warlike_is_that_what_you_want"),
        (else_try),
            (str_store_string, s12, "str_our_men_are_ready_to_ride_forth_at_your_bidding_are_you_sure_this_is_what_you_want"),
        (try_end),
        ], "{s12}", "minister_declare_war_confirm", []
    ],

    [anyone | plyr, "minister_declare_war_confirm", [
        (str_store_faction_name, s12, "$g_faction_selected"),
        ], "It is. I wish to make war on {s12}.", "minister_declare_war_confirm_yes", [
        (call_script, "script_diplomacy_start_war_between_kingdoms", "fac_player_supporters_faction", "$g_faction_selected", logent_player_faction_declares_war),
    ]],

    [anyone | plyr, "minister_declare_war_confirm", [
        (str_store_faction_name, s12, "$g_faction_selected"),
        ], "Hmm. Perhaps not.", "minister_pretalk", []
    ],

    [anyone, "minister_declare_war_confirm_yes", [
        (str_store_faction_name, s12, "$g_faction_selected"),
    ], "As you command. We are now at war with the {s12}. May the heavens grant us victory.", "minister_pretalk", []],
]
