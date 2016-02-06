from source.header_operations import *
from source.header_common import s3, s4, s21

from source.header_dialogs import anyone, plyr

from source.module_constants import npc_mission_kingsupport, \
    companions_begin, companions_end

from source.statement import StatementBlock


trigger_event_block = StatementBlock(
    # updates objection state
    (try_begin),
        (troop_slot_ge, ":npc", "slot_troop_days_on_mission", 5),
        (troop_slot_eq, ":npc", "slot_troop_current_mission", npc_mission_kingsupport),

        (troop_get_slot, ":other_npc", ":npc", "slot_troop_kingsupport_opponent"),

        (troop_slot_eq, ":other_npc", "slot_troop_kingsupport_objection_state", 0),
        (troop_set_slot, ":other_npc", "slot_troop_kingsupport_objection_state", 1),

        (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_troop_name, s3, ":npc"),
            (str_store_troop_name, s4, ":other_npc"),
            (display_message, "str_s4_ready_to_voice_objection_to_s3s_mission_if_in_party"),
        (try_end),
    (try_end),

    (try_begin),
        (main_party_has_troop, ":npc"),
        (try_begin),
            (eq, "$npc_with_political_grievance", 0),

            (troop_slot_eq, ":npc", "slot_troop_kingsupport_objection_state", 1),
            (assign, "$npc_with_political_grievance", ":npc"),
        (try_end),
    (try_end),
)


trigger_dialog_block = StatementBlock(
    (gt, "$npc_with_political_grievance", 0),
    (eq, "$g_infinite_camping", 0),
    (eq, "$disable_npc_kingsupport", 0),
    (try_begin),
        (main_party_has_troop, "$npc_with_political_grievance"),
        (neq, "$g_player_is_captive", 1),

        (assign, "$npc_map_talk_context", "slot_troop_kingsupport_objection_state"),

        (start_map_conversation, "$npc_with_political_grievance", -1),
    (else_try),
        (assign, "$npc_with_political_grievance", 0),
    (try_end),
)

dialogs = [

    [anyone, "event_triggered", [
        (store_conversation_troop, "$map_talk_troop"),
        (is_between, "$map_talk_troop", companions_begin, companions_end),

        (eq, "$map_talk_troop", "$npc_with_political_grievance"),
        (eq, "$npc_map_talk_context", "slot_troop_kingsupport_objection_state"),

        (store_sub, ":npc_no", "$g_talk_troop", "trp_npc1"),
        (store_add, ":string", "str_npc1_kingsupport_objection", ":npc_no"),
        (str_store_string, s21, ":string"),
    ],
     "{s21}", "companion_political_grievance_response", [
         (assign, "$npc_with_political_grievance", 0),
         (troop_set_slot, "$map_talk_troop", "slot_troop_kingsupport_objection_state", 2),
     ]],

    [anyone | plyr, "companion_political_grievance_response", [],
     "Your opinion is noted.", "close_window", [
         (troop_get_slot, ":grievance", "$map_talk_troop", "slot_troop_morality_penalties"),
         (val_add, ":grievance", 25),
         (troop_set_slot, "$map_talk_troop", "slot_troop_morality_penalties", ":grievance"),
     ]],
]
