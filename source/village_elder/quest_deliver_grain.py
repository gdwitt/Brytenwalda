from source.header_common import *
from source.header_dialogs import anyone, plyr
from source.module_constants import *
from source.header_operations import *
from source.statement import StatementBlock


quest_block = StatementBlock(
    (eq, ":quest_no", "qst_deliver_grain"),
    (try_begin),
        (is_between, ":giver_center_no", villages_begin, villages_end),
        (call_script, "script_get_troop_item_amount", ":giver_troop", "itm_grain"),
        (eq, reg0, 0),
        (neg | party_slot_ge, ":giver_center_no", slot_town_prosperity, 40),
        (assign, ":quest_target_center", ":giver_center_no"),
        (store_random_in_range, ":quest_target_amount", 4, 8),
        (assign, ":quest_expiration_days", 30),
        (assign, ":quest_dont_give_again_period", 25),
        (assign, ":result", ":quest_no"),
    (try_end),
)


dialogs = [

    [anyone, "village_elder_tell_mission", [
        (eq, "$random_quest_no", "qst_deliver_grain")],
     "{My good sir/My good lady}, our village has been going through such "
     "hardships lately. The harvest has been bad, and recently some merciless "
     "bandits took away our seed grain that we had reserved for the planting "
     "season. If we cannot find some grain soon, we will not be able to plant "
     "our fields and then we will have nothing to eat for the coming year. If "
     "you can help us, we would be indebted to you forever.",
     "village_elder_tell_deliver_grain_mission", [
         (quest_get_slot, ":quest_target_center", "$random_quest_no", slot_quest_target_center),
         (str_store_party_name_link, s3, ":quest_target_center"),
         (quest_get_slot, reg5, "$random_quest_no", slot_quest_target_amount),
         (setup_quest_text, "$random_quest_no"),
         (str_store_string, s2, "@The elder of the village of {s3} asked you "
                                "to bring them {reg5} packs of grain."),
     ]],

    [anyone | plyr, "village_elder_tell_deliver_grain_mission", [],
     "Hmmm. How much grain do you need?",
     "village_elder_tell_deliver_grain_mission_2", []],

    [anyone | plyr, "village_elder_tell_deliver_grain_mission", [],
     "I can't be bothered with this. Ask help from someone else.",
     "village_elder_deliver_grain_mission_reject", []],

    [anyone, "village_elder_tell_deliver_grain_mission_2", [
        (quest_get_slot, reg5, "$random_quest_no", slot_quest_target_amount)],
     "I think {reg5} packs of grain will let us start the planting. Hopefully, "
     "we can find charitable people to help us with the rest.",
     "village_elder_tell_deliver_grain_mission_3", []],

    [anyone | plyr, "village_elder_tell_deliver_grain_mission_3", [],
     "Then I will go and find you the grain you need.",
     "village_elder_deliver_grain_mission_accept", []],

    [anyone | plyr, "village_elder_tell_deliver_grain_mission_3", [],
     "I am afraid I don't have time for this. You'll need to find help elsewhere.",
     "village_elder_deliver_grain_mission_reject", []],

    [anyone, "village_elder_deliver_grain_mission_accept", [],
     "Thank you, {sir/madam}. We'll be praying for you night and day.",
     "close_window", [
         (assign, "$g_leave_encounter", 1),
         (call_script, "script_change_player_relation_with_center", "$current_town", 5),
         (call_script, "script_start_quest", "$random_quest_no", "$g_talk_troop"),
     ]],

    [anyone, "village_elder_deliver_grain_mission_reject", [],
     "Yes {sir/madam}, of course. I am sorry if I have bothered you with our troubles.",
     "close_window", [
         (troop_set_slot, "$g_talk_troop", slot_troop_does_not_give_quest, 1)
     ]],

    [anyone | plyr, "village_elder_active_mission_2", [
        (store_partner_quest, ":elder_quest"),
        (eq, ":elder_quest", "qst_deliver_grain"),
        (quest_get_slot, ":quest_target_amount", "qst_deliver_grain",
         slot_quest_target_amount),
        (call_script, "script_get_troop_item_amount", "trp_player", "itm_grain"),
        (assign, ":cur_amount", reg0),
        (ge, ":cur_amount", ":quest_target_amount"),
        (assign, reg5, ":quest_target_amount"),
    ], "Indeed. I brought you {reg5} packs of grain.",
     "village_elder_deliver_grain_thank", []
     ],

    [anyone, "village_elder_deliver_grain_thank", [
        (str_store_party_name, s13, "$current_town")],
     "My good {lord/lady}. You have saved us from hunger and desperation. We "
     "cannot thank you enough, but you'll always be in our prayers. The village "
     "of {s13} will not forget what you have done for us.",
     "village_elder_deliver_grain_thank_2", [

         (quest_get_slot, ":quest_target_amount", "qst_deliver_grain", slot_quest_target_amount),
         (troop_remove_items, "trp_player", "itm_grain", ":quest_target_amount"),
         (add_xp_as_reward, 350),  # gdw400
         (call_script, "script_change_center_prosperity", "$current_town", 4),
         (call_script, "script_change_player_relation_with_center", "$current_town", 5),
         (call_script, "script_end_quest", "qst_deliver_grain"),
         (call_script, "script_add_log_entry", logent_helped_peasants, "trp_player", "$current_town", -1, -1),
     ]],

    [anyone, "village_elder_deliver_grain_thank_2", [],
     "My good {lord/lady}, please, is there anything I can do for you?",
     "village_elder_talk", []],
]
