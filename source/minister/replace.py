from source.header_operations import *
from source.header_common import *
from source.header_dialogs import *
from source.module_constants import *

dialogs = [
    [anyone, "minister_replace", [],
     "Very good. Whom will you appoint in my stead?", "minister_replace_select", []
    ],

    [anyone | plyr | repeat_for_troops, "minister_replace_select", [
        (store_repeat_object, ":troop_no"),
        (is_between, ":troop_no", companions_begin, companions_end),
        (main_party_has_troop, ":troop_no"),
        (troop_slot_eq, ":troop_no", "slot_troop_prisoner_of_party", -1),
        (str_store_troop_name, s4, ":troop_no"),
        ], "{s4}", "minister_replace_confirm", [
        (store_repeat_object, "$g_player_minister"),
    ]],

    [anyone | plyr, "minister_replace_select", [
        (troop_get_slot, ":spouse", "trp_player", "slot_troop_spouse"),
        (gt, ":spouse", 0),
        (troop_get_type, ":is_female", ":spouse"),
        (neg | troop_slot_eq, ":spouse", "slot_troop_occupation", slto_kingdom_hero),

        (this_or_next | eq, ":is_female", 1),  # Skip if it is not female
        (this_or_next | eq, ":is_female", 3),  # Skip if it is not female
        (this_or_next | eq, ":is_female", 5),  # Skip if it is not female
        (eq, ":is_female", 7),  # Skip if it is not female
        (str_store_troop_name, s4, ":spouse"),
        (neq, ":spouse", "$g_talk_troop"),

        # husband disabled as he is an active lord
        ], "My wife, {s4}.", "minister_replace_confirm", [
        (troop_get_slot, "$g_player_minister", "trp_player", "slot_troop_spouse"),
    ]],

    [anyone | plyr, "minister_replace_select", [
        (str_store_string, s4, "@A prominent citizen from the area"),
        ], "{s4}", "minister_replace_confirm", [
        (assign, "$g_player_minister", "trp_temporary_minister"),
        (troop_set_faction, "trp_temporary_minister", "fac_player_supporters_faction"),
    ]],

    [anyone | plyr, "minister_replace_select", [], "Actually, hold on with that.", "minister_pretalk", []],

    # if old minister is a companion, add it to the party
    [anyone, "minister_replace_confirm", [
        (troop_slot_eq, "$g_talk_troop", "slot_troop_occupation", slto_player_companion),
        ], "Very good. {s9} is your new minister. I shall prepare to rejoin you.", "close_window", [
        (str_store_troop_name, s9, "$g_player_minister"),

        (party_add_members, "p_main_party", "$g_talk_troop", 1),

        # remove from party
        (try_begin),
            (main_party_has_troop, "$g_player_minister"),
            (party_remove_members, "p_main_party", "$g_player_minister", 1),
        (try_end),

        # abort all quests on which the troop was being given? todo: confirm what this does.
        (try_for_range, ":minister_quest", all_quests_begin, all_quests_end),
            (quest_slot_eq, ":minister_quest", slot_quest_giver_troop, "$g_talk_troop"),
            (call_script, "script_abort_quest", ":minister_quest", 0),
        (try_end),
    ]],

    # general case
    [anyone, "minister_replace_confirm", [],
     "Very good. {s9} is your new minister. It has been an honor to serve you.", "close_window", [
         (str_store_troop_name, s9, "$g_player_minister"),

         (try_begin),
            (main_party_has_troop, "$g_player_minister"),
            (party_remove_members, "p_main_party", "$g_player_minister", 1),
         (try_end),
    ]],
]
