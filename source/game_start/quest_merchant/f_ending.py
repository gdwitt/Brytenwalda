from source.header_operations import *
from source.header_common import s1, s2, s3, s5, reg0
from source.header_dialogs import anyone, plyr

from source.module_constants import slot_faction_leader


dialogs = [
    [anyone, "start", [
        (is_between, "$g_talk_troop", "trp_briton_merchant", "trp_startup_merchants_end"),
        (check_quest_active, "qst_save_town_from_bandits"),

        (store_div, ":number_of_civilian_loses_div_2", "$number_of_civilian_loses", 2),

        (assign, ":player_success", "$number_of_bandits_killed_by_player"),
        (try_begin),
            (eq, "$town_fight_hero_fallen", 0),
            (store_add, ":player_success", "$number_of_bandits_killed_by_player", 1),
        (try_end),

        (val_sub, ":player_success", ":number_of_civilian_loses_div_2"),
        (val_max, ":player_success", 0),

        (call_script, "script_change_player_relation_with_center", "$g_starting_town", ":player_success"),

        (try_begin),
            (eq, "$town_fight_hero_fallen", 0),
            (gt, "$number_of_bandits_killed_by_player", 2),
            (str_store_string, s3, "str_you_fought_well_at_town_fight_survived"),
            (troop_add_gold, "trp_player", 200),
        (else_try),
            (eq, "$town_fight_hero_fallen", 0),
            (gt, "$number_of_bandits_killed_by_player", 0),
            (str_store_string, s3, "str_you_fought_normal_at_town_fight_survived"),
            (troop_add_gold, "trp_player", 200),
        (else_try),
            (eq, "$town_fight_hero_fallen", 0),
            (eq, "$number_of_bandits_killed_by_player", 0),
            (str_store_string, s3, "str_you_fought_bad_at_town_fight_survived"),
            (troop_add_gold, "trp_player", 100),
        (else_try),
            (eq, "$town_fight_hero_fallen", 1),
            (ge, "$number_of_bandits_killed_by_player", 2),
            (str_store_string, s3, "str_you_fought_well_at_town_fight"),
            (troop_add_gold, "trp_player", 100),
        (else_try),
            (str_store_string, s3, "str_you_wounded_at_town_fight"),
            (troop_add_gold, "trp_player", 100),
        (try_end),

        (try_begin),
            (ge, "$number_of_civilian_loses", 1),
            (assign, reg0, "$number_of_civilian_loses"),
            (str_store_string, s2, "str_unfortunately_reg0_civilians_wounded_during_fight_more"),
        (else_try),
            (eq, "$number_of_civilian_loses", 1),
            (assign, reg0, "$number_of_civilian_loses"),
            (str_store_string, s2, "str_unfortunately_reg0_civilians_wounded_during_fight"),
        (else_try),
            (str_store_string, s2, "str_also_one_another_good_news_is_any_civilians_did_not_wounded_during_fight"),
        (try_end),

        (call_script, "script_succeed_quest", "qst_save_town_from_bandits"),
        (call_script, "script_end_quest", "qst_save_town_from_bandits"),
        ], "{s3}{s2}", "merchant_quest_4e", []
     ],

    [anyone | plyr, "merchant_quest_4e", [
        (try_begin),
            (eq, "$g_killed_first_bandit", 1),
            (gt, "$number_of_bandits_killed_by_player", 2),
            (str_store_string, s1, "str_you_fought_well_at_town_fight_survived_answer"),
        (else_try),
            (eq, "$g_killed_first_bandit", 1),
            (gt, "$number_of_bandits_killed_by_player", 0),
            (str_store_string, s1, "str_you_fought_normal_at_town_fight_survived_answer"),
        (else_try),
            (eq, "$g_killed_first_bandit", 1),
            (eq, "$number_of_bandits_killed_by_player", 0),
            (str_store_string, s1, "str_you_fought_bad_at_town_fight_survived_answer"),
        (else_try),
            (eq, "$g_killed_first_bandit", 0),
            (ge, "$number_of_bandits_killed_by_player", 2),
            (str_store_string, s1, "str_you_fought_well_at_town_fight_answer"),
        (else_try),
            (str_store_string, s1, "str_you_wounded_at_town_fight_answer"),
        (try_end),
        ], "{s1}", "merchant_finale", []],

    [anyone | plyr, "merchant_quest_4e", [],
     "The Heavens alone grant us victory.", "merchant_finale", []],

    [anyone | plyr, "merchant_quest_4e", [],
     "I'm glad to see that you're alive, too.", "merchant_finale", []],

    [anyone, "merchant_finale", [
        (faction_get_slot, ":faction_leader", "$g_encountered_party_faction", slot_faction_leader),
        (str_store_troop_name, s5, ":faction_leader"),
        ],
        "Yes, yes... Now, a couple of my boys have the watch captain pinned "
        "down in a back room, with a knife at his throat. I''ll need to go "
        "drag him before {s5} and explain what this breach of the peace is all "
        "about. You don't need to be part of that, though. "
        "Hopefully we'll meet again!", "close_window", [
        (change_screen_map),
    ]],
]
