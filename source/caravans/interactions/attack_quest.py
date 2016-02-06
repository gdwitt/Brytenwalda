from source.header_operations import *
from source.header_common import s17

from source.header_dialogs import anyone, plyr

from source.module_constants import tc_party_encounter


dialogs = [

    [anyone | plyr, "merchant_talk", [
        (le, "$talk_context", tc_party_encounter),
        (check_quest_active, "qst_cause_provocation"),
        (neg | check_quest_concluded, "qst_cause_provocation"),

        (quest_slot_eq, "qst_cause_provocation", "slot_quest_target_faction", "$g_encountered_party_faction"),

        (quest_get_slot, ":giver_troop", "qst_cause_provocation", "slot_quest_giver_troop"),
        (store_faction_of_troop, ":giver_troop_faction", ":giver_troop"),

        (str_store_faction_name, s17, ":giver_troop_faction"),
        ], "You are trespassing in the territory of the {s17}. I am confiscating "
           "this caravan and all its goods!", "caravan_start_war_quest_1", []
     ],

    [anyone, "caravan_start_war_quest_1", [
        (quest_get_slot, ":giver_troop", "qst_cause_provocation", "slot_quest_giver_troop"),
        (store_faction_of_troop, ":giver_troop_faction", ":giver_troop"),
        (str_store_faction_name, s17, ":giver_troop_faction"),
    ], "What? What nonsense is this? We are at peace with the {s17}, and are "
       "free to cross its lands!", "caravan_start_war_quest_2", []
     ],

    [anyone | plyr, "caravan_start_war_quest_2", [],
     "We'll see about that! Defend yourselves!", "merchant_attack", []
     ],

    [anyone | plyr, "caravan_start_war_quest_2", [],
     "Hmm. Maybe this was all a misunderstanding. Farewell.", "close_window", [
         (assign, "$g_leave_encounter", 1)]
     ],
]
