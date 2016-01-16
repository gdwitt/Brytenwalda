from ..header_game_menus import *
from ..module_constants import *
import introduction, character_creation


start_menu_0 = \
    ("start_game_0", menu_text_color(0xFF000000) | mnf_disable_all_keys,
     "It rains. It is cold, too cold and for a moment you are afraid... "
     "but then you start to remember who you are.",
     "none",
     [], [
         ("introduction", [], "Prelude",
          [(jump_to_menu, "mnu_introduction_2")]),

         ("continue", [], "Character Creation",
          [(jump_to_menu, "mnu_start_game_1")]),

         ("start_mod", [], "Quick Character (for mod testing)",
          [
              (troop_set_type, "trp_player", 0),
              (assign, "$character_gender", tf_male),
              (set_show_messages, 0),

              (troop_add_gold, "trp_player", 43000),
              (troop_raise_attribute, "trp_player", ca_strength, 5),
              (troop_raise_attribute, "trp_player", ca_agility, 5),
              (troop_raise_attribute, "trp_player", ca_intelligence, 5),
              (troop_raise_attribute, "trp_player", ca_charisma, 5),
              (troop_raise_skill, "trp_player", skl_weapon_master, 5),
              (troop_raise_skill, "trp_player", skl_leadership, 5),
              (troop_raise_skill, "trp_player", skl_looting, 5),
              (troop_raise_skill, "trp_player", skl_shield, 5),
              (troop_raise_skill, "trp_player", skl_inventory_management, 5),
              (troop_raise_skill, "trp_player", skl_power_throw, 5),
              (troop_raise_skill, "trp_player", skl_pathfinding, 5),
              (troop_raise_skill, "trp_player", skl_riding, 5),
              (troop_raise_proficiency_linear, "trp_player", wp(100), 10),
              (troop_add_item, "trp_player", "itm_spear2", 1),
              (troop_add_item, "trp_player", "itm_noblearmor21res", 0),
              (troop_add_item, "trp_player", "itm_shieldtarcza4", 0),
              (troop_add_item, "trp_player", "itm_roman_horse1", 0),
              (troop_equip_items, "trp_player"),

              (add_xp_to_troop, 1000, "trp_player"),
              (troop_set_slot, "trp_player", slot_troop_renown, 450),
              (set_show_messages, 1),

              (change_screen_map),
          ]),

         ("go_back", [], "Go back", [(jump_to_menu, "mnu_start_game_0")])
     ])

custom_game_menu = (
    "start_game_3", mnf_disable_all_keys,
    "Choose your scenario:",
    "none",
    [
        (assign, "$g_custom_battle_scenario", 0),
        (assign, "$g_custom_battle_scenario", "$g_custom_battle_scenario"),
    ],
    [("go_back", [], "Go back", [(change_screen_quit),])]
)

tutorial_menu = (
    "tutorial", mnf_disable_all_keys,
    "You approach a field where the locals are training with weapons. You can "
    "practice here to improve your combat skills.",
    "none", [
        (try_begin),
        (eq, "$g_tutorial_entered", 1),
        (change_screen_quit),
        (else_try),
        (set_passage_menu, "mnu_tutorial"),
        (assign, "$g_tutorial_entered", 1),
        (try_end),
    ],
    [
        ("continue", [], "Continue...",
         [
             (modify_visitors_at_site, "scn_tutorial_training_ground"),
             (reset_visitors, 0),
             (set_player_troop, "trp_player"),
             (assign, "$g_player_troop", "trp_player"),
             (troop_raise_attribute, "$g_player_troop", ca_strength, 12),
             (troop_raise_attribute, "$g_player_troop", ca_agility, 9),
             (troop_raise_attribute, "$g_player_troop", ca_charisma, 5),
             (troop_raise_skill, "$g_player_troop", skl_shield, 3),
             (troop_raise_skill, "$g_player_troop", skl_athletics, 2),
             (troop_raise_skill, "$g_player_troop", skl_riding, 3),
             (troop_raise_skill, "$g_player_troop", skl_power_strike, 1),
             (troop_raise_skill, "$g_player_troop", skl_power_draw, 5),
             (troop_raise_skill, "$g_player_troop", skl_weapon_master, 4),
             (troop_raise_skill, "$g_player_troop", skl_ironflesh, 1),
             (troop_raise_skill, "$g_player_troop", skl_horse_archery, 6),
             (troop_raise_proficiency_linear, "$g_player_troop", wpt_one_handed_weapon, 70),
             (troop_raise_proficiency_linear, "$g_player_troop", wpt_two_handed_weapon, 70),
             (troop_raise_proficiency_linear, "$g_player_troop", wpt_polearm, 70),
             (troop_raise_proficiency_linear, "$g_player_troop", wpt_crossbow, 70),
             (troop_raise_proficiency_linear, "$g_player_troop", wpt_throwing, 70),

             (troop_clear_inventory, "$g_player_troop"),
             (troop_add_item, "$g_player_troop", "itm_leather_tunic1", 0),
             (troop_add_item, "$g_player_troop", "itm_leather_boots1", 0),
             (troop_add_item, "$g_player_troop", "itm_practice_sword", 0),
             (troop_add_item, "$g_player_troop", "itm_quarter_staff", 0),
             (troop_equip_items, "$g_player_troop"),
             (set_visitor, 0, "trp_player"),
             (set_visitor, 32, "trp_tutorial_fighter_1"),
             (set_visitor, 33, "trp_tutorial_fighter_2"),
             (set_visitor, 34, "trp_tutorial_fighter_3"),
             (set_visitor, 35, "trp_tutorial_fighter_4"),
             (set_visitor, 40, "trp_tutorial_master_archer"),
             (set_visitor, 41, "trp_tutorial_archer_1"),
             (set_visitor, 42, "trp_tutorial_archer_1"),
             (set_visitor, 60, "trp_tutorial_master_horseman"),
             (set_visitor, 61, "trp_tutorial_rider_1"),
             (set_visitor, 62, "trp_tutorial_rider_1"),
             (set_visitor, 63, "trp_tutorial_rider_2"),
             (set_visitor, 64, "trp_tutorial_rider_2"),
             (set_jump_mission, "mt_tutorial_training_ground"),
             (jump_to_scene, "scn_tutorial_training_ground"),
             (change_screen_mission),
         ]),

        ("go_back_dot", [], "Go back.", [(change_screen_quit),]),
    ]
)

# the final menu of character creation is the one that the game hard-hiredly goes
# after the hard-wired menu of skill choice.
# the other menus must also be in this order
first_menus = [start_menu_0, character_creation.menus[-1], custom_game_menu,
               tutorial_menu]

menus = character_creation.menus[:-1] + introduction.menus

scripts = character_creation.scripts
