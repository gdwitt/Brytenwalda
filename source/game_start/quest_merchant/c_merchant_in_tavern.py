from source.header_dialogs import anyone, plyr, auto_proceed
from source.header_parties import ai_bhvr_patrol_location
from source.header_game_menus import *
from source.header_items import *
from source.module_constants import *


dialogs = [

    # At tavern merchant asks if player wants the quest again.
    (anyone, "start", [
        (is_between, "$g_talk_troop", "trp_briton_merchant", "trp_startup_merchants_end"),
        (eq, "$talk_context", tc_tavern_talk),
        (neg|check_quest_active, "qst_collect_men"),
        (neg|check_quest_finished, "qst_collect_men"),
        ], "So, willing to help me out?", "merchant_quest_tavern_1a", []
    ),

    [anyone | plyr, "merchant_quest_tavern_1a", [],
        "Yes, I'll collect some men from around the villages.",
        "merchant_quest_tavern_1b", [
        (str_store_troop_name, s9, "$g_talk_troop"),
        (str_store_party_name, s1, "$g_starting_town"),
        (str_store_string, s2, "str_start_up_quest_message_1"),

        (call_script, "script_start_quest", "qst_collect_men", "$g_talk_troop"),
        ]
    ],

    (anyone | plyr, "merchant_quest_tavern_1a", [],
        "No, not yet.", "close_window", []),

    (anyone, "merchant_quest_tavern_1b", [
        (is_between, "$g_talk_troop", "trp_briton_merchant", "trp_startup_merchants_end"),
        (eq, "$talk_context", tc_tavern_talk),
        ], "Great, see you then.", "close_window", []
    ),

    # At tavern, merchant tells player has not enough men
    [anyone | auto_proceed, "start", [
        (is_between, "$g_talk_troop", "trp_briton_merchant", "trp_startup_merchants_end"),
        (eq, "$talk_context", tc_tavern_talk),
        (check_quest_active, "qst_collect_men"),
        (neg | check_quest_succeeded, "qst_collect_men"),

        (call_script, "script_party_count_members_with_full_health", "p_main_party"),
        (assign, "$temp", reg0),
        ], "{!}.", "start_up_quest_2_next", []
    ],

    [anyone, "start_up_quest_2_next", [
        (lt, "$temp", 6),
        (try_begin),
            (eq, "$temp", 1),
            (str_store_string, s11, "str_please_sir_my_lady_go_find_some_volunteers_i_do_not_know_how_much_time_we_have"),
        (else_try),
            (str_store_string, s11, "str_you_need_more_men_sir_my_lady"),
        (try_end),
    ], "{!}{s11}", "close_window", []],

    # Merchant tells player it has enough men: qst_collect_men completed
    [anyone, "start_up_quest_2_next", [
        (ge, "$temp", 6),

        (str_store_party_name, s9, "$current_town"),

    ], "Splendid work. You have hired enough men to take on the bandits. Now -- "
       "travellers entering {s9} have told us that there is a small group of "
       "robbers lurking on the outside of town. I suspect that they are all "
       "from the same band, the one that took my brother. Hunt them down and "
       "defeat them, and make them disclose the location of their lair!",
        "merchant_quest_2a", [
        (call_script, "script_succeed_quest", "qst_collect_men"),
        (call_script, "script_end_quest", "qst_collect_men"),
     ]],

    # start `qst_learn_where_merchant_brother_is`
    [anyone | plyr, "merchant_quest_2a", [],
     "Very well. I shall hunt for bandits.", "close_window", [
        (str_store_party_name, s9, "$current_town"),
        (str_store_string, s2, "str_start_up_quest_message_2"),
        (call_script, "script_start_quest", "qst_learn_where_merchant_brother_is", "$g_talk_troop"),

        # create bandits
        (set_spawn_radius, 2),
        (spawn_around_party, "$current_town", "pt_leaded_looters"),
        (assign, ":spawned_bandits", reg0),

        (party_get_position, pos0, "$current_town"),
        (party_set_ai_behavior, ":spawned_bandits", ai_bhvr_patrol_location),
        (party_set_ai_patrol_radius, ":spawned_bandits", 3),
        (party_set_ai_target_position, ":spawned_bandits", pos0),
    ]],

    [anyone | plyr, "merchant_quest_2a", [],
     "Why don't you come with us?", "merchant_quest_2a_whynotcome", []],

    [anyone, "merchant_quest_2a_whynotcome", [],
     "Because I'm paying you to go take care of it. That's the short answer. The "
     "long answer is that I've got some leads to follow up here in town, and I "
     "have just as much chance of getting knocked on my head as you, if that's "
     "what you're asking. But I respect your question. Now, what do you say?",
     "merchant_quest_2a", []],

    [anyone | plyr, "merchant_quest_2a", [],
     "I cannot deal with this matter at this time.", "close_window", []],
]
