from source.header_dialogs import anyone, plyr, auto_proceed, party_tpl
from source.header_operations import *
from source.header_parties import *
from source.module_constants import *
from source.lazy_flag import LazyFlag


dialogs = [
    [anyone | plyr, "village_elder_talk", [
        (eq, "$g_talk_troop", "trp_village_66_elder"),
        (check_quest_active, "qst_talk_to_zamoshie_elder"),
        (neg | check_quest_finished, "qst_talk_to_zamoshie_elder")
    ],
     "May your days be long, father. Tell me -- what is happening around here?",
     "oim_intro_zamoshie_elder", [
         (call_script, "script_end_quest", "qst_talk_to_zamoshie_elder"),
         (call_script, "script_change_player_relation_with_faction", "fac_kingdom_15", 1),
     ]],

    [anyone | plyr, "village_elder_talk", [
        (eq, "$g_talk_troop", "trp_village_66_elder"),
        (check_quest_succeeded, "qst_deal_with_zamoshie_bandits"),
        (neg | check_quest_finished, "qst_deal_with_zamoshie_bandits")
    ], "I come to talk about the bandits...", "oim_zamoshie_killed_bandits", []
     ],

    [anyone | plyr, "village_elder_talk", [
        (eq, "$g_talk_troop", "trp_village_66_elder"),
        (check_quest_succeeded, "qst_zamoshie_lower_taxes"),
        (neg | check_quest_finished, "qst_zamoshie_lower_taxes"), ],
     "I come to talk about the taxes...", "oim_zamoshie_lower_taxes_done", []],

    [anyone | plyr, "village_elder_talk", [
        (eq, "$g_talk_troop", "trp_village_66_elder"),
        (check_quest_active, "qst_oim_bring_goods_zamoshie"),
        (neg | check_quest_finished, "qst_oim_bring_goods_zamoshie"), ],
     "I come to talk about the goods...", "oim_check_bring_goods", []],

    [anyone | plyr, "village_elder_talk", [
        (eq, "$g_talk_troop", "trp_village_66_elder"),
        (check_quest_finished, "qst_talk_to_zamoshie_elder"), ],
     "Perhaps I could offer more aid?", "oim_choose_quests", []],

    ['trp_village_66_elder', "oim_intro_zamoshie_elder", [],
     "Well, hello there... When I was young, we were free men who fought for our "
     "right to farm without taxes. They called me Will Stutely.",
     "oim_intro_zamoshie_elder_1", []
     ],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_intro_zamoshie_elder_1", [],
     "And do you have some work for me? Something that will give me a chance "
     "to swing my sword, win myself some glory - and fill my purse! It's a "
     "little too empty at the moment...",
     "oim_intro_zamoshie_elder_4", []
     ],

    ['trp_village_66_elder', "oim_intro_zamoshie_elder_4", [],
     "Aye, there is always work for a daring soul but I have no coin left. "
     "Believe it or not, the Brythonic lords of Rheged just sit in their halls "
     "waiting for some enemy army huddling in their towns, too afraid to stick "
     "their noses out of the gates. Meanwhile, bandits roam the roads giving "
     "travelers and merchants no peace... We can't even travel to the town due "
     "to fear of it being overtaken! And to make matters worse, our warlord "
     "taxes us so heavily that we have nothing for ourselves, and soon "
     "starvation is unavoidable...",
     "oim_intro_zamoshie_elder_5", []
     ],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_intro_zamoshie_elder_5", [
        (neg | check_quest_active, "qst_deal_with_zamoshie_bandits"),
        (neg | check_quest_finished, "qst_deal_with_zamoshie_bandits"),
    ], "Find and wipe out the bandits.", "oim_intro_kill_bandits_start", []],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_intro_zamoshie_elder_5", [
        (neg | check_quest_active, "qst_zamoshie_lower_taxes"),
        (neg | check_quest_finished, "qst_zamoshie_lower_taxes"),
    ], "Persuade the warlord to lower taxes.", "oim_intro_taxes_lower", []],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_intro_zamoshie_elder_5", [
        (neg | check_quest_active, "qst_oim_bring_goods_zamoshie"),
        (neg | check_quest_finished, "qst_oim_bring_goods_zamoshie"),
    ], "Bring in some goods.", "oim_bring_goods_in_zamoshie_intro", []],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_intro_zamoshie_elder_5", [],
     "Leave...", "close_window", []],

    ['trp_village_66_elder', "oim_intro_kill_bandits_start", [],
     "Bandits have settled in the forest nearby, and set out to plunder us "
     "each day. They are many and have stolen some of my best bows. Our peasants "
     "are not trained for battle...",
     "oim_intro_kill_bandits_dialog", []
     ],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_intro_kill_bandits_dialog", [],
     "Agree...", "oim_intro_kill_bandits_dialog_start_quest", []],

    [LazyFlag('trp_village_66_elder') | plyr,
     "oim_intro_kill_bandits_dialog_start_quest", [],
     "Bandits? Sounds like my kind of work! Tell me how I can find them.",
     "oim_intro_kill_bandits_dialog_start_quest_1", []],

    ['trp_village_66_elder', "oim_intro_kill_bandits_dialog_start_quest_1", [],
     "They are lurking in the forest right past the village. Go and defeat "
     "the bastards... We'll reward you well.",
     "close_window", [
         # code starting bandits quest
         (setup_quest_text, "qst_deal_with_zamoshie_bandits"),
         (str_store_string, s4,
          "@Pyr the Elder has asked you to deal with the forest bandits north of Llan Forfael"),
         #   #(call_script, "script_start_quest", "qst_deal_with_zamoshie_bandits", "$g_talk_troop"),
         (start_quest, "qst_deal_with_zamoshie_bandits"), (quest_set_slot, "qst_deal_with_zamoshie_bandits", slot_quest_current_state, 1),
         # (set_spawn_radius, 3),
         # (spawn_around_party,"p_village_88","pt_neko"),
         # (assign, ":qst_neko_party", reg0),
         # (quest_set_slot, "qst_mod_trouble", slot_quest_target_party, ":qst_neko_party"),
         # #(quest_set_slot, "qst_mod_trouble", slot_quest_xp_reward, 1000),
         # (party_set_ai_behavior, ":qst_neko_party", ai_bhvr_hold),
         # (party_set_flags, ":qst_neko_party", pf_default_behavior, 0),
         # (party_set_ai_object, ":qst_neko_party", "p_main_party"),
         # (party_get_position, pos0, "p_town_41"),
         # (party_set_ai_patrol_radius, ":qst_neko_party", 0),
         # (str_store_troop_name, s9, "trp_hareck"),
         #   (setup_quest_text, "qst_mod_trouble",),
         #   (str_store_string, s2, "@{s9} has asked you to deal with the plundering band of Cantabrians"),
         #   #(call_script, "script_start_quest", "qst_deal_with_zamoshie_bandits", "$g_talk_troop"),
         # (remove_troop_from_site,"trp_npcneko","scn_town_41_tavern")
         # (party_set_ai_target_position, "pt_eadfrith", pos0),]],
         (set_spawn_radius, 2),
         (quest_get_slot, ":quest_target_center", "qst_deal_with_zamoshie_bandits", slot_quest_target_center),
         (spawn_around_party, ":quest_target_center", "pt_zamoshie_bandits"),
         (assign, ":quest_target_party", reg0),
         (quest_set_slot, "qst_deal_with_zamoshie_bandits", slot_quest_target_party, ":quest_target_party"),
         (quest_set_slot, "qst_deal_with_zamoshie_bandits", slot_quest_xp_reward, 600),
         (quest_set_slot, "qst_deal_with_zamoshie_bandits", slot_quest_gold_reward, 100),
         (quest_set_slot, "qst_deal_with_zamoshie_bandits", slot_quest_current_state, 0),
         (quest_set_slot, "qst_deal_with_zamoshie_bandits", slot_quest_giver_troop, "$g_talk_troop"),
         (party_set_ai_behavior, ":quest_target_party", ai_bhvr_hold),
         (party_set_ai_object, ":quest_target_party", "p_main_party"),

         (party_set_flags, ":quest_target_party", pf_default_behavior, 0),
         # (str_store_troop_name, s9, "$g_talk_troop"),
         # (setup_quest_text, "qst_deal_with_zamoshie_bandits"),
         # (str_store_string, s2, "@The elder {s9} asked you to deal with bandits"),
         # (call_script, "script_start_quest", "qst_deal_with_zamoshie_bandits", "$g_talk_troop"),
     ]],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_intro_kill_bandits_dialog", [],
     "Refuse...", "oim_intro_kill_bandits_dialog_refuge", []
     ],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_intro_kill_bandits_dialog_refuge", [],
     "I have urgent business elsewhere, so I'm afraid I cannot help.",
     "oim_intro_kill_bandits_dialog_refuge_1", []
     ],

    ['trp_village_66_elder', "oim_intro_kill_bandits_dialog_refuge_1", [],
     "Very well then... We shall just have to search for another who might "
     "protect us. What else can we do?",
     "oim_intro_zamoshie_elder_5", []
     ],

    # start quest kill bandits
    [party_tpl | LazyFlag("pt_zamoshie_bandits") | auto_proceed, "start", [],
     "{!}NOT SHOWN", "zamoshien_badits_dialog_prebattle_1", []
     ],

    [anyone, "zamoshien_badits_dialog_prebattle_1", [],
     "Well met! It has been a long time since we've seen an interesting "
     "personage. What brings you here, toad?",
     "zamoshien_badits_dialog_prebattle_2", []],

    [anyone | plyr, "zamoshien_badits_dialog_prebattle_2", [],
     "You speak with an eloquent tongue... I would presume you fight just as "
     "well? I am on the hunt for some local bandits - perhaps that would be you?",
     "zamoshien_badits_dialog_prebattle_3", []],

    [anyone, "zamoshien_badits_dialog_prebattle_3", [],
     "We are no bandits, but fair and upright forest brothers. We do for "
     "ourselves the best we can, rob from the rich, and give to the poor - and "
     "take but a token share for ourselves, as reward for our daring feats of arms.",
     "zamoshien_badits_dialog_prebattle_4", []],

    [anyone | plyr, "zamoshien_badits_dialog_prebattle_4", [],
     "That's strange... According to the local villagers, it is you who are "
     "taking from the poor even their last pittance. This seems far from noble "
     "to me... And they have asked of me to put an end to this disgraceful "
     "situation.",
     "zamoshien_badits_dialog_prebattle_5", [
         (quest_set_slot, "qst_deal_with_zamoshie_bandits", slot_quest_current_state, 1),
         (call_script, "script_succeed_quest", "qst_deal_with_zamoshie_bandits")]
     ],

    [anyone, "zamoshien_badits_dialog_prebattle_5",
     [(party_set_ai_object, "pt_zamoshie_bandits", "p_village_66"),
      (party_set_ai_behavior, "pt_zamoshie_bandits", ai_bhvr_travel_to_party), ],
     "Strange business this. Some nameless passer-by dares to slander us. I "
     "like that sword. It will look better with your blood on it!",
     "close_window", [(encounter_attack)]
     ],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_zamoshie_killed_bandits", [],
     "Hello again my good man - the bandits are done for. They shall pester you "
     "no more. Do you remember your promise?", "oim_zamoshie_killed_bandits_1", []
     ],

    ['trp_village_66_elder', "oim_zamoshie_killed_bandits_1", [],
     "Of course, how could I forget? We are poor and starving. But I have this "
     "weapon from youth you could use. And thank you for your help!",
     "oim_zamoshie_killed_bandits_2", [
         #  insert code quest reward
         # (call_script, "script_troop_add_gold", "trp_player", 5),#100gdw
         (troop_add_item, "trp_player", "itm_khergit_bowreserv", 0),
         # gdw special set up in item_kinds for yeoman bow
         (add_xp_as_reward, 350),
         (call_script, "script_change_player_relation_with_center", "$current_town", 5),
         (call_script, "script_change_player_relation_with_faction", "fac_kingdom_15", 2),
         (call_script, "script_end_quest", "qst_deal_with_zamoshie_bandits"),
     ]],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_zamoshie_killed_bandits_2", [],
     "Perhaps I could offer you further aid?", "oim_choose_quests", []],

    # choose quests. Experimental
    [LazyFlag('trp_village_66_elder') | auto_proceed, "oim_choose_quests", [
        (assign, ":result", 0),
        (try_begin),
            (neg | check_quest_active, "qst_deal_with_zamoshie_bandits"),
            (neg | check_quest_finished, "qst_deal_with_zamoshie_bandits"),
            (val_add, ":result", 1),
        (end_try),
        (try_begin),
            (neg | check_quest_active, "qst_zamoshie_lower_taxes"),
            (neg | check_quest_finished, "qst_zamoshie_lower_taxes"),
            (val_add, ":result", 1),
        (end_try),
        (try_begin),
            (neg | check_quest_active, "qst_oim_bring_goods_zamoshie"),
            (neg | check_quest_finished, "qst_oim_bring_goods_zamoshie"),
            (val_add, ":result", 1),
        (end_try),
        (eq, ":result", 0),
    ], "{!}NOT SHOWN", "oim_help_to_find_icon", []],

    ['trp_village_66_elder', "oim_choose_quests", [], "Well...",
     "oim_choose_quests_answer", []],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_choose_quests_answer", [
        (neg | check_quest_active, "qst_deal_with_zamoshie_bandits"),
        (neg | check_quest_finished, "qst_deal_with_zamoshie_bandits"),
    ], "Find and wipe out the bandits.", "oim_intro_kill_bandits_start", []],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_choose_quests_answer", [
        (neg | check_quest_active, "qst_zamoshie_lower_taxes"),
        (neg | check_quest_finished, "qst_zamoshie_lower_taxes"),
    ], "Persuade your warlord to lower the taxes.", "oim_intro_taxes_lower", []],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_choose_quests_answer", [
        (neg | check_quest_active, "qst_oim_bring_goods_zamoshie"),
        (neg | check_quest_finished, "qst_oim_bring_goods_zamoshie"),
    ], "Bring in some goods.", "oim_bring_goods_in_zamoshie_intro", []],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_choose_quests_answer", [],
     "Return...", "village_elder_pretalk", []],

    ['trp_village_66_elder', "oim_help_to_find_icon", [],
     "Thank you, my friend. We have no other needs.", "village_elder_pretalk", []],

    ['trp_village_66_elder', "oim_intro_taxes_lower", [],
     "There is one more thing... Our lord, I think he is in Caer Ligualid now, "
     "has set the taxes so high that we cannot bear it! Our very survival is "
     "at stake! We thought of sending humble messengers to him, but we are too "
     "frightened... And the roads are far too perilous. Come to our aid, good "
     "{man/lady}. Talk to the lord, and beg him to lower our taxes.",
     "oim_intro_taxes_lower_1", []
     ],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_intro_taxes_lower_1", [],
     "Agree...", "oim_intro_taxes_lower_agree", []],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_intro_taxes_lower_agree", [],
     "I could speak to him on your behalf, surely... But I arrived not long ago in these lands. I know no one, and no one can stand by my word but I alone. To persuade the warlord would be no easy task...",
     "close_window", [
         # code to start quest

         (quest_set_slot, "qst_zamoshie_lower_taxes", slot_quest_target_troop, "trp_knight_15_3"),
         (quest_set_slot, "qst_zamoshie_lower_taxes", slot_quest_target_party, "trp_knight_15_3"),
         (quest_set_slot, "qst_zamoshie_lower_taxes", slot_quest_xp_reward, 100),
         (quest_set_slot, "qst_zamoshie_lower_taxes", slot_quest_gold_reward, 10),
         (quest_set_slot, "qst_zamoshie_lower_taxes", slot_quest_current_state, 0),
         (quest_set_slot, "qst_zamoshie_lower_taxes", slot_quest_target_amount, 200),
         (quest_set_slot, "qst_zamoshie_lower_taxes", slot_quest_giver_troop, "trp_village_66_elder"),
         (str_store_troop_name, s9, "$g_talk_troop"),
         (str_store_troop_name_link, s10, "trp_knight_15_3"),
         (setup_quest_text, "qst_zamoshie_lower_taxes"),
         (str_store_string, s2, "@{s9} asked you to {s10} to lower taxes"),
         (call_script, "script_start_quest", "qst_zamoshie_lower_taxes", "$g_talk_troop"),
     ]],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_intro_taxes_lower_1", [],
     "Refuse...", "oim_choose_quests_disagree", []],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_choose_quests_disagree", [],
     "I am but a passer-by in these lands... It is no business of mine to "
     "petition the ruler on behalf of his serfs. You shall have to find another "
     "to run this errand for you.", "oim_choose_quests_disagree_1", []],

    ['trp_village_66_elder', "oim_choose_quests_disagree_1", [],
     "Well, I have my answer then. But know this - one cannot live by the "
     "sword alone... You would be wise to master the art of speech as well. "
     "Otherwise you will not be worth the soil you stand upon.",
     "close_window", []],
]

dialogs += [

    [LazyFlag('trp_village_66_elder') | plyr, "oim_zamoshie_lower_taxes_done", [],
     "I spoke to the warlord. Your tax debts are forgiven. You may rejoice!",
     "oim_zamoshie_lower_taxes_done_1", []],

    ['trp_village_66_elder', "oim_zamoshie_lower_taxes_done_1", [],
     "I bow low before you, my good {man/lady}. You have saved us from eviction "
     "or death. Here, take this bow as a reward for all your help.",
     "oim_zamoshie_lower_taxes_done_2", [
         # insert code for reward
         (troop_add_item, "trp_player", "itm_khergit_bowreserv", 0),
         # gdw special set up in item_kinds for yeoman bow
         (add_xp_as_reward, 150),
         (call_script, "script_change_player_relation_with_center", "$current_town", 6),
         (call_script, "script_end_quest", "qst_zamoshie_lower_taxes"),
         (call_script, "script_change_player_relation_with_faction", "fac_kingdom_15", 1),
     ]],

    [LazyFlag('trp_village_66_elder') | plyr, "oim_zamoshie_lower_taxes_done_2",
     [], "If there is anything else I can do, please tell me.",
     "oim_choose_quests", []],

    # start intro of quest "oim_bring_goods_in_zamoshie"
    ['trp_village_66_elder', "oim_bring_goods_in_zamoshie_intro", [],
     "As you well know, master, there is war in these lands... Traders no "
     "longer pass through the villages with their goods. We must go buy "
     "everything at the town market. But our people fear the road to town - "
     "the journey is too dangerous. If you bring us three sets of tools we "
     "would be grateful.",
     "oim_bring_goods_in_zamoshie_intro_answer", []],

    [LazyFlag('trp_village_66_elder') | plyr,
     "oim_bring_goods_in_zamoshie_intro_answer", [], "Agree...",
     "oim_bring_goods_in_zamoshie_intro_answer_ok", []],

    [LazyFlag('trp_village_66_elder') | plyr,
     "oim_bring_goods_in_zamoshie_intro_answer_ok", [],
     "So be it. I shall deliver you the goods, and perhaps I shall learn a bit about trading myself!",
     "village_elder_talk", [
         # code to start quest deliver goods zamoshie village
         (quest_set_slot, "qst_oim_bring_goods_zamoshie", slot_quest_xp_reward, 250),
         # (quest_set_slot, "qst_oim_bring_goods_zamoshie", slot_quest_gold_reward, 50),#gdw gets arrows instead
         (quest_set_slot, "qst_oim_bring_goods_zamoshie", slot_quest_current_state, 0),
         (quest_set_slot, "qst_oim_bring_goods_zamoshie", slot_quest_giver_troop, "$g_talk_troop"),
         (str_store_troop_name, s9, "$g_talk_troop"),
         (str_store_item_name, s10, "itm_tools"),
         (setup_quest_text, "qst_oim_bring_goods_zamoshie"),
         (str_store_string, s2, "@{s9} asked you to bring {s10}"),
         (call_script, "script_start_quest", "qst_oim_bring_goods_zamoshie",
          "$g_talk_troop"),
     ]],

    [LazyFlag('trp_village_66_elder') | plyr,
     "oim_bring_goods_in_zamoshie_intro_answer", [], "Refuse...",
     "oim_bring_goods_in_zamoshie_intro_answer_net", []
     ],

    [LazyFlag('trp_village_66_elder') | plyr,
     "oim_bring_goods_in_zamoshie_intro_answer_net", [],
     "I have dedicated myself to the bow-making. I have scarce time to drive a "
     "merchant's cart.",
     "oim_bring_goods_in_zamoshie_intro_answer_net_1", []
     ],

    ['trp_village_66_elder', "oim_bring_goods_in_zamoshie_intro_answer_net_1", [],
     "'Tis a poor refusal you make, {sir/madam}. 'Tis no disgrace for a good "
     "warrior to learn the craft of trading. And no merchant would last long "
     "in these lands, were he not a little skilled at holding a sword.",
     "oim_choose_quests", []
     ],

    [anyone, "oim_check_bring_goods",
     [(store_item_kind_count, ":item_count", "itm_tools"),
      (ge, ":item_count", 3), ],
     "I am so happy. Accept these prize arrows as my gift.", "village_elder_talk", [
         (troop_remove_item, "trp_player", "itm_tools"),
         (troop_remove_item, "trp_player", "itm_tools"),
         (troop_remove_item, "trp_player", "itm_tools"),
         # (call_script, "script_troop_add_gold", "trp_player", 100),
         (troop_add_item, "trp_player", "itm_barbed_arrows", 0),
         # gdw special set up in item_kinds for yeoman bow
         (add_xp_as_reward, 300),
         (call_script, "script_change_player_relation_with_center", "$current_town", 5),
         (call_script, "script_end_quest", "qst_oim_bring_goods_zamoshie"),
         (call_script, "script_change_player_relation_with_faction", "fac_kingdom_15", 1),
     ]],

    [anyone, "oim_check_bring_goods",
     [(store_item_kind_count, ":item_count", "itm_tools"),
      (lt, ":item_count", 3), ],
     "Alas, this meets but part of our needs. Deliver all the goods, and we "
     "shall pay you the full amount of your reward.",
     "close_window", []],
]
