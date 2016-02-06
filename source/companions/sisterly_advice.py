from source.header_operations import *
from source.header_common import s5

from source.header_dialogs import anyone, plyr

from source.module_constants import companions_begin, companions_end

from source.statement import StatementBlock


trigger_dialog_block = StatementBlock(
    (eq, "$disable_sisterly_advice", 0),
    (eq, "$g_infinite_camping", 0),
    (gt, "$npc_with_sisterly_advice", 0),
    (try_begin),
        (main_party_has_troop, "$npc_with_sisterly_advice"),
        (neq, "$g_player_is_captive", 1),

        (assign, "$npc_map_talk_context", "slot_troop_woman_to_woman_string"),

        (start_map_conversation, "$npc_with_sisterly_advice", -1),
    (else_try),
        (assign, "$npc_with_sisterly_advice", 0),
    (try_end),
)


dialogs = [
    [anyone, "event_triggered", [
        (eq, "$npc_map_talk_context", "slot_troop_woman_to_woman_string"),
        (store_conversation_troop, "$map_talk_troop"),
        (is_between, "$map_talk_troop", companions_begin, companions_end),

        (store_sub, ":npc_no", "$map_talk_troop", "trp_npc1"),
        (store_add, ":speech", "str_npc1_woman_to_woman", ":npc_no"),
        (str_store_string, s5, ":speech"),
    ],
     "{s5}", "companion_sisterly_advice", [
         (troop_set_slot, "$map_talk_troop", "slot_troop_woman_to_woman_string", -1),
         (assign, "$npc_with_sisterly_advice", 0),
     ]],

    [anyone | plyr, "companion_sisterly_advice", [],
     "Thank you.", "close_window", []
     ],

    [anyone | plyr, "companion_sisterly_advice", [],
     "I would prefer not to discuss such things.", "close_window", [
         (assign, "$disable_sisterly_advice", 1),
     ]],
]
