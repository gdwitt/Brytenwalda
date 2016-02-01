from source.header_operations import *
from source.header_common import *

from source.header_dialogs import *
from source.module_constants import *


dialog_option = \
    [anyone, "minister_issues", [
        (eq, 1, 0),
        ], "{!}[Should not appear - there to prevent error related to center_captured_lord_advice]",
        "center_captured_lord_advice", []
    ]

dialogs = [

    [anyone | plyr | repeat_for_troops, "center_captured_lord_advice", [
        (store_repeat_object, ":troop_no"),
        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (neq, "$g_talk_troop", ":troop_no"),
        (neq, "trp_player", ":troop_no"),
        (store_troop_faction, ":faction_no", ":troop_no"),
        (eq, ":faction_no", "fac_player_supporters_faction"),
        (str_store_troop_name, s11, ":troop_no"),
        (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", ":troop_no"),

        (try_begin),
            (troop_slot_eq, ":troop_no", slot_lord_recruitment_argument, argument_benefit),
            (str_store_string, s12, "str__promised_fief"),
        (else_try),
            (str_clear, s12),
        (try_end),

        (try_begin),
            (eq, reg0, 0),
            (str_store_string, s1, "str_no_fiefss12"),
        (else_try),
            (str_store_string, s1, "str_fiefs_s0s12"),
        (try_end),
        ], "{s11}. {s1}", "center_captured_lord_advice_2", [
        (store_repeat_object, "$temp"),
    ]],

    [anyone | plyr, "center_captured_lord_advice", [
        (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", "trp_player"),
        (str_store_party_name, s1, "$g_center_taken_by_player_faction"),

        (try_begin),
            (is_between, "$g_talk_troop", pretenders_begin, pretenders_end),
            (str_store_string, s12, "str_please_s65_"),
        (else_try),
            (str_clear, s12),
        (try_end),
        ], "{s12}I want to have {s1} for myself. (fiefs: {s0})", "center_captured_lord_advice_2", [
        (assign, "$temp", "trp_player"),
    ]],

    [anyone | plyr, "center_captured_lord_advice", [
        (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", "$g_talk_troop"),
        (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
        (is_between, "$g_talk_troop", pretenders_begin, pretenders_end),
        ], "{s66}, you should have {s1} for yourself. (fiefs: {s0})", "center_captured_lord_advice_2", [
        (assign, "$temp", "$g_talk_troop"),
    ]],

    # grant fief via minister
    [anyone, "center_captured_lord_advice_2", [
        (eq, "$g_talk_troop", "$g_player_minister"),
        ], "As you wish, {sire/my lady}. {reg6?I:{reg7?You:{s11}}} will be the new {reg3?lady:lord} of {s1}.",
        "minister_issues", [
        (assign, ":new_owner", "$temp"),

        (call_script, "script_give_center_to_lord", "$g_center_taken_by_player_faction", ":new_owner", 0),

        (try_begin),
            (faction_slot_eq, "$players_kingdom", slot_faction_political_issue, "$g_center_taken_by_player_faction"),
            (faction_set_slot, "$players_kingdom", slot_faction_political_issue, -1),
        (try_end),

        # give some troops
        (try_begin),
            (neq, ":new_owner", "trp_player"),
            (try_for_range, ":unused", 0, 4),
                (call_script, "script_cf_reinforce_party", "$g_center_taken_by_player_faction"),
            (try_end),
        (try_end),

        (assign, reg6, 0),
        (assign, reg7, 0),
        (try_begin),
            (eq, ":new_owner", "$g_talk_troop"),
            (assign, reg6, 1),
        (else_try),
            (eq, ":new_owner", "trp_player"),
            (assign, reg7, 1),
        (else_try),
            (str_store_troop_name, s11, ":new_owner"),
        (try_end),
        (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
        (troop_get_type, reg3, ":new_owner"),
        (val_mod, reg3, 2),
        (assign, "$g_center_taken_by_player_faction", -1),
    ]],

    # grant fief lord
    # todo: very similar to previous dialog. Make it equal but with a different string.
    [anyone, "center_captured_lord_advice_2", [],
     "Hmmm. All right, {playername}. I value your counsel highly. {reg6?I:{reg7?You:{s11}}} "
     "will be the new {reg3?lady:lord} of {s1}.", "close_window", [
        (assign, ":new_owner", "$temp"),

        (troop_set_slot, ":new_owner", slot_lord_recruitment_argument, 0),

        (call_script, "script_give_center_to_lord", "$g_center_taken_by_player_faction", ":new_owner", 0),
        (try_begin),
            (faction_slot_eq, "$players_kingdom", slot_faction_political_issue, "$g_center_taken_by_player_faction"),
            (faction_set_slot, "$players_kingdom", slot_faction_political_issue, -1),
        (try_end),

        # give some troops
        (try_begin),
            (neq, ":new_owner", "trp_player"),
            (try_for_range, ":unused", 0, 4),
                (call_script, "script_cf_reinforce_party", "$g_center_taken_by_player_faction"),
            (try_end),
        (try_end),

        (assign, reg6, 0),
        (assign, reg7, 0),
        (try_begin),
            (eq, ":new_owner", "$g_talk_troop"),
            (assign, reg6, 1),
        (else_try),
            (eq, ":new_owner", "trp_player"),
            (assign, reg7, 1),
        (else_try),
            (str_store_troop_name, s11, ":new_owner"),
        (try_end),

        (str_store_party_name, s1, "$g_center_taken_by_player_faction"),
        (troop_get_type, reg3, "$temp"),
        (val_mod, reg3, 2),
        (assign, "$g_center_taken_by_player_faction", -1),
    ]],
]
