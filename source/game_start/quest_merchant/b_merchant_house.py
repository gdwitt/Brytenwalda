from source.header_dialogs import anyone, plyr
from source.header_mission_templates import *

from source.header_game_menus import mnf_disable_all_keys
from source.header_music import mtf_sit_town_infiltrate, mtf_sit_tavern, \
    mtf_sit_town
from source.module_constants import slot_scene_visited, tc_tavern_talk, \
    tc_merchants_house


menus = [
    ("b_merchant_house", mnf_disable_all_keys, "{s11}", "none", [
        (try_begin),
            (eq, "$g_killed_first_bandit", 1),
            (str_store_string, s11, "str_killed_bandit_at_alley_fight"),
        (else_try),
            (str_store_string, s11, "str_wounded_by_bandit_at_alley_fight"),
        (try_end)
        ], [

        ("continue", [], "Continue...", [
            (call_script, "script_prepare_merchant_house"),
        ]),
    ]),
]

scripts = [
    ("prepare_merchant_house", [
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

        (set_jump_mission, "mt_merchant_house"),

        (jump_to_scene, ":town_room_scene"),
        (change_screen_mission),
    ])
]

mission_templates = [
    ("merchant_house", 0, -1, "Meeting with the merchant", [
        (0,mtef_team_0,af_override_horse,0,1,[]),
        (1,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
        (2,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
        (3,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
        (4,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
        (5,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
        (6,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
        (7,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
        (8,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
        (9,mtef_visitor_source|mtef_team_0,af_override_horse,0,1,[]),
        ], [

        (ti_on_agent_spawn, 0, 0, [], [
            (store_trigger_param_1, ":agent_no"),

            (try_begin),
                (agent_get_troop_id, ":troop_no", ":agent_no"),
                (is_between, ":troop_no", "trp_briton_merchant", "trp_startup_merchants_end"),
                (agent_set_team, ":agent_no", 7),
                (team_set_relation, 0, 7, 0),
            (try_end),
        ]),

        (1, 0, ti_once, [], [
            (assign, "$dialog_with_merchant_ended", 0),
            (store_current_scene, ":cur_scene"),
            (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
            (try_begin),
                (eq, "$sneaked_into_town", 1),
                (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
            (else_try),
                (eq, "$talk_context", tc_tavern_talk),
                (call_script, "script_music_set_situation_with_culture", mtf_sit_tavern),
            (else_try),
                (call_script, "script_music_set_situation_with_culture", mtf_sit_town),
            (try_end),
        ]),

        (1, 0, 0, [
            (assign, ":continue", 0),
            (try_begin),
                (ge, "$dialog_with_merchant_ended", 6),
                (assign, ":continue", 1),
            (else_try),
                (ge, "$dialog_with_merchant_ended", 1),
                (neg|conversation_screen_is_active),

                (try_begin),
                    (eq, "$dialog_with_merchant_ended", 1),
                    (check_quest_active, "qst_collect_men"),
                    (tutorial_box, "str_start_up_first_quest", "@Tutorial"),
                (try_end),

                (val_add, "$dialog_with_merchant_ended", 1),
                (assign, ":continue", 0),
            (try_end),

            (try_begin),
                (conversation_screen_is_active),
                (tutorial_message, -1),
                (assign, ":continue", 0),
            (try_end),

            (eq, ":continue", 1),
        ], [
            (tutorial_message_set_size, 17, 17),
            (tutorial_message_set_position, 500, 650),
            (tutorial_message_set_center_justify, 0),
            (tutorial_message_set_background, 1),
            (tutorial_message, "str_press_tab_to_exit_from_town"),
        ]),

        (ti_inventory_key_pressed, 0, 0, [
            (set_trigger_result, 1),
        ], []),

        # tab after talked to merchant -> jump to map
        (ti_tab_pressed, 0, 0, [
            (try_begin),
                (gt, "$dialog_with_merchant_ended", 0),

                (assign, ":max_dist", 0),
                (party_get_position, pos1, "$current_town"),
                (try_for_range, ":unused", 0, 10),
                    (map_get_random_position_around_position, pos0, pos1, 2),
                    (get_distance_between_positions, ":dist", pos0, pos1),
                    (ge, ":dist", ":max_dist"),
                    (assign, ":max_dist", ":dist"),
                    (copy_position, pos2, pos0),
                (try_end),

                (party_set_position, "p_main_party", pos2),

                (finish_mission),

                (tutorial_message, -1),
                (tutorial_message_set_background, 0),

                (change_screen_map),
                (set_trigger_result, 1),
            (else_try),
                (display_message, "str_cannot_leave_now"),
            (try_end),
      ], []),
    ]),
]

dialogs = [
    (anyone, "start", [
        (is_between, "$g_talk_troop", "trp_briton_merchant", "trp_startup_merchants_end"),
        (eq, "$talk_context", tc_merchants_house),
        (neg|check_quest_finished, "qst_collect_men"),

        (try_begin),
            (eq, "$g_killed_first_bandit", 1),
            (str_store_string, s1, "str_are_you_all_right"),
        (else_try),
            (str_store_string, s1, "str_you_are_awake"),
        (try_end),
        ], "{s1}", "merchant_quest_1_prologue_1", []
    ),

    (anyone, "merchant_quest_1_prologue_1", [],
        "You seem a little disoriented. I do not know who you are or where "
        "you're from, and, to tell you the truth, I do not care. I'm just a "
        "simple merchant, but things did not go well for me here. So, I am "
        "planning to travel to another country, peaceful and rainless, I hope. "
        "I have heard that in the East gold flows from watery fontains, so "
        "maybe I'll go try my fortune in Constantinople or Alexandria.",
     "merchant_quest_1_prologue_2", []),

    (anyone, "merchant_quest_1_prologue_2", [],
        "Anyways, I advise you, before I leave, to do the same and seek your own "
        "fortune in other lands. Britannia and Hibernia are a bloody ravaged "
        "swampland, and its' people nothing more than war fodder. Poverty feeds "
        "on the weak, and the strong men abuse the sword and the lance to impose "
        "their power and control over the humble ones. In order to trade we must "
        "pay heavy taxes in each city, sort out bandits and pirates, and pray "
        "that a local lord, ignorant and lazy, do not decide to get half of our "
        "merchandise to fund his next feast or war campaign.",
        "merchant_quest_1_prologue_3", []),

    (anyone,"merchant_quest_1_prologue_3", [],
        "But I am overextending myself. Take my advice and go away from this "
        "hellhole. Until there is a powerful king able to succeed at imposing "
        "order, law and unity, a task at which even Arthur Pendragon failed, "
        "those islands will remain a vulture's feasting table. This forgotten "
        "corner of Europe is wretched to it's very roots, and there are no heroes "
        "to bring even a faint hope of peace to the good souls living here. So "
        "I say, seek your destiny elsewhere.",
        "merchant_quest_1a", []),

    (anyone|plyr,"merchant_quest_1a", [],
        "I am here to stay, Merchant. It is wrong to think that misfortunes come "
        "from the west or from the east. They originate within one's own mind.",
        "merchant_quest_1b", []),

    (anyone|plyr, "merchant_quest_1a", [],
        "Thank you for your help, but I have other things to do right now.",
        "close_window", [
        (assign, "$dialog_with_merchant_ended", 1),
    ]),

    (anyone, "merchant_quest_1b", [],
        "Oh? Yes... that is very wise. -His face grows long as he contemplates "
        "your words.- You are brave too, like my former son. I tell you what. "
        "You can have these items that are too heavy for my traveling trunk. "
        "Now  get out of here, I have work to do. Good luck stranger...",
        "merchant_quest_1c", [
        (str_store_troop_name, s9, "$g_talk_troop"),
        (str_store_party_name, s1, "$g_starting_town"),
        (str_store_string, s2, "str_start_up_quest_message_1"),

        (call_script, "script_start_quest", "qst_collect_men", "$g_talk_troop"),
    ]),

    [anyone|plyr,"merchant_quest_1c", [],
        "Very good, sir. I'll go collect some men from around the villages.",
        "merchant_quest_1d", []
    ],

    [anyone,"merchant_quest_1d", [
        (str_store_party_name, s1, "$current_town"),
        ],
        "Good. You can find me again in the tavern here in {s1} after "
        "you've got your group together. Then we'll speak about what "
        "we do next.", "close_window", [
        (assign, "$dialog_with_merchant_ended", 1),
    ]],
]
