from source.header_common import *
from source.header_dialogs import anyone, plyr, auto_proceed
from source.module_constants import *
from source.header_operations import *


from . import recruit, buy_cattle, ask_enemies, give_money, make_fire, \
    quest_deliver_cattle, quest_deliver_grain, quest_fugitive, quest_train_peasants, \
    quest_oim_dmitriy_gerasim, quest_zamoshie, quest_others


_start_dialogs = [
    [anyone, "start", [
        (is_between, "$g_talk_troop", village_elders_begin, village_elders_end),
        (eq, "$g_talk_troop_met", 0),
        (party_slot_eq, "$current_town", "slot_town_lord", "trp_player"),
        (str_store_party_name, s9, "$current_town")
    ], "Welcome to {s9}, my {lord/lady}. We were rejoiced by the news that "
       "you are the new {lord/lady} of our humble village. I am the village "
       "elder and I will be honoured to serve you in any way I can.",
     "village_elder_talk", []
     ],

    [anyone, "start", [
        (is_between, "$g_talk_troop", village_elders_begin, village_elders_end),
        (eq, "$g_talk_troop_met", 0),
        (str_store_party_name, s9, "$current_town")
    ], "Good day, {sir/madam}, and welcome to {s9}. I am the elder of this "
       "village.", "village_elder_talk", []
     ],

    [anyone, "start", [
        (is_between, "$g_talk_troop", village_elders_begin, village_elders_end),
        (party_slot_eq, "$current_town", "slot_town_lord", "trp_player")
    ], "{My lord/My lady}, you honour our humble village with your presence.",
     "village_elder_talk", []
     ],

    [anyone, "start", [
        (is_between, "$g_talk_troop", village_elders_begin, village_elders_end)
    ], "Good day, {sir/madam}.", "village_elder_talk", []],
]

_talk_dialogs = [

    [anyone, "village_elder_pretalk", [],
     "Is there anything else I can do for you?", "village_elder_talk", []
     ],

    # -> `make_fire.py`
    [anyone | plyr, "village_elder_talk", [
        make_fire.village_elder_talk_condition,
    ],
     "I need you to set a large fire on the outskirts of this village.",
     "village_elder_ask_set_fire", []],

    # -> `recruit.py`
    [anyone | plyr, "village_elder_talk", [
        (call_script, "script_cf_village_recruit_volunteers_condition", 0, 0),
        (store_troop_gold, ":money", "trp_player"),
        (ge, ":money", 40),
    ], "I need help finding men who want to join me. Of course, here's a reward "
     "of 40 coins for you.", "village_elder_recruit_start", [
         (troop_remove_gold, "trp_player", 40),
     ]],

    # -> `ask_enemies.py`
    [anyone | plyr, "village_elder_talk", [],
     "Have you seen any enemies around here recently?",
     "village_elder_ask_enemies", []],

    # -> _mission_dialogs
    [anyone | plyr, "village_elder_talk", [
        (store_partner_quest, ":elder_quest"),
        (ge, ":elder_quest", 0),
    ], "About the task you asked of me...",
     "village_elder_active_mission_1", []
     ],

    # -> _trade_dialogs
    [anyone | plyr, "village_elder_talk", [
        (party_slot_eq, "$current_town", "slot_village_state", 0),
        (party_slot_lt, "$current_town", "slot_village_infested_by_bandits", 1)
        ],
     "I want to buy some supplies. I will pay with gold.",
     "village_elder_trade_begin", []
     ],

    # -> _trade_dialogs
    [anyone | plyr, "village_elder_talk", [
        (ge, "$g_talk_troop_faction_relation", 0),
        (store_partner_quest, ":elder_quest"),
        (lt, ":elder_quest", 0)
    ], "Do you have any tasks I can help you with?",
     "village_elder_request_mission_ask", []
     ],

    [anyone | plyr, "village_elder_talk", [], "[Leave]", "close_window", []],
]


_trade_dialogs = [

    [anyone, "village_elder_trade_begin", [],
     "Of course, {sir/madam}. Do you want to buy goods or cattle?",
     "village_elder_trade_talk", []],

    # goods
    [anyone | plyr, "village_elder_trade_talk", [],
     "I want to buy food and supplies.", "village_elder_trade", []],

    [anyone, "village_elder_trade", [],
     "We have some food and other supplies in our storehouse. Come have a look.",
     "village_elder_pretalk", [(change_screen_trade, "$g_talk_troop"), ]],

    # -> `buy_cattle.py`
    [anyone | plyr, "village_elder_trade_talk", [
        (party_slot_eq, "$current_town", "slot_village_state", 0),
        (party_slot_lt, "$current_town", "slot_village_infested_by_bandits", 1),

        # can't trade cattle when there is a mission to buy them.
        (assign, ":quest_village", 0),
        (try_begin),
            (check_quest_active, "qst_deliver_cattle"),
            (quest_slot_eq, "qst_deliver_cattle", slot_quest_target_center, "$current_town"),
            (assign, ":quest_village", 1),
        (try_end),
        (eq, ":quest_village", 0),
    ], "I want to buy some cattle.", "village_elder_buy_cattle", []],

    # cancel
    [anyone | plyr, "village_elder_trade_talk", [],
     "I changed my mind. I don't need to buy anything.", "village_elder_pretalk",
     []],
]


_mission_dialogs = [

    # Mission progress
    [anyone, "village_elder_active_mission_1", [],
     "Yes {sir/madam}, have you made any progress on it?",
     "village_elder_active_mission_2", []],

    # working on.
    [anyone | plyr, "village_elder_active_mission_2", [],
     "I am still working on it.", "village_elder_active_mission_3", []],

    [anyone, "village_elder_active_mission_3", [],
     "Thank you, {sir/madam}. We are praying for your success everyday.",
     "village_elder_pretalk", []],

    # cancel mission
    [anyone | plyr, "village_elder_active_mission_2", [],
     "I am afraid I won't be able to finish it.", "village_elder_mission_failed",
     []],

    [anyone, "village_elder_mission_failed", [],
     "Ah, I am sorry to hear that {sir/madam}. I'll try to think of something else.",
     "village_elder_pretalk", [
         (store_partner_quest, ":elder_quest"),
         (call_script, "script_abort_quest", ":elder_quest", 1)]
     ],

    # ask for mission -> already on a mission.
    [anyone, "village_elder_request_mission_ask", [
        (store_partner_quest, ":elder_quest"),
        (ge, ":elder_quest", 0)
    ], "Well {sir/madam}, you are already engaged with a task helping us. "
       "We cannot ask more from you.",
     "village_elder_pretalk", []
     ],

    # ask for mission -> no missions available
    [anyone, "village_elder_request_mission_ask", [
        (troop_slot_eq, "$g_talk_troop", slot_troop_does_not_give_quest, 0)
    ], "No {sir/madam}, We don't have any other tasks for you.",
     "village_elder_pretalk", []],

    # todo: what does `auto_proceed` do?
    [anyone | auto_proceed, "village_elder_request_mission_ask", [],
     "A task?", "village_elder_tell_mission", [
         (call_script, "script_get_quest", "$g_talk_troop"),
         (assign, "$random_quest_no", reg0),
     ]],

    # ask for mission -> no missions available
    [anyone, "village_elder_tell_mission", [],
     "Thank you, {sir/madam}, but we do not really need anything right now.",
     "village_elder_pretalk", []
     ],
]

dialogs = recruit.dialogs \
          + buy_cattle.dialogs \
          + ask_enemies.dialogs \
          + give_money.dialogs \
          + quest_deliver_cattle.dialogs \
          + quest_deliver_grain.dialogs \
          + quest_fugitive.dialogs \
          + quest_train_peasants.dialogs \
          + make_fire.dialogs \
          + quest_oim_dmitriy_gerasim.dialogs \
          + quest_zamoshie.dialogs \
          + quest_others.dialogs \
          + _start_dialogs + _talk_dialogs + _trade_dialogs + _mission_dialogs
