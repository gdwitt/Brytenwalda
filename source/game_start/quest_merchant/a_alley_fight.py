from source.header_dialogs import anyone, auto_proceed
from source.header_mission_templates import *
from source.header_game_menus import *
from source.header_music import mtf_sit_ambushed
from source.mission_template_triggers import common_battle_init_banner, \
    common_inventory_not_available
from source.module_constants import *


menus = [
    ("start_phase_3", mnf_disable_all_keys,
     "{s16}^^You are exhausted by the time you find the inn in {s1}, and fall "
     "asleep quickly. However, you awake before dawn and are eager to explore "
     "your surroundings. You venture out onto the streets, which are still "
     "deserted. All of a sudden, you hear a sound that stands the hairs of your "
     "neck on end -- the rasp of a blade sliding from its scabbard...", "none", [
        (set_background_mesh, "mesh_pic_extra_malvado"),

        (str_store_party_name, s1, "$g_starting_town"),
        (str_clear, s16),
        ], [
        # scene where the player fights alone in an alley
        ("continue", [], "Continue...", [
            (assign, "$g_starting_town", "$current_town"),

            (party_set_morale, "p_main_party", 100),
            (set_encountered_party, "$current_town"),

            # creates the alley fight
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
    ]),
]


dialogs = [
    # Alley talk
    [anyone | auto_proceed, "start", [
         (is_between, "$g_talk_troop", "trp_briton_merchant", "trp_startup_merchants_end"),
         (eq, "$talk_context", tc_back_alley),
         (eq, "$talked_with_merchant", 0),
     ], "{!}.", "start_up_quest_1_next", []],

    [anyone, "start_up_quest_1_next", [],
     "Are you all right? Well.... I guess you're alive, at any rate. I'm not "
     "sure that we can say the same for the other fellow. That's one less thief "
     "to trouble our streets at night, although Heaven knows he won't be the "
     "last.... Let's talk more inside.",
     "close_window", [
         (assign, "$talked_with_merchant", 1),
         (mission_disable_talk),
     ]],
]


mission_templates = [
    ("alley_fight", mtf_battle_mode, charge, "Alley fight", [
        (0, mtef_team_0|mtef_use_exact_number, af_override_horse, aif_start_alarmed, 7, []),
        (1, mtef_team_1|mtef_visitor_source, af_override_horse, aif_start_alarmed, 20, []),
        (2, mtef_team_1|mtef_visitor_source, af_override_horse, aif_start_alarmed, 20, []),
        (3, mtef_team_1|mtef_visitor_source, af_override_horse, aif_start_alarmed, 20, []),
        ], [
        common_battle_init_banner,

        common_inventory_not_available,

        (ti_on_agent_spawn, 0, 0, [], [
            (store_trigger_param_1, ":agent_no"),
            (get_player_agent_no, ":player_agent"),
            (neq, ":agent_no", ":player_agent"),

            (assign, "$g_main_attacker_agent", ":agent_no"),
            (agent_ai_set_aggressiveness, ":agent_no", 199),

            (try_begin),
                (agent_get_troop_id, ":troop_no", ":agent_no"),
                (is_between, ":troop_no", "trp_briton_merchant", "trp_startup_merchants_end"),
                (agent_set_team, ":agent_no", 7),
                (team_set_relation, 0, 7, 0),
            (try_end),
        ]),

        (0, 0, 0, [
            (eq, "$talked_with_merchant", 0),
            ], [
            (get_player_agent_no, ":player_agent"),
            (agent_get_position, pos0, ":player_agent"),

            (try_for_agents, ":agent_no"),
                (agent_get_troop_id, ":troop_no", ":agent_no"),
                (is_between, ":troop_no", "trp_briton_merchant", "trp_startup_merchants_end"),
                (agent_set_scripted_destination, ":agent_no", pos0),
                (agent_get_position, pos1, ":agent_no"),
                (get_distance_between_positions, ":dist", pos0, pos1),
                (le, ":dist", 150),
                (assign, "$talk_context", tc_back_alley),
                (start_mission_conversation, ":troop_no"),
            (try_end),
        ]),

        (1, 0, 0, [], [
            (get_player_agent_no, ":player_agent"),
            (ge, "$g_main_attacker_agent", 0),
            (ge, ":player_agent", 0),
            (agent_is_active, "$g_main_attacker_agent"),
            (agent_is_active, ":player_agent"),
            (agent_get_position, pos0, ":player_agent"),
            (agent_get_position, pos1, "$g_main_attacker_agent"),
            (get_distance_between_positions, ":dist", pos0, pos1),
            (ge, ":dist", 5),
            (agent_set_scripted_destination, "$g_main_attacker_agent", pos0),
        ]),

        (ti_tab_pressed, 0, 0, [], [
            (display_message, "str_cannot_leave_now"),
        ]),

        # set music
        (0, 0, ti_once, [], [
            (call_script, "script_music_set_situation_with_culture", mtf_sit_ambushed),
            (set_party_battle_mode),
        ]),

        # spawn merchant
        (0, 0, ti_once, [
            (neg|main_hero_fallen),
            (num_active_teams_le, 1),
            ], [
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
            (add_visitors_to_current_scene, 3, ":troop_of_merchant", 1, 0),
        ]),

        # exit after talking to the merchant
        (1, 0, ti_once, [
            (eq, "$talked_with_merchant", 1),
            ], [
            (try_begin),
                (main_hero_fallen),
                (assign, "$g_killed_first_bandit", 0),
            (else_try),
                (assign, "$g_killed_first_bandit", 1),
            (try_end),

            (finish_mission),
            (assign, "$g_main_attacker_agent", 0),
            (assign, "$talked_with_merchant", 1),

            (get_player_agent_no, ":player_agent"),
            (store_agent_hit_points, ":hit_points", ":player_agent"),

            (try_begin),
               (lt, ":hit_points", 90),
               (agent_set_hit_points, ":player_agent", 90),
            (try_end),

            (jump_to_menu, "mnu_b_merchant_house"),
        ]),

        # exit after falling
        (1, 3, ti_once, [
            (main_hero_fallen),
            ], [
            (try_begin),
                (main_hero_fallen),
                (assign, "$g_killed_first_bandit", 0),
            (else_try),
                (assign, "$g_killed_first_bandit", 1),
            (try_end),

            (finish_mission),
            (assign, "$g_main_attacker_agent", 0),
            (assign, "$talked_with_merchant", 1),

            (get_player_agent_no, ":player_agent"),
            (store_agent_hit_points, ":hit_points", ":player_agent"),

            (try_begin),
                (lt, ":hit_points", 90),
                (agent_set_hit_points, ":player_agent", 90),
            (try_end),

            (jump_to_menu, "mnu_b_merchant_house"),
        ]),
    ])
]
