from source.header_operations import *
from source.header_common import s5

from source.header_dialogs import anyone, plyr

from source.module_constants import companions_begin, companions_end

from source.statement import StatementBlock


trigger_dialog_block = StatementBlock(
    (eq, "$disable_local_histories", 0),
    (eq, "$g_infinite_camping", 0),
    (try_for_range, ":npc", companions_begin, companions_end),
        (main_party_has_troop, ":npc"),
        (troop_slot_eq, ":npc", "slot_troop_home_speech_delivered", 0),
        (troop_get_slot, ":home", ":npc", "slot_troop_home"),
        (gt, ":home", 0),
        (store_distance_to_party_from_party, ":distance", ":home", "p_main_party"),
        (lt, ":distance", 7),

        (assign, "$npc_map_talk_context", "slot_troop_home"),

        (start_map_conversation, ":npc", -1),
    (try_end),
)


dialogs = [
    [anyone, "event_triggered", [
        (store_conversation_troop, "$map_talk_troop"),
        (eq, "$g_infinite_camping", 0),
        (eq, "$npc_map_talk_context", "slot_troop_home"),
        (is_between, "$map_talk_troop", companions_begin, companions_end),

        (troop_get_slot, ":speech", "$map_talk_troop", "slot_troop_home_intro"),
        (str_store_string, s5, ":speech"),
     ],
     "{s5}", "companion_home_description", [
         (troop_set_slot, "$map_talk_troop", "slot_troop_home_speech_delivered", 1),
     ]],

    [anyone | plyr, "companion_home_description", [],
     "Tell me more.", "companion_home_description_2", []
     ],

    [anyone | plyr, "companion_home_description", [],
     "We don't have time to chat just now.", "close_window", []
     ],

    [anyone | plyr, "companion_home_description", [],
     "I prefer my companions not to bother me with such trivialities.",
     "close_window", [
         (assign, "$disable_local_histories", 1),
     ]],

    [anyone, "companion_home_description_2", [
        (troop_get_slot, ":speech", "$map_talk_troop", "slot_troop_home_description"),
        (str_store_string, s5, ":speech"),
        ], "{s5}", "companion_home_description_3", []
     ],

    [anyone, "companion_home_description_3", [
        (troop_get_slot, ":speech", "$map_talk_troop", "slot_troop_home_description_2"),
        (str_store_string, s5, ":speech"),
        ], "{s5}", "close_window", []
     ],
]
