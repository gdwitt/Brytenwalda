from source.header_operations import *
from source.header_common import s2, s4, s9, pos0, pos1, pos2, pos6, reg1
from source.header_dialogs import anyone, plyr, auto_proceed
from source.header_mission_templates import mtef_visitor_source, \
    mtef_scene_source, mtef_team_0, af_override_horse, mtef_team_1, aif_start_alarmed
from source.header_triggers import *

from source.module_constants import *

import source.mission_template_triggers


dialogs = [
    # Relative found.
    [anyone, "start", [
         (is_between, "$g_talk_troop", "trp_briton_merchant", "trp_startup_merchants_end"),
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
         (faction_get_slot, ":local_ruler", "$g_encountered_party_faction", slot_faction_leader),
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
     "All right. I'll lead your men.", "merchant_quest_4b8", []],

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
        (call_script, "script_start_quest", "qst_save_town_from_bandits", "$g_talk_troop"),
        (call_script, "script_prepare_town_fight"),
     ]],

    [anyone, "merchant_quest_4_decline", [],
     "Right. I can keep my men standing by. If you let this go too long, then I "
     "suppose that I shall have to finish this affair without you, but I would "
     "be most pleased if you could be part of it as well. For now, take what time "
     "you need.",
     "close_window", []],

    # catch conversation during town_fight mission template
    [anyone|auto_proceed, "start", [
        (is_between, "$g_talk_troop", "trp_briton_merchant", "trp_startup_merchants_end"),
        (eq, "$talk_context", tc_town_talk),
        (check_quest_active, "qst_save_town_from_bandits"),

        ], "{!}.", "merchant_quest_4_start", []
    ],

    [anyone, "merchant_quest_4_start", [], "It's time, lads! Up and at them!",
     "close_window", [
        (try_for_agents, ":agent_no"),
            (agent_get_troop_id, ":agent_troop_id", ":agent_no"),
            (ge, ":agent_troop_id", "trp_looter"),
            (le, ":agent_troop_id", "trp_desert_bandit"),
            (agent_set_team, ":agent_no", 1),
        (try_end),

        (get_player_agent_no, ":player_agent"),

        (assign, ":minimum_distance", 1000),
        # make every member of team 1 to run to closest from team 2 and vice-versa.
        (try_for_agents, ":agent_id_1"),
            (neq, ":agent_id_1", ":player_agent"),
            (agent_get_team, ":agent_team_1", ":agent_id_1"),
            (eq, ":agent_team_1", 0),
            (agent_get_position, pos0, ":agent_id_1"),

            (try_for_agents, ":agent_id_2"),
                (agent_get_team, ":agent_team_2", ":agent_id_2"),
                (eq, ":agent_team_2", 1),
                (agent_get_position, pos1, ":agent_id_2"),

                (get_distance_between_positions, ":dist", pos0, pos1),

                (le, ":dist", ":minimum_distance"),
                (assign, ":minimum_distance", ":dist"),
                (copy_position, pos2, pos1),
            (try_end),

            (agent_set_scripted_destination, ":agent_id_1", pos2, 0),
            (agent_set_speed_limit, ":agent_id_1", 10),
        (try_end),
    ]],
]

scripts = [
    ("prepare_town_fight", [
        (str_store_party_name_link, s9, "$g_starting_town"),
        (str_store_string, s2, "str_save_town_from_bandits"),

        (assign, "$g_mt_mode", tcm_default),
        (store_faction_of_party, ":town_faction", "$current_town"),
        (faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_3_troop),
        (faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
        (faction_get_slot, ":tier_4_troop", ":town_faction", slot_faction_tier_4_troop),

        (party_get_slot, ":town_scene", "$current_town", slot_town_center),
        (modify_visitors_at_site, ":town_scene"),
        (reset_visitors),

        # town walkers spawned at #32, #33, #34, #35, #36, #37, #38 and #39
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

        # guards spawned at #25, #26 and #27
        (set_visitors, 25, ":tier_2_troop", 1),
        (set_visitors, 26, ":tier_3_troop", 1),
        (set_visitors, 27, ":tier_4_troop", 1),

        # enemies
        (set_visitors, 10, "trp_looter", 1),
        (set_visitors, 11, "trp_bandit", 1),
        (set_visitors, 12, "trp_looter", 1),
        (set_visitors, 24, "trp_looter", 1),
        (set_visitors, 2, "trp_looter", 2),
        (set_visitors, 4, "trp_looter", 1),
        (set_visitors, 5, "trp_looter", 2),
        (set_visitors, 6, "trp_looter", 1),
        (set_visitors, 7, "trp_looter", 1),

        # merchant
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
        (set_visitors, 3, ":troop_of_merchant", 1),

        (set_jump_mission, "mt_town_fight"),
        (jump_to_scene, ":town_scene"),
        (change_screen_mission),
    ]),
]


mission_templates = [
    ("town_fight", 0, -1, "Town Fight", [
        (0, mtef_scene_source|mtef_team_0, af_override_horse, 0, 1, []),
        (1, mtef_scene_source|mtef_team_0, af_override_horse, 0, 1, []),
        (2, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []),
        (3, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []),
        (4, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []),
        (5, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []),
        (6, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []),
        (7, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []),
        (8, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []),
        (9, mtef_visitor_source, af_override_horse, 0, 1, []),
        (10, mtef_visitor_source, af_override_horse, 0, 1, []),
        (11, mtef_visitor_source|mtef_team_1, af_override_horse, 0, 1, []),
        (12, mtef_visitor_source|mtef_team_1, af_override_horse, 0, 1, []),
        (13, mtef_visitor_source|mtef_team_1, af_override_horse, 0, 1, []),
        (14, mtef_visitor_source, af_override_horse, 0, 1, []),
        (15, mtef_visitor_source, af_override_horse, 0, 1, []),
        (16, mtef_visitor_source, af_override_horse, 0, 1, []),
        (17, mtef_visitor_source, af_override_horse, 0, 1, []),
        (18, mtef_visitor_source, af_override_horse, 0, 1, []),
        (19, mtef_visitor_source, af_override_horse, 0, 1, []),
        (20, mtef_visitor_source, af_override_horse, 0, 1, []),
        (21, mtef_visitor_source|mtef_team_1, af_override_horse, 0, 1, []),
        (22, mtef_visitor_source|mtef_team_1, af_override_horse, 0, 1, []),
        (23, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []), #guard
        (24, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []), #guard
        (25, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []), #guard
        (26, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []), #guard
        (27, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []), #guard
        (28, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []), #guard
        (29, mtef_visitor_source, af_override_horse, 0, 1, []),
        (30, mtef_visitor_source, af_override_horse, 0, 1, []),
        (31, mtef_visitor_source, af_override_horse, 0, 1, []),
        (32, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []), #town walker point
        (33, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []), #town walker point
        (34, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []), #town walker point
        (35, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []), #town walker point
        (36, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []), #town walker point
        (37, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []), #town walker point
        (38, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []), #town walker point
        (39, mtef_visitor_source|mtef_team_0, af_override_horse, 0, 1, []), #town walker point
        (40, mtef_visitor_source|mtef_team_1, af_override_horse, aif_start_alarmed, 1, []), #in towns, can be used for guard reinforcements
        (41, mtef_visitor_source|mtef_team_1, af_override_horse, aif_start_alarmed, 1, []), #in towns, can be used for guard reinforcements
        (42, mtef_visitor_source|mtef_team_1, af_override_horse, aif_start_alarmed, 1, []), #in towns, can be used for guard reinforcements
        (43, mtef_visitor_source|mtef_team_1, af_override_horse, aif_start_alarmed, 1, []), #in towns, can be used for guard reinforcements
        (44, mtef_visitor_source|mtef_team_1, af_override_horse, aif_start_alarmed, 1, []),
        (45, mtef_visitor_source|mtef_team_1, af_override_horse, aif_start_alarmed, 1, []),
        (46, mtef_visitor_source|mtef_team_1, af_override_horse, aif_start_alarmed, 1, []),
        (47, mtef_visitor_source|mtef_team_1, af_override_horse, aif_start_alarmed, 1, []),
        ], [
        source.mission_template_triggers.common_battle_init_banner,

        (ti_before_mission_start, 0, 0, [], [
            (call_script, "script_change_banners_and_chest")
        ]),

        (ti_on_agent_spawn, 0, 0, [], [
            (store_trigger_param_1, ":agent_no"),

            (agent_set_team, ":agent_no", 0),
        ]),

        (ti_before_mission_start, 0, 0, [], [
            (mission_disable_talk),

            (assign, "$g_main_attacker_agent", 0),
            (set_party_battle_mode),

            (assign, "$number_of_bandits_killed_by_player", 0),
            (assign, "$number_of_civilian_loses", 0),

            (set_fixed_point_multiplier, 100),
        ]),

        (1, 0, ti_once, [
            (call_script, "script_init_town_walker_agents"),
            ], []
        ),

        # count dead civilians and player-killed bandits
        (ti_on_agent_killed_or_wounded, 0, 0, [], [
            (store_trigger_param_1, ":dead_agent_no"),
            (store_trigger_param_2, ":killer_agent_no"),
            #(store_trigger_param_3, ":is_wounded"),

            (try_begin),
                (agent_get_team, ":dead_agent_team_no", ":dead_agent_no"),
                (eq, ":dead_agent_team_no", 1),

                (get_player_agent_no, ":player_agent"),
                (eq, ":player_agent", ":killer_agent_no"),

                (val_add, "$number_of_bandits_killed_by_player", 1),
            (else_try),
                (eq, ":dead_agent_team_no", 0),
                (val_add, "$number_of_civilian_loses", 1),
            (try_end),
        ]),

        # the merchant is counting to start
        (1, 0, 0, [
            (lt, "$merchant_sign_count", 8),
            (val_add, "$merchant_sign_count", 1),

            (try_begin),
                (eq, "$merchant_sign_count", 2),
                (get_player_agent_no, ":player_agent"),
                (try_for_agents, ":agent_no"),
                    (agent_get_troop_id, ":agent_troop_id", ":agent_no"),
                    (ge, ":agent_troop_id", "trp_briton_merchant"),
                    (lt, ":agent_troop_id", "trp_startup_merchants_end"),

                    (assign, "$g_city_merchant_troop_id", ":agent_troop_id"),
                    (assign, "$g_city_merchant_agent_id", ":agent_no"),

                    (agent_get_position, pos0, ":player_agent"),
                    (agent_get_position, pos1, ":agent_no"),

                    (assign, ":max_dif", -1000),
                    (try_for_range, ":target_entry_point", 0, 64),
                        (entry_point_get_position, pos6, ":target_entry_point"),
                        (get_distance_between_positions, ":dist_to_player", pos0, pos6),
                        (get_distance_between_positions, ":dist_to_merchant", pos1, pos6),
                        (store_sub, ":dif", ":dist_to_merchant", ":dist_to_player"),
                        (ge, ":dist_to_merchant", 15),
                        (ge, ":dif", ":max_dif"),
                        (copy_position, pos2, pos6),
                        (assign, ":max_dif", ":dif"),
                    (try_end),

                    (agent_set_scripted_destination, ":agent_no", pos2, 0),
                    (agent_set_speed_limit, ":agent_no", 10),
                (try_end),
            (else_try),
                (eq, "$merchant_sign_count", 5),

                (get_player_agent_no, ":player_agent"),
                (agent_get_position, pos0, ":player_agent"),

                (agent_set_scripted_destination, "$g_city_merchant_agent_id", pos0, 0),
                (agent_set_speed_limit, "$g_city_merchant_agent_id", 10),
            (else_try),
                (eq, "$merchant_sign_count", 7),

                (agent_clear_scripted_mode, "$g_city_merchant_agent_id"),

                (assign, "$talk_context", tc_town_talk),
                (start_mission_conversation, "$g_city_merchant_troop_id"),
            (try_end),
        ], []),

        # make each team member run to closest bandit
        (1, 0, 0, [], [
            (eq, "$merchant_sign_count", 8),

            (get_player_agent_no, ":player_agent"),

            # for all team members of player's team
            (try_for_agents, ":agent_no"),
                (neq, ":agent_no", ":player_agent"),
                (agent_is_alive, ":agent_no"),
                (agent_get_team, ":agent_team", ":agent_no"),
                (eq, ":agent_team", 0),

                (agent_get_position, pos0, ":agent_no"),

                # select closest bandit
                (assign, ":minimum_distance", 10000),
                (try_for_agents, ":bandit_no"),
                    (agent_is_alive, ":bandit_no"),
                    (agent_get_team, ":bandit_team", ":bandit_no"),
                    (eq, ":bandit_team", 1),

                    (agent_get_position, pos1, ":bandit_no"),

                    (get_distance_between_positions, ":dist", pos0, pos1),
                    (le, ":dist", ":minimum_distance"),
                    (assign, ":minimum_distance", ":dist"),
                    (copy_position, pos2, pos1),
                (try_end),

                # order move if too far
                (assign, reg1, ":dist"),
                (try_begin),
                    (le, ":minimum_distance", 500),
                    (agent_clear_scripted_mode, ":agent_no"),
                (else_try),
                    (lt, ":minimum_distance", 10000),
                    (agent_set_scripted_destination, ":agent_no", pos2, 0),
                (try_end),
            (try_end),
        ]),

        # tick walkers movement
        (3, 0, 0, [
            (lt, "$merchant_sign_count", 8),
            (call_script, "script_tick_town_walkers")
            ], []
        ),

        (2, 0, 0, [
            (call_script, "script_center_ambiance_sounds")
            ], []
        ),

        # end mission
        (1, 4, ti_once, [
            (this_or_next|main_hero_fallen),
            (num_active_teams_le, 1),

            (eq, "$merchant_sign_count", 8),
            ], [
            (try_begin),
                (main_hero_fallen),
                (assign, "$town_fight_hero_fallen", 1),
            (else_try),
                (assign, "$town_fight_hero_fallen", 0),
            (try_end),

            (mission_enable_talk),

            (finish_mission),

            (unlock_achievement, ACHIEVEMENT_GET_UP_STAND_UP),
        ]),

        (ti_inventory_key_pressed, 0, 0, [
            (try_begin),
                (eq, "$g_mt_mode", tcm_default),
                (set_trigger_result, 1),
            (else_try),
                (eq, "$g_mt_mode", tcm_disguised),
                (display_message,"str_cant_use_inventory_disguised"),
            (else_try),
                (display_message, "str_cant_use_inventory_now"),
            (try_end),
            ], []
        ),

        (ti_tab_pressed, 0, 0, [
            (display_message, "str_cannot_leave_now"),
            ], []
        ),
    ]),
]
