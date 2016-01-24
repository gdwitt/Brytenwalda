from source.header_dialogs import anyone, plyr
from source.header_game_menus import *
from source.header_items import *
from source.header_parties import pf_always_visible
from source.module_constants import *


dialogs = [

    [anyone, "start", [
        (is_between, "$g_talk_troop", "trp_briton_merchant", "trp_startup_merchants_end"),
        (eq, "$talk_context", tc_tavern_talk),
        (check_quest_active, "qst_learn_where_merchant_brother_is"),
        (neg | check_quest_succeeded, "qst_learn_where_merchant_brother_is"),
        ], "Find those bandits before it is too late.", "close_window", []
    ],

    # found leader
    [anyone, "start", [
        (eq, "$talk_context", tc_party_encounter),
        (check_quest_active, "qst_learn_where_merchant_brother_is"),
        (is_between, "$g_talk_troop", "trp_sea_raider_leader", "trp_bandit_leaders_end"),
        ], "What do you want?", "looter_leader_1", []
     ],

    [anyone | plyr, "looter_leader_1", [],
        "I've been looking for you. Tell me where you keep your prisoners, "
        "and I'll let you go.", "looter_leader_2", []
    ],

    [anyone | plyr, "looter_leader_1", [],
        "Nothing. We'll leave you in peace.", "close_window", [
        (assign, "$g_leave_encounter", 1),
    ]],

    [anyone, "looter_leader_2", [],
        "Hah! Those prisoners are only going free if you pay their ransom. "
        "I want scillingas! A lot of them! Did you bring any coins?",
        "looter_leader_3", []
    ],

    [anyone | plyr, "looter_leader_3", [],
        "No, but I brought steel.", "close_window", []
    ],

    # talk to the defeated leader that kidnapped the merchant relative
    [anyone, "start", [
        (is_between, "$g_talk_troop", "trp_sea_raider_leader", "trp_bandit_leaders_end"),
        (check_quest_active, "qst_learn_where_merchant_brother_is"),
        (eq, "$talk_context", tc_hero_defeated),
        ],
        "Firth (pace)! Firth! Spare me! Spare my life! Let me go --He falls to "
        "his knees--, and I'll go far away from here, and learn an honest "
        "trade, and you'll never hear of me again!", "bandit_leader_1a", []
    ],

    [anyone | plyr, "bandit_leader_1a", [
        (is_between, "$g_talk_troop", "trp_sea_raider_leader", "trp_bandit_leaders_end"),
        ],
        "I'll spare your life -- but in exchange, I want information. Either you "
        "or your mates kidnapped the brother of a prominent merchant in town. "
        "Tell me where you're hiding him, and give me your word that you'll stop "
        "troubling the people of these parts, and you can go free.",
        "bandit_leader_1b", []
    ],

    # bandit tells place of hideout
    [anyone, "bandit_leader_1b", [
        (is_between, "$g_talk_troop", "trp_sea_raider_leader", "trp_bandit_leaders_end"),

        (assign, ":possible_villages", 0),
        (try_for_range, ":village_no", villages_begin, villages_end),
            (party_slot_eq, ":village_no", slot_village_bound_center, "$g_starting_town"),
            (val_add, ":possible_villages", 1),
        (try_end),

        (store_random_in_range, ":random_village", 0, ":possible_villages"),
        (val_add, ":random_village", 1),

        (try_for_range, ":village_no", villages_begin, villages_end),
            (party_slot_eq, ":village_no", slot_village_bound_center, "$g_starting_town"),
            (val_sub, ":random_village", 1),
            (eq, ":random_village", 0),
            (assign, "$lair_neighboor_village", ":village_no"),
        (try_end),

        (str_store_party_name_link, s9, "$lair_neighboor_village"),

        (set_spawn_radius, 4),
        (spawn_around_party, "$lair_neighboor_village", "pt_looter_lair"),
        (party_set_flags, reg0, pf_always_visible, 1),
        ],
        "Oh bless you, {sir/my lady}. Bless you. We've done the lad no harm. "
        "We've been keeping him in our hideout near {s9}. I'll describe the area "
        "nearby in detail, so there's no mistaking it...", "close_window", [

        (call_script, "script_succeed_quest", "qst_learn_where_merchant_brother_is"),
        (call_script, "script_end_quest", "qst_learn_where_merchant_brother_is"),

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
        (str_store_string, s2, "str_find_the_lair_near_s9_and_free_the_brother_of_the_prominent_s10_merchant"),

        (call_script, "script_start_quest", "qst_save_relative_of_merchant", ":troop_of_merchant"),
    ]],

    # In case player returns to merchant, have a sentence.
    [anyone, "start", [
        (is_between, "$g_talk_troop", "trp_briton_merchant", "trp_startup_merchants_end"),
        (eq, "$talk_context", tc_tavern_talk),

        (check_quest_active, "qst_save_relative_of_merchant"),
        (neg | check_quest_succeeded, "qst_save_relative_of_merchant"),

        (str_store_party_name, s9, "$current_town"),
        ],
     "So, you've found out where they hid my brother? Splendid work. I flatter "
     "myself that I'm a fine judge of character, and you look to be a {man/woman} "
     "who can get things done. Now, go out and save his unworthy hide!",
     "merchant_quest_3a", []
    ],

    [anyone | plyr, "merchant_quest_3a", [],
        "Very well. I go now to attack the bandits in their lair, and find your brother.",
        "close_window", []
    ],

    [anyone | plyr, "merchant_quest_3a", [],
        "I cannot deal with this matter at this time.", "close_window", []
    ],

    # conversation to relative during bandit lair mission after lair is cleaned.
    ["trp_relative_of_merchant", "start", [
        (try_begin),
            (check_quest_active, "qst_save_relative_of_merchant"),
            (call_script, "script_succeed_quest", "qst_save_relative_of_merchant"),
        (try_end),

        (str_store_party_name, s9, "$g_starting_town"),

        (assign, "$relative_of_merchant_is_found", 1),
        ],
        "Thank you! Thank you, {sir/my lady}, for rescuing me from those fiends. "
        "Did my brother in {s9} put you onto their track?", "relative_saved_1a", []
    ],

    [anyone | plyr, "relative_saved_1a", [],
        "Yes. I told him that I would find you. I advise you to return to your "
        "family as quickly as you can -- and be careful on the road.",
        "close_window", []
    ],
]


# mission template triggers for the Bandit Lair template
lair_mission_templates_triggers = [

    # add merchant relative to scene after all bandits are killed.
    (2, 0, ti_once, [
        (neg|main_hero_fallen),
        (num_active_teams_le, 1),
        ], [

        (party_get_template_id, ":template", "$g_encountered_party"),
        (try_begin),
            (eq, ":template", "pt_looter_lair"),
            (check_quest_active, "qst_save_relative_of_merchant"),

            # insert merchant relative into entry far from player position
            (get_player_agent_no, ":player_agent"),
            (agent_get_position, pos0, ":player_agent"),
            (assign, ":minimum_distance", 100000),
            (try_for_range, ":entry_no", 1, 10),
                (entry_point_get_position, pos1, ":entry_no"),
                (get_distance_between_positions, ":dist", pos0, pos1),
                (le, ":dist", ":minimum_distance"),
                (ge, ":dist", 1000),
                (assign, ":nearest_entry_point", ":entry_no"),
                (assign, ":minimum_distance", ":dist"),
            (try_end),

            (add_visitors_to_current_scene, ":nearest_entry_point", "trp_relative_of_merchant", 1, 0),
         (try_end),
       ]),

    # make merchant relative run to player
    (ti_on_agent_spawn, 0, 0, [], [
        (store_trigger_param_1, ":agent_no"),

        (assign, "$relative_of_merchant_is_found", 0),

        (try_begin),
            (agent_is_human, ":agent_no"),
            (agent_is_alive, ":agent_no"),
            (agent_get_team, ":agent_team", ":agent_no"),
            (eq, ":agent_team", 1),

            (agent_get_position, pos4, ":agent_no"),
            (agent_set_scripted_destination, ":agent_no", pos4, 1),
        (try_end),

        (try_begin),
            (agent_get_troop_id, ":troop_no", ":agent_no"),
            (eq, ":troop_no", "trp_relative_of_merchant"),
            (agent_set_team, ":agent_no", 7),
            (team_set_relation, 0, 7, 0),
        (try_end),
    ]),

    # make merchant relative talk to player when it is too close
    (0, 0, 0, [
        (party_get_template_id, ":template", "$g_encountered_party"),
        (eq, ":template", "pt_looter_lair"),
        (check_quest_active, "qst_save_relative_of_merchant"),
        (eq, "$relative_of_merchant_is_found", 0),
        ], [
        (get_player_agent_no, ":player_agent"),
        (agent_get_position, pos0, ":player_agent"),

        (try_for_agents, ":agent_no"),
            (agent_get_troop_id, ":troop_no", ":agent_no"),
            (eq, ":troop_no", "trp_relative_of_merchant"),
            (agent_set_scripted_destination, ":agent_no", pos0),
            (agent_get_position, pos1, ":agent_no"),
            (get_distance_between_positions, ":dist", pos0, pos1),
            (le, ":dist", 200),
            (start_mission_conversation, "trp_relative_of_merchant"),
        (try_end),
    ]),

    (1, 4, ti_once, [
        (assign, ":continue", 0),

        (party_get_template_id, ":template", "$g_encountered_party"),
        (try_begin),
            (eq, ":template", "pt_looter_lair"),
            (check_quest_active, "qst_save_relative_of_merchant"),

            (this_or_next|main_hero_fallen),
            (eq, "$relative_of_merchant_is_found", 1),

            (assign, ":continue", 1),
        (else_try),
            (this_or_next|neq|eq, ":template", "pt_looter_lair"),
            (neg|check_quest_active, "qst_save_relative_of_merchant"),

            (store_mission_timer_a, ":cur_time"),
            (ge, ":cur_time", 5),

            (this_or_next | main_hero_fallen),
            (num_active_teams_le, 1),

            (assign, ":continue", 1),
        (try_end),

        (eq, ":continue", 1),
        ], [
        (try_begin),
            (main_hero_fallen),
        (else_try),
            (party_set_slot, "$g_encountered_party", slot_party_ai_substate, 2),
        (try_end),

        (finish_mission),
    ])
]
