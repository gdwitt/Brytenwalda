from source.header_operations import *
from source.header_common import *

from source.header_dialogs import *
from source.module_constants import *


dialog_option = \
    [anyone | plyr, "minister_talk", [
        (faction_get_slot, ":current_marshal", "$players_kingdom", "slot_faction_marshall"),
        (try_begin),
            # existing marshal
            (ge, ":current_marshal", 0),
            (try_begin),
                (gt, ":current_marshal", 0),
                (str_store_troop_name, s4, ":current_marshal"),
            (else_try),
                (str_store_string, s4, "str_myself"),
            (try_end),
            (str_store_string, s4, "@I wish to replace {s4} as marshal."),
        (else_try),
            # no existing marshal
            (str_store_string, s4, "@I wish to appoint a new marshal."),
        (try_end),
        ], "{s4}", "minister_change_marshal", []
    ]

dialogs = [

    [anyone, "minister_change_marshal", [
        (store_current_hours, ":hours"),
        (val_sub, ":hours", "$g_player_faction_last_marshal_appointment"),
        (faction_get_slot, ":centralization", "fac_player_supporters_faction", "slot_faction_centralization"),
        (val_clamp, ":centralization", -3, 4),
        (store_mul, ":reset_time", ":centralization", 8),
        (val_add, ":reset_time", 48),
        (lt, ":hours", ":reset_time"),
        ], "You have just made such an appointment, {sire/my lady}. If you countermand your decree so soon, "
           "there will be great confusion. We will need to wait a few days.", "minister_pretalk", []
    ],

    [anyone, "minister_change_marshal", [],
     "Who should be the new marshal?", "minister_change_marshal_choose", []
    ],

    [anyone | plyr, "minister_change_marshal_choose", [],
     "I will be marshall for now", "minister_pretalk", [
        (call_script, "script_appoint_faction_marshall", "fac_player_supporters_faction", "trp_player"),
        (store_current_hours, ":hours"),
        (assign, "$g_recalculate_ais", 1),
        (assign, "$g_player_faction_last_marshal_appointment", ":hours"),

        (try_begin),
            (faction_slot_eq, "fac_player_supporters_faction", "slot_faction_political_issue", 1),

            (faction_set_slot, "fac_player_supporters_faction", "slot_faction_political_issue", 0),
            (troop_set_slot, "trp_player", "slot_troop_stance_on_faction_issue", -1),
            (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
                (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
                (eq, ":active_npc_faction", "fac_player_supporters_faction"),
                (troop_set_slot, ":active_npc", "slot_troop_stance_on_faction_issue", -1),
            (try_end),
        (try_end),
    ]],

    [anyone | plyr, "minister_change_marshal_choose", [],
     "For a short while, we should have no marshal", "minister_pretalk", [
        (call_script, "script_appoint_faction_marshall", "fac_player_supporters_faction", -1),
        (try_begin),
            (faction_slot_eq, "fac_player_supporters_faction", "slot_faction_political_issue", 1),
            (faction_set_slot, "fac_player_supporters_faction", "slot_faction_political_issue", 0),

            (troop_set_slot, "trp_player", "slot_troop_stance_on_faction_issue", -1),
            (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
                (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
                (eq, ":active_npc_faction", "fac_player_supporters_faction"),
                (troop_set_slot, ":active_npc", "slot_troop_stance_on_faction_issue", -1),
            (try_end),
        (try_end),
        (assign, "$g_recalculate_ais", 1),
    ]],

    [anyone | plyr | repeat_for_troops, "minister_change_marshal_choose", [
        (store_repeat_object, ":lord"),
        (is_between, ":lord", active_npcs_begin, active_npcs_end),
        (troop_slot_eq, ":lord", "slot_troop_occupation", slto_kingdom_hero),
        (store_faction_of_troop, ":lord_faction", ":lord"),
        (eq, ":lord_faction", "fac_player_supporters_faction"),
        (str_store_troop_name, s4, ":lord"),
        ], "{s4}", "minister_pretalk", [

        (store_repeat_object, ":lord"),
        (call_script, "script_appoint_faction_marshall", "fac_player_supporters_faction", ":lord"),
        (store_current_hours, ":hours"),
        (assign, "$g_player_faction_last_marshal_appointment", ":hours"),
        (try_begin),
            (faction_slot_eq, "fac_player_supporters_faction", "slot_faction_political_issue", 1),

            (faction_set_slot, "fac_player_supporters_faction", "slot_faction_political_issue", 0),

            (troop_set_slot, "trp_player", "slot_troop_stance_on_faction_issue", -1),
            (try_for_range, ":active_npc", active_npcs_begin, active_npcs_end),
                (store_faction_of_troop, ":active_npc_faction", ":active_npc"),
                (eq, ":active_npc_faction", "fac_player_supporters_faction"),
                (troop_set_slot, ":active_npc", "slot_troop_stance_on_faction_issue", -1),
            (try_end),
        (try_end),
        (assign, "$g_recalculate_ais", 1),
    ]],

    [anyone | plyr, "minister_change_marshal_choose", [], "Never mind", "minister_pretalk", []],
]
