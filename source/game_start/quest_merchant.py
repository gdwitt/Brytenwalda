from source.header_dialogs import anyone, plyr, auto_proceed
from source.header_parties import ai_bhvr_patrol_location
from ..header_game_menus import *
from ..header_items import *
from ..module_constants import *


menus = [
    # todo: if in modding mode, allow jumping directly to map.
    ("start_phase_2", mnf_disable_all_keys,
     "...Anno Domini 636...\
 ^The world is at war and respects only the law of the sword and spear. Realms are born and die every single day. Kings die on the battlefield.\
 ^In the north and east, the Angles consolidate domains and claim more land. Oswald, the new lord of the north, now rules Bernacia, Deira and Elmet.\
 ^In the south, the Saxons, led by Cynegils, have teamed up with Oswald and cornered Penda, King of the Angles of Mierce, The March. Will Mierce resist being surrounded by enemies? King Penda is bloody and violent -- many kings have been killed by his sword, and it seems his sword will kill many more.\
 ^Meanwhile, Christianity is extending out from Centware, land of the Jutes, converting the barbarians.\
 ^Pushed against the coast, the Welsh are fighting for every inch of land, but they are too divided. Dreaming of a king to unify them all and lead them to final victory, they wish for the return of King Arthur. But Arthur is dead, and all eyes look to Cynddylan, the king of Pengwern.\
 ^ And Gwynedd, the kingdom fertile with great warriors, is silent, unable to hear the sound of the armies advancing to threaten their land. Gwynedd mourns great king Cadwallon, scourge of the Angles and Saxons, who has left a son, a king three year old.\
 ^In the snowy lands of the far north fight the Irish, Dal Riata, and the Picts. Their kings share blood, but the Irish are invading the land of Cait, the Kingdom of the Picts. The Picts, with their faces painted and their female warriors, are now united under one king and are stronger than ever.\
 ^Across the sea, in Ireland, Domnaill mac Aedo of Ui Neill clan has emerged as High King in Temair after defeating his enemies, but it is nothing more than a prestigious title. Although he is called the most powerful of the island, around him clans are fighting for land, women and cattle in fratricidal wars. War in Ireland is endemic.\
 ^Who can bring light to this world of war and misery? The world was chaos, and chaos was war.\
 ^This is... BRYTENWALDA.",
     "none", [
         (set_background_mesh, "mesh_pic_extra_barco")
        ], [

        ("debug_option", [
            (eq, "$debug_game_mode", 1)
            ], "[Debug mode] Start game without merchant quest.", [
            (change_screen_return, 0),
        ]),

         ("town_1", [(eq, "$current_startup_quest_phase", 0),
                     (is_between, "$character_nationality", 13, 19),
                     # Pict      or Briton
                     ],
          "I need go to Alt Clut, in the Briton Kingdom of Alt Clut.",
          [
              (assign, "$current_town", "p_town_6"),
              (assign, "$g_starting_town", "$current_town"),
              (assign, "$g_journey_string", "str_journey_to_praven"),
              (jump_to_menu, "mnu_start_phase_2_5"),
          ]),

         ("town_2", [(eq, "$current_startup_quest_phase", 0),
                     (neg | is_between, "$character_nationality", 13, 22),
                     # NOT Pict or Briton or Irish
                     ],
          "I need go to Grantebrycge, in the Angle Kingdom of the East Englas",
          [
              (assign, "$current_town", "p_town_8"),
              (assign, "$g_starting_town", "$current_town"),
              (assign, "$g_journey_string", "str_journey_to_reyvadin"),
              (jump_to_menu, "mnu_start_phase_2_5"),
          ]),

         ("town_3", [(eq, "$current_startup_quest_phase", 0),
                     (is_between, "$character_nationality", 16, 19),
                     # Briton
                     ],
          "I need go to Din Gonwy, in the Briton kingdom of Gwynedd.",
          [
              (assign, "$current_town", "p_town_13"),
              (assign, "$g_starting_town", "$current_town"),
              (assign, "$g_journey_string", "str_journey_to_tulga"),
              (jump_to_menu, "mnu_start_phase_2_5"),
          ]),

         ("town_4", [(eq, "$current_startup_quest_phase", 0),
                     (neg | is_between, "$character_nationality", 13, 22),
                     # NOT Pict or Briton or Irish
                     ],
          "I need go to Cantwaraburh, in the Christian Kingdom of Centware.",
          [
              (assign, "$current_town", "p_town_1"),
              (assign, "$g_starting_town", "$current_town"),
              (assign, "$g_journey_string", "str_journey_to_sargoth"),
              (jump_to_menu, "mnu_start_phase_2_5"),
          ]),

         ("town_5", [(eq, "$current_startup_quest_phase", 0),
                     (is_between, "$character_nationality", 19, 22),  # Irish
                     ],
          "I need go to Clochair, in the Irish Kingdom of Airgialla.",
          [
              (assign, "$current_town", "p_town_40"),
              (assign, "$g_starting_town", "$current_town"),
              (assign, "$g_journey_string", "str_journey_to_jelkala"),
              (jump_to_menu, "mnu_start_phase_2_5"),
          ]),

         ("town_6", [(eq, "$current_startup_quest_phase", 0),
                     (is_between, "$character_nationality", 19, 22),
                     # Irish
                     ],
          "I need go to Dun Iasgach, in the Irish kingdom of Mumain.",
          [
              (assign, "$current_town", "p_town_35"),
              (assign, "$g_starting_town", "$current_town"),
              (assign, "$g_journey_string", "str_journey_to_shariz"),
              (jump_to_menu, "mnu_start_phase_2_5"),
          ]),
     ]),

    ("start_phase_2_5", mnf_disable_all_keys, "{!}{s16}", "none", [
        (str_store_party_name, s1, "$g_starting_town"),
        (str_store_string, s16, "$g_journey_string"),
        (set_background_mesh, "mesh_pic_extra_barco"),
    ], [
         ("continue", [], "Continue...", [(jump_to_menu, "mnu_start_phase_3")]),
     ]),

    ("start_phase_3", mnf_disable_all_keys,
     "{s16}^^You are exhausted by the time you find the inn in {s1}, and fall "
     "asleep quickly. However, you awake before dawn and are eager to explore "
     "your surroundings. You venture out onto the streets, which are still "
     "deserted. All of a sudden, you hear a sound that stands the hairs of your "
     "neck on end -- the rasp of a blade sliding from its scabbard...", "none", [
         (set_background_mesh, "mesh_pic_extra_malvado"),
         (assign, ":continue", 1),
         (try_begin),
             (eq, "$current_startup_quest_phase", 1),
             (try_begin),
                 (eq, "$g_killed_first_bandit", 1),
                 (str_store_string, s11, "str_killed_bandit_at_alley_fight"),
             (else_try),
                 (str_store_string, s11, "str_wounded_by_bandit_at_alley_fight"),
             (try_end),
             (jump_to_menu, "mnu_start_phase_4"),
             (assign, ":continue", 0),
         (else_try),
             (eq, "$current_startup_quest_phase", 3),
         (try_begin),
             (eq, "$g_killed_first_bandit", 1),
             (str_store_string, s11, "str_killed_bandit_at_alley_fight"),
         (else_try),
            (str_store_string, s11, "str_wounded_by_bandit_at_alley_fight"),
         (try_end),
             (jump_to_menu, "mnu_start_phase_4"),
             (assign, ":continue", 0),
         (try_end),

         (str_store_party_name, s1, "$g_starting_town"),
         (str_clear, s16),
         (eq, ":continue", 1),
     ], [
         # scene where the player fights alone in an alley
         ("continue", [], "Continue...", [
              (assign, "$g_starting_town", "$current_town"),

              (party_set_morale, "p_main_party", 100),
              (set_encountered_party, "$current_town"),
              (call_script, "script_prepare_alley_to_fight"),
          ]),
     ]),

    ("start_phase_4", mnf_disable_all_keys, "{s11}", "none", [
        (assign, ":continue", 1),
        (try_begin),
            (eq, "$current_startup_quest_phase", 2),
            (change_screen_return),
            (assign, ":continue", 0),
        (else_try),
            (eq, "$current_startup_quest_phase", 3),
            (str_store_string, s11, "str_merchant_and_you_call_some_townsmen_and_guards_to_get_ready_and_you_get_out_from_tavern"),
        (else_try),
            (eq, "$current_startup_quest_phase", 4),
            (try_begin),
                (eq, "$g_killed_first_bandit", 1),
                (str_store_string, s11, "str_town_fight_ended_you_and_citizens_cleaned_town_from_bandits"),
            (else_try),
               (str_store_string, s11, "str_town_fight_ended_you_and_citizens_cleaned_town_from_bandits_you_wounded"),
            (try_end),
        (try_end),

        (eq, ":continue", 1),
    ], [
         # scene where the player appears inside the merchant house
         ("continue", [
             (this_or_next | eq, "$current_startup_quest_phase", 1),
             (eq, "$current_startup_quest_phase", 4),
         ], "Continue...", [
              (assign, "$town_entered", 1),

              (try_begin),
                  (eq, "$current_town", "p_town_1"),
                  (assign, ":town_merchant", "trp_pict_merchant"),
                  (assign, ":town_room_scene", "scn_town_1_room"),
              (else_try),
                  (eq, "$current_town", "p_town_13"),
                  (assign, ":town_merchant", "trp_engle_merchant"),
                  (assign, ":town_room_scene", "scn_town_5_room"),
              (else_try),
                  (eq, "$current_town", "p_town_6"),
                  (assign, ":town_merchant", "trp_briton_merchant"),
                  (assign, ":town_room_scene", "scn_town_6_room"),
              (else_try),
                  (eq, "$current_town", "p_town_8"),
                  (assign, ":town_merchant", "trp_saxon_merchant"),
                  (assign, ":town_room_scene", "scn_town_8_room"),
              (else_try),
                  (eq, "$current_town", "p_town_35"),
                  (assign, ":town_merchant", "trp_centware_merchant"),
                  (assign, ":town_room_scene", "scn_town_10_room"),
              (else_try),
                  (eq, "$current_town", "p_town_40"),
                  (assign, ":town_merchant", "trp_irish_merchant"),
                  (assign, ":town_room_scene", "scn_town_19_room"),
              (try_end),

              (modify_visitors_at_site, ":town_room_scene"),
              (reset_visitors),
              (set_visitor, 0, "trp_player"),
              (set_visitor, 9, ":town_merchant"),

              (assign, "$talk_context", tc_merchants_house),

              (assign, "$dialog_with_merchant_ended", 0),

              (set_jump_mission, "mt_meeting_merchant"),

              (jump_to_scene, ":town_room_scene"),
              (change_screen_mission),
          ]),

         ("continue", [
              (eq, "$current_startup_quest_phase", 3),
          ], "Continue...", [
             (call_script, "script_prepare_town_to_fight"),
          ]),
     ]),
]


scripts = [
    # script that creates the alley fight, in game start
    ("prepare_alley_to_fight", [
        (party_get_slot, ":scene_no", "$current_town", slot_town_alley),
        (modify_visitors_at_site, ":scene_no"),
        (reset_visitors),
        (set_visitor, 0, "trp_player"),

        (set_visitor, 3, "trp_mountain_bandit"),

        (assign, "$talked_with_merchant", 0),
        (set_jump_mission, "mt_alley_fight"),
        (jump_to_scene, ":scene_no"),
        (change_screen_mission),
    ]),

    # script that creates the fight on the streets, part of the first mission
    ("prepare_town_to_fight", [
        (str_store_party_name_link, s9, "$g_starting_town"),
        (str_store_string, s2, "str_save_town_from_bandits"),
        (call_script, "script_start_quest", "qst_save_town_from_bandits", "$g_talk_troop"),

        (assign, "$g_mt_mode", tcm_default),
        (store_faction_of_party, ":town_faction", "$current_town"),
        (faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_3_troop),
        (faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
        (faction_get_slot, ":tier_4_troop", ":town_faction", slot_faction_tier_4_troop),

        (party_get_slot, ":town_scene", "$current_town", slot_town_center),
        (modify_visitors_at_site, ":town_scene"),
        (reset_visitors),

        # people spawned at #32, #33, #34, #35, #36, #37, #38 and #39 are town walkers.
        (try_begin),
            (try_for_range, ":unused_temp", 1, 5),
                (try_for_range, ":walker_no", 0, num_town_walkers),
                    (store_add, ":troop_slot", slot_center_walker_0_troop, ":walker_no"),
                    (party_get_slot, ":walker_troop_id", "$current_town", ":troop_slot"),
                    (gt, ":walker_troop_id", 0),
                    (store_add, ":entry_no", town_walker_entries_start, ":walker_no"),
                    (set_visitor, ":entry_no", ":walker_troop_id"),
                (try_end),
            (try_end),
        (try_end),

        # guards will be spawned at #25, #26 and #27
        (set_visitors, 25, ":tier_2_troop", 1),
        (set_visitors, 26, ":tier_3_troop", 1),
        (set_visitors, 27, ":tier_4_troop", 1),

        # enemies at positions 10-12
        (set_visitors, 10, "trp_looter", 1),
        (set_visitors, 11, "trp_bandit", 1),
        (set_visitors, 12, "trp_looter", 1),

        (store_faction_of_party, ":starting_town_faction", "$g_starting_town"),

        (try_begin),
            (eq, ":starting_town_faction", "fac_kingdom_18"),
            (assign, ":troop_of_merchant", "trp_briton_merchant"),
        (else_try),
            (eq, ":starting_town_faction", "fac_kingdom_4"),
            (assign, ":troop_of_merchant", "trp_saxon_merchant"),
        (else_try),
            (eq, ":starting_town_faction", "fac_kingdom_1"),
            (assign, ":troop_of_merchant", "trp_pict_merchant"),
        (else_try),
            (eq, ":starting_town_faction", "fac_kingdom_23"),
            (assign, ":troop_of_merchant", "trp_engle_merchant"),
        (else_try),
            (eq, ":starting_town_faction", "fac_kingdom_31"),
            (assign, ":troop_of_merchant", "trp_irish_merchant"),
        (else_try),
            (eq, ":starting_town_faction", "fac_kingdom_28"),
            (assign, ":troop_of_merchant", "trp_centware_merchant"),
        (try_end),
        (str_store_troop_name, s10, ":troop_of_merchant"),

        # more enemies
        (set_visitors, 24, "trp_looter", 1),
        (set_visitors, 2, "trp_looter", 2),
        (set_visitors, 4, "trp_looter", 1),
        (set_visitors, 5, "trp_looter", 2),
        (set_visitors, 6, "trp_looter", 1),
        (set_visitors, 7, "trp_looter", 1),

        # the merchant
        (set_visitors, 3, ":troop_of_merchant", 1),

        (set_jump_mission, "mt_town_fight"),
        (jump_to_scene, ":town_scene"),
        (change_screen_mission),
    ]),
]


dialogs = [

    # Quest 0 - Alley talk
    [anyone | auto_proceed, "start", [
         (is_between, "$g_talk_troop", "trp_briton_merchant", "trp_startup_merchants_end"),
         (eq, "$talk_context", tc_back_alley),
         (eq, "$talked_with_merchant", 0),
     ],
     "{!}.", "start_up_quest_1_next", []],

    [anyone, "start_up_quest_1_next", [],
     "Are you all right? Well.... I guess you're alive, at any rate. I'm not "
     "sure that we can say the same for the other fellow. That's one less thief "
     "to trouble our streets at night, although Heaven knows he won't be the "
     "last.... Let's talk more inside.",
     "close_window", [
         (assign, "$talked_with_merchant", 1),
         (mission_disable_talk),
     ]],

    # Quest 1 - Repeating dialog sentence
    [anyone | auto_proceed, "start", [
         (is_between, "$g_talk_troop", "trp_briton_merchant", "trp_startup_merchants_end"),
         (eq, "$talk_context", tc_tavern_talk),

         (call_script, "script_party_count_members_with_full_health", "p_main_party"),
         (assign, ":total_party_size", reg0),

         (assign, ":continue", 0),
         (try_begin),
             (check_quest_active, "qst_collect_men"),
             (neg | check_quest_succeeded, "qst_collect_men"),

             (le, ":total_party_size", 5),

             (try_begin),
                 (le, ":total_party_size", 1),
                 (str_store_string, s11, "str_please_sir_my_lady_go_find_some_volunteers_i_do_not_know_how_much_time_we_have"),
             (else_try),
                 (str_store_string, s11, "str_you_need_more_men_sir_my_lady"),
             (try_end),
             (assign, ":continue", 1),
         (else_try),
             (check_quest_active, "qst_learn_where_merchant_brother_is"),
             (neg | check_quest_succeeded, "qst_learn_where_merchant_brother_is"),
             (str_store_string, s11, "str_do_not_waste_time_go_and_learn_where_my_brother_is"),
             (assign, ":continue", 1),
         (try_end),
         (eq, ":continue", 1),
     ],
     "{!}.", "start_up_quest_2_next", []
     ],

    [anyone, "start_up_quest_2_next", [], "{!}{s11}", "close_window", []],

    # Quest 2 - First dialog sentence
    [anyone, "start", [
         (is_between, "$g_talk_troop", "trp_briton_merchant", "trp_startup_merchants_end"),
         (eq, "$talk_context", tc_tavern_talk),

         (check_quest_active, "qst_collect_men"),
         (neg | check_quest_succeeded, "qst_duel_for_lady"),
         (call_script, "script_party_count_members_with_full_health",
          "p_main_party"),
         (ge, reg0, 6),

         (str_store_party_name, s9, "$current_town"),
     ],
     "Splendid work. You have hired enough men to take on the bandits. Now -- "
     "travellers entering {s9} have told us that there is a small group of "
     "robbers lurking on the outside of town. I suspect that they are all from "
     "the same band, the one that took my brother. Hunt them down and defeat "
     "them, and make them disclose the location of their lair!",
     "merchant_quest_2a", [
         (call_script, "script_succeed_quest", "qst_collect_men"),
         (call_script, "script_end_quest", "qst_collect_men"),
     ]],

    # Quest 3 - First dialog sentence/Repeating dialog sentence
    [anyone, "start", [
         (is_between, "$g_talk_troop", "trp_briton_merchant",
          "trp_startup_merchants_end"),
         (eq, "$talk_context", tc_tavern_talk),

         (check_quest_active, "qst_save_relative_of_merchant"),
         (neg | check_quest_succeeded, "qst_save_relative_of_merchant"),

         (str_store_party_name, s9, "$current_town"),
     ],
     "So, you've found out where they hid my brother? Splendid work. I flatter "
     "myself that I'm a fine judge of character, and you look to be a {man/woman} "
     "who can get things done. Now, go out and save his unworthy hide!",
     "merchant_quest_3a", []],

    # Quest 3 - All succeeded - First dialog sentence
    [anyone, "start", [
         (is_between, "$g_talk_troop", "trp_briton_merchant",
          "trp_startup_merchants_end"),
         (eq, "$talk_context", tc_tavern_talk),

         (check_quest_active, "qst_save_relative_of_merchant"),
         (check_quest_succeeded, "qst_save_relative_of_merchant"),
     ],
     "Well... My brother is home safe. I'm not sure what to do with him -- maybe "
     "pack him off to a monastery outside Britannia. That way, if he gets "
     "knocked on the head in a street brawl, no one can say it's my fault. But "
     "that's not your problem. Here's the rest of your reward. It was "
     "well-earned.", "merchant_quest_3b", [
         (call_script, "script_finish_quest", "qst_save_relative_of_merchant", 100),
         (troop_add_gold, "trp_player", 200),
     ]],

    [anyone | plyr, "merchant_quest_3b", [],
     "The money is most welcome, and I am glad to have been of service",
     "merchant_quest_4a", []
     ],

    [anyone, "merchant_quest_4a", [],
     "Good! Now... Are you interested in making some more?", "merchant_quest_4b", []
     ],

    [anyone | plyr, "merchant_quest_4b", [],
     "Possibly. What do you need?", "merchant_quest_4b1", []
     ],

    [anyone, "merchant_quest_4b1", [],
     "Remember how I told you that the bandits had an ally inside the walls? "
     "I think I know who it is -- the captain of the watch, no less. Some months "
     "ago this captain, seeing the amount of profit we merchants were making "
     "from trade across the frontiers, decided to borrow some money to sponsor "
     "a caravan. Unfortunately, like many who are new to commerce, he failed "
     "to realize that great profit only comes with great risk. So he sank all "
     "his money into the most expensive commodities, and of course his caravan "
     "was captured and looted, and he lost everything.",
     "merchant_quest_4b2", []
     ],

    [anyone, "merchant_quest_4b2", [],
     "As a consequence, it seems, our captain turned to villainy to recoup his "
     "fortune. I supposed I'd do the same if, the Heavens forbid, I ever faced "
     "indebtedness and ruination. Now, any watch captain worth his salary will "
     "have a few thieves and robbers on his payroll, to inform on the rest, but "
     "our captain decides to employ these bastards wholesale. He brings them "
     "into the town, lets them do as they will, and takes a share of their "
     "take. You've heard of poachers turning gamekeepers? Well, in the "
     "unfortunate land of Britannia, sometimes gamekeepers will turn poacher. "
     "Luckily, there's are still a few brave, honest souls in the watch who've "
     "told me how he works.", "merchant_quest_4b3", []
     ],

    [anyone, "merchant_quest_4b3", [
         (faction_get_slot, ":local_ruler", "$g_encountered_party_faction",
          slot_faction_leader),
         (str_store_troop_name, s4, ":local_ruler"),
     ],
     "Now -- here's my plan. I could bring this to the attention of {s4}, "
     "lord of the city, but that would mean an inquiry, my word against "
     "the captain's, and witnesses can be bought and evidence destroyed, "
     "or maybe the whole thing will be forgotten if the enemy comes across "
     "the border again, and all I'll get for my trouble is a knife in the "
     "ribs. In time of war, you see, a king's eye wanders far from his domain, "
     "and his subjects suffer. So I've got another idea. I've got a small "
     "group of townsfolk together, some men in my employ and some others who've "
     "lost relatives to these bandits, and we'll storm the captain's home and "
     "bring him in chains before {s4}, hopefully with a few captured bandits "
     "to explain how things stack up.", "merchant_quest_4b4", []
     ],

    [anyone, "merchant_quest_4b4", [],
     "All I need now is someone to lead my little army into battle -- and I "
     "can't think of anyone better than you. So, what do you say?",
     "merchant_quest_4b5", []
     ],

    [anyone | plyr, "merchant_quest_4b5", [],
     "How do I know that you're telling me the truth?", "merchant_quest_4b6", []
     ],

    [anyone, "merchant_quest_4b6", [
         (str_store_party_name, s4, "$g_encountered_party"),
     ],
     "Oh, well, I suppose it's possible that I found a dozen bandits who were "
     "willing to give their lives to give a passing stranger a false impression "
     "of life in old {s4}... Well, I guess you can't really know if my word is "
     "good, but I reckon you've learned by now that my money is good, and "
     "there's another 100 scillingas, or maybe a bit more, that's waiting for "
     "you if you'll do me this last little favor. So what do you say?",
     "merchant_quest_4b7", []
     ],

    [anyone | plyr, "merchant_quest_4b7", [],
     "All right. I'll lead your men.", "merchant_quest_4b8", []
     ],

    [anyone | plyr, "merchant_quest_4b7", [],
     "I'm sorry. This is too much, too fast. I need time to think.",
     "merchant_quest_4_decline", []
     ],

    [anyone, "merchant_quest_4b8", [],
     "Splendid. It's been a long time since I staked so much on a single throw "
     "of the dice, and frankly I find it exhilarating. My men are ready to move "
     "on your word. Are you ready?",
     "merchant_quest_4b9", []],

    [anyone | plyr, "merchant_quest_4b9", [],
     "Yes. Give them the sign.", "merchant_quest_4_accept", []],

    [anyone | plyr, "merchant_quest_4b9", [],
     "Not now. I will need to rest before I can fight again.",
     "merchant_quest_4_decline", []],

    [anyone, "merchant_quest_4_accept", [],
     "Good! Now -- strike hard, strike fast, and the captain and his henchmen "
     "won't know what hit them. May the heavens be with you!",
     "close_window", [
         (assign, "$current_startup_quest_phase", 3),
         (jump_to_menu, "mnu_start_phase_3"),
         (finish_mission),
     ]],

    [anyone, "merchant_quest_4_decline",  # was startup
     [],
     "Right. I can keep my men standing by. If you let this go too long, then I "
     "suppose that I shall have to finish this affair without you, but I would "
     "be most pleased if you could be part of it as well. For now, take what time "
     "you need.",
     "close_window", []],

    # QUEST 2 - Learning where prominent's brother is.
    [anyone | plyr, "merchant_quest_2a", [],
     "Very well. I shall hunt for bandits.", "close_window", [
         (str_store_party_name, s9, "$current_town"),
         (str_store_string, s2, "str_start_up_quest_message_2"),
         (call_script, "script_start_quest", "qst_learn_where_merchant_brother_is",
          "$g_talk_troop"),

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

    # Quest 3 - Saving merchant's brother.
    [anyone | plyr, "merchant_quest_3a", [],
     "Very well. I go now to attack the bandits in their lair, and find your brother.",
     "close_window", []
     ],

    [anyone | plyr, "merchant_quest_3a", [],
     "I cannot deal with this matter at this time.", "close_window", []
     ],

    [anyone, "start", [
        (is_between, "$g_talk_troop", "trp_briton_merchant", "trp_startup_merchants_end"),

         (this_or_next | eq, "$talk_context", tc_tavern_talk),
         (neq, "$dialog_with_merchant_ended", 0),

         (assign, ":continue", 0),
         (try_begin),
             (neg | check_quest_succeeded, "qst_collect_men"),
             (neg | check_quest_active, "qst_collect_men"),
             (assign, ":continue", 1),
         (else_try),
             (neg | check_quest_active, "qst_collect_men"),
             (neg | check_quest_succeeded, "qst_learn_where_merchant_brother_is"),
             (neg | check_quest_active, "qst_learn_where_merchant_brother_is"),
             (assign, ":continue", 1),
         (else_try),
             (neg | check_quest_active, "qst_collect_men"),
             (neg | check_quest_active, "qst_learn_where_merchant_brother_is"),
             (neg | check_quest_succeeded, "qst_save_relative_of_merchant"),
             (neg | check_quest_active, "qst_save_relative_of_merchant"),
             (assign, ":continue", 1),
         (try_end),

         (eq, ":continue", 1),
     ],
     "good luck, {sir/my lady}.", "merchant_quest_persuasion12", []],

    [anyone | auto_proceed, "start", [
         (is_between, "$g_talk_troop", "trp_briton_merchant",
          "trp_startup_merchants_end"),

         (this_or_next | eq, "$talk_context", tc_tavern_talk),
         (neq, "$dialog_with_merchant_ended", 0),

         (check_quest_finished, "qst_save_relative_of_merchant"),
         (neg | check_quest_succeeded, "qst_save_town_from_bandits"),
         (neg | check_quest_active, "qst_save_town_from_bandits"),
     ], "{!}.", "merchant_quest_4b4", []
     ],

    [anyone | plyr, "merchant_quest_3a", [
         (neg | check_quest_finished, "qst_collect_men"),
         (neg | check_quest_active, "qst_collect_men"),
     ],
     "You make a persuasive case. I will help you.", "merchant_quest_persuasion", []
     ],

    [anyone | plyr, "merchant_quest_persuasion", [
         (check_quest_finished, "qst_collect_men"),
         (neg | check_quest_finished, "qst_learn_where_merchant_brother_is"),
         (neg | check_quest_active, "qst_learn_where_merchant_brother_is"),
     ],
     "You make a persuasive case. I will help you.", "merchant_quest_2", []
     ],

    [anyone | plyr, "merchant_quest_persuasion", [
         (check_quest_finished, "qst_collect_men"),
         (check_quest_finished, "qst_learn_where_merchant_brother_is"),
         (neg | check_quest_finished, "qst_save_relative_of_merchant"),
         (neg | check_quest_active, "qst_save_relative_of_merchant"),
     ],
     "You make a persuasive case. I will help you.", "merchant_quest_3", []
     ],

    [anyone | plyr, "merchant_quest_persuasion", [
         (check_quest_finished, "qst_collect_men"),
         (check_quest_finished, "qst_learn_where_merchant_brother_is"),
         (check_quest_finished, "qst_save_relative_of_merchant"),
         (neg | check_quest_finished, "qst_save_town_from_bandits"),
         (neg | check_quest_active, "qst_save_town_from_bandits"),
     ],
     "You make a persuasive case. I will help you.", "merchant_quest_4b8", []
     ],

    [anyone | plyr, "merchant_quest_persuasion12", [],
     "Thank you. Farewell.", "close_window", []
     ],

    [anyone, "merchant_quest_2", [],
     "Now -- go find and defeat that group of bandits.", "merchant_quest_2a", []
     ],

    [anyone, "merchant_quest_3", [],
     "Now -- go attack that bandit hideout, get my brother back, and show those "
     "brigands what happens to those who threaten my household.",
     "merchant_quest_3a", []
     ],

    [anyone, "start", [
         (is_between, "$g_talk_troop", "trp_relative_of_merchant",
          "trp_relative_of_merchant"),
     ],
     "Oh -- thank the heavens... Thank the heavens... Am I safe?", "close_window", []],

    [anyone, "start", [
         (is_between, "$g_talk_troop", "trp_briton_merchant",
          "trp_startup_merchants_end"),
         (eq, "$g_do_one_more_meeting_with_merchant", 1),
         (faction_get_slot, ":faction_leader", "$g_encountered_party_faction",
          slot_faction_leader),
         (str_store_troop_name, s5, ":faction_leader"),
     ],
     "Ah... {playername}. Things didn't go quite so well as I had hoped. {s5} "
     "couldn't quite find it in him to overlook my little breach of the peace. "
     "Oh, he's grateful enough that I got rid of his crooked captain -- a guard "
     "who'll let in bandits will let in an enemy army, if the price is right -- "
     "but he can't exactly have me running around here as a lasting reminder of "
     "his failure to take care of things himself.",
     "merchant_closing_statement_2", []
     ],

    [anyone | plyr, "merchant_closing_statement_2", [],
     "That hardly seems fair...", "merchant_closing_statement_3", []
     ],

    [anyone, "merchant_closing_statement_3", [],
     "Fair? This is Britannia and Hibernia, {my boy/my lady}! Kings do what they "
     "will, and the rest of us do as they must. He didn't string me up, and "
     "instead gave me time to sell my properties -- even put in a word with "
     "the other merchants that they best pay me a fair price, too. That's "
     "gracious enough, as kings go -- but he's a weak king, as they all are "
     "here, and weak kings must always look to their authority first, and "
     "justice second. I suppose I'd do the same, in his shoes.",
     "merchant_closing_statement_4", []
     ],

    [anyone, "merchant_closing_statement_4", [],
     "Anyway, I wouldn't go rubbing your part in this affair in {s5}'s face -- "
     "but he's taken note of you, and decided that you're not worth hanging, and "
     "that's something to which I'll raise a glass any day of the week. He might "
     "even have work for you, further down the road. Or, you can sell your sword "
     "to one of his competitors. Anyway, I hope you've learned a bit about what "
     "it will take to stay alive in this troubled land, and I suspect that the "
     "money you've earned won't go to waste. Good luck.",
     "close_window", [
         (assign, "$g_do_one_more_meeting_with_merchant", 2),
     ]],

    [anyone | auto_proceed, "start", [
         (is_between, "$g_talk_troop", "trp_briton_merchant", "trp_startup_merchants_end"),
         (check_quest_finished, "qst_save_town_from_bandits"),
         (eq, "$g_do_one_more_meeting_with_merchant", 2),
     ],
     "{!}.", "merchant_quests_last_word", []],

    [anyone, "merchant_quests_last_word", [],
     "I am preparing to leave town in a short while. It's been an honor to know you. Good luck.",
     "close_window", []
     ],
]
