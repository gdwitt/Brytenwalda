from source.header_operations import *
from source.header_common import *

from source.header_dialogs import anyone, plyr

from source.module_constants import villages_begin, villages_end, \
    slot_troop_does_not_give_quest, slot_quest_target_center, slot_quest_target_amount

from source.statement import StatementBlock


quest_block = StatementBlock(
    (eq, ":quest_no", "qst_train_peasants_against_bandits"),
    (try_begin),
        (is_between, ":giver_center_no", villages_begin, villages_end),
        (store_skill_level, ":player_trainer", "skl_trainer", "trp_player"),
        (gt, ":player_trainer", 0),
        (store_random_in_range, ":quest_target_amount", 5, 8),
        (assign, ":quest_target_center", ":giver_center_no"),
        (assign, ":quest_expiration_days", 20),
        (assign, ":quest_dont_give_again_period", 60),  # chief
        (assign, ":result", ":quest_no"),
    (try_end),
)


dialogs = [

    [anyone, "village_elder_tell_mission", [
        (eq, "$random_quest_no", "qst_train_peasants_against_bandits")
    ],
     "We are suffering greatly at the hands of a group of bandits. They take our "
     "food and livestock, and kill anyone who doesn't obey them immediately. "
     "Our men are angry that we cannot defend ourselves, but we are only "
     "simple farmers... However, with some help, I think that some of the "
     "people here could be more than that. We just need an experienced warrior "
     "to teach us how to fight.",
     "village_elder_tell_train_peasants_against_bandits_mission", [
         (quest_get_slot, ":quest_target_center", "$random_quest_no", slot_quest_target_center),
         (str_store_party_name_link, s13, ":quest_target_center"),
         (quest_get_slot, reg5, "$random_quest_no", slot_quest_target_amount),
         (setup_quest_text, "$random_quest_no"),
         (str_store_string, s2, "@The elder of the village of {s13} asked you to train {reg5} peasants to fight against local bandits."),
     ]],

    [anyone | plyr, "village_elder_tell_train_peasants_against_bandits_mission", [],
     "I can teach you how to defend yourself.",
     "village_elder_train_peasants_against_bandits_mission_accept", []],

    [anyone | plyr, "village_elder_tell_train_peasants_against_bandits_mission", [],
     "You peasants have no business taking up arms. Just pay the bandits and be off with it.",
     "village_elder_train_peasants_against_bandits_mission_reject", []],

    [anyone, "village_elder_train_peasants_against_bandits_mission_accept", [],
     "You will? Oh, splendid! We would be deeply indebted to you, {sir/madam}. "
     "I'll instruct the village folk to assemble here and receive your training. "
     "If you can teach us how to defend ourselves, I promise you'll receive "
     "everything we can give you in return for your efforts.", "close_window", [
         (assign, "$g_leave_encounter", 1),
         (call_script, "script_change_player_relation_with_center", "$current_town", 7),
         (call_script, "script_start_quest", "$random_quest_no", "$g_talk_troop"),
     ]],

    [anyone, "village_elder_train_peasants_against_bandits_mission_reject", [],
     "Yes, of course {sir/madam}. Thank you for your counsel.", "close_window", [
         (troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 1)
     ]],
]
