from source.header_common import *
from source.header_dialogs import anyone, plyr
from source.module_constants import *
from source.header_operations import *
from source.statement import StatementBlock


quest_block = StatementBlock(
    (eq, ":quest_no", "qst_deliver_cattle"),
    (try_begin),
        (is_between, ":giver_center_no", villages_begin, villages_end),
        (party_get_slot, ":num_cattle", ":giver_center_no", slot_village_number_of_cattle),
        (lt, ":num_cattle", 50),
        (assign, ":quest_target_center", ":giver_center_no"),
        (store_random_in_range, ":quest_target_amount", 5, 10),
        (assign, ":quest_expiration_days", 30),
        (assign, ":quest_dont_give_again_period", 25),  # chief gdw
        (assign, ":result", ":quest_no"),
    (try_end),
)


dialogs = [

    [anyone, "village_elder_tell_mission",
     [(eq, "$random_quest_no", "qst_deliver_cattle")],
     "Bandits have driven away our cattle. Our pastures are empty. If we had "
     "just a few heads of cattle we could start to raise a herd again.",
     "village_elder_tell_deliver_cattle_mission", [
         (quest_get_slot, ":quest_target_center", "$random_quest_no", slot_quest_target_center),
         (str_store_party_name_link, s3, ":quest_target_center"),
         (quest_get_slot, reg5, "$random_quest_no", slot_quest_target_amount),
         (setup_quest_text, "$random_quest_no"),
         (str_store_string, s2, "@The elder of the village of {s3} asked you to "
                                "bring them {reg5} heads of cattle."),
     ]],

    [anyone | plyr, "village_elder_tell_deliver_cattle_mission", [],
     "How many animals do you need?",
     "village_elder_tell_deliver_cattle_mission_2", []],

    [anyone | plyr, "village_elder_tell_deliver_cattle_mission", [],
     "I don't have time for this. Ask help from someone else.",
     "village_elder_deliver_cattle_mission_reject", []],

    [anyone, "village_elder_tell_deliver_cattle_mission_2",
     [(quest_get_slot, reg5, "$random_quest_no", slot_quest_target_amount)],
     "I think {reg5} heads will suffice for a small herd.",
     "village_elder_tell_deliver_cattle_mission_3", []],

    [anyone | plyr, "village_elder_tell_deliver_cattle_mission_3", [],
     "Then I will bring you the cattle you need.",
     "village_elder_deliver_cattle_mission_accept", []],

    [anyone | plyr, "village_elder_tell_deliver_cattle_mission_3", [],
     "I am afraid I don't have time for this. You'll need to find help elsewhere.",
     "village_elder_deliver_cattle_mission_reject", []],

    [anyone, "village_elder_deliver_cattle_mission_accept", [],
     "Thank you, {sir/madam}. We'll be praying for you night and day.",
     "close_window", [
        (assign, "$g_leave_encounter", 1),
        (call_script, "script_change_player_relation_with_center", "$current_town", 3),
        (call_script, "script_start_quest", "$random_quest_no", "$g_talk_troop"),
      ]],

    [anyone, "village_elder_deliver_cattle_mission_reject", [],
     "Yes {sir/madam}, of course. I am sorry if I have bothered you with our "
     "troubles.", "close_window", [
        (troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 1),
      ]],
]


dialogs += [
    [anyone, "start", [
        (is_between, "$g_talk_troop", village_elders_begin, village_elders_end),
        (store_partner_quest, ":elder_quest"),
        (eq, ":elder_quest", "qst_deliver_cattle"),
        (check_quest_succeeded, ":elder_quest"),
        (quest_get_slot, reg5, "qst_deliver_cattle", slot_quest_target_amount)],
     "My good {sir/madam}. Our village is grateful for your help. Thanks to "
     "the {reg5} heads of cattle you have brought, we can now raise our own herd.",
     "village_elder_deliver_cattle_thank", [
        (add_xp_as_reward, 400),

        (call_script, "script_change_center_prosperity", "$current_town", 4),
        (call_script, "script_change_player_relation_with_center", "$current_town", 7),
        (call_script, "script_end_quest", "qst_deliver_cattle"),
        (call_script, "script_add_log_entry", logent_helped_peasants, "trp_player", "$current_town", -1, -1),
      ]],

    [anyone, "village_elder_deliver_cattle_thank", [],
     "My good {lord/lady}, please, is there anything I can do for you?",
     "village_elder_talk", []],
]
