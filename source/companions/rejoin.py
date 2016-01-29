from source.header_operations import *
from source.header_common import s5, s19, s20, s21, reg3

from source.header_dialogs import anyone, plyr, auto_proceed

from source.module_constants import *

from source.statement import StatementBlock


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

    # rejoin for finding him at a town.
    [anyone, "start", [
        (is_between, "$g_talk_troop", companions_begin, companions_end),
        (this_or_next|eq, "$talk_context", tc_tavern_talk),
        (this_or_next|eq, "$talk_context", tc_town_talk),
        (eq, "$talk_context", tc_court_talk),
        (main_party_has_troop, "$g_talk_troop")
        ], "Let's leave whenever you are ready.", "close_window", []
     ],

    [anyone, "start", [
        (is_between, "$g_talk_troop", companions_begin, companions_end),
        (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, 0),
        (troop_slot_eq, "$g_talk_troop", slot_troop_turned_down_twice, 1),
        ], "Please do not waste any more of my time today, {sir/madame}. "
           "Perhaps we shall meet again in our travels.", "close_window", []
    ],

    # first encounter with companion
    [anyone, "start", [
        (is_between, "$g_talk_troop", companions_begin, companions_end),
        (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, 0),
        (eq, "$g_talk_troop_met", 0),
        (troop_get_slot, ":intro", "$g_talk_troop", slot_troop_intro),
        (str_store_string, s5, ":intro"),
        (str_store_party_name, s20, "$g_encountered_party"),
        ], "{s5}", "companion_recruit_intro_response", [
        (troop_set_slot, "$g_talk_troop", slot_troop_first_encountered, "$g_encountered_party"),
    ]],

    [anyone | plyr, "companion_recruit_intro_response", [
        (troop_get_slot, ":intro_response", "$g_talk_troop", slot_troop_intro_response_1),
        (str_store_string, s5, ":intro_response")
        ], "{s5}", "companion_recruit_backstory_a", []
    ],

    [anyone | plyr, "companion_recruit_intro_response", [
        (troop_get_slot, ":intro_response", "$g_talk_troop", slot_troop_intro_response_2),
        (str_store_string, s5, ":intro_response")
        ], "{s5}", "close_window", []
    ],

    [anyone, "companion_recruit_backstory_a", [
        (troop_get_slot, ":backstory_a", "$g_talk_troop", slot_troop_backstory_a),
        (str_store_string, s5, ":backstory_a"),
        (str_store_string, s19, "str_here_plus_space"),
        (str_store_party_name, s20, "$g_encountered_party"),
        ], "{s5}", "companion_recruit_backstory_b", []
    ],

    [anyone, "companion_recruit_backstory_b", [
        (troop_get_slot, ":backstory_b", "$g_talk_troop", slot_troop_backstory_b),
        (str_store_string, s5, ":backstory_b"),
        (str_store_party_name, s20, "$g_encountered_party"),
        ], "{s5}", "companion_recruit_backstory_c", []
    ],

    [anyone, "companion_recruit_backstory_c", [
        (troop_get_slot, ":backstory_c", "$g_talk_troop", slot_troop_backstory_c),
        (str_store_string, s5, ":backstory_c"),
        ], "{s5}", "companion_recruit_backstory_response", []
    ],

    [anyone | plyr, "companion_recruit_backstory_response", [
        (troop_get_slot, ":backstory_response", "$g_talk_troop", slot_troop_backstory_response_1),
        (str_store_string, s5, ":backstory_response")
        ], "{s5}", "companion_recruit_signup", []
    ],

    [anyone | plyr, "companion_recruit_backstory_response", [
        (troop_get_slot, ":backstory_response", "$g_talk_troop", slot_troop_backstory_response_2),
        (str_store_string, s5, ":backstory_response")
        ], "{s5}", "close_window", []
    ],

    [anyone, "companion_recruit_signup", [
        (troop_get_slot, ":signup", "$g_talk_troop", slot_troop_signup),
        (str_store_string, s5, ":signup"),
        (str_store_party_name, s20, "$g_encountered_party"),
        ], "{s5}", "companion_recruit_signup_b", []
    ],

    [anyone, "companion_recruit_signup_b", [
        (troop_get_slot, ":signup", "$g_talk_troop", slot_troop_signup_2),
        (troop_get_slot, reg3, "$g_talk_troop", slot_troop_payment_request),#

        (str_store_string, s5, ":signup"),
        (str_store_party_name, s20, "$g_encountered_party"),
        ], "{s5}", "companion_recruit_signup_response", []
    ],

    [anyone | plyr, "companion_recruit_signup_response", [
        (neg|hero_can_join, "p_main_party")
        ], "Unfortunately, I can't take on any more hands in my party "
           "right now.", "close_window", []
    ],

    [anyone | plyr, "companion_recruit_signup_response", [
        (hero_can_join, "p_main_party"),
        (troop_get_slot, ":signup_response", "$g_talk_troop", slot_troop_signup_response_1),
        (str_store_string, s5, ":signup_response")
        ], "{s5}", "companion_recruit_payment", []
    ],

    [anyone | plyr, "companion_recruit_signup_response", [
        (hero_can_join, "p_main_party"),
        (troop_get_slot, ":signup_response", "$g_talk_troop", slot_troop_signup_response_2),
        (str_store_string, s5, ":signup_response")
        ], "{s5}", "close_window", []
    ],

    [anyone | auto_proceed, "companion_recruit_payment", [
      (troop_slot_eq, "$g_talk_troop", slot_troop_payment_request, 0),
        ], ".", "companion_recruit_signup_confirm", []
    ],

    [anyone, "companion_recruit_payment", [
        (store_sub, ":npc_offset", "$g_talk_troop", "trp_npc1"),
        (store_add, ":dialog_line", "str_npc1_payment", ":npc_offset"),
        (str_store_string, s5, ":dialog_line"),
        (troop_get_slot, reg3, "$g_talk_troop", slot_troop_payment_request),
        (str_store_party_name, s20, "$g_encountered_party"),
        ], "{s5}", "companion_recruit_payment_response", []],

    [anyone | plyr, "companion_recruit_payment_response", [
        (hero_can_join, "p_main_party"),
        (troop_get_slot, ":amount_requested", "$g_talk_troop", slot_troop_payment_request),
        (store_troop_gold, ":gold", "trp_player"),
        (ge, ":gold", ":amount_requested"),
        (assign, reg3, ":amount_requested"),
        (store_sub, ":npc_offset", "$g_talk_troop", "trp_npc1"),
        (store_add, ":dialog_line", "str_npc1_payment_response", ":npc_offset"),
        (str_store_string, s5, ":dialog_line"),
        ], "{s5}", "companion_recruit_signup_confirm", [
        (troop_get_slot, ":amount_requested", "$g_talk_troop", slot_troop_payment_request),
        (gt, ":amount_requested", 0),
        (troop_remove_gold, "trp_player", ":amount_requested"),
        (troop_set_slot, "$g_talk_troop", slot_troop_payment_request, 0),
    ]],

    [anyone | plyr, "companion_recruit_payment_response", [],
     "Sorry. I can't afford that at the moment.", "close_window", []
    ],

    [anyone, "start", [
        (is_between, "$g_talk_troop", companions_begin, companions_end),
        (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, 0),
        (troop_slot_eq, "$g_talk_troop", slot_troop_met_previously, 1),
        (troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, 0),
        ], "We meet again.", "companion_recruit_meet_again", [
        (troop_set_slot, "$g_talk_troop", slot_troop_turned_down_twice, 1),
    ]],

    [anyone | plyr, "companion_recruit_meet_again", [],
     "So... What have you been doing since our last encounter?",
     "companion_recruit_backstory_delayed", []
    ],

    [anyone | plyr, "companion_recruit_meet_again", [], "Good day to you.", "close_window", []],

    [anyone, "start", [
        (is_between, "$g_talk_troop", companions_begin, companions_end),
        (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, 0),
        (troop_slot_eq, "$g_talk_troop", slot_troop_met_previously, 0),
        (troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, 0),
        ], "Yes?", "companion_recruit_secondchance", [
        (troop_set_slot, "$g_talk_troop", slot_troop_turned_down_twice, 1),
    ]],

    [anyone | plyr, "companion_recruit_secondchance", [],
     "My apologies if I was rude earlier. What was your story again?",
     "companion_recruit_backstory_b", []
    ],

    [anyone | plyr, "companion_recruit_secondchance", [],
     "Never mind.", "close_window", []
    ],

    [anyone, "companion_recruit_backstory_delayed", [
        (troop_get_slot, ":backstory_delayed", "$g_talk_troop", slot_troop_backstory_delayed),
        (str_store_string, s5, ":backstory_delayed")
    ], "{s5}", "companion_recruit_backstory_delayed_response", []],

    [anyone | plyr, "companion_recruit_backstory_delayed_response", [],
     "I might be able to use you in my shield wall.",
     "companion_recruit_signup_b", []
    ],

    [anyone | plyr, "companion_recruit_backstory_delayed_response", [],
     "I'll let you know if I hear of anything.", "close_window", []
    ],

    [anyone, "companion_recruit_signup_confirm", [],
     "Good! Give me a few moments to prepare and I'll be ready to move.",
     "close_window", [
         (call_script, "script_recruit_troop_as_companion", "$g_talk_troop")
    ]],

    # Rehire dialogues
    [anyone, "start", [
        (is_between, "$g_talk_troop", companions_begin, companions_end),
        (neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
        (troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, pp_history_indeterminate),

        (troop_get_slot, ":prison_center", "$g_talk_troop", slot_troop_prisoner_of_party),
        (lt, ":prison_center", centers_begin),
        ], "My offer to rejoin you still stands, if you'll have me.",
        "companion_rehire", []
    ],

    # If the companion and the player were separated in battle
    [anyone, "start", [
        (is_between, "$g_talk_troop", companions_begin, companions_end),
        (neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
        (troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, pp_history_scattered),

        (this_or_next|eq, "$talk_context", tc_hero_freed),
        (neg|troop_slot_ge, "$g_talk_troop", slot_troop_prisoner_of_party, 0),

        (neq, "$talk_context", tc_prison_break),

        (assign, ":battle_fate", "str_battle_fate_1"),
        (store_random_in_range, ":fate_roll", 0, 5),
        (val_add, ":battle_fate", ":fate_roll"),
        (str_store_string, s19, ":battle_fate"),
        (troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
        (str_store_string, s5, ":honorific"),
        ], "It is good to see you alive, {s5}! {s19}, and I did not know whether "
           "you had been captured, or slain, or got away. I've been roaming "
           "around since then, looking for you. Shall I get my gear together "
           "and rejoin your shield wall?", "companion_rehire", [
        (troop_set_slot, "$g_talk_troop", slot_troop_playerparty_history, pp_history_indeterminate),
        (troop_set_slot, "$g_talk_troop", slot_troop_prisoner_of_party, -1),
    ]],

    [anyone | plyr, "start", [
        (is_between, "$g_talk_troop", companions_begin, companions_end),
        (neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
        (troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, pp_history_scattered),

        (troop_slot_ge, "$g_talk_troop", slot_troop_prisoner_of_party, 0),

        (neq, "$talk_context", tc_prison_break),

        ], "I've come to break you out of here.", "companion_prison_break_chains", []
    ],

    [anyone, "companion_prison_break_chains", [],
     "Thank the heavens you came! However, I'm not going anywhere with these "
     "chains on my legs. You'll need to get the key away from the guard "
     "somehow.", "close_window", []
    ],

    # If the player and the companion parted on bad terms
    [anyone, "start", [
        (is_between, "$g_talk_troop", companions_begin, companions_end),
        (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, 0),
        (troop_slot_eq, "$g_talk_troop", slot_troop_turned_down_twice, 0),
        (troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, pp_history_quit),
        (troop_get_slot, ":speech", "$g_talk_troop", slot_troop_rehire_speech),
        (str_store_string, s5, ":speech"),
        ], "{s5}", "companion_rehire", [
            (troop_set_slot, "$g_talk_troop", slot_troop_playerparty_history, pp_history_indeterminate),
    ]],

    # If the player and the companion parted on good terms
    [anyone, "start", [
        (is_between, "$g_talk_troop", companions_begin, companions_end),
        (troop_slot_eq, "$g_talk_troop", slot_troop_occupation, 0),
        (troop_slot_eq, "$g_talk_troop", slot_troop_playerparty_history, pp_history_dismissed),
        (troop_get_slot, ":honorific", "$g_talk_troop", slot_troop_honorific),
        (str_store_string, s21, ":honorific"),
        (troop_get_slot, ":speech", "$g_talk_troop", slot_troop_backstory_delayed),
        (str_store_string, s5, ":speech"),
        ], "It is good to see you, {s21}! To tell you the truth, I had hoped "
           "to run into you.", "companion_was_dismissed", [
        (troop_set_slot, "$g_talk_troop", slot_troop_playerparty_history, pp_history_indeterminate),
    ]],

    [anyone, "companion_was_dismissed", [
        (neg | troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
        (troop_get_slot, ":speech", "$g_talk_troop", slot_troop_backstory_delayed),
        (str_store_string, s5, ":speech"),
        ], "{s5}. Would you want me to rejoin your shield wall?",
        "companion_rehire", []
    ],

    [anyone | plyr, "companion_rehire", [
        (hero_can_join, "p_main_party"),
    ], "Welcome back, my friend!", "companion_recruit_signup_confirm", []],

    [anyone | plyr, "companion_rehire", [],
     "Sorry, I can't take on anyone else right now.", "companion_rehire_refused", []],

    [anyone, "companion_rehire_refused", [],
     "Well... Look me up if you change your mind, eh?", "close_window", [
        (troop_get_slot, ":current_town_no", "$g_talk_troop", slot_troop_cur_center),

        (try_begin),
            (neg|is_between, ":current_town_no", towns_begin, towns_end),

            (store_random_in_range, ":town_no", towns_begin, towns_end),
            (troop_set_slot, "$g_talk_troop", slot_troop_cur_center, ":town_no"),

            (try_begin),
                (ge, "$cheat_mode", 1),
                (assign, reg3, ":current_town_no"),
                (str_store_party_name, s5, ":town_no"),
                (display_message, "@{!}current town was {reg3}, now moved to {s5}"),
            (try_end),
        (try_end),
    ]],

    # Default dialog for rehire
    [anyone, "start", [
        (is_between, "$g_talk_troop", companions_begin, companions_end),
        (neg|troop_slot_eq, "$g_talk_troop", slot_troop_occupation, slto_kingdom_hero),
        (troop_get_slot, ":prison_center", "$g_talk_troop", slot_troop_prisoner_of_party),
        (lt, ":prison_center", centers_begin),
        ], "So... Do you want me back yet?", "companion_rehire", []
    ],
]
