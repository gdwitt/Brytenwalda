from source.header_operations import *
from source.header_common import s5, s11, reg5, reg11

from source.header_dialogs import anyone, plyr

from source.module_constants import companions_begin, companions_end, \
    pclash_penalty_to_self, pclash_penalty_to_other, pclash_penalty_to_both

from source.statement import StatementBlock


simple_triggers = [
    (24, [
        (eq, "$disable_npc_clashes", 0),

        # Count NPCs in party (npcs_in_party) and get the "grievance_divisor",
        # which determines how fast grievances go away.
        # grievance_divisor = 100 - npcs_in_party + trp_player.skl_persuasion
        (assign, ":npcs_in_party", 0),
        (assign, ":grievance_divisor", 100),

        (try_for_range, ":npc1", companions_begin, companions_end),
            (main_party_has_troop, ":npc1"),
            (val_add, ":npcs_in_party", 1),
        (try_end),
        (val_sub, ":grievance_divisor", ":npcs_in_party"),
        (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
        (val_add, ":grievance_divisor", ":persuasion_level"),

        # Activate personality clash from 24 hours ago
        # scheduled personality clashes require at least 24hrs together
        (try_begin),
             (gt, "$personality_clash_after_24_hrs", 0),
             (try_begin),
                  (troop_get_slot, ":other_npc", "$personality_clash_after_24_hrs", "slot_troop_personalityclash_object"),
                  (main_party_has_troop, "$personality_clash_after_24_hrs"),
                  (main_party_has_troop, ":other_npc"),
                  (assign, "$npc_with_personality_clash", "$personality_clash_after_24_hrs"),
             (try_end),
             (assign, "$personality_clash_after_24_hrs", 0),
        (try_end),

        (try_for_range, ":npc", companions_begin, companions_end),
            (try_begin),
                (main_party_has_troop, ":npc"),

                # Change grievance over time by the factor 90/grievance_divisor
                (troop_get_slot, ":grievance", ":npc", "slot_troop_personalityclash_penalties"),
                (val_mul, ":grievance", 90),
                (val_div, ":grievance", ":grievance_divisor"),
                (troop_set_slot, ":npc", "slot_troop_personalityclash_penalties", ":grievance"),

                (troop_get_slot, ":grievance", ":npc", "slot_troop_morality_penalties"),
                (val_mul, ":grievance", 90),
                (val_div, ":grievance", ":grievance_divisor"),
                (troop_set_slot, ":npc", "slot_troop_morality_penalties", ":grievance"),

                # Affect moral by personalityclash
                (try_begin),
                    (troop_slot_ge, ":npc", "slot_troop_personalityclash_state", 1),

                    # if party contains the clashing npc
                    (troop_get_slot, ":object", ":npc", "slot_troop_personalityclash_object"),
                    (main_party_has_troop, ":object"),
                    # reduce moral
                    (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", "slot_troop_personalityclash_state"),
                (try_end),

                # Affect moral by personalityclash2
                (try_begin),
                    (troop_slot_ge, ":npc", "slot_troop_personalityclash2_state", 1),

                    (troop_get_slot, ":object", ":npc", "slot_troop_personalityclash2_object"),
                    (main_party_has_troop, ":object"),
                    (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", "slot_troop_personalityclash2_state"),
                (try_end),

                # Decrease grievance by 10% for personality matches
                (try_begin),
                    (troop_slot_ge, ":npc", "slot_troop_personalitymatch_state", 1),

                    (troop_get_slot, ":object", ":npc", "slot_troop_personalitymatch_object"),
                    (main_party_has_troop, ":object"),
                    (troop_get_slot, ":grievance", ":npc", "slot_troop_personalityclash_penalties"),
                    (val_mul, ":grievance", 9),
                    (val_div, ":grievance", 10),
                    (troop_set_slot, ":npc", "slot_troop_personalityclash_penalties", ":grievance"),
                (try_end),

                # Active personality clash 1 if at least 24 hours have passed
                (try_begin),
                    (eq, "$npc_with_personality_clash", 0),
                    (eq, "$npc_with_personality_clash_2", 0),
                    (eq, "$personality_clash_after_24_hrs", 0),
                    (troop_slot_eq, ":npc", "slot_troop_personalityclash_state", 0),
                    (troop_get_slot, ":other_npc", ":npc", "slot_troop_personalityclash_object"),
                    (main_party_has_troop, ":other_npc"),

                    (assign, "$personality_clash_after_24_hrs", ":npc"),
                (try_end),
            (try_end),
        (try_end),
    ])
]


scripts = [
    # todo: add comments to this script with more details
    ("post_battle_personality_clash_check", [
        (try_begin),
            (eq, "$disable_npc_clashes", 0),

            # personality clash 2
            (try_for_range, ":npc", companions_begin, companions_end),
                (troop_slot_eq, ":npc", "slot_troop_personalityclash2_state", 0),

                (main_party_has_troop, ":npc"),
                (neg|troop_is_wounded, ":npc"),

                (troop_get_slot, ":other_npc", ":npc", "slot_troop_personalityclash2_object"),
                (main_party_has_troop, ":other_npc"),
                (neg|troop_is_wounded, ":other_npc"),

                (assign, "$npc_with_personality_clash_2", ":npc"),
            (try_end),

            # personality match
            (try_for_range, ":npc", companions_begin, companions_end),
                (troop_slot_eq, ":npc", "slot_troop_personalitymatch_state", 0),

                (main_party_has_troop, ":npc"),
                (neg|troop_is_wounded, ":npc"),

                (troop_get_slot, ":other_npc", ":npc", "slot_troop_personalitymatch_object"),
                (main_party_has_troop, ":other_npc"),
                (neg|troop_is_wounded, ":other_npc"),
                (assign, "$npc_with_personality_match", ":npc"),
            (try_end),

            # trigger personality clash 2
            (try_begin),
                (gt, "$npc_with_personality_clash_2", 0),
                (try_begin),
                    (eq, "$cheat_mode", 1),
                    (display_message, "str_personality_clash_conversation_begins"),
                (try_end),

                (try_begin),
                    (main_party_has_troop, "$npc_with_personality_clash_2"),
                    (assign, "$npc_map_talk_context", "slot_troop_personalityclash2_state"),
                    (start_map_conversation, "$npc_with_personality_clash_2"),
                (else_try),
                    (assign, "$npc_with_personality_clash_2", 0),
                (try_end),
            # trigger personality match
            (else_try),
                (gt, "$npc_with_personality_match", 0),
                (try_begin),
                    (eq, "$cheat_mode", 1),
                    (display_message, "str_personality_match_conversation_begins"),
                (try_end),

                (try_begin),
                    (main_party_has_troop, "$npc_with_personality_match"),
                    (assign, "$npc_map_talk_context", "slot_troop_personalitymatch_state"),
                    (start_map_conversation, "$npc_with_personality_match"),
                (else_try),
                    (assign, "$npc_with_personality_match", 0),
                (try_end),
            (try_end),
        (try_end),
     ]),

    # INPUT: arg1 = troop_no for companion1 arg2 = troop_no for companion2 arg3 = slot_for_clash_state
    # slot_for_clash_state means: 1=give full penalty to companion1; 2=give full penalty to companion2; 3=give penalty equally
    ("reduce_companion_morale_for_clash", [
        (store_script_param, ":companion_1", 1),
        (store_script_param, ":companion_2", 2),
        (store_script_param, ":slot_for_clash_state", 3),

        (troop_get_slot, ":clash_state", ":companion_1", ":slot_for_clash_state"),
        (troop_get_slot, ":grievance_1", ":companion_1", "slot_troop_personalityclash_penalties"),
        (troop_get_slot, ":grievance_2", ":companion_2", "slot_troop_personalityclash_penalties"),
        (try_begin),
          (eq, ":clash_state", pclash_penalty_to_self),
          (val_add, ":grievance_1", 5),
        (else_try),
          (eq, ":clash_state", pclash_penalty_to_other),
          (val_add, ":grievance_2", 5),
        (else_try),
          (eq, ":clash_state", pclash_penalty_to_both),
          (val_add, ":grievance_1", 3),
          (val_add, ":grievance_2", 3),
        (try_end),
        (troop_set_slot, ":companion_1", "slot_troop_personalityclash_penalties", ":grievance_1"),
        (troop_set_slot, ":companion_2", "slot_troop_personalityclash_penalties", ":grievance_2"),
    ]),
]


trigger_dialog_block = StatementBlock(
    (eq, "$disable_npc_clashes", 0),
    (gt, "$npc_with_personality_clash", 0),
    (eq, "$g_infinite_camping", 0),
    (troop_get_slot, ":object", "$npc_with_personality_clash", "slot_troop_personalityclash_object"),
    (try_begin),
        (main_party_has_troop, "$npc_with_personality_clash"),
        (main_party_has_troop, ":object"),
        (neq, "$g_player_is_captive", 1),

        (assign, "$npc_map_talk_context", "slot_troop_personalityclash_state"),

        (start_map_conversation, "$npc_with_personality_clash", -1),
    (else_try),
        (assign, "$npc_with_personality_clash", 0),
    (try_end),
)


dialogs = [
    # Personality clash 2 objections
    [anyone, "event_triggered", [
        (store_conversation_troop, "$map_talk_troop"),
        (is_between, "$map_talk_troop", companions_begin, companions_end),

        (eq, "$map_talk_troop", "$npc_with_personality_clash_2"),
        (eq, "$npc_map_talk_context", "slot_troop_personalityclash2_state"),

        (troop_get_slot, ":speech", "$map_talk_troop", "slot_troop_personalityclash2_speech"),
        (troop_get_slot, ":object", "$map_talk_troop", "slot_troop_personalityclash2_object"),
        (str_store_troop_name, s11, ":object"),
        (str_store_string, s5, ":speech"),
    ], "{s5}", "companion_personalityclash2_b", [
         (assign, "$npc_with_personality_clash_2", 0),
         (troop_get_slot, ":grievance", "$map_talk_troop", "slot_troop_personalityclash_penalties"),
         (val_add, ":grievance", 5),
         (troop_set_slot, "$map_talk_troop", "slot_troop_personalityclash_penalties", ":grievance"),

         (troop_get_slot, ":object", "$map_talk_troop", "slot_troop_personalityclash2_object"),
         (call_script, "script_troop_change_relation_with_troop", "$map_talk_troop", ":object", -15),
     ]],

    # Companion argues about a clash
    [anyone, "companion_personalityclash2_b", [],
     "{s5}", "companion_personalityclash2_response", [
         (troop_get_slot, ":speech", "$map_talk_troop", "slot_troop_personalityclash2_speech_b"),
         (troop_get_slot, ":object", "$map_talk_troop", "slot_troop_personalityclash2_object"),
         (str_store_troop_name, 11, ":object"),
         (str_store_string, 5, ":speech"),
     ]],

    # Player supports npc
    [anyone | plyr, "companion_personalityclash2_response", [
        (troop_get_slot, ":object", "$map_talk_troop",
         "slot_troop_personalityclash2_object"),
        (str_store_troop_name, s11, ":object"),
        (troop_get_type, reg11, ":object"),
        (val_mod, reg11, 2),
    ], "{s11} is a valuable member of this company. I don't want you picking "
       "any more fights with {reg11?her:him}.",
     "close_window", [
         (troop_set_slot, "$map_talk_troop", "slot_troop_personalityclash2_state",
          pclash_penalty_to_self),
     ]],

    # Player supports other npc
    [anyone | plyr, "companion_personalityclash2_response", [
        (troop_get_slot, ":object", "$map_talk_troop",
         "slot_troop_personalityclash2_object"),
        (str_store_troop_name, s11, ":object"),
        ##Gender fix chief altura
        (troop_get_type, reg11, ":object"),
        (val_mod, reg11, 2),
        # gender fix acaba chief
    ], "Tell {s11} you have my support in this, and {reg11?she:he} should hold {reg11?her:his} tongue.",
     "close_window", [
         (troop_set_slot, "$map_talk_troop", "slot_troop_personalityclash2_state",
          pclash_penalty_to_other),
     ]],

    # Player supports neither
    [anyone | plyr, "companion_personalityclash2_response", [],
     "I don't have time for your petty dispute. Do not bother me with this again.",
     "close_window", [
         (troop_set_slot, "$map_talk_troop", "slot_troop_personalityclash2_state",
          pclash_penalty_to_both),
     ]],

    # Personality clash objection
    [anyone, "event_triggered", [
        (store_conversation_troop, "$map_talk_troop"),
        (is_between, "$map_talk_troop", companions_begin, companions_end),

        (eq, "$map_talk_troop", "$npc_with_personality_clash"),
        (eq, "$npc_map_talk_context", "slot_troop_personalityclash_state"),

        (troop_get_slot, ":speech", "$map_talk_troop", "slot_troop_personalityclash_speech"),
        (troop_get_slot, ":object", "$map_talk_troop", "slot_troop_personalityclash_object"),
        (str_store_troop_name, 11, ":object"),
        (str_store_string, 5, ":speech"),
    ],
     "{s5}", "companion_personalityclash_b", [
         (assign, "$npc_with_personality_clash", 0),
         (troop_get_slot, ":grievance", "$map_talk_troop",
          "slot_troop_personalityclash_penalties"),
         (val_add, ":grievance", 5),
         (troop_set_slot, "$map_talk_troop", "slot_troop_personalityclash_penalties",
          ":grievance"),

         (troop_get_slot, ":object", "$map_talk_troop", "slot_troop_personalityclash_object"),
         (
         call_script, "script_troop_change_relation_with_troop", "$map_talk_troop",
         ":object", -15),
     ]],

    # Companion argues about a clash
    [anyone, "companion_personalityclash_b", [],
     "{s5}", "companion_personalityclash_response", [
         (troop_get_slot, ":speech", "$map_talk_troop", "slot_troop_personalityclash_speech_b"),
         (troop_get_slot, ":object", "$map_talk_troop", "slot_troop_personalityclash_object"),
         (str_store_troop_name, reg11, ":object"),
         (str_store_string, reg5, ":speech"),
     ]],

    # Player supports npc
    [anyone | plyr, "companion_personalityclash_response", [
        (troop_get_slot, ":object", "$map_talk_troop", "slot_troop_personalityclash_object"),
        (str_store_troop_name, s11, ":object"),
        (troop_get_type, reg11, ":object"),
        (val_mod, reg11, 2),
    ], "{s11} is a capable member of this company. I don't want you picking "
       "any more fights with {reg11?her:him}.", "close_window", [
         (troop_set_slot, "$map_talk_troop", "slot_troop_personalityclash_state",
          pclash_penalty_to_self),
     ]],

    # Player supports other npc
    [anyone | plyr, "companion_personalityclash_response", [
        (troop_get_slot, ":object", "$map_talk_troop", "slot_troop_personalityclash_object"),
        (str_store_troop_name, s11, ":object"),
        (troop_get_type, reg11, ":object"),
        (val_mod, reg11, 2),
    ], "Tell {s11} you have my support in this, and {reg11?she:he} should "
       "hold {reg11?her:his} tongue.", "close_window", [
         (troop_set_slot, "$map_talk_troop", "slot_troop_personalityclash_state",
          pclash_penalty_to_other),
     ]],

    # Player supports neither
    [anyone | plyr, "companion_personalityclash_response", [],
     "I don't have time for your petty dispute. Do not bother me with this again.",
     "close_window", [
         (troop_set_slot, "$map_talk_troop", "slot_troop_personalityclash_state",
          pclash_penalty_to_both),
     ]],

    # Personality match
    [anyone, "event_triggered", [
        (store_conversation_troop, "$map_talk_troop"),
        (eq, "$npc_map_talk_context", "slot_troop_personalitymatch_state"),
        (is_between, "$map_talk_troop", companions_begin, companions_end),
        (eq, "$map_talk_troop", "$npc_with_personality_match"),

        (troop_get_slot, ":speech", "$map_talk_troop", "slot_troop_personalitymatch_speech"),
        (troop_get_slot, ":object", "$map_talk_troop", "slot_troop_personalitymatch_object"),
        (str_store_troop_name, reg11, ":object"),
        (str_store_string, reg5, ":speech"),
    ],
     "{s5}", "companion_personalitymatch_b", [
         (assign, "$npc_with_personality_match", 0),
         (troop_get_slot, ":object", "$map_talk_troop", "slot_troop_personalitymatch_object"),
         (call_script, "script_troop_change_relation_with_troop", "$map_talk_troop", ":object", 15),
     ]],

    [anyone, "companion_personalitymatch_b", [
        (troop_get_slot, ":speech", "$map_talk_troop", "slot_troop_personalitymatch_speech_b"),
        (troop_get_slot, ":object", "$map_talk_troop", "slot_troop_personalitymatch_object"),
        (str_store_troop_name, reg11, ":object"),
        (str_store_string, reg5, ":speech"),

        ], "{s5}", "companion_personalitymatch_response", []
     ],

    [anyone | plyr, "companion_personalitymatch_response", [],
     "Very good.", "close_window", [
         (troop_set_slot, "$map_talk_troop", "slot_troop_personalitymatch_state", 1),
     ]],
]
