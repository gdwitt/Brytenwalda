from source.header_operations import *
from source.header_common import *

from source.header_dialogs import *

from source.module_constants import walled_centers_begin, walled_centers_end, \
    slto_kingdom_hero, kings_begin, lords_end


dialog_option = \
    [anyone | plyr, "dplmc_constable_talk", [],
     "I want to release a prisoner.", "dplmc_constable_talk_ask_prisoner", []
    ]


dialogs = [

    [anyone, "dplmc_constable_talk_ask_prisoner", [],
     "Alright, which prisoner do you want to release?", "dplmc_constable_talk_prisoner_select", []
    ],

    # select prisoner
    [anyone | plyr | repeat_for_troops, "dplmc_constable_talk_prisoner_select", [
        (store_repeat_object, ":troop_no"),
        (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
        (is_between, ":troop_no", kings_begin, lords_end),
        (troop_get_slot, ":party", ":troop_no", "slot_troop_prisoner_of_party"),

        (assign, ":can_release", 0),
        (try_begin),
            (is_between, ":party", walled_centers_begin, walled_centers_end),
            (party_slot_eq, ":party", "slot_town_lord", "trp_player"),
            (assign, ":can_release", 1),
        (else_try),
            (eq, ":party", "p_main_party"),
            (assign, ":can_release", 1),
        (try_end),
        (eq, ":can_release", 1),

        (str_store_troop_name, s10, ":troop_no"),
        (store_faction_of_troop, ":faction_no", ":troop_no"),
        (str_store_faction_name_link, s11, ":faction_no"),
        ], "{s10} of {s11}.", "dplmc_constable_exchange_prisoner_ask_confirm", [
        (store_repeat_object, "$diplomacy_var"),
        (store_faction_of_troop, "$g_faction_selected", "$diplomacy_var"),
    ]],

    [anyone | plyr, "dplmc_constable_talk_prisoner_select", [],
     "No one.", "dplmc_constable_pretalk", []
    ],

    [anyone, "dplmc_constable_exchange_prisoner_ask_confirm", [
        (str_store_troop_name, s10, "$diplomacy_var"),
        (store_faction_of_troop, ":faction_no", "$diplomacy_var"),
        (str_store_faction_name_link, s11, ":faction_no")
        ], "As you wish, I will tell the prison guard to release {s10} of {s11}.",
        "dplmc_constable_exchange_prisoner_confirm", []
    ],

    [anyone | plyr, "dplmc_constable_exchange_prisoner_confirm", [],
     "Very well.", "dplmc_constable_pretalk", [
        (troop_get_slot, ":party", "$diplomacy_var", "slot_troop_prisoner_of_party"),

        (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_party_name, s7, ":party"), #debug
            (display_message, "@{!}DEBUG - prisoner of: {s7}"),
        (try_end),

        (party_remove_prisoners, ":party", "$diplomacy_var", 1),
        (try_begin),
            (main_party_has_troop, "$diplomacy_var"),
            (party_remove_prisoners, "p_main_party", "$diplomacy_var", 1),
        (try_end),
        (call_script, "script_remove_troop_from_prison", "$diplomacy_var"),
        (str_store_troop_name, s7, "$diplomacy_var"),
        (display_message, "str_dplmc_has_been_set_free"),
        # todo: these values should be equal for all release prisoner
        (call_script, "script_change_player_relation_with_troop", "$diplomacy_var", 3),
        (call_script, "script_change_player_honor", 1),
    ]],

    [anyone | plyr, "dplmc_constable_exchange_prisoner_confirm", [],
     "No, I changed my mind.", "dplmc_constable_pretalk", []],
]
