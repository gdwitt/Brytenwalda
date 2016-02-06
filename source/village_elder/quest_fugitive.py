from source.header_operations import *
from source.header_common import *

from source.header_dialogs import anyone, plyr

# todo: this quest is set by a lord.

dialogs = [

    [anyone | plyr, "village_elder_talk", [
        (check_quest_active, "qst_hunt_down_fugitive"),
        (neg | check_quest_concluded, "qst_hunt_down_fugitive"),
        (quest_slot_eq, "qst_hunt_down_fugitive", "slot_quest_target_center",
         "$current_town"),
        (quest_get_slot, ":quest_target_dna", "qst_hunt_down_fugitive",
         "slot_quest_target_dna"),
        (call_script, "script_get_name_from_dna_to_s50", ":quest_target_dna"),
        (str_store_string, s4, s50),
    ],
     "I am looking for a man by the name of {s4}. I was told he may be hiding here.",
     "village_elder_ask_fugitive", []],

    [anyone | plyr, "village_elder_talk", [
        (check_quest_active, "qst_bounty_1"),
        (neg | check_quest_concluded, "qst_bounty_1"),
        (quest_slot_eq, "qst_bounty_1", "slot_quest_target_center", "$current_town"),
        (quest_get_slot, ":quest_target_dna", "qst_bounty_1",
         "slot_quest_target_dna"),
        (call_script, "script_get_name_from_dna_to_s50", ":quest_target_dna"),
        (str_store_string, s4, s50),
    ],
     "I am looking for a fugitive by the name of {s4}. I was told they may be hiding here.",
     "village_elder_ask_fugitive", []],
    [anyone | plyr, "village_elder_talk", [
        (check_quest_active, "qst_bounty_2"),
        (neg | check_quest_concluded, "qst_bounty_2"),
        (quest_slot_eq, "qst_bounty_2", "slot_quest_target_center", "$current_town"),
        (quest_get_slot, ":quest_target_dna", "qst_bounty_2",
         "slot_quest_target_dna"),
        (call_script, "script_get_name_from_dna_to_s50", ":quest_target_dna"),
        (str_store_string, s4, s50),
    ],
     "I am looking for a fugitive by the name of {s4}. I was told they may be hiding here.",
     "village_elder_ask_fugitive", []],

    [anyone | plyr, "village_elder_talk", [
        (check_quest_active, "qst_bounty_3"),
        (neg | check_quest_concluded, "qst_bounty_3"),
        (quest_slot_eq, "qst_bounty_3", "slot_quest_target_center", "$current_town"),
        (quest_get_slot, ":quest_target_dna", "qst_bounty_3",
         "slot_quest_target_dna"),
        (call_script, "script_get_name_from_dna_to_s50", ":quest_target_dna"),
        (str_store_string, s4, s50),
    ],
     "I am looking for a fugitive by the name of {s4}. I was told they may be hiding here.",
     "village_elder_ask_fugitive", []],

    [anyone | plyr, "village_elder_talk", [
        (check_quest_active, "qst_bounty_4"),
        (neg | check_quest_concluded, "qst_bounty_4"),
        (quest_slot_eq, "qst_bounty_4", "slot_quest_target_center", "$current_town"),
        (quest_get_slot, ":quest_target_dna", "qst_bounty_4",
         "slot_quest_target_dna"),
        (call_script, "script_get_name_from_dna_to_s50", ":quest_target_dna"),
        (str_store_string, s4, s50),
    ],
     "I am looking for a fugitive by the name of {s4}. I was told they may be hiding here.",
     "village_elder_ask_fugitive", []],

    [anyone | plyr, "village_elder_talk", [
        (check_quest_active, "qst_bounty_5"),
        (neg | check_quest_concluded, "qst_bounty_5"),
        (quest_slot_eq, "qst_bounty_5", "slot_quest_target_center", "$current_town"),
        (quest_get_slot, ":quest_target_dna", "qst_bounty_5",
         "slot_quest_target_dna"),
        (call_script, "script_get_name_from_dna_to_s50", ":quest_target_dna"),
        (str_store_string, s4, s50),
    ],
     "I am looking for a fugitive by the name of {s4}. I was told they may be hiding here.",
     "village_elder_ask_fugitive", []],

    [anyone | plyr, "village_elder_talk", [
        (check_quest_active, "qst_bounty_6"),
        (neg | check_quest_concluded, "qst_bounty_6"),
        (quest_slot_eq, "qst_bounty_6", "slot_quest_target_center", "$current_town"),
        (quest_get_slot, ":quest_target_dna", "qst_bounty_6",
         "slot_quest_target_dna"),
        (call_script, "script_get_name_from_dna_to_s50", ":quest_target_dna"),
        (str_store_string, s4, s50),
    ],
     "I am looking for a fugitive by the name of {s4}. I was told they may be hiding here.",
     "village_elder_ask_fugitive", []],
    # chief acaba bounty quest

    [anyone, "village_elder_ask_fugitive", [(is_currently_night)],
     "Strangers come and go to our village, {sir/madam}. But I doubt you'll run "
     "into him at this hour of the night. You would have better luck during "
     "the day.", "village_elder_pretalk", []],

    [anyone, "village_elder_ask_fugitive", [],
     "Strangers come and go to our village, {sir/madam}. If he is hiding here, "
     "you will surely find him if you look around.", "close_window", []],
]
