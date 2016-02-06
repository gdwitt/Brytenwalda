from source.header_operations import *
from source.header_common import *
from source.header_triggers import *
from source.header_mission_templates import *
from source.header_skills import skl_leadership, skl_persuasion

from source.module_constants import *


#chief guardaespaldas para player cuando visita lugares caba'drin
bodyguard_triggers = [
 (ti_after_mission_start, 0, ti_once, [(neq, "$g_mt_mode", tcm_disguised)], #condition for not sneaking in; to exclude prison-breaks, etc change to (eq, "$g_mt_mode", tcm_default")
   [
    #Get number of bodyguards
    (store_skill_level, ":leadership", skl_leadership, "trp_player"),
    (store_skill_level, ":persuasion", skl_persuasion, "trp_player"),
    (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
    #(store_attribute_level, ":char", ca_charisma, "trp_player"),
    (val_div, ":leadership", 4),#gdw4
    (val_div, ":persuasion", 4),#gdw4
    #val_div, ":char", 3),
    (val_div, ":renown", 450),#gdw500
    (store_add, ":max_guards", ":renown", ":leadership"),
    (val_add, ":max_guards", ":persuasion"),
    (val_min, ":max_guards", 5),#3

    (ge, ":max_guards", 1),
    #Get player info
    (get_player_agent_no, ":player"),
    (agent_get_team, ":playerteam", ":player"),
    (agent_get_horse, ":use_horse", ":player"), #If the player spawns with a horse, the bodyguard will too.

    (assign, ":bodyguard_count", 0),
    (party_get_num_companion_stacks, ":num_of_stacks", "p_main_party"),
    (try_for_range, ":i", 0, ":num_of_stacks"),
        (party_stack_get_troop_id, ":troop_id", "p_main_party", ":i"),
        (neq, ":troop_id", "trp_player"),
        (troop_is_hero, ":troop_id"),
        (neg|troop_is_wounded, ":troop_id"),
        (val_add, ":bodyguard_count", 1),

        (try_begin), #For prison-breaks
            (this_or_next|eq, "$talk_context", tc_escape),
            (eq, "$talk_context", tc_prison_break),
            (troop_set_slot, ":troop_id", slot_troop_will_join_prison_break, 1),
        (try_end),

        (assign, ":entry_point", 0),
        (assign, ":mission_tpl", 0),
        (try_begin),
            (party_slot_eq, "$current_town", "slot_party_type", spt_village),
            (assign, ":entry_point", 11), #Village Elder's Entry
            (assign, ":mission_tpl", "mt_village_center"),
        (else_try),
            (this_or_next|eq, "$talk_context", tc_prison_break),
            (this_or_next|eq, "$talk_context", tc_escape),
            (eq, "$talk_context", tc_town_talk),
            (assign, ":entry_point", 24), #Prison Guard's Entry
            (try_begin),
                (party_slot_eq, "$current_town", "slot_party_type", spt_castle),
                (assign, ":mission_tpl", "mt_castle_visit"),
            (else_try),
                (assign, ":mission_tpl", "mt_town_center"),
            (try_end),
        (else_try),
            (eq, "$talk_context", tc_tavern_talk),
            (assign, ":entry_point", 17), #First NPC Tavern Entry
        (else_try),
            (eq, "$talk_context", tc_odin_cave),
            (assign, ":entry_point", 1),
        (else_try),
               (eq, "$talk_context", tc_roman_dungeon),
            (assign, ":entry_point", 1),
            #(assign, ":entry_point", 0),#35
            #(assign, ":entry_point", 32),
        (try_end),
        (try_begin),
            (neq, "$talk_context", tc_tavern_talk),
            (gt, ":use_horse", 0),
            (mission_tpl_entry_set_override_flags, ":mission_tpl", ":entry_point", 0),
        (try_end),
        (store_current_scene, ":cur_scene"),
        (modify_visitors_at_site, ":cur_scene"),
        (add_visitors_to_current_scene, ":entry_point", ":troop_id", 1),

        (eq, ":bodyguard_count", ":max_guards"),
        (assign, ":num_of_stacks", 0), #Break Loop
    (try_end), #Stack Loop
    (gt, ":bodyguard_count", 0), #If bodyguards spawned...
    (set_show_messages, 0),
    (team_give_order, ":playerteam", 8, mordr_follow), #Division 8 to avoid potential conflicts
    (set_show_messages, 1),
   ]),

 (ti_on_agent_spawn, 0, 0, [],
   [
    (store_trigger_param_1, ":agent"),
    (agent_get_troop_id, ":troop", ":agent"),
    (neq, ":troop", "trp_player"),
    (troop_is_hero, ":troop"),
    (main_party_has_troop, ":troop"),

    (get_player_agent_no, ":player"),
    (agent_get_team, ":playerteam", ":player"),
    (agent_get_position,pos1,":player"),

    (agent_set_team, ":agent", ":playerteam"),
    (agent_set_division, ":agent", 8),
    (agent_add_relation_with_agent, ":agent", ":player", 1),
    (agent_set_is_alarmed, ":agent", 1),
    (store_random_in_range, ":shift", 1, 3),
    (val_mul, ":shift", 100),
    (position_move_y, pos1, ":shift"),
    (store_random_in_range, ":shift", 1, 3),
    (store_random_in_range, ":shift_2", 0, 2),
    (val_mul, ":shift_2", -1),
    (try_begin),
        (neq, ":shift_2", 0),
        (val_mul, ":shift", ":shift_2"),
    (try_end),
    (position_move_x, pos1, ":shift"),
    (agent_set_position, ":agent", pos1),
   ]),

 (ti_on_agent_killed_or_wounded, 0, 0, [],
    [
     (store_trigger_param_1, ":dead_agent"),

     (agent_get_troop_id, ":troop", ":dead_agent"),
     (neq, ":troop", "trp_player"),
     (troop_is_hero, ":troop"),
     (main_party_has_troop, ":troop"),
     (party_wound_members, "p_main_party", ":troop", 1),
    ]),
 ]
#chief bodyboard acaba caba'drin