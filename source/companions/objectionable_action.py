from source.header_operations import *
from source.header_common import s5, s21
from source.header_dialogs import anyone, plyr

from source.statement import StatementBlock

from ..module_constants import tms_acknowledged, slot_troop_morality_penalties, \
    tms_dismissed, tms_no_problem, companions_begin, companions_end, \
    slot_troop_morality_type, slot_troop_morality_state, slot_troop_morality_value, \
    slot_troop_2ary_morality_type, slot_troop_2ary_morality_state, slot_troop_2ary_morality_value, \
    slot_troop_morality_speech, slot_troop_2ary_morality_speech


def _affect_morality_by_action(slot, slot_state, slot_value):
    return StatementBlock(
        (troop_slot_eq, ":npc", slot, ":action_type"),
        (troop_get_slot, ":value", ":npc", slot_value),
        (try_begin),
            (troop_slot_eq, ":npc", slot_state, tms_acknowledged),
            # npc is betrayed, major penalty to player honor and morale
            (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
            (val_mul, ":value", 2),
            (val_add, ":grievance", ":value"),
            (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),
        (else_try),
            (troop_slot_eq, ":npc", slot_state, tms_dismissed),
            # npc is quietly disappointed
            (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
            (val_add, ":grievance", ":value"),
            (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),
        (else_try),
            # npc raises the issue for the first time
            (troop_slot_eq, ":npc", slot_state, tms_no_problem),
            (gt, ":value", ":grievance_minimum"),
            (assign, "$npc_with_grievance", ":npc"),
            (assign, "$npc_grievance_string", ":action_string"),
            (assign, "$npc_grievance_slot", slot_state),
            (assign, ":grievance_minimum", ":value"),
            (assign, "$npc_praise_not_complaint", 0),
            (try_begin),
                (lt, ":value", 0),
                (assign, "$npc_praise_not_complaint", 1),
            (try_end),
        (try_end),
    )


scripts = [
    # Updates grievance of companions by actions that it does not like.
    ("objectionable_action", [
        (store_script_param_1, ":action_type"),
        (store_script_param_2, ":action_string"),

        (assign, ":grievance_minimum", -2),
        (try_for_range, ":npc", companions_begin, companions_end),
            (main_party_has_troop, ":npc"),

            # Primary morality check
            (try_begin),
                _affect_morality_by_action(slot_troop_morality_type,
                                           slot_troop_morality_state,
                                           slot_troop_morality_value),

            # Secondary morality check
            (else_try),
                _affect_morality_by_action(slot_troop_2ary_morality_type,
                                           slot_troop_2ary_morality_state,
                                           slot_troop_2ary_morality_value),
            (try_end),

            (try_begin),
                (gt, "$npc_with_grievance", 0),
                (eq, "$npc_praise_not_complaint", 0),
                (str_store_troop_name, 4, "$npc_with_grievance"),
                (display_message, "@{s4} looks upset."),
            (try_end),
        (try_end),
     ]),
]

dialogs = [
    [anyone, "event_triggered", [
        (store_conversation_troop, "$map_talk_troop"),
        (is_between, "$map_talk_troop", companions_begin, companions_end),

        (eq, "$map_talk_troop", "$npc_with_grievance"),
        (eq, "$npc_map_talk_context", slot_troop_morality_state),

        (try_begin),
            (eq, "$npc_grievance_slot", slot_troop_morality_state),
            (troop_get_slot, ":speech", "$map_talk_troop", slot_troop_morality_speech),
        (else_try),
            (troop_get_slot, ":speech", "$map_talk_troop", slot_troop_2ary_morality_speech),
        (try_end),

        (str_store_string, s21, "$npc_grievance_string"),
        (str_store_string, s5, ":speech"),
    ],
     "{s5}", "companion_objection_response", [
         (assign, "$npc_with_grievance", 0),
     ]],

    [anyone | plyr, "companion_objection_response", [
        (eq, "$npc_praise_not_complaint", 1),
    ], "Thanks, I appreciate your opinion.", "close_window", [
         (troop_set_slot, "$map_talk_troop", "$npc_grievance_slot",
          tms_acknowledged),
     ]],

    [anyone | plyr, "companion_objection_response", [
        (eq, "$npc_praise_not_complaint", 0),
    ], "Hopefully it won't happen again.", "close_window", [
         (troop_set_slot, "$map_talk_troop", "$npc_grievance_slot",
          tms_acknowledged),
     ]],

    [anyone | plyr, "companion_objection_response", [
        (eq, "$npc_praise_not_complaint", 0),
    ], "Your objection is noted. Now fall back in line.", "close_window", [
         (troop_set_slot, "$map_talk_troop", "$npc_grievance_slot", tms_dismissed),
         (troop_get_slot, ":grievance", "$map_talk_troop",
          slot_troop_morality_penalties),
         (val_add, ":grievance", 10),
         (troop_set_slot, "$map_talk_troop", slot_troop_morality_penalties,
          ":grievance"),
     ]],
]
