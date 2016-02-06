from source.header_operations import *
from source.header_common import *

from source.header_dialogs import *

from source.module_constants import slto_kingdom_hero, active_npcs_begin, kingdom_ladies_end


dialog_option = \
    [anyone | plyr, "minister_talk", [
        # todo: what is this condition? spouse + minister?
        (is_between, "$g_player_minister", active_npcs_begin, kingdom_ladies_end),
        ], "I wish to indict a disloyal vassal for treason.", "minister_indict", []
    ]

dialogs = [

    [anyone, "minister_indict", [],
     "Grim news, {sire/my lady}. Who do you believe is planning to betray you?", "minister_indict_select", []
    ],

    [anyone | plyr | repeat_for_troops, "minister_indict_select", [
        (store_repeat_object, ":troop_no"),
        (troop_slot_eq, ":troop_no", "slot_troop_occupation", slto_kingdom_hero),
        (store_faction_of_troop, ":faction", ":troop_no"),
        (eq, ":faction", "fac_player_supporters_faction"),
        (str_store_troop_name, s11, ":troop_no"),
        ], "{s11}", "minister_indict_confirm", [
        (store_repeat_object, "$lord_selected"),
    ]],

    [anyone | plyr, "minister_indict_select", [], "Never mind.", "minister_pretalk", []],

    [anyone, "minister_indict_confirm", [
        (str_store_troop_name, s4, "$lord_selected"),
        (troop_get_type, reg4, "$lord_selected"),
        (val_mod, reg4, 2),
        ], "Think carefully on this, {sire/my lady}. If you indict {s4} for treason unjustly, "
           "you may find others becoming nervous about serving you. On the other hand, if you "
           "truly believe that {reg4?she:he} is about to betray you, then perhaps it is best "
           "to move first, to secure control of {reg4?her:his} fortresses.",
        "minister_indict_confirm_answer", []
    ],

    [anyone | plyr, "minister_indict_confirm_answer", [],
     "I have thought long enough. Issue the indictment!", "minister_indict_conclude", []
    ],

    [anyone | plyr, "minister_indict_confirm_answer", [],
     "Perhaps I should wait a little while longer..", "minister_pretalk", []
    ],

    [anyone, "minister_indict_conclude", [], "It has been sent, {sire/my lady}.", "minister_pretalk", [
        (call_script, "script_indict_lord_for_treason", "$lord_selected", "fac_player_supporters_faction"),
    ]],
]
