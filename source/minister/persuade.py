from source.header_operations import *
from source.header_common import *

from source.header_dialogs import *
from source.module_constants import *


dialog_option = \
    [anyone | plyr, "minister_talk", [
        (is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),
        (faction_get_slot, ":faction_leader", "fac_player_supporters_faction", slot_faction_leader),
        (eq, ":faction_leader", "trp_player"),
        ], "I want to persuade a lord of joining our kingdom.", "dplmc_minister_persuasion_fief_ask", []
    ]

dialogs = [
    [anyone, "dplmc_minister_persuasion_fief_ask", [
        (assign, ":companion_found", 0),
        (try_for_range, ":emissary", companions_begin, companions_end),
        (main_party_has_troop, ":emissary"),
        (assign, ":companion_found", 1),
        (try_end),
        (eq, ":companion_found", 1),
        ], "Your emissary can't go with empty hands. We have to offer a fief. Which one would you like to offer?",
        "dplmc_minister_persuasion_fief", []
    ],

    [anyone, "dplmc_minister_persuasion_fief_ask", [],
     "Unfortunately, there is no one to send right now.", "minister_pretalk", []
    ],

    [anyone | plyr | repeat_for_parties, "dplmc_minister_persuasion_fief", [
        (store_repeat_object, ":center"),
        (is_between, ":center", centers_begin, centers_end),
        (neq, ":center", "$g_player_court"),
        (store_faction_of_party, ":center_faction", ":center"),
        (eq, ":center_faction", "fac_player_supporters_faction"),
        (neg | party_slot_ge, ":center", slot_town_lord, active_npcs_begin),  # ie, owned by player or unassigned
        (str_store_party_name, s11, ":center"),
        ], "{s11}", "dplmc_minister_persuade_lord_faction_ask", [
        (store_repeat_object, "$diplomacy_var2"),
    ]],

    [anyone | plyr, "dplmc_minister_persuasion_fief", [], "Never mind -- there is no fief I can offer.",
     "minister_pretalk", []
    ],

    [anyone, "dplmc_minister_persuade_lord_faction_ask", [],
     "Where does the lord, whom you want to persuade, live?", "dplmc_minister_persuade_lord_faction", []
    ],

    [anyone | plyr | repeat_for_factions, "dplmc_minister_persuade_lord_faction", [
        (store_repeat_object, ":faction_no"),
        (is_between, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
        (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
        (str_store_faction_name, s11, ":faction_no"),
        ], "{s11}", "dplmc_minister_persuade_lord_ask", [
        (store_repeat_object, "$g_faction_selected"),
    ]],

    [anyone | plyr, "dplmc_minister_persuade_lord_faction", [], "Nowhere.", "minister_pretalk", []],

    [anyone, "dplmc_minister_persuade_lord_ask", [], "Who shall be persuaded?", "dplmc_minister_persuade_lord", []],

    [anyone | plyr | repeat_for_troops, "dplmc_minister_persuade_lord", [
        (store_repeat_object, ":troop_no"),
        (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_kingdom_hero),
        (store_faction_of_troop, ":faction", ":troop_no"),
        (is_between, ":faction", npc_kingdoms_begin, npc_kingdoms_end),
        (faction_get_slot, ":faction_leader", ":faction", slot_faction_leader),
        (neq, ":faction_leader", ":troop_no"),

        (eq, ":faction", "$g_faction_selected"),
        (troop_slot_eq, ":troop_no", slot_troop_met, 1),

        # target still wants to talk
        (neg | troop_slot_ge, ":troop_no", slot_troop_intrigue_impatience, 100),
        (str_store_troop_name, s11, ":troop_no"),
        ], "{s11}", "dplmc_minister_persuasion_emissary", [
        (store_repeat_object, "$diplomacy_var"),
        (assign, "$g_initiative_selected", dplmc_npc_mission_persuasion),
    ]],

    [anyone | plyr, "dplmc_minister_persuade_lord", [], "I can't think of anyone.", "minister_pretalk", []],

    [anyone, "dplmc_minister_persuasion_emissary", [],
     "Who shall I send? You should choose the one with the highest persuasion skill!", "minister_emissary_select", []
    ],

    # dispatch emissary to persuade
    [anyone, "minister_emissary_dispatch", [
        (str_store_troop_name, s11, "$g_emissary_selected"),
        (str_store_faction_name, s12, "$g_faction_selected"),
        (eq, "$g_initiative_selected", dplmc_npc_mission_persuasion),
        (str_store_troop_name, s13, "$diplomacy_var"),
        (str_store_party_name, s14, "$diplomacy_var2"),
        ], "Very well -- I shall send {s11} to {s12} to persuade {s13} and offer him {s14}.",
     "minister_diplomatic_dispatch_confirm", []
    ],
]
