from source.statement import StatementBlock
from ..header_common import s21
from source.header_dialogs import anyone, plyr
from ..header_operations import *
from ..module_constants import *


trigger_event_block = StatementBlock(
    # it is on a mission
    (troop_slot_ge, ":npc", slot_troop_current_mission, 1),

    # the hero is not in a rejoin mission or it can join the party
    (this_or_next|neg|troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_rejoin_when_possible),
    (hero_can_join, "p_main_party"),

    (assign, "$npc_to_rejoin_party", ":npc"),
)


trigger_dialog_block = StatementBlock(
    (gt, "$npc_to_rejoin_party", 0),
    (eq, "$g_infinite_camping", 0),
    (try_begin),
        (neg|main_party_has_troop, "$npc_to_rejoin_party"),
        (neq, "$g_player_is_captive", 1),

        (assign, "$npc_map_talk_context", slot_troop_days_on_mission),
        (start_map_conversation, "$npc_to_rejoin_party", -1),
    (else_try),
        # if it is not able to join, enter rejoin mission.
        (troop_set_slot, "$npc_to_rejoin_party", slot_troop_current_mission, npc_mission_rejoin_when_possible),
        (assign, "$npc_to_rejoin_party", 0),
    (try_end),
)


dialogs = [
    [anyone, "event_triggered", [
        (store_conversation_troop, "$map_talk_troop"),
        (is_between, "$map_talk_troop", companions_begin, companions_end),

        (eq, "$map_talk_troop", "$npc_to_rejoin_party"),
        (neg | main_party_has_troop, "$map_talk_troop"),

        (troop_slot_eq, "$map_talk_troop", slot_troop_current_mission, npc_mission_rejoin_when_possible),
        (troop_slot_eq, "$map_talk_troop", slot_troop_occupation, slto_player_companion),
        (troop_get_slot, ":string", "$map_talk_troop", slot_troop_honorific),
        (str_store_string, s21, ":string"),
        ], "Greetings, {s21}. Are you ready for me to rejoin you?",
     "companion_rejoin_response",
     [(assign, "$npc_to_rejoin_party", 0)]
     ],

    [anyone | plyr, "companion_rejoin_response", [
        (hero_can_join, "p_main_party"),
        (neg | main_party_has_troop, "$map_talk_troop"),
    ], "Welcome back, friend!", "close_window", [
         (party_add_members, "p_main_party", "$map_talk_troop", 1),
         (assign, "$npc_to_rejoin_party", 0),
         (troop_set_slot, "$map_talk_troop", slot_troop_current_mission, 0),
         (troop_set_slot, "$map_talk_troop", slot_troop_days_on_mission, 0),
     ]],

    [anyone | plyr, "companion_rejoin_response", [],
     "Unfortunately, I cannot take you back just yet.",
     "companion_rejoin_refused", [
         (troop_set_slot, "$map_talk_troop", slot_troop_current_mission, npc_mission_rejoin_when_possible),
         (troop_set_slot, "$map_talk_troop", slot_troop_days_on_mission, 0),
         (assign, "$npc_to_rejoin_party", 0),
     ]],

    [anyone, "companion_rejoin_refused", [],
     "As you wish. I will take care of some business, and try again in a few days.",
     "close_window", []
     ],
]
