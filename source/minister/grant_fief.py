from source.header_operations import *
from source.header_common import *

from source.header_dialogs import *
from source.module_constants import *


dialog_option = \
    [anyone | plyr, "minister_talk", [
        (is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),
        ], "I wish you to grant one of my vassals a fief.", "minister_grant_fief", []
    ]

dialogs = [

    [anyone, "minister_grant_fief", [
        (faction_get_slot, ":fief_on_agenda", "$players_kingdom", slot_faction_political_issue),
        (str_clear, s12),
        (try_begin),
            (is_between, ":fief_on_agenda", centers_begin, centers_end),
            (str_store_party_name, s4, ":fief_on_agenda"),
            (str_store_string, s12, "str_minister_advice_select_fief"),
        (else_try),
            (eq, ":fief_on_agenda", 1),
            (str_store_string, s12, "str_minister_advice_select_fief_wait"),
        (try_end),
        ], "Which of your fiefs do you wish to grant?{s12}", "minister_grant_fief_select", []
    ],

    [anyone | plyr | repeat_for_parties, "minister_grant_fief_select", [
        (store_repeat_object, ":center_no"),
        (is_between, ":center_no", centers_begin, centers_end),
        (store_faction_of_party, ":center_faction", ":center_no"),
        (eq, ":center_faction", "fac_player_supporters_faction"),
        (neg | party_slot_eq, ":center_no", "slot_village_infested_by_bandits", "trp_peasant_woman"),
        (neq, ":center_no", "$g_player_court"),
        (party_get_slot, ":town_lord", ":center_no", "slot_town_lord"),

        (try_begin),
            (ge, ":town_lord", active_npcs_begin),
            (store_faction_of_troop, ":town_lord_faction", ":town_lord"),
            (neq, ":town_lord_faction", "fac_player_supporters_faction"),
            (assign, ":town_lord", -1),
        (try_end),
        (le, ":town_lord", 0),

        (str_store_party_name, s1, ":center_no"),
        (str_clear, s12),
        (try_begin),
            (party_slot_eq, ":center_no", "slot_town_lord", -1),
            (str_store_string, s12, "str_unassigned_center"),
        (try_end),
        ], "{s1}{s12}", "minister_grant_fief_select_recipient", [
        (store_repeat_object, "$fief_selected"),
    ]],

    [anyone | plyr, "minister_grant_fief_select", [], "Never mind", "minister_pretalk", []],

    [anyone, "minister_grant_fief_select_recipient", [
        (str_clear, s12),
        (try_begin),
            (faction_slot_eq, "$players_kingdom", slot_faction_political_issue, "$fief_selected"),

            (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
                (troop_set_slot, ":active_npc", slot_troop_temp_slot, 0),
            (try_end),

            (assign, ":popular_favorite", -1),
            (assign, ":votes_for_popular_favorite", 0),

            (try_for_range, ":active_npc", heroes_begin, heroes_end),
                (troop_set_slot, ":active_npc", slot_troop_temp_slot, 0),
            (try_end),

            (assign, ":popular_favorite", -1),
            (assign, ":votes_for_popular_favorite", 0),
            (troop_set_slot, "trp_player", slot_troop_temp_slot, 0),

            (try_for_range, ":active_npc", heroes_begin, heroes_end),
                (this_or_next | is_between, ":active_npc", active_npcs_begin, active_npcs_end),
                (troop_slot_eq, ":active_npc", slot_troop_occupation, slto_kingdom_hero),
                (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
                (eq, ":active_npc_faction", "fac_player_supporters_faction"),
                (troop_get_slot, ":selected_npc", ":active_npc", slot_troop_stance_on_faction_issue),
                (ge, ":selected_npc", 0),

                (troop_get_slot, ":votes_accumulated", ":selected_npc", slot_troop_temp_slot),
                (val_add, ":votes_accumulated", 1),
                (troop_set_slot, ":selected_npc", slot_troop_temp_slot, ":votes_accumulated"),

                (gt, ":votes_accumulated", ":votes_for_popular_favorite"),
                (assign, ":votes_for_popular_favorite", ":votes_accumulated"),
                (assign, ":popular_favorite", ":selected_npc"),
            (try_end),

            (is_between, ":popular_favorite", heroes_begin, heroes_end),
            (str_store_troop_name, s4, ":popular_favorite"),
            (assign, reg4, ":votes_for_popular_favorite"),

            (str_store_string, s12, "str_minister_advice_fief_leading_vassal"),
        (try_end),

        ], "And who will you choose to receive the fief?{s12}", "minister_grant_fief_select_recipient_choice", []
    ],

    [anyone | plyr | repeat_for_troops, "minister_grant_fief_select_recipient_choice", [
        (store_repeat_object, ":troop_no"),
        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),

        (is_between, ":troop_no", heroes_begin, heroes_end),
        (store_faction_of_troop, ":troop_faction", ":troop_no"),
        (is_between, ":troop_faction", kingdoms_begin, kingdoms_end),
        (this_or_next | eq, ":troop_faction", "$players_kingdom"),
        (eq, ":troop_faction", "fac_player_supporters_faction"),

        (str_store_troop_name, s11, ":troop_no"),
        (call_script, "script_print_troop_owned_centers_in_numbers_to_s0", ":troop_no"),

        (try_begin),
            (troop_slot_eq, "$g_talk_troop", slot_lord_recruitment_argument, argument_benefit),
            (str_store_string, s12, "str__promised_fief"),
        (else_try),
            (str_clear, s12),
        (try_end),

        (try_begin),
            (eq, reg0, 0),
            (str_store_string, s0, "str_no_fiefss12"),
        (else_try),
            (str_store_string, s0, "str_fiefs_s0s12"),
        (try_end),

        # add relation string
        (str_store_string_reg, s12, s63),  # save s63, clobbering s12 (perhaps already overwritten)
        (call_script, "script_troop_get_player_relation", ":troop_no"),
        (call_script, "script_describe_relation_to_s63", reg0),
        (str_store_string_reg, s1, s63),  # clobber s1
        (str_store_string_reg, s63, s12),  # revert s63
        (str_store_string, s1, "str_dplmc_s0_comma_s1"),  # write to s1
        ], "{!}{s11} {s1}.", "minister_grant_fief_complete", [
        (store_repeat_object, "$lord_selected"),
    ]],

    [anyone | plyr, "minister_grant_fief_select_recipient_choice", [], "Never mind", "minister_pretalk", []],

    [anyone, "minister_grant_fief_complete", [], "Very well - {s2} shall receive {s1}.", "minister_pretalk", [
        (call_script, "script_give_center_to_lord", "$fief_selected", "$lord_selected", 0),
        (str_store_party_name, s1, "$fief_selected"),
        (str_store_troop_name, s2, "$lord_selected"),

        (try_begin),
            (faction_slot_eq, "$players_kingdom", slot_faction_political_issue, "$fief_selected"),
            (faction_set_slot, "$players_kingdom", slot_faction_political_issue, -1),
        (try_end),

        (call_script, "script_add_log_entry", logent_castle_given_to_lord_by_player, "trp_player", "$fief_selected", "$lord_selected", "$g_encountered_party_faction"),
    ]],
]
