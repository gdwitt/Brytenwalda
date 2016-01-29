from source.header_operations import *
from source.header_common import *
from source.header_triggers import *
from source.header_mission_templates import *
from source.header_troops import *
from source.header_items import *
from source.header_sounds import sf_looping
from source.header_music import mtf_sit_siege, mtf_sit_travel, mtf_sit_arena
from source.header_skills import *

from source.module_constants import *

from .formations import formations_triggers, AI_triggers
from .bodyguard import bodyguard_triggers
from .flail import flail_triggers
from .weapon_break import common_weapon_break
from .ai_weapons import common_wpn_swapping
from .death_camera import common_init_deathcam, common_start_deathcam, \
    common_move_deathcam, common_rotate_deathcam
from .shield_bash import sp_shield_bash_1, sp_shield_bash_2, sp_shield_bash_3, \
    mp_shield_bash_1, mp_shield_bash_2
from .rain_and_snow import rain
from .fall_backwards import common_andar_cae
from .decapitate import theoris_decapitation
from .volley_order import order_volley_triggers
from .health_regeneration import WP_HR_on_death
import volley_order

scripts = volley_order.scripts


#caba'drin fuerza uso de lanzas en batalla chief
common_weapon_use_spawn = (
 1, 0, ti_once, [],
   # Just after spawn, mark lancers, spears, horse archers using a slot.
   # Force lancers to equip lances, horse archers to equip bows
  [(call_script, "script_weapon_use_classify_agent")])   
   
common_weapon_use = (
2, 0, 0, [],
   # Check to make sure there are no lance users on foot, if so force them to
   # switch to their sword.
   # For mounted lancers and foot spears, affect their Decision on weapon use,
   # based on if closest 3 enemies are within 5 meters and if currently attacking/defending.
   [
    (get_player_agent_no, ":player"),
    (agent_get_team, ":player_team", ":player"),   
    # Run through all active NPCs on the battle field.
    (try_for_agents, ":agent"),
     # Hasn't been defeated.
        (agent_is_alive, ":agent"),
        (agent_is_human, ":agent"),
            (neq, ":agent", ":player"), #fix motomataru chief
        (agent_get_slot, ":swap_timer", ":agent", slot_agent_weapon_swap),
        (try_begin), #Begin Timer - Only swap weapon once every 24 seconds
            (is_between, ":swap_timer", 1, 12),
            (val_add, ":swap_timer", 1),
            (agent_set_slot, ":agent", slot_agent_weapon_swap, ":swap_timer"),
        (else_try),
            (gt, ":swap_timer", 11),
            (agent_set_slot, ":agent", slot_agent_weapon_swap, 0),
        (try_end),
        (agent_slot_eq, ":agent", slot_agent_weapon_swap, 0), #End Timer - Only swap weapon once every 24 seconds
        (assign, ":caba_order", 3), # -For Caba'drin Orders
        (assign, ":weapon_order", 0),
        (try_begin),
            (agent_get_team, ":team", ":agent"),
            (eq, ":team", ":player_team"),
            (agent_get_division, ":class", ":agent"),
            (team_get_weapon_usage_order, ":weapon_order", ":team", ":class"),
           
            (store_add, ":ordered_class", ":class", slot_party_cabadrin_order_d0),
            (party_get_slot, ":caba_order_index", "p_main_party", ":ordered_class"),
            (store_div, ":caba_order", ":caba_order_index", 100),
            (val_mul, ":caba_order", 100),
            (val_sub, ":caba_order_index", ":caba_order"),
            (store_div, ":caba_order", ":caba_order_index", 10),
            (val_mul, ":caba_order", 10),
            (store_sub, ":caba_order", ":caba_order_index", ":caba_order"),
        (try_end),
        (eq, ":caba_order", 3), # For Caba'drin orders; no active weapon order
        (neq, ":weapon_order", wordr_use_blunt_weapons), #Not ordered to use blunts
        (try_begin),
            (agent_get_slot, ":lance", ":agent", slot_agent_lance),
            (gt, ":lance", 0),  # Lancer?
     # Get wielded item.
            (agent_get_wielded_item, ":wielded", ":agent", 0),
      # They riding a horse?
            (agent_get_horse, ":horse", ":agent"),
            (try_begin),
                (le, ":horse", 0), # Isn't riding a horse.
                (agent_set_slot, ":agent", slot_agent_lance, 0), # No longer a lancer
                (eq, ":wielded", ":lance"), # Still using lance?
                (call_script, "script_weapon_use_backup_weapon", ":agent"), # Then equip a close weapon
                (agent_set_slot, ":agent", slot_agent_weapon_swap, 1), #Swap timer
            (else_try),
     # Still mounted
                (agent_get_position, pos1, ":agent"), # Find distance of nearest 3 enemies
                (call_script, "script_get_closest3_distance_of_enemies_at_pos1", ":team", pos1),
                (assign, ":avg_dist", reg0),
                (assign, ":closest_dist", reg1),
                (try_begin),
                    (this_or_next|lt, ":closest_dist", 300), # Closest enemy within 3 meters?
                    (lt, ":avg_dist", 800), # Are the 3 enemies within an average of 8 meters?
                    (agent_get_combat_state, ":combat", ":agent"),
                    (gt, ":combat", 3), # Agent currently in combat? ...avoids switching before contact
                    (eq, ":wielded", ":lance"), # Still using lance?
                    (call_script, "script_weapon_use_backup_weapon", ":agent"), # Then equip a close weapon
                    (agent_set_slot, ":agent", slot_agent_weapon_swap, 1), #Swap timer
                (else_try),
                    (neq, ":wielded", ":lance"), # Enemies farther than 5 meters and/or not fighting, and not using lance?
                    (agent_set_wielded_item, ":agent", ":lance"), # Then equip it!
                    (agent_set_slot, ":agent", slot_agent_weapon_swap, 1), #Swap timer
                (try_end),
            (try_end),
        (else_try),
            (agent_get_slot, ":spear", ":agent", slot_agent_spear),   
            (gt, ":spear", 0), # Spear-Unit?

            # Motomataru formation exclusion TODO revamp with slot when implemented
            (assign, ":in_formation", 0),
            (agent_get_division, ":division", ":agent"),
            (try_begin),
                (store_add, ":slot", slot_team_d0_type, ":division"),
                (this_or_next|team_slot_eq, ":player_team", ":slot", sdt_infantry),
                (team_slot_eq, ":player_team", ":slot", sdt_polearm),    #formation equip only on infantry
                (store_add, ":slot", slot_team_d0_formation, ":division"),
                (neg|team_slot_eq, ":player_team", ":slot", formation_none),
                (assign, ":in_formation", 1),
            (try_end),
            (eq, ":in_formation", 0),
            #end Motomataru formation exclusion chief

    
            (agent_get_wielded_item, ":wielded", ":agent", 0), # Get wielded
            (agent_get_position, pos1, ":agent"), # Find distance of nearest 3 enemies
            (call_script, "script_get_closest3_distance_of_enemies_at_pos1", ":team", pos1),
            (assign, ":avg_dist", reg0),
            (assign, ":closest_dist", reg1),
            (try_begin),
                (this_or_next|lt, ":closest_dist", 200), # Closest enemy within 2 meters?
                (lt, ":avg_dist", 500), # Are the 3 enemies within an average of 5 meters?
                (agent_get_combat_state, ":combat", ":agent"),
                (gt, ":combat", 3), # Agent currently in combat? ...avoids switching before contact
                (eq, ":wielded", ":spear"), # Still using spear?
                (call_script, "script_weapon_use_backup_weapon", ":agent"), # Then equip a close weapon
                (agent_set_slot, ":agent", slot_agent_weapon_swap, 1), #Swap timer
            (else_try),
                (neq, ":wielded", ":spear"), # Enemies farther than 5 meters and/or not fighting, and not using spear?
                (agent_set_wielded_item, ":agent", ":spear"), # Then equip it! 
                (agent_set_slot, ":agent", slot_agent_weapon_swap, 1), #Swap timer               
            (try_end),
        (try_end),
    (try_end),
    ])
#chief acaba
#####freelancer chief
###freelancer chief
freelancer_siege_triggers = (
    ti_on_agent_spawn, 0, 0, [(eq, "$freelancer_state", 1)],
        [
            (get_player_agent_no, ":player"),
            (ge, ":player", 0),
            (agent_is_active, ":player"),
            (store_trigger_param_1, ":agent_no"),
            (eq, ":player", ":agent_no"),
            (agent_get_team, ":player_team", ":player"),
            (team_set_order_listener, ":player_team", -1),
            (val_add, ":player_team", 2),
            (agent_set_team, ":player", ":player_team"),
        ])
#freelancer acaba chief

###legshot rigale chief
##common_rigale_legshot = (    
##    ti_on_agent_hit, 0, 0, [],    
##    [       
##    (store_trigger_param_1, ":agent"),      
##    (agent_is_human, ":agent"),       
##    (agent_is_active,":agent"),        
##    (agent_is_alive,":agent"), 
##    (store_trigger_param_3, ":damage"),      
##    (set_trigger_result, -1),
##    (ge, ":damage", 15),
##    (set_trigger_result, ":damage"),
###    (ge, ":damage", 10), #strong blow      
###    (store_agent_hit_points, ":hp", ":agent", 1),      
###    (val_sub, ":hp", 5),      
###    (ge, ":damage", ":hp"),      
##    (agent_get_position, pos1, ":agent"),      
##    (get_distance_between_positions, ":distance", pos1, pos0),
##    (try_begin),
##        (is_between, ":damage", 15,31), #strong blow      
##        (is_between, ":distance", 30, 90), #legshot      
##        (agent_set_speed_limit, ":agent", 3),     
##    (else_try),    
##        (is_between, ":damage", 21,31),    
##        (is_between, ":distance", 0, 30), #legshot      
##        (agent_set_animation, ":agent","anim_fall_head_front_legshot"),    
##    (else_try),
##        (gt, ":damage", 30), #strong blow      
##        (is_between, ":distance", 0, 90), #legshot      
##        (agent_set_speed_limit, ":agent", 1), 
##    (try_end),
## 
##    ])
###legshot chief acaba


#tocar instrumento en ciudades chief Entretenimiento bardo
common_play_instrument = (0, 0, 2, [(game_key_clicked, gk_defend)],
   [
    (get_player_agent_no, ":player"),
    (agent_get_wielded_item, ":shield", ":player", 1),
    (is_between, ":shield", instruments_begin, instruments_end),
    (store_random_in_range, ":music", "snd_your_flag_taken", "snd_enemy_scored_a_point"),
    (agent_play_sound, ":player", ":music"),
   ])
#entretenimiento bardo acaba
#####dodge, esquivar de xenoarg
##common_damage_system_1 = (ti_on_agent_hit, 0, 0, [],
##[
##    (store_trigger_param_1, ":agent"),
##    (store_trigger_param_2, ":attacker"),    
##    (store_trigger_param_3, ":damage"),
##    (agent_get_troop_id, ":troop", ":agent"),
##    (agent_get_troop_id, ":attacker_troop", ":attacker"),
##    (assign, ":dodged", 0),
##    (agent_set_no_death_knock_down_only, ":agent", 1), #disable death
##    (agent_set_slot, ":agent", slot_agent_avoid, 0),#clear this value now.
##    
##    #HUMANS
##    (try_begin),
##        (agent_is_human, ":agent"),#branch if not human
##
##        #Damage is avoided 5% per point of Reflexes(formerly Athletics) 3% for non-heroes.
##        (try_begin),
##            (store_skill_level, ":reflexes",  "skl_athletics", ":troop"),
##            (gt, ":reflexes", 0),    
##            (try_begin),
##                (troop_is_hero, ":troop"),
##                (val_mul, ":reflexes", 5),
##            (else_try),
##                (val_mul, ":reflexes", 5),
##            (try_end),
##            (store_random_in_range, ":random_no", 1, 100),
##            (try_begin),
##                (le, ":random_no", ":reflexes"),
##                (assign, ":damage", 0),
##                (assign,":dodged",1),
##                (try_begin),
##                    (eq, ":troop", "trp_player"),
##                    (display_message, "@You dodge the attack!"),
##                (else_try),
##                    (eq, ":attacker_troop", "trp_player"),
##                    (display_message, "@Enemy dodge the attack!"),
##                (try_end),            
##            (try_end),
##        (try_end),        
##        (try_end),        
##    
##        
##    (val_max, ":damage", 0),#No negative damage, plz kthxbai
##    
##    #Display something constructive about damage taken / received.
##    (try_begin),
##        (neq, ":dodged", 1),
##        (eq, ":attacker_troop", "trp_player"),
##        (assign, reg1, ":damage"),
##        (display_message, "@Damage dealt by attack: {reg1}",0xFF11FF11),
##    (else_try),
##        (neq, ":dodged", 1),
##        (eq, ":troop", "trp_player"),
##        (assign, reg1, ":damage"),
##        (display_message, "@Damage taken from attack: {reg1}",0xFFFFFF00),
##    (try_end),
##    
##    (try_begin),
##        (eq, ":dodged", 1),
##        (store_agent_hit_points, ":hp", ":agent", 1), #store current hp
##        (agent_set_slot, ":agent", slot_agent_avoid, ":hp"), #inside slot
##    (else_try),
##        (eq, ":dodged", 2),
##        (store_agent_hit_points, ":hp", ":agent", 1), #store current hp
##        (agent_set_slot, ":agent", slot_agent_avoid, ":hp"), #inside slot            
##    (else_try),
##        (store_agent_hit_points, ":hp", ":agent", 1), #store current hp
##        (val_sub, ":hp", ":damage"),    
##        (try_begin),
##            (gt, ":hp", 0),
##            (agent_set_slot, ":agent", slot_agent_avoid, ":hp"), #set Agent not to die
##        (else_try),
##            (agent_set_slot, ":agent", slot_agent_avoid, 0),
##            (agent_set_no_death_knock_down_only, ":agent", 0), #enable death, Agent is now dead.
##        (try_end),
##    (try_end),
##])

#exp extra CC commander chief
custom_commander_init_hero_begin_xp = (
  0, 0, ti_once, [],
   [
    (try_for_agents, ":agent_no"),
      (agent_is_human, ":agent_no"),
      (agent_get_troop_id, ":troop_no", ":agent_no"),
      (troop_is_hero, ":troop_no"),
      (troop_get_xp, ":troop_xp", ":troop_no"),
      (troop_set_slot, ":troop_no", slot_troop_extra_xp_limit, ":troop_xp"),
    (try_end),
   ])

custom_commander_give_hero_extra_xp = (
  1, 0, 0, [],
   [
    (get_player_agent_no, ":player_agent"),
    (try_for_agents, ":agent_no"),
      (agent_is_human, ":agent_no"),
      (agent_get_troop_id, ":troop_no", ":agent_no"),
      (troop_is_hero, ":troop_no"),
      (troop_get_xp, ":troop_xp", ":troop_no"),
      (troop_get_slot, ":troop_extra_xp_limit", ":troop_no", slot_troop_extra_xp_limit),
      (gt, ":troop_xp", ":troop_extra_xp_limit"),
      (store_sub, ":xp_dif", ":troop_xp", ":troop_extra_xp_limit"),
      (store_attribute_level, ":troop_int", ":troop_no", ca_intelligence),
      (store_mul, ":extra_xp", ":troop_int", 3),
      (val_mul, ":extra_xp", ":xp_dif"),
      (val_div, ":extra_xp", 100),
      (set_show_messages, 0),
      (add_xp_to_troop, ":extra_xp", ":troop_no"),
      (set_show_messages, 1),
      (try_begin),
        (eq, ":agent_no", ":player_agent"),
        (gt, ":extra_xp", 0),
        (eq, "$g_report_extra_xp",1),
        (assign, reg1, ":extra_xp"),
      #  (display_message, "@You got {reg1} extra experience because of your intelligence."), #puesto off chief para no tantos mensajes en batalla
      (try_end),
      (troop_get_xp, ":troop_final_xp", ":troop_no"),
      (troop_set_slot, ":troop_no", slot_troop_extra_xp_limit, ":troop_final_xp"),
      ## add wpn points
      (troop_get_slot, ":troop_cur_xp_for_wp", ":troop_no", slot_troop_cur_xp_for_wp),
      (troop_get_slot, ":troop_xp_limit_for_wp", ":troop_no", slot_troop_xp_limit_for_wp),
      (store_sub, ":xp_added", ":troop_final_xp", ":troop_xp"),
      (val_add, ":troop_cur_xp_for_wp", ":xp_added"),
      (troop_set_slot, ":troop_no", slot_troop_cur_xp_for_wp, ":troop_cur_xp_for_wp"),
      (gt, ":troop_cur_xp_for_wp", ":troop_xp_limit_for_wp"),
      (troop_add_proficiency_points, ":troop_no", 1),
      # increase limit
      (assign, ":xp_limit_added", 16000),
      (store_skill_level, ":skill_bonus", skl_weapon_master, ":troop_no"),
      (val_add, ":skill_bonus", 10),
      (val_div, ":xp_limit_added", ":skill_bonus"),
      (val_add, ":troop_xp_limit_for_wp", ":xp_limit_added"),
      (troop_set_slot, ":troop_no", slot_troop_xp_limit_for_wp, ":troop_xp_limit_for_wp"),
      (try_begin),
        (eq, ":agent_no", ":player_agent"),
        #(display_message, "@You got 1 weapon point.", 0xEEEE00),
      (try_end),
      ## add wpn points
    (try_end),
   ])
##cc commmander xp acaba 
#CC commander chief cambia velocidad del caballo si esta herido y por skill riding
custom_commander_horse_speed = (
  1, 0, 0, [],
  [
  (get_player_agent_no, ":player_agent"),
  (try_for_agents, ":agent_no"),
    (agent_is_alive, ":agent_no"),
    (agent_is_human, ":agent_no"),
    (agent_get_horse, ":horse_agent", ":agent_no"),
    (try_begin),
      (ge, ":horse_agent", 0),
      (store_agent_hit_points, ":horse_hp",":horse_agent"),
      (store_sub, ":lost_hp", 100, ":horse_hp"),
      (try_begin),
        (le, ":lost_hp", 20),
        (val_div, ":lost_hp", 2),
        (store_add, ":speed_factor", 100, ":lost_hp"),
      (else_try),
        (val_div, ":lost_hp", 2),
        (store_sub, ":speed_factor", 120, ":lost_hp"),
      (try_end),
      ## horse charging
      (agent_get_slot, ":horse_stamina", ":agent_no", slot_agent_horse_stamina),
      (agent_get_troop_id, ":agent_troop", ":agent_no"),
      (store_skill_level, ":skl_level", skl_riding, ":agent_troop"),
      (try_begin),
        (eq, ":agent_no", ":player_agent"),
        (try_begin),
          (key_is_down, key_left_control),
          (val_sub, ":horse_stamina", 20),
          (val_add, ":horse_stamina", ":skl_level"),
          (val_max, ":horse_stamina", 0),
          (agent_set_slot, ":agent_no", slot_agent_horse_stamina, ":horse_stamina"),
          (try_begin),
            (le, ":horse_stamina", 0),
            (agent_set_slot, ":agent_no", slot_agent_horse_is_charging, 0),
          (else_try),
            (agent_set_slot, ":agent_no", slot_agent_horse_is_charging, 1),
          (try_end),
        (else_try),
          (agent_set_slot, ":agent_no", slot_agent_horse_is_charging, 0),
          (val_add, ":horse_stamina", 3),
          (store_div, ":half_skl_level", ":skl_level", 3),
          (val_add, ":horse_stamina", ":half_skl_level"),
          (val_min, ":horse_stamina", ":horse_hp"),
          (agent_set_slot, ":agent_no", slot_agent_horse_stamina, ":horse_stamina"),
        (try_end),
        #(assign, reg1, ":horse_stamina"),
        #(display_message, "@Horse Stamina: {reg1}/100"),
      (else_try),
        (try_begin),
          (agent_slot_eq, ":agent_no", slot_agent_horse_is_charging, 0),
          (try_begin),
            (lt, ":horse_stamina", ":horse_hp"),
            (val_add, ":horse_stamina", 6),
            (val_min, ":horse_stamina", ":horse_hp"),
            (agent_set_slot, ":agent_no", slot_agent_horse_stamina, ":horse_stamina"),
            (store_div, ":half_horse_hp", ":horse_hp", 2),
            (store_random_in_range, ":r", ":half_horse_hp", ":horse_hp"),
            (gt, ":horse_stamina", ":r"),
            (agent_set_slot, ":agent_no", slot_agent_horse_is_charging, 1),
          (try_end),
        (else_try),
          (agent_slot_eq, ":agent_no", slot_agent_horse_is_charging, 1),
          (try_begin),
            (gt, ":horse_stamina", 0),
            (val_sub, ":horse_stamina", 10),
            (val_max, ":horse_stamina", 0),
            (agent_set_slot, ":agent_no", slot_agent_horse_stamina, ":horse_stamina"),
            (le, ":horse_stamina", 0),
            (agent_set_slot, ":agent_no", slot_agent_horse_is_charging, 0),
          (try_end),
        (try_end),
      (try_end),
      (try_begin),
        (agent_slot_eq, ":agent_no", slot_agent_horse_is_charging, 1),
        (store_add, ":speed_multi", ":skl_level", 5),
        (val_mul, ":speed_multi", ":speed_multi"),
        (val_div, ":speed_multi", 4),
      (else_try),
        (assign, ":speed_multi", 0),
      (try_end),
      (val_add, ":speed_multi", 100),
      (val_mul, ":speed_factor", ":speed_multi"),
      (val_div, ":speed_factor", 100),
      (agent_set_horse_speed_factor, ":agent_no", ":speed_factor"),
    (try_end),
  (try_end),
  ])
#chief CC pierde renombre si cae en batalla
custom_commander_hero_wounded =(
  ti_on_agent_killed_or_wounded, 0, 0, [],
    [
      (store_trigger_param_1, ":wounded_agent_no"),
      (store_trigger_param_2, ":killer_agent_no"),
      
      (get_player_agent_no, ":player_agent"),
      (agent_get_troop_id, ":player_troop", ":player_agent"),
      
      (try_begin),
        (eq, ":killer_agent_no", ":player_agent"),
        (agent_is_human, ":wounded_agent_no"),
        (agent_get_troop_id, ":wounded_troop", ":wounded_agent_no"),
         (troop_slot_eq, ":wounded_troop", slot_troop_occupation, slto_kingdom_hero),
        (try_begin),
          (troop_is_hero, ":wounded_troop"),
          (store_character_level, ":troop_level", ":wounded_troop"),
          (store_character_level, ":player_level", ":player_troop"),
          (store_sub, ":renown_change", ":troop_level", ":player_level"),
          (val_max, ":renown_change", 0),
          (val_div, ":renown_change", 4),
          (try_begin),
            (agent_is_ally, ":wounded_agent_no"),
            (val_mul, ":renown_change", -1),
          (try_end),
          (call_script,"script_change_troop_renown", ":player_troop", ":renown_change"),
        (try_end),
      (else_try),
        (eq, ":wounded_agent_no", ":player_agent"),
        (agent_is_human, ":killer_agent_no"),
        (agent_get_troop_id, ":killer_troop", ":killer_agent_no"),
        (try_begin),
          (troop_is_hero, ":killer_troop"),
          (store_character_level, ":troop_level", ":killer_troop"),
          (store_character_level, ":player_level", ":player_troop"),
          (store_sub, ":renown_change", ":troop_level", ":player_level"),
          (val_min, ":renown_change", 0),
          (val_div, ":renown_change", 4),
          (call_script,"script_change_troop_renown", ":player_troop", ":renown_change"),
        (try_end),
      (try_end),
    ])
#chief CC renombre acaba
# Register 0: damage dealer item_id Commander criticos chief CC
custom_commander_critical_strike =(
  ti_on_agent_hit, 0, 0, [         (eq, "$sp_criticos", 1),
],
    [
      (store_trigger_param_1, ":inflicted_agent"),
      (store_trigger_param_2, ":dealer_agent"),
      (store_trigger_param_3, ":inflicted_damage"),
      
      (set_trigger_result, -1),
      (gt, ":inflicted_damage", 0),
      (set_trigger_result, ":inflicted_damage"),
      (get_player_agent_no, ":player_agent"),
      (try_begin),
        (agent_is_human, ":dealer_agent"),
        (assign, ":dealer_item_id", reg0),
        (gt, ":dealer_item_id", -1),
        
        (try_begin), 
          ## knock_back between humans with melee weapons
          (agent_is_human, ":inflicted_agent"),
          (agent_get_position, pos1, ":inflicted_agent"),
          (agent_get_position, pos2, ":dealer_agent"),
          (try_begin),
            (position_is_behind_position, pos2, pos1),
            (item_get_type, ":item_type", ":dealer_item_id"),
            (this_or_next|eq, ":item_type", itp_type_one_handed_wpn),
            (this_or_next|eq, ":item_type", itp_type_two_handed_wpn),
            (eq, ":item_type", itp_type_polearm),
            # dest damage ratio is 1/2
            (assign, ":dest_damage", ":inflicted_damage"),
            (val_div, ":dest_damage", 3),#gdw3
            (store_agent_hit_points, ":inflicted_agent_hp", ":inflicted_agent", 1),
            (val_sub, ":inflicted_agent_hp", ":dest_damage"),
            (val_max, ":inflicted_agent_hp", 0),
            (agent_set_hit_points, ":inflicted_agent", ":inflicted_agent_hp", 1),
            # messages for player
            (assign, reg1, ":dest_damage"),
            (try_begin),
              (eq, ":dealer_agent", ":player_agent"),
              (display_message, "@Delivered {reg1} extra damage from behind!", 0xFF0000),
            (else_try),
              (eq, ":inflicted_agent", ":player_agent"),
              (display_message, "@Received {reg1} extra damage from behind!", 0xFF0000),
            (try_end),
          (try_end),
        (else_try),
          # inflicted_agent is horse, dealer_troop is on foot and uses polearm or thrust
          (neg|agent_is_human, ":inflicted_agent"),
          (agent_get_horse, ":dealer_agent_horse_id", ":dealer_agent"),
          (eq, ":dealer_agent_horse_id", -1),
          (agent_get_action_dir, ":action_dir", ":dealer_agent"),
          (item_get_type, ":item_type", ":dealer_item_id"),
          (assign, ":extra_damage_rate", 0),
          (try_begin),
            (eq, ":item_type", itp_type_polearm),
            (try_begin),
              (eq, ":action_dir", 0),
              (assign, ":extra_damage_rate", 150), #chief incrementa#gdw180 mod already has doubled power of spears was at 180
                (store_random_in_range, ":random_no", 1, 100),
                (try_begin), #el caballo retrocede chief
                    (le, ":random_no", 50),
                    (agent_set_animation, ":inflicted_agent","anim_horse_rear"),
                (try_end),
            (else_try),
                (assign, ":extra_damage_rate", 90), #chief incrementa #gdw120 
            (try_end),
          (else_try),
            #(this_or_next|eq, ":item_type", itp_type_one_handed_wpn),#gdw two handers much more likely to damage plus i've separated them from polearms in the battleorers menu
            (eq, ":item_type", itp_type_two_handed_wpn),
            (eq, ":action_dir", 0),
            (assign, ":extra_damage_rate", 60),#gdw75 why even include these?
          (try_end),
          (gt, ":extra_damage_rate", 0),
          (store_mul, ":extra_damage", ":inflicted_damage", ":extra_damage_rate"),
          (val_div, ":extra_damage", 100),
          (store_agent_hit_points, ":inflicted_agent_hp", ":inflicted_agent", 1),
          (val_sub, ":inflicted_agent_hp", ":extra_damage"),
          (val_max, ":inflicted_agent_hp", 0),
          (agent_set_hit_points, ":inflicted_agent", ":inflicted_agent_hp", 1),
          # messages for player
          (assign, reg1, ":extra_damage"),
          (try_begin),
            (eq, ":dealer_agent", ":player_agent"),
            (try_begin),
              (agent_get_rider, ":rider_agent", ":inflicted_agent"),
              (gt, ":rider_agent", -1),
              (display_message, "@Delivered {reg1} extra damage to horse."),
            (else_try),
              (display_message, "@Delivered {reg1} extra damage."),
            (try_end),
          (try_end),
          (try_begin),
            (agent_get_horse, ":player_horse_id", ":player_agent"),
            (eq, ":player_horse_id", ":inflicted_agent"),
            (display_message, "@Horse received {reg1} extra damage."),
          (try_end),
        (try_end),
      (try_end),
    ])
###custom commander CC acaba chief
##############Spear bracing The Mercenary empieza chief, retocado por floris
##Spear Bracing Kit by The Mercenary
##spearwall_trigger_1 = (0.2, 0, ti_once, [], [
##        (assign,"$spear_in_position",0),
##        (assign,"$setting_use_spearwall",1),
##        (try_for_agents,":agent"),
##          (agent_set_slot,":agent",slot_agent_spearwall,0),
##          (agent_set_slot,":agent",slot_agent_x,0),
##          (agent_set_slot,":agent",slot_agent_y,0),
##          (agent_set_slot,":agent",slot_agent_z,0),
##          (agent_set_slot,":agent",slot_agent_speed,0),
##        (try_end),
##        ])
##
##spearwall_trigger_2 = (0.2, 0, 0, [(eq,"$setting_use_spearwall",1)], [
##        (set_fixed_point_multiplier, 100),
##        (try_for_agents,":agent"),
##          (agent_is_alive,":agent"),
##          (agent_get_slot,":oldagentx",":agent",slot_agent_x),
##          (agent_get_slot,":oldagenty",":agent",slot_agent_y),
##          (agent_get_slot,":oldagentz",":agent",slot_agent_z),
##          (agent_get_position, pos1, ":agent"),
##          (position_get_x,":agentx",pos1),
##          (position_get_y,":agenty",pos1),
##          (position_get_z,":agentz",pos1),
##          (position_set_x,pos2,":oldagentx"),
##          (position_set_y,pos2,":oldagenty"),
##          (position_set_z,pos2,":oldagentz"),
##          (position_set_x,pos1,":agentx"),
##          (position_set_y,pos1,":agenty"),
##          (position_set_z,pos1,":agentz"),
##          (get_distance_between_positions,":speed",pos1,pos2),
##          (agent_set_slot,":agent",slot_agent_x,":agentx"),
##          (agent_set_slot,":agent",slot_agent_y,":agenty"),
##          (agent_set_slot,":agent",slot_agent_z,":agentz"),
##          (agent_set_slot,":agent",slot_agent_speed,":speed"),
##        (try_end),
##        ])
##
##spearwall_trigger_3 = (0, 0, 0, [(eq,"$spear_in_position",1),(this_or_next|game_key_clicked, gk_attack),
##        (this_or_next|game_key_clicked, gk_defend),(this_or_next|game_key_clicked, gk_defend),
##        (this_or_next|game_key_clicked, gk_move_forward),(this_or_next|game_key_clicked, gk_move_backward),
##        (this_or_next|game_key_clicked, gk_move_left),(this_or_next|game_key_clicked, gk_move_right),
##        (this_or_next|game_key_clicked, gk_equip_primary_weapon),(this_or_next|game_key_clicked, gk_equip_secondary_weapon),
##        (this_or_next|game_key_clicked, gk_action),(game_key_clicked, gk_sheath_weapon)
##        ],
##       [(get_player_agent_no,":player"),
##        (agent_is_alive,":player"),
##        (display_message,"@Releasing spear.",0x6495ed),
##        (agent_set_animation, ":player", "anim_release_thrust_staff"),
##        (assign,"$spear_in_position",0),
##        ])
##
##spearwall_trigger_4 = (0.2, 0, 0, [(eq,"$setting_use_spearwall",1)], [
##        (try_for_agents,":agent"),
##          (agent_get_horse,":horse",":agent"),
##          (neg|gt,":horse",0),
##          (agent_get_slot,":speartimer",":agent",slot_agent_spearwall),
##          (lt,":speartimer",10),
##          (val_add,":speartimer",2),
##          (agent_set_slot,":agent",slot_agent_spearwall,":speartimer"),
##        (try_end),
##        ])
##
##spearwall_trigger_5 = (3, 0, 0, [(eq,"$spear_in_position",1)],[
##        (get_player_agent_no,":player"),
##        (agent_is_alive,":player"),
##        (agent_set_animation, ":player", "anim_spearwall_hold"),
##        ])
##
##spearwall_trigger_6 = (0.1, 0, 0, [(eq,"$setting_use_spearwall",1)], [
##        (get_player_agent_no,":player"),
##        (agent_get_team,":playerteam",":player"),
##        (try_for_agents,":agent"),
##           (agent_is_alive,":agent"),
##           (neq,":agent",":player"),
##           (agent_is_human,":agent"),
##           (agent_get_horse,":horse",":agent"),
##           (neg|gt,":horse",0),
##           (agent_get_slot,":speartimer",":agent",slot_agent_spearwall),
##           (ge,":speartimer",10),
##           (agent_get_simple_behavior,":state",":agent"),
##           (agent_get_team,":team1",":agent"),
##           (agent_get_class,":class",":agent"),
##           (team_get_movement_order,":order",":team1",":class"),
##           (assign,":continue",0),
##           (try_begin),
##              (neq,":team1",":playerteam"),
##              (this_or_next|eq,":state",aisb_hold),
##              (this_or_next|eq,":state",aisb_flock),
##              (eq,":state",aisb_go_to_pos),
##              (assign,":continue",1),
##           (else_try),
##              (this_or_next|eq,":order",mordr_hold),
##              (eq,":order",mordr_stand_ground),
##              (this_or_next|eq,":state",aisb_hold),
##              (this_or_next|eq,":state",aisb_flock),
##              (this_or_next|eq,":state",aisb_melee),
##              (eq,":state",aisb_go_to_pos),
##              (assign,":continue",1),
##           (try_end),
##           (eq,":continue",1),
##           (assign,":continue",0),
##           (try_begin),
##              (eq,":team1",":playerteam"),
##              #(eq,"$rout",0),
##              (assign,":continue",1),
##           (else_try),
##              #(eq,"$airout",0),
##              (assign,":continue",1),
##           (try_end),
##           (eq,":continue",1),
##           (assign,":continue",0),
##           (agent_get_wielded_item, ":handone", ":agent", 0),
##           (agent_get_wielded_item, ":handtwo", ":agent", 1),
##           (assign,"$spear_dist",145),
##           (try_for_range,":spear","itm_staff_pitchfork","itm_wessexbanner1"),
##              (this_or_next|eq,":handone",":spear"),
##              (eq,":handtwo",":spear"),
##              (assign,":continue",1),
##              (try_begin),
##                 (eq,":spear","itm_staff_pitchfork"),
##                 (assign,"$spear_dist",154),
##              (else_try),
##                 (eq,":spear","itm_spear_sharppitchfork"),
##                 (assign,"$spear_dist",154),
##              (else_try),
##                 (eq,":spear","itm_spear_hvy"),
##                 (assign,"$spear_dist",154),
##              (else_try),
##                 (eq,":spear","itm_spear1"),
##                 (assign,"$spear_dist",149),
##              (else_try),
##                 (eq,":spear","itm_spearlight"),
##                 (assign,"$spear_dist",159),
##              (else_try),
##                 (eq,":spear","itm_spear_hasta"),
##                 (assign,"$spear_dist",154),
##              (else_try),
##                 (eq,":spear","itm_spearboar"),
##                 (assign,"$spear_dist",154),
##              (else_try),
##                 (eq,":spear","itm_spearlong"),
##                 (assign,"$spear_dist",259),
##              (else_try),
##                 (eq,":spear","itm_spearwarlong"),
##                 (assign,"$spear_dist",254),
##              (else_try),
##                 (eq,":spear","itm_spear_blade2t2"),
##                 (assign,"$spear_dist",164),
##              (else_try),
##                 (eq,":spear","itm_spear_blade2t2"),
##                 (assign,"$spear_dist",154),
##              (else_try),
##                 (eq,":spear","itm_spear_blade2t2"),
##                 (assign,"$spear_dist",154),
##              (else_try),
##                 (eq,":spear","itm_spear_briton2ht3"),
##                 (assign,"$spear_dist",261),
##              (else_try),
##                 (eq,":spear","itm_spear_britonshortt2"),
##                 (assign,"$spear_dist",161),
##              (else_try),
##                 (eq,":spear","itm_spear_britonmedt2"),
##                 (assign,"$spear_dist",166),
##              (else_try),
##                 (eq,":spear","itm_spear_britonlight"),
##                 (assign,"$spear_dist",254),
##              (else_try),
##                 (eq,":spear","itm_spear_briton_longt2"),
##                 (assign,"$spear_dist",231),
##              (else_try),
##                 (eq,":spear","itm_longspeart3"),
##                 (assign,"$spear_dist",251),
##              (else_try),
##                 (eq,":spear","itm_twohand_speart3"),
##                 (assign,"$spear_dist",199),
##              (else_try),
##                 (eq,":spear","itm_germanshortspeart2"),
##                 (assign,"$spear_dist",122),
##              (else_try),
##                 (eq,":spear","itm_saxon_medium_speart2"),
##                 (assign,"$spear_dist",175),
##              (else_try),
##                 (eq,":spear","itm_engle_speart2"),
##                 (assign,"$spear_dist",235),
##              (else_try),
##                 (eq,":spear","itm_hunting_spear"),
##                 (assign,"$spear_dist",149),
##              (else_try),
##                 (eq,":spear","itm_hunting_spear"),
##                 (assign,"$spear_dist",157),
##              (else_try),
##                 (eq,":spear","itm_medium_speaript3"),
##                 (assign,"$spear_dist",157),
##              (else_try),
##                 (eq,":spear","itm_pictish_boar_speart2"),
##                 (assign,"$spear_dist",145),
##              (else_try),
##                 (eq,":spear","itm_warspear_godelict3"),
##                 (assign,"$spear_dist",145),
##              (else_try),
##                 (eq,":spear","itm_spear_lightgael"),
##                 (assign,"$spear_dist",145),
##              (else_try),
##                 (eq,":spear","itm_spear_elitequest1"),
##                 (assign,"$spear_dist",180),
##              (else_try),
##                 (eq,":spear","itm_spear_elitequest2"),
##                 (assign,"$spear_dist",155),
##              (else_try),
##                 (eq,":spear","itm_spear_elitequest3"),
##                 (assign,"$spear_dist",155),
##              (else_try),
##                 (eq,":spear","itm_saxon_medium_speart2"),
##                 (assign,"$spear_dist",165),
##              (else_try),
##                 (eq,":spear","itm_saxon_medium_speart2"),
##                 (assign,"$spear_dist",180),
##              (else_try),
##                 (assign,":continue",0),
##              (try_end),
##           (try_end),
##           (eq,":continue",1),
##           (assign,":victim",-1),
##           (agent_get_position,pos1,":agent"),
##           (try_for_agents,":possible_victim"),
##              (agent_is_alive,":possible_victim"),
##              (neg|agent_is_human,":possible_victim"),
##              (agent_get_rider,":rider",":possible_victim"),
##              (ge,":rider",0),
##              (agent_get_team,":team2",":rider"),
##              (teams_are_enemies,":team1",":team2"),
##              (agent_get_position,pos2,":possible_victim"),
##              (get_distance_between_positions,":dist",pos1,pos2),
##              (lt,":dist","$spear_dist"),
##              (neg|position_is_behind_position,pos2,pos1),
##              (agent_get_slot,":speed",":possible_victim",slot_agent_speed),
##              (ge,":speed",120), # Remember to change this if the timing on speed checks changes
##              (assign,":victim",":possible_victim"),
##           (try_end),
##           (gt,":victim",-1),
##           (agent_set_animation, ":agent", "anim_spearwall_hold"),
##           (agent_play_sound,":victim","snd_metal_hit_high_armor_high_damage"),
##           (agent_set_animation,":victim","anim_horse_rear"), #anadida animacion para que caballo retroceda
##           (store_agent_hit_points,":hp",":victim",0),
##           (store_agent_hit_points,":oldhp",":victim",1),
###Floris: disabled those lines to make the spear brace even more effective.
###           (val_div,":speed",2), # Remember to change this if the timing on speed checks changes
###           (val_sub,":speed",15),
##           (val_sub,":hp",":speed"),
##           (val_max,":hp",0),
##           (agent_set_slot,":agent",slot_agent_spearwall,0),
##           (agent_get_horse,":playerhorse",":player"),           
##           (agent_set_hit_points,":victim",":hp",0),
##           (agent_deliver_damage_to_agent,":victim",":victim"),
##           (try_begin),
##              (eq,":victim",":playerhorse"),
##              (store_agent_hit_points,":hp",":victim",1),
##              (val_sub,":oldhp",":hp"),
##              (assign,reg1,":oldhp"),
##              (display_message,"@Your horse received {reg1} damage from a braced spear!",0xff4040),
##           (try_end),
##        (try_end),
##        ])
##
##spearwall_trigger_7 = (0.1, 0, 0, [(eq,"$spear_in_position",1)], [
##        (get_player_agent_no,":player"),
##        (agent_is_alive,":player"),
##        (store_agent_hit_points,":hp",":player",1),
##        (lt,":hp","$spear_hp"),
##        (display_message,"@The injury causes your grip on the spear to slip!",0xff4040),
##        (agent_set_animation, ":player", "anim_release_thrust_staff"),
##        (assign,"$spear_in_position",0),
##        ])
##
##spearwall_trigger_8 = (0.1, 0, 0, [(eq,"$spear_in_position",1)], [
##        (get_player_agent_no,":player"),
##        (agent_is_alive,":player"),
##        (agent_get_slot,":speartimer",":player",slot_agent_spearwall),
##        (ge,":speartimer",10),
##        (assign,":victim",-1),
##        (agent_get_position,pos1,":player"),
##        (try_for_agents,":possible_victim"),
##           (agent_is_alive,":possible_victim"),
##           (neg|agent_is_human,":possible_victim"),
##           (agent_get_rider,":rider",":possible_victim"),
##           (ge,":rider",0),
##           (neg|agent_is_ally,":rider"),
##           (agent_get_position,pos2,":possible_victim"),
##           (get_distance_between_positions,":dist",pos1,pos2),
##           (lt,":dist","$spear_dist"),
##           (neg|position_is_behind_position,pos2,pos1),
##           (agent_get_slot,":speed",":possible_victim",slot_agent_speed),
##           (ge,":speed",120), # Remember to change this if the timing on speed checks changes
##           (assign,":victim",":possible_victim"),
##        (try_end),
##        (gt,":victim",-1),
##        (agent_play_sound,":victim","snd_metal_hit_high_armor_high_damage"),
##        (store_agent_hit_points,":hp",":victim",0),
##        (store_agent_hit_points,":oldhp",":victim",1),
###Floris: disabled those lines to make the spear brace even more effective.
###        (val_div,":speed",2), # Remember to change this if the timing on speed checks changes
###       (val_sub,":speed",15),
##        (val_sub,":hp",":speed"),
##        (val_max,":hp",0),
##        (agent_set_hit_points,":victim",":hp",0),
##        (agent_deliver_damage_to_agent,":victim",":victim"),
##        (agent_set_slot,":player",slot_agent_spearwall,0),
##        (store_agent_hit_points,":hp",":victim",1),
##        (val_sub,":oldhp",":hp"),
##        (assign,reg1,":oldhp"),
##        (display_message,"@Spear-wall dealt {reg1} damage!"),
##        ])
##
##spearwall_trigger_9 = (0, 0, 2, [(key_clicked, key_j),(eq,"$setting_use_spearwall",1)],
##       [(assign,":continue",0),
##        (get_player_agent_no,":player"),
##        (agent_is_alive,":player"),
##        (agent_get_wielded_item, ":handone", ":player", 0),
##        (agent_get_wielded_item, ":handtwo", ":player", 1),
##        (assign,"$spear_dist",145),
##           (try_for_range,":spear","itm_staff_pitchfork","itm_wessexbanner1"),
##              (this_or_next|eq,":handone",":spear"),
##              (eq,":handtwo",":spear"),
##              (assign,":continue",1),
##              (try_begin),
##                 (eq,":spear","itm_staff_pitchfork"),
##                 (assign,"$spear_dist",154),
##              (else_try),
##                 (eq,":spear","itm_spear_sharppitchfork"),
##                 (assign,"$spear_dist",154),
##              (else_try),
##                 (eq,":spear","itm_spear_hvy"),
##                 (assign,"$spear_dist",154),
##              (else_try),
##                 (eq,":spear","itm_spear1"),
##                 (assign,"$spear_dist",149),
##              (else_try),
##                 (eq,":spear","itm_spearlight"),
##                 (assign,"$spear_dist",159),
##              (else_try),
##                 (eq,":spear","itm_spear_hasta"),
##                 (assign,"$spear_dist",154),
##              (else_try),
##                 (eq,":spear","itm_spearboar"),
##                 (assign,"$spear_dist",154),
##              (else_try),
##                 (eq,":spear","itm_spearlong"),
##                 (assign,"$spear_dist",259),
##              (else_try),
##                 (eq,":spear","itm_spearwarlong"),
##                 (assign,"$spear_dist",254),
##              (else_try),
##                 (eq,":spear","itm_spear_blade2t2"),
##                 (assign,"$spear_dist",164),
##              (else_try),
##                 (eq,":spear","itm_spear_blade2t2"),
##                 (assign,"$spear_dist",154),
##              (else_try),
##                 (eq,":spear","itm_spear_blade2t2"),
##                 (assign,"$spear_dist",154),
##              (else_try),
##                 (eq,":spear","itm_spear_briton2ht3"),
##                 (assign,"$spear_dist",261),
##              (else_try),
##                 (eq,":spear","itm_spear_britonshortt2"),
##                 (assign,"$spear_dist",161),
##              (else_try),
##                 (eq,":spear","itm_spear_britonmedt2"),
##                 (assign,"$spear_dist",166),
##              (else_try),
##                 (eq,":spear","itm_spear_britonlight"),
##                 (assign,"$spear_dist",254),
##              (else_try),
##                 (eq,":spear","itm_spear_briton_longt2"),
##                 (assign,"$spear_dist",231),
##              (else_try),
##                 (eq,":spear","itm_longspeart3"),
##                 (assign,"$spear_dist",251),
##              (else_try),
##                 (eq,":spear","itm_twohand_speart3"),
##                 (assign,"$spear_dist",199),
##              (else_try),
##                 (eq,":spear","itm_germanshortspeart2"),
##                 (assign,"$spear_dist",122),
##              (else_try),
##                 (eq,":spear","itm_saxon_medium_speart2"),
##                 (assign,"$spear_dist",175),
##              (else_try),
##                 (eq,":spear","itm_engle_speart2"),
##                 (assign,"$spear_dist",235),
##              (else_try),
##                 (eq,":spear","itm_hunting_spear"),
##                 (assign,"$spear_dist",149),
##              (else_try),
##                 (eq,":spear","itm_hunting_spear"),
##                 (assign,"$spear_dist",157),
##              (else_try),
##                 (eq,":spear","itm_medium_speaript3"),
##                 (assign,"$spear_dist",157),
##              (else_try),
##                 (eq,":spear","itm_pictish_boar_speart2"),
##                 (assign,"$spear_dist",145),
##              (else_try),
##                 (eq,":spear","itm_warspear_godelict3"),
##                 (assign,"$spear_dist",145),
##              (else_try),
##                 (eq,":spear","itm_spear_lightgael"),
##                 (assign,"$spear_dist",145),
##              (else_try),
##                 (eq,":spear","itm_spear_elitequest1"),
##                 (assign,"$spear_dist",180),
##              (else_try),
##                 (eq,":spear","itm_spear_elitequest2"),
##                 (assign,"$spear_dist",155),
##              (else_try),
##                 (eq,":spear","itm_spear_elitequest3"),
##                 (assign,"$spear_dist",155),
##              (else_try),
##                 (eq,":spear","itm_saxon_medium_speart2"),
##                 (assign,"$spear_dist",165),
##              (else_try),
##                 (eq,":spear","itm_saxon_medium_speart2"),
##                 (assign,"$spear_dist",180),
##              (else_try),
##                 (assign,":continue",0),
##              (try_end),
##        (try_end),
##        (eq,":continue",1),
##          (agent_get_horse,":horse",":player"),
##        (neg|gt,":horse",0),
##        (neq, "$spear_in_position", 1),
##        (display_message,"@Bracing spear for charge.",0x6495ed),
##        (agent_set_animation, ":player", "anim_spearwall_hold"),
##        (assign, "$spear_in_position", 1),
##        (store_agent_hit_points,"$spear_hp",":player",1),
##        ])
#######spear bracing acaba chief
###chief multiplayer chief
#####

###first aid
##first_aid_multi = (0, 0, 60, [(key_clicked, key_h)], # o pressed?
##
##        [
##      (store_trigger_param_1, ":agent_id"),
##      (multiplayer_is_server),
##      (assign, ":cost", 500), #gold required for healing
##      (agent_get_player_id,":player_no",":agent_id"),
##      (try_begin),
##        (player_is_active, ":player_no"),
##        (player_get_gold, ":player_gold", ":player_no"),
##        (gt, ":player_gold", ":cost"),
##       (agent_set_hit_points,":agent_id",100,0), #refill health
##        (val_sub, ":player_gold", ":cost"),
##        (player_set_gold, ":player_no", ":player_gold", multi_max_gold_that_can_be_stored),
##         (display_message,"@You treat your wounds!",0x6495ed),
##            (multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_pevic_thrust"),
####        (else_try),
####         (display_message,"@You cannt do this now!",0x6495ed),
##      (try_end),
##
####             (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_man_warcry"),
####             (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_shield_hit_metal_wood"),
####            (multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_taunt"),
##
##        ])

multi_warcry = (0, 0, 60, [(key_clicked, key_b)], # o pressed?
                             
        [

        (multiplayer_get_my_player,":player_no"),
           (neg|player_is_busy_with_menus, ":player_no"),
              (player_get_agent_id, ":player_agent",":player_no"),
      (agent_is_human, ":player_agent"),
       (agent_get_horse,":agent_mounted",":player_agent"),
           (eq,":agent_mounted",-1),

             (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_man_warcry"),
             (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_shield_hit_metal_wood"),
            (multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_taunt"),
            
        ])


hunt_taunting = (0, 0, 60, [(key_clicked, key_u)], # o pressed?
                             
        [
                 #  (multiplayer_is_server),
        (multiplayer_get_my_player,":player_no"),
           (neg|player_is_busy_with_menus, ":player_no"),
              (player_get_agent_id, ":player_agent",":player_no"),
      (agent_is_human, ":player_agent"),
       (agent_get_horse,":agent_mounted",":player_agent"),
           (eq,":agent_mounted",-1),

               (try_begin),
                     (agent_get_wielded_item, ":wielded",":player_agent", 0),
                (this_or_next|eq, ":wielded", "itm_horn1"),#hornhealer
                   (this_or_next|eq, ":wielded", "itm_horn_of_arthur"),#horn of rheged 
                   (eq, ":wielded", "itm_horn_multiplayer"), # tiene cuerno?

          (agent_get_position,pos6,":player_agent"),
          (agent_get_team, ":wielder_team", ":player_agent"),
          (assign, ":heal_count", 0),
          (try_for_agents,":agent"),
              (agent_is_alive,":agent"),    
              (agent_get_team, ":target_team", ":agent"),
              (eq, ":target_team", ":wielder_team"),
                   (agent_set_slot,":agent", slot_agent_has_been_healed, 0), #chief
              #(neq,":agent",":player_agent"),
              (agent_get_position,pos4,":agent"),
              (get_distance_between_positions,":dist",pos6,pos4),
              (le,":dist",3500),
              (agent_get_slot, ":healed", ":agent", slot_agent_has_been_healed),
              (eq, ":healed", 0),
                          (store_agent_hit_points, ":cur_hp",":agent",0),
                          (try_begin),
                              (lt,":cur_hp",100),
                              (store_agent_hit_points, ":cur_hit_points",":agent",1),
                              (val_add,":cur_hit_points",6),
                              (agent_set_hit_points,":agent",":cur_hit_points",1),
              
                              (agent_set_slot,":agent", slot_agent_has_been_healed, 1),
                              (val_add, ":heal_count", 1),
##                (agent_get_player_id,":player",":agent"), #msg para heal #puesto off para no saturar de mensajes
##                     (multiplayer_send_2_int_to_server,multiplayer_event_message_server, 6, ":player"), ### 1 ist the number of healing
                 #   (display_message, "@You heallllll ally."),
                          (try_end),
                 (try_end),                
            (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_horn"),
            (multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_tekst"),
            #(multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_howl"),
        (else_try),
            (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_man_warcry"),
            (multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_howl"),
        (try_end),
            
        ])

multi_ambient_sounds = (1,0,30,[],[
         
        (store_current_scene,":current_scene"),
    #    (store_random_in_range,":random",0,8),

        (try_begin),
##            (eq,":random",0),
            (this_or_next|eq,":current_scene","scn_multi_scene_4"),
            (this_or_next|eq,":current_scene","scn_multi_scene_7"),
            (this_or_next|eq,":current_scene","scn_multi_scene_13"),
            (eq,":current_scene","scn_multi_scene_10"),
            (play_sound,"snd_desert_winds"),
        (else_try),
            (this_or_next|eq,":current_scene","scn_multi_scene_1"),
            (eq,":current_scene","scn_multi_scene_9"),
            (play_sound,"snd_marsh_bugs"),
        (else_try),
##            (eq,":random",1),
            (eq,":current_scene","scn_multi_scene_2"),
            (play_sound,"snd_heavy_waves_on_shore"),
        (else_try),
##            (eq,":random",2),
            (this_or_next|eq,":current_scene","scn_multi_scene_14"),
            (eq,":current_scene","scn_multi_scene_3"),
            (play_sound,"snd_wind_heavy"),
        (else_try),
##            (eq,":random",1),
            (this_or_next|eq,":current_scene","scn_multi_scene_12"),
            (this_or_next|eq,":current_scene","scn_multi_scene_16"),
            (this_or_next|eq,":current_scene","scn_multi_scene_17"),
            (eq,":current_scene","scn_multi_scene_8"),
            (play_sound,"snd_wind_solobird"),
        (else_try),
##            (eq,":random",2),
            (eq,":current_scene","scn_multi_scene_11"),
            (play_sound,"snd_wind_through_trees"),
        (end_try),
        ])

siege_multi_items = (1,0,800,[(multiplayer_is_server)],[
         
        (try_for_range,":entry",40,50), #para atacantes
            (entry_point_get_position,pos1,":entry"),
            (set_spawn_position,pos1),
            (spawn_item,"itm_torch",0),
        (end_try),

        (try_for_range,":entry",2,15), #para defensores
            (entry_point_get_position,pos1,":entry"),
            (set_spawn_position,pos1),
            (spawn_item,"itm_bolts",0),
        (end_try),
        
        (try_for_range,":entry",16,22), #para defensores
            (entry_point_get_position,pos1,":entry"),
            (set_spawn_position,pos1),
            (spawn_item,"itm_scale_arm_gloves",0),
        (end_try),

##        (store_random_in_range,":chance",0,3), # 1 in 3 chance of spawning salmon
##        
##        (try_begin),
##            (eq,":chance",0),
##            (store_random_in_range,":salmon",0,50),
##            (entry_point_get_position,pos1,":salmon"),
##            (set_spawn_position,pos1),
##            (spawn_item,"itm_salmon_sword",0), # fear the salmon
##        (end_try),
        
        # For now removed pistol and replaced with hunting knife.
        
        # (try_for_range,":entry",95,100),
            # (entry_point_get_position,pos1,":entry"),
            # (set_spawn_position,pos1),
            # (spawn_item,"itm_basic_sling",0),
            # (position_move_x,pos1,10,0),
            # (spawn_item,"itm_cartridges",0),
        # (end_try),
        
        ])    
#chief multiplayer acaba
############################################################################ banners dan vida a tropas cercanas age of blades
banner_heal_multi = (0, 0, 60, [(key_clicked, key_j)], # o pressed?
                             
        [         # (multiplayer_is_server),
            (multiplayer_get_my_player,":player_no"),
           (neg|player_is_busy_with_menus, ":player_no"),

              (player_get_agent_id, ":player_agent",":player_no"),
                     (agent_get_wielded_item, ":wielded",":player_agent", 0),
#           (try_for_range,":spear","itm_wessexbanner1","itm_heraldicbannert3"),
              (this_or_next|eq,":wielded","itm_wessexbanner1"),
              (this_or_next|eq,":wielded","itm_cavalrybannert2"),
              (this_or_next|eq,":wielded","itm_spearbannert2"),
              (this_or_next|eq,":wielded","itm_spearbanner4"),
              (this_or_next|eq,":wielded","itm_spearbanner5"),
              (this_or_next|eq,":wielded","itm_wessexbanner6"),
              (this_or_next|eq,":wielded","itm_wessexbanner7"),
              (this_or_next|eq,":wielded","itm_wessexbanner8"),
              (eq,":wielded","itm_wessexbanner9"),
#cura
          (agent_get_position,pos6,":player_agent"),
          (agent_get_team, ":wielder_team", ":player_agent"),
          (assign, ":heal_count", 0),
          (try_for_agents,":agent"),
              (agent_is_alive,":agent"),    
              (agent_get_team, ":target_team", ":agent"),
              (eq, ":target_team", ":wielder_team"),
              #(neq,":agent",":player_agent"),
                   (agent_set_slot,":agent", slot_agent_has_been_healed, 0), #chief
              (agent_get_position,pos4,":agent"),
              (get_distance_between_positions,":dist",pos6,pos4),
              (le,":dist",1500),
              (agent_get_slot, ":healed", ":agent", slot_agent_has_been_healed),
              (eq, ":healed", 0),
                          (store_agent_hit_points, ":cur_hp",":agent",0),
                          (try_begin),
                              (lt,":cur_hp",100),
                              (store_agent_hit_points, ":cur_hit_points",":agent",1),
                              (val_add,":cur_hit_points",20),
                              (agent_set_hit_points,":agent",":cur_hit_points",1),
              
                              (agent_set_slot,":agent", slot_agent_has_been_healed, 1),
                              (val_add, ":heal_count", 1),
##                (agent_get_player_id,":player",":agent"), #msg para heal #puesto off chief para no saturar
##                     (multiplayer_send_2_int_to_server,multiplayer_event_message_server, 7, ":player"), ### 1 ist the number of healing
#             (display_message, "@You heallllll ally."),
                          (try_end),
                 (try_end),
#curas
                        (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_crash"),
            (multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_pevic_thrust"),
            
        ])

#1 fire arrow chief empieza siege warfare
fire_arrow_initialize_multi = (0, 0, ti_once, [],[
        (set_fixed_point_multiplier, 100),
        (get_scene_boundaries, pos20, pos21),
        (position_get_x, "$g_min_x", pos20),
        (position_get_y, "$g_min_y", pos20),
        (position_get_x, "$g_max_x", pos21),
        (position_get_y, "$g_max_y", pos21),
        (assign, "$g_min_z", 5),
        (assign, "$g_max_z", 6000),
        (val_add, "$g_min_x", 6),
        (val_add, "$g_min_x", 6),
        (val_sub, "$g_max_x", 6),
        (val_sub, "$g_max_y", 6),
        #(assign, reg1, "$g_min_x"),
        #(assign, reg2, "$g_max_x"),
        #(assign, reg3, "$g_min_y"),
        #(assign, reg4, "$g_max_y"),
        #(assign, reg5, "$g_min_z"),
        #(assign, reg6, "$g_max_z"),
        #(display_message, "@DEBUG: x({reg1}-{reg2}) y({reg3}-{reg4}) z({reg5}-{reg6})"),
])

fire_arrow_routine_multi = (0.01, 0, 0,
  [ ],#(troop_slot_ge, "trp_global_value", slot_gloval_max_fire_arrow, 1),
  [
      (multiplayer_is_server),
    (call_script, "script_fire_arrow_routine"),
  ])
  
toggle_fire_arrow_mode_multi = (0, 0, 0, [], #Highlander a esto le anadimos lo de los nombres chiefg
  [
        (try_begin),
    (troop_get_slot, ":key", "trp_global_value", slot_gloval_fire_arrow_key), 
    (key_clicked, ":key"), ###tecla h chief
    (call_script,"script_toggle_fire_arrow_mode"),
        (try_end),
        (try_begin),
          (key_is_down, key_left_alt),
          (start_presentation, "prsnt_multiplayer_name_projection_display"),
        (try_end),
  ])
  
fire_element_life_multi = (3, 0, 0,
  [],#(troop_slot_ge, "trp_global_value", slot_gloval_max_flame_slot, 1),
  [

      (call_script, "script_flame_routine")])
  
destructible_object_initialize_multi  = (
  ti_before_mission_start, 0, 0, [],[
      (call_script,"script_initialize_agents_use_fire_arrow"),
      (call_script, "script_destructible_object_initialize")])
###fire arrow acaba

#respiracion chief para multi Anade respiracion mas bleed - bloodloss
respiracion_moribunda = (0, 0, 12, [
    ], # o pressed?
##                             
        [
####      (multiplayer_is_server),
####          (try_for_agents,":agent"),
####              (agent_is_alive,":agent"),    
####                          (store_agent_hit_points, ":cur_hp",":agent",0),
####                          (try_begin),
####                              (lt,":cur_hp",30),
####
         (try_for_agents,":cur_agent"), # loops through all players.
            (agent_is_alive,":cur_agent"), #  test for alive players.
            (agent_is_human,":cur_agent"), # test for player that are human.
            (store_agent_hit_points,":cur_agent_hp",":cur_agent", 1), # stores the hp value of the alive and human players.
            (le, ":cur_agent_hp",25), #55 = max? #27.5 = 50% # test if the players hp is greater than 27.5 and if true exit the loop.
            #(store_add,":cur_full_health", ":cur_agent_hp",0),
            #(agent_set_hit_points,":cur_agent", ":cur_full_health",1),
        #(else_try),
            (store_sub,":damage",":cur_agent_hp",1), # if the above try_for_agents statement failed, store the players hp and subtract 1 from it.
         (agent_get_position, pos1, ":cur_agent"),
         (position_move_z, pos1, 150), #makes the blood higher, otherwise it's on ground level
         (position_move_x, pos1, -35), #makes the blood out from the torso towards the arm stump
         (position_move_y, pos1, -10), #makes the blood come out severed stump
         (position_rotate_x, pos1, -90), #makes the blood spurt downwards
         (particle_system_burst, "psys_game_blood_2", pos1, 100), #100 as power.

         (agent_set_hit_points,":cur_agent", ":damage",1), # update the players hp value with the new calculation value from above.
                    (agent_play_sound, ":cur_agent", "snd_breathing_heavy"), # if the value is one then play death sound.
                                       # (display_message, "@You take 1 damage from blood loss."),
                 (try_begin),
                    (le,":cur_agent_hp",1),
                    (agent_stop_sound, ":cur_agent"),
                                        (agent_set_hit_points,":cur_agent",0,1),#insta-death, muerte fija al decapitar
                (try_end),
##                          (try_begin),
##                                          (agent_get_player_id,":player",":cur_agent"),
##                                          (player_is_active, ":player"),
####                 (try_begin),
####                    (le,":cur_agent_hp",2),
####                                          (multiplayer_send_2_int_to_server,multiplayer_event_message_server, 2, ":player"), ### 1 ist the number of healing
######                          (else_try), #puesto off para no saturar
######                                          (multiplayer_send_2_int_to_server,multiplayer_event_message_server, 1, ":player"), ### 1 ist the number of healing
####                (try_end),
##                                (try_end),
                      #  (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_breathing_heavy"),
####                (agent_get_player_id,":player",":agent"), #msg
####                     (multiplayer_send_2_int_to_server,multiplayer_event_message_server, 1, ":player"), 
####             (display_message, "@You heallllll ally."),
####                          (try_end),
                         (try_end),
        ])

#fatiga ti_on_agent_spawn, 0, 0
sistema_fatiga = (ti_on_agent_spawn, 0, 0, [(eq, "$sp_fatigas", 1),#start up the staminan bar
],[    #determina fatiga al principio de la batalla para todos
#    (get_player_agent_no, ":player_agent"),

        (store_trigger_param_1, ":agent_no"),

#    (try_for_agents, ":agent_no"),
        (agent_is_alive,":agent_no"), # 
      (agent_is_human, ":agent_no"),

        (store_agent_hit_points,":cur_agent_hp",":agent_no", 1), # stores the hp value of the alive and human players.
        (assign, ":basic_stamina",":cur_agent_hp"),
          (agent_get_troop_id, ":troop", ":agent_no"),
        (store_skill_level, ":fatigue",  "skl_athletics", ":troop"),
        (val_mul, ":fatigue", 4), #obtenemos total fatigue min 90 max 210#gdw was at 3
        (val_add, ":basic_stamina", ":fatigue"), #obtenemos total fatigue min 60 max 141
        (val_mul, ":basic_stamina", 5), #obtenemos total fatigue min 90 max 210#was 3/2gdw
        (val_div, ":basic_stamina", 3), #obtenemos total fatigue min 90 max 210#gdw from X1.5 to X2 this was too much not sure if changed this
        (agent_set_slot, ":agent_no", slot_agent_fatiga_inicial, ":basic_stamina"), #se la aplicamos al agente
        (agent_set_slot, ":agent_no", slot_agent_fatiga, ":basic_stamina"), #se la aplicamos al agente

        (start_presentation, "prsnt_staminabar"),
       # (try_begin),
       #     (eq, ":agent_no", ":player_agent"),
       #     (assign, reg1, ":basic_stamina"),
       #     (display_message, "@Stamina: {reg1}"),
       # (try_end),
    #(try_end),
    ])

recupera_fatiga = (3, 0, 0, [    #gdw tried this at 15 and it seems that it is too powerful it makes it very hard to get stamina to display         
    (this_or_next|game_key_is_down, gk_move_forward),
   (this_or_next|game_key_is_down, gk_move_backward),
    (this_or_next|game_key_is_down, gk_move_left),
   (game_key_is_down, gk_move_right),
    ],[    #determina fatiga al principio de la batalla para todos determine fatigue at beginning of battle for all
        (neg|is_presentation_active, "prsnt_staminabar_multi"),        
       #(neg|is_presentation_active, "prsnt_battle"),
        #(neg|is_presentation_active, "prsnt_order_display"),
         (neg|main_hero_fallen),

        (get_player_agent_no, ":player_no"),
        (agent_is_alive,":player_no"), # 
         (agent_is_human, ":player_no"),
           (start_presentation, "prsnt_staminabar"),
    ])
#6 4
suma_fatigue = (5, 0, 0, [(eq, "$sp_fatigas", 1),(is_presentation_active, "prsnt_staminabar"),],[    #suma 1 mas agilidad cada 4 segundos
#    (get_player_agent_no, ":player_agent"),

    (try_for_agents, ":agent_no"),
        (agent_is_alive,":agent_no"), #  test for alive players.
      (agent_is_human, ":agent_no"),
        (agent_get_slot, ":basic_stamina", ":agent_no", slot_agent_fatiga),
        (agent_get_slot, ":basic_stamina_i", ":agent_no", slot_agent_fatiga_inicial),
        (lt, ":basic_stamina", ":basic_stamina_i"),

          (agent_get_troop_id, ":troop", ":agent_no"),
        (store_skill_level, ":fatigue",  "skl_athletics", ":troop"),
        (val_add, ":fatigue", 1), #suma agilidad un punto#gdwput to 2 then returned  to 1 too big a change
        (val_add, ":basic_stamina", ":fatigue"), #suma agilidad cada dos segundos
        (agent_set_slot, ":agent_no", slot_agent_fatiga, ":basic_stamina"), #se la aplicamos al agente
       # (try_begin), #text for testing
       #     (eq, ":agent_no", ":player_agent"),
       #     (assign, reg1, ":basic_stamina"),
       #     (display_message, "@ Sumas Stamina: {reg1}"),
       # (try_end),

    (try_end),  

    ])
#gdw "reduce fatigue for running"
resta_fatigue_porcorrer = (8, 0, 0, [(eq, "$sp_fatigas", 1), #F123 - 1.41 -> Submod
    (this_or_next|game_key_is_down, gk_move_forward),#gdw was 6, , tekporary test
    (this_or_next|game_key_is_down, gk_move_left),
   (game_key_is_down, gk_move_right),
    (neg|key_is_down,key_left_shift), #not walking
                                     ],[

    (neg|main_hero_fallen),
        (get_player_agent_no, ":player"),
        (agent_is_alive,":player"), #  test for alive players.
       (agent_is_human, ":player"),
       (agent_get_horse,":agent_mounted",":player"),
           (eq,":agent_mounted",-1),

        (assign, ":stamina_coste", 2),

           (agent_get_item_slot, ":cur_armor", ":player", ek_body),#Here we are getting body armor
            (try_begin),
                (is_between, ":cur_armor", armadura_pesada_begin, armadura_pesada3_end),
               (val_add, ":stamina_coste", 2),#gdwalreay penalty in scripts
            (else_try),
                (is_between, ":cur_armor", armadura_media_begin, armadura_media_end),
                (val_add, ":stamina_coste", 1),#gdwalready penalty in scripts
##           (else_try),
##                (eq, ":cur_armor", "itm_no_item"), #ni suma ni resta, no tiene nada
           (else_try),
                (is_between, ":cur_armor", desnudos_begin, desnudos_end), #es equipamiento ritual
                (val_sub, ":stamina_coste", 1),
            (try_end),

           (agent_get_item_slot, ":cur_armor", ":player", ek_head),#Here we are getting head armor
                 (try_begin),
                    (is_between, ":cur_armor", yelmos_pesados2_begin, yelmos_pesados2_end),
                    (val_add, ":stamina_coste", 1),
                 (try_end),

             (agent_get_item_slot, ":cur_armor", ":player", ek_foot),#Here we are getting leg armor
             (try_begin),
                 (is_between, ":cur_armor", calzado_pesados_begin, calzado_pesados_end),
                 (val_add, ":stamina_coste", 1),
             (try_end),

             #no heavy gloves in Brytenwalda.
        # (agent_get_item_slot, ":cur_armor", ":player", ek_gloves),#Here we are getting arm armor
        #     (try_begin),
        #        (this_or_next|eq, ":cur_armor", "itm_mail_gloves"),
        #        (eq, ":cur_armor", "itm_scale_arm_gloves"),
        #       (val_add, ":stamina_coste", 1),
        #     (try_end),
            # (agent_get_item_slot, ":cur_armor", ":agent_no", ek_gloves),#Here we are getting arm armor
            # (try_begin),
            #    (is_between, ":cur_armor", guantes_pesados_begin, guantes_pesados_end),
            #    (val_add, ":stamina_coste", 1),
            #(try_end),

            #Now for the four armaments every agent may carry (not wear)
            (agent_get_item_slot,":cur_arma",":player",ek_item_0),
            (try_begin),
                # (this_or_next|is_between, ":cur_arma", armas_pesadas_begin, armas_pesadas_end), #un arma es mas comoda de llevar, por ahora no quitamos stamina
                 (this_or_next|is_between, ":cur_arma", escudos_pesados_begin, escudos_pesados_end),
                (is_between, ":cur_arma", escudos_pesados2_begin, escudos_pesados2_end),
                (val_add, ":stamina_coste", 1), #un escudo de 70-90 cm es bastante pesado, en torno a 4-6 kg.
            (try_end),

            (agent_get_item_slot,":cur_arma",":player",ek_item_1),
            (try_begin),
                # (this_or_next|is_between, ":cur_arma", armas_pesadas_begin, armas_pesadas_end), #un arma es mas comoda de llevar, por ahora no quitamos stamina
                 (this_or_next|is_between, ":cur_arma", escudos_pesados_begin, escudos_pesados_end),
                (is_between, ":cur_arma", escudos_pesados2_begin, escudos_pesados2_end),
                (val_add, ":stamina_coste", 1), #un escudo de 70-90 cm es bastante pesado, en torno a 4-6 kg.
            (try_end),

            (agent_get_item_slot,":cur_arma",":player",ek_item_2),
            (try_begin),
                # (this_or_next|is_between, ":cur_arma", armas_pesadas_begin, armas_pesadas_end), #un arma es mas comoda de llevar, por ahora no quitamos stamina
                 (this_or_next|is_between, ":cur_arma", escudos_pesados_begin, escudos_pesados_end),
                (is_between, ":cur_arma", escudos_pesados2_begin, escudos_pesados2_end),
                (val_add, ":stamina_coste", 1), #un escudo de 70-90 cm es bastante pesado, en torno a 4-6 kg.
            (try_end),

            (agent_get_item_slot,":cur_arma",":player",ek_item_3),
            (try_begin),
                # (this_or_next|is_between, ":cur_arma", armas_pesadas_begin, armas_pesadas_end), #un arma es mas comoda de llevar, por ahora no quitamos stamina
                 (this_or_next|is_between, ":cur_arma", escudos_pesados_begin, escudos_pesados_end),
                (is_between, ":cur_arma", escudos_pesados2_begin, escudos_pesados2_end),
                (val_add, ":stamina_coste", 1), #un escudo de 70-90 cm es bastante pesado, en torno a 4-6 kg.
            (try_end),
   
        (agent_get_slot, ":basic_stamina", ":player", slot_agent_fatiga),
        (val_sub, ":basic_stamina", ":stamina_coste"), #maximo 8 para un hombre totalmente equipado, y minimo 1 para un picto desnudo

        (val_max, ":basic_stamina", 1), #siempre va a restar un minimo de 1
        (agent_set_slot, ":player", slot_agent_fatiga, ":basic_stamina"), #se la aplicamos al agente

        (try_begin), 

        (le, ":basic_stamina", 4),
                                          (agent_set_animation, ":player","anim_strike_fall_back_rise"),
        (agent_play_sound, ":player", "snd_breathing_heavy"), # if the value is one then play death sound.
            (display_message, "@ You're so tired you can barely move a muscle."),
        (try_end),    

    ])


resta_fatigue = (ti_on_agent_hit, 0, 0, [(eq, "$sp_fatigas", 1),],[
    (store_trigger_param_1, ":inflicted_agent"),
    (store_trigger_param_2, ":dealer_agent"),

        (agent_is_alive,":dealer_agent"), #  test for alive players.
   (agent_is_human, ":dealer_agent"),
    (set_trigger_result, -1),
    (get_player_agent_no, ":player_agent"),
    (try_begin),
        (agent_is_alive,":inflicted_agent"), #  test for alive players.
        (agent_is_human, ":inflicted_agent"),    

            (agent_get_wielded_item, ":wielded",":dealer_agent", 0),
        (try_begin),
            (this_or_next|is_between, ":wielded", "itm_club_stick", "itm_spathaswordt2"), #armas pequenas
            (is_between, ":wielded", "itm_irish_shsword", "itm_pictish_longsword1"),
            (assign, ":stamina_cost", 1), #pierde fatiga cada golpe.
        (else_try),
            (this_or_next|is_between, ":wielded", "itm_spathaswordt2", "itm_irish_shsword"),
            (this_or_next|is_between, ":wielded", "itm_staff1", "itm_spear_blade2t2"),
            (this_or_next|is_between, ":wielded", "itm_spear_britonshortt2", "itm_twohand_speart3"),
            (this_or_next|is_between, ":wielded", "itm_engle_speart2", "itm_wessexbanner1"),
            (this_or_next|is_between, ":wielded", "itm_darts", "itm_lyre"),
            (is_between, ":wielded", "itm_pictish_longsword1", "itm_tree_axe2h"),
            (assign, ":stamina_cost", 2), #pierde fatiga cada golpe.
        (else_try),
            (this_or_next|is_between, ":wielded", "itm_tree_axe2h", "itm_staff1"),
            (this_or_next|is_between, ":wielded", "itm_twohand_speart3", "itm_germanshortspeart2"),
            (is_between, ":wielded", "itm_spear_briton2ht3", "itm_spear_britonshortt2"),
            (assign, ":stamina_cost", 4), #pierde fatiga cada golpe.
        (else_try),
            (assign, ":stamina_cost", 2), #pierde fatiga cada golpe.
        (try_end),
  #     (try_begin), #integrado en el peso por correr
   #        (this_or_next|is_between, ":wielded", "itm_celtic_shield_smalla", "itm_hshield1"),
   #        (is_between, ":wielded", "itm_shieldtarcza19", "itm_norman_shield_1"),
   #        (val_add, ":stamina_cost", 1), #pierde fatiga cada golpe.
    #   (try_end),
           (agent_get_slot, ":dealer_stamina", ":dealer_agent", slot_agent_fatiga),
        (val_sub, ":dealer_stamina", ":stamina_cost"),
        (val_max, ":dealer_stamina", 1),
        (agent_set_slot, ":dealer_agent", slot_agent_fatiga, ":dealer_stamina"), #se la aplicamos al agente
        (agent_get_slot, ":inflicted_stamina", ":inflicted_agent", slot_agent_fatiga),
        (val_sub, ":inflicted_stamina", ":stamina_cost"),
        (val_max, ":inflicted_stamina", 1),
        (agent_set_slot, ":inflicted_agent", slot_agent_fatiga, ":inflicted_stamina"), #se la aplicamos al agente

      # (try_begin),
      #      (eq, ":dealer_agent", ":player_agent"),
      #      (assign, reg1, ":dealer_stamina"),
      #      (display_message, "@ Lose Stamina for your strike: {reg1}"),
      #  (else_try),
      #      (eq, ":inflicted_agent", ":player_agent"),
      #      (assign, reg1, ":inflicted_stamina"),
      #      (display_message, "@ Lose Stamina for blow received: {reg1}"),
      #  (try_end),
    (try_end),

    (agent_get_slot, ":basic_stamina", ":dealer_agent", slot_agent_fatiga),
    (agent_get_slot, ":basic_stamina_i", ":dealer_agent", slot_agent_fatiga_inicial),
    (store_div, ":qua_stamina_i", ":basic_stamina_i", 4),
  #  (store_div, ":half_stamina_i", ":basic_stamina_i", 2),

    (try_begin),
        (lt, ":basic_stamina", 6),
            (agent_set_animation, ":dealer_agent","anim_fatigues1"),
              (agent_play_sound, ":dealer_agent", "snd_breathing_heavy"),
        (try_begin),
            (eq, ":dealer_agent", ":player_agent"),
           (display_message, "@You are exhausted and have no strength to strike!", 0xFF0000),
        (try_end),
   (else_try),
        (lt, ":basic_stamina", ":qua_stamina_i"),
       (eq, ":dealer_agent", ":player_agent"),
       (display_message, "@Your stamina is low. You must rest.", 0xFF0000),
    (try_end),
    ])

#fatiga acaba chief
#xenoarg para performance en batallas chief
common_performance_code = (ti_on_agent_killed_or_wounded, 0, 0, [],
   [
    (store_trigger_param_1, ":dead_agent_no"),
    (try_for_range, ":i", 0, 3),
        (agent_get_wielded_item, ":item", ":dead_agent_no", ":i"),
        (gt, ":item", 0),
        (agent_unequip_item, ":dead_agent_no", ":item"),
    (try_end),
])

###chief multiplayer chief acaba
#amarillo chief desangran tropas y hacen menos dano blood loss
monitor_health = (
    0.05, 0.0, 0.0,
        [(eq, "$sp_criticos", 1),],
        [
            (call_script,"script_monitor_health"),
        ])

bleed = (
    1.0, 0.0, 0.0,
        [(eq, "$sp_criticos", 1),],
        [
            (call_script,"script_bleed"),
      (call_script, "script_update_order_panel_map"), ## CC chief ponemos aqui llamada a caballo stamina
        ])
###chief blood loss acaba
###fatiga multiplayer
sistema_fatiga_multi = (ti_on_agent_spawn, 0, 0, [              

    ],[    #determina fatiga al principio de la batalla para todos
        (store_trigger_param_1, ":agent_no"),
        (multiplayer_get_my_player,":player_no"),
           (player_is_active, ":player_no"),
           #(neg|player_is_busy_with_menus, ":player_no"),
           # (neg|is_presentation_active, "prsnt_staminabar"),

             (player_get_agent_id, ":my_agent_id",":player_no"),
           (eq, ":agent_no", ":my_agent_id"),
        
        (agent_is_alive,":agent_no"), # 
      (agent_is_human, ":agent_no"),
     #    (neg|agent_is_non_player, ":agent_no"),
        
        (store_agent_hit_points,":cur_agent_hp",":agent_no", 1), # stores the hp value of the alive and human players.
        (assign, ":basic_stamina",":cur_agent_hp"),
        (val_add, ":basic_stamina", 20), #obtenemos total fatigue min 60 max 141
        (agent_set_slot, ":agent_no", slot_agent_fatiga_inicial, ":basic_stamina"), #se la aplicamos al agente
        (agent_set_slot, ":agent_no", slot_agent_fatiga, ":basic_stamina"), #se la aplicamos al agente
    
           (start_presentation, "prsnt_staminabar_multi"),
        #    (try_end),
#    (try_end),
    ])

recupera_fatiga_multi = (0, 0, 3, [
(game_key_clicked, gk_attack),
 #(game_key_is_down, gk_attack),
       # (key_clicked, gk_attack),
            ],[    #determina fatiga al principio de la batalla para todos
 
      (multiplayer_get_my_player, ":my_player"),
           (neg|player_is_busy_with_menus, ":my_player"),
           (player_is_active, ":my_player"),
      (player_get_agent_id, ":my_agent", ":my_player"),
      (try_for_agents, ":agent"),
        (agent_is_human, ":agent"),
        (agent_is_alive, ":agent"),
        (try_begin),
        (eq, ":agent", ":my_agent"),
          (neg|is_presentation_active, "prsnt_multiplayer_escape_menu"),
         (neg|is_presentation_active, "prsnt_multiplayer_stats_chart_deathmatch"),
         (neg|is_presentation_active,        "prsnt_staminabar_multi"),
    (start_presentation, "prsnt_staminabar_multi"),
        (else_try),
            #(display_message,"@ "),
        (try_end),
        (try_end),
    ])

suma_fatigue_multi = (4, 0, 0, [(is_presentation_active, "prsnt_staminabar_multi"),
],[    

    (try_for_agents, ":agent_no"),

        (agent_is_alive,":agent_no"), #  test for alive players.
      (agent_is_human, ":agent_no"),
##            (try_begin),
##        (is_presentation_active, "prsnt_staminabar_multi"),
        (agent_get_slot, ":basic_stamina", ":agent_no", slot_agent_fatiga),
        (agent_get_slot, ":basic_stamina_i", ":agent_no", slot_agent_fatiga_inicial),
        (lt, ":basic_stamina", ":basic_stamina_i"),

        (val_add, ":basic_stamina", 6), #siempre va a sumar un minimo de 1
        (agent_set_slot, ":agent_no", slot_agent_fatiga, ":basic_stamina"), #se la aplicamos al agente
##            (else_try),
##           (start_presentation, "prsnt_staminabar_multi"),
##    (try_end),  
    (try_end),    
    ])

fatigue_bots_multi = (30, 0, 0, [
],[    

    (try_for_agents, ":agent_no"),
      (agent_is_non_player, ":agent_no"),
        (agent_is_alive,":agent_no"), #  test for alive players.
      (agent_is_human, ":agent_no"),
        (assign, ":basic_stamina",70),
        (val_add, ":basic_stamina", 5), #obtenemos total fatigue min 60 max 141
        (agent_set_slot, ":agent_no", slot_agent_fatiga_inicial, ":basic_stamina"), #se la aplicamos al agente
       (agent_set_slot, ":agent_no", slot_agent_fatiga, ":basic_stamina"), #se la aplicamos al agente
    (try_end),    
    ])

#gdw 3 0 0
resta_fatigue_porcorrer_multi = (4, 0, 0, [         (is_presentation_active, "prsnt_staminabar_multi"),
    (this_or_next|game_key_is_down, gk_move_forward),
   (this_or_next|game_key_is_down, gk_move_backward),
    (this_or_next|game_key_is_down, gk_move_left),
   (game_key_is_down, gk_move_right),
                                                    (neg|key_is_down,key_left_shift), #Don't trip if walking
       # (neg|main_hero_fallen),
                                     ],[   

        (multiplayer_get_my_player,":player"),

              (player_get_agent_id, ":agent_no",":player"),
        (agent_is_alive,":agent_no"), #  test for alive players.
      (agent_is_human, ":agent_no"),
       (agent_get_horse,":agent_mounted",":agent_no"),
           (eq,":agent_mounted",-1),

        (assign, ":stamina_coste", 1),

           (agent_get_item_slot, ":cur_armor", ":agent_no", ek_body),#Here we are getting body armor
            (try_begin),
                (is_between, ":cur_armor", armadura_pesada_begin, armadura_pesada3_end),
               (val_add, ":stamina_coste", 2),
            (else_try),
                (is_between, ":cur_armor", armadura_media_begin, armadura_media_end),
                (val_add, ":stamina_coste", 1),
##           (else_try),
##                (eq, ":cur_armor", "itm_no_item"), #ni suma ni resta, no tiene nada
           (else_try),
                (is_between, ":cur_armor", desnudos_begin, desnudos_end), #es equipamiento ritual
                (val_sub, ":stamina_coste", 1),
            (try_end),

           (agent_get_item_slot, ":cur_armor", ":agent_no", ek_head),#Here we are getting head armor
                 (try_begin),
                    (is_between, ":cur_armor", yelmos_pesados2_begin, yelmos_pesados2_end),
                    (val_add, ":stamina_coste", 1),
                 (try_end),

             (agent_get_item_slot, ":cur_armor", ":agent_no", ek_foot),#Here we are getting leg armor
             (try_begin),
                 (is_between, ":cur_armor", calzado_pesados_begin, calzado_pesados_end),
                 (val_add, ":stamina_coste", 1),
             (try_end),

             #no heavy gloves in Brytenwalda.
            # (agent_get_item_slot, ":cur_armor", ":agent_no", ek_gloves),#Here we are getting arm armor
            # (try_begin),
                # (is_between, ":cur_armor", guantes_pesados_begin, guantes_pesados_end),
                # (val_add, ":stamina_coste", 1),
            # (try_end),

            #Now for the four armaments every agent may carry
           (agent_get_item_slot,":cur_arma",":agent_no",ek_item_0),
           (try_begin),
               # (this_or_next|is_between, ":cur_arma", armas_pesadas_begin, armas_pesadas_end), #un arma es mas comoda de llevar, por ahora no quitamos stamina
                (this_or_next|is_between, ":cur_arma", escudos_pesados_begin, escudos_pesados_end),
               (is_between, ":cur_arma", escudos_pesados2_begin, escudos_pesados2_end),
               (val_add, ":stamina_coste", 1), #un escudo de 70-90 cm es bastante pesado, en torno a 4-6 kg.
           (try_end),
           (agent_get_item_slot,":cur_arma",":agent_no",ek_item_1),
           (try_begin),
               # (this_or_next|is_between, ":cur_arma", armas_pesadas_begin, armas_pesadas_end), #un arma es mas comoda de llevar, por ahora no quitamos stamina
                (this_or_next|is_between, ":cur_arma", escudos_pesados_begin, escudos_pesados_end),
               (is_between, ":cur_arma", escudos_pesados2_begin, escudos_pesados2_end),
               (val_add, ":stamina_coste", 1), #un escudo de 70-90 cm es bastante pesado, en torno a 4-6 kg.
           (try_end),

           (agent_get_item_slot,":cur_arma",":agent_no",ek_item_2),
           (try_begin),
               # (this_or_next|is_between, ":cur_arma", armas_pesadas_begin, armas_pesadas_end), #un arma es mas comoda de llevar, por ahora no quitamos stamina
                (this_or_next|is_between, ":cur_arma", escudos_pesados_begin, escudos_pesados_end),
               (is_between, ":cur_arma", escudos_pesados2_begin, escudos_pesados2_end),
               (val_add, ":stamina_coste", 1), #un escudo de 70-90 cm es bastante pesado, en torno a 4-6 kg.
           (try_end),

           (agent_get_item_slot,":cur_arma",":agent_no",ek_item_3),
           (try_begin),
               # (this_or_next|is_between, ":cur_arma", armas_pesadas_begin, armas_pesadas_end), #un arma es mas comoda de llevar, por ahora no quitamos stamina
                (this_or_next|is_between, ":cur_arma", escudos_pesados_begin, escudos_pesados_end),
               (is_between, ":cur_arma", escudos_pesados2_begin, escudos_pesados2_end),
               (val_add, ":stamina_coste", 1), #un escudo de 70-90 cm es bastante pesado, en torno a 4-6 kg.
           (try_end),
              (try_begin), 
        (game_key_clicked, gk_jump),#por saltar
         (val_add, ":stamina_coste", 4),
            (try_end),
                (agent_get_slot, ":basic_stamina", ":agent_no", slot_agent_fatiga),

            (try_begin),
        (le, ":basic_stamina", 4),
##                        (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_breathing_heavy"),
            (multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_strike_fall_back_rise"),
        (agent_play_sound, ":agent_no", "snd_breathing_heavy"), # if the value is one then play death sound.
                                         # (multiplayer_send_2_int_to_server,multiplayer_event_message_server, 3, ":player"), ### 1 ist the number of healing
            #(display_message, "@ no puedes con el alma para correr mas"),
    (try_end),


        (val_sub, ":basic_stamina", ":stamina_coste"), #maximo 10 para un hombre totalmente equipado, y minimo 1 para un picto desnudo

        (val_max, ":basic_stamina", 1), #siempre va a restar un minimo de 1
        (agent_set_slot, ":agent_no", slot_agent_fatiga, ":basic_stamina"), #se la aplicamos al agente
#    (try_end),
# (try_end),    

    ])


resta_fatigue_multi= (1, 0, 0, [      (is_presentation_active, "prsnt_staminabar_multi"),
                                      (this_or_next|game_key_is_down, gk_defend),
        (game_key_is_down, gk_attack),
],[
        (multiplayer_get_my_player,":player"),
           (player_is_active, ":player"),
           (neg|player_is_busy_with_menus, ":player"),
              (player_get_agent_id, ":agent_no",":player"),

        (agent_is_alive,":agent_no"), #  test for alive players.
   (agent_is_human, ":agent_no"),
       (agent_get_horse,":agent_mounted",":agent_no"),
           (eq,":agent_mounted",-1),
    (set_trigger_result, -1),
    (try_begin),
            (agent_get_wielded_item, ":wielded",":agent_no", 0),
            (assign, ":stamina_cost", 1), #pierde fatiga cada golpe.
        (try_begin),
            (this_or_next|is_between, ":wielded", "itm_club_stick", "itm_spathaswordt2"), #armas pequenas
            (is_between, ":wielded", "itm_irish_shsword", "itm_pictish_longsword1"),
            (val_add, ":stamina_cost", 1), #pierde fatiga cada golpe.
        (else_try),
            (this_or_next|is_between, ":wielded", "itm_spathaswordt2", "itm_irish_shsword"),
            (this_or_next|is_between, ":wielded", "itm_staff1", "itm_spear_blade2t2"),
            (this_or_next|is_between, ":wielded", "itm_spear_britonshortt2", "itm_twohand_speart3"),
            (this_or_next|is_between, ":wielded", "itm_engle_speart2", "itm_wessexbanner1"),
            (this_or_next|is_between, ":wielded", "itm_darts", "itm_lyre"),
            (is_between, ":wielded", "itm_pictish_longsword1", "itm_tree_axe2h"),
            (val_add, ":stamina_cost", 2), #pierde fatiga cada golpe.
        (else_try),
            (this_or_next|is_between, ":wielded", "itm_tree_axe2h", "itm_staff1"),
            (this_or_next|is_between, ":wielded", "itm_twohand_speart3", "itm_germanshortspeart2"),
            (is_between, ":wielded", "itm_spear_briton2ht3", "itm_spear_britonshortt2"),
            (val_add, ":stamina_cost", 4), #pierde fatiga cada golpe.
        (try_end),
##        (try_begin), #player pierde stamina por correr yet
##            (this_or_next|is_between, ":wielded", "itm_celtic_shield_smalla", "itm_hshield"),
##            (is_between, ":wielded", "itm_shieldtarcza19", "itm_norman_shield_1"),
##            (val_add, ":stamina_cost", 1), #pierde fatiga cada golpe.
##        (try_end),
        (agent_get_slot, ":inflicted_stamina", ":agent_no", slot_agent_fatiga),
        (val_sub, ":inflicted_stamina", ":stamina_cost"),
        (val_max, ":inflicted_stamina", 1),
        (agent_set_slot, ":agent_no", slot_agent_fatiga, ":inflicted_stamina"), #se la aplicamos al agente

    (try_end),

##    (store_trigger_param_3, ":damage"),
##   (gt, ":damage", 0),

    (agent_get_slot, ":basic_stamina", ":agent_no", slot_agent_fatiga),
    
    (try_begin),
##        (le, ":basic_stamina", 10), #animacion y sonido aplicados en correr ya
##            (multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_fatigues1"),
##                                          (multiplayer_send_2_int_to_server,multiplayer_event_message_server2, 3, ":player"), ### 1 ist the number of healing
#    (else_try),
        (lt, ":basic_stamina", 6),
            (multiplayer_send_int_to_server,multiplayer_event_animation_at_player, "anim_fatigues1"),
                                      #   (multiplayer_send_2_int_to_server,multiplayer_event_message_server, 3, ":player"), ### 1 ist the number of healing
##   (else_try), #puesto off chief para no saturar
##        (lt, ":basic_stamina", 25),
##                                         (multiplayer_send_2_int_to_server,multiplayer_event_message_server2, 1, ":player"), ### 1 ist the number of healing
    (try_end),





                       # (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_corazon_late2"),

    ])
#fatiga multiplayer acaba
#rain multiplayer
rain_multi = (
    ti_before_mission_start, 0, ti_once, [
        (store_current_scene, ":cur_scene"),
           (neq, ":cur_scene", "scn_multi_scene_3"),
],
   [
        #(multiplayer_is_server), # test for a multiplayer server.
                (store_random_in_range, ":rain_chance", 1,11),
                (try_begin),
                    (eq, ":rain_chance", 1),                    
           (set_rain, 1, 80),
           (set_global_cloud_amount, 75),
           (set_global_haze_amount, 35),
##                    (store_random_in_range, ":rain_power", 50, 100),
##                    (store_random_in_range, ":haze_power", 25, 65),
##                    (set_global_haze_amount, ":haze_power"),
##                    (set_rain, 1, ":rain_power"),                    
                (else_try),
                    (eq, ":rain_chance", 2),                    
           (set_rain, 1, 50),
           (set_global_cloud_amount, 65),
           (set_global_haze_amount, 15),
##                    (store_random_in_range, ":rain_power", 50, 100),
##                    (store_random_in_range, ":haze_power", 25, 65),
##                    (set_global_haze_amount, ":haze_power"),
##                    (set_rain, 1, ":rain_power"),                    
                (else_try),
                    (eq, ":rain_chance", 3),                    
           (set_fog_distance, 55, 0x333333),
           (set_global_cloud_amount, 25),
           (set_global_haze_amount, 45),
##                    (store_random_in_range, ":fog_distance", 50, 75),
##                    (store_random_in_range, ":haze_power", 25, 65),
##                    (set_global_haze_amount, ":haze_power"),
##                                        (set_fog_distance, ":fog_distance", 0x333333),
                (else_try),
                    (eq, ":rain_chance", 4),                    
           (set_rain, 1, 60),
           (set_global_cloud_amount, 65),
           (set_global_haze_amount, 25),
##                    (store_random_in_range, ":rain_power", 50, 100),
##                    (store_random_in_range, ":haze_power", 25, 65),
##                    (set_global_haze_amount, ":haze_power"),
##                    (set_rain, 1, ":rain_power"),                    
##                                        (call_script, "script_change_rain_or_snow"),
                (else_try),
                    (eq, ":rain_chance", 5),                    
           (set_rain, 1, 100),
           (set_global_cloud_amount, 80),
           (set_global_haze_amount, 15),
##                    (store_random_in_range, ":rain_power", 50, 100),
##                    (store_random_in_range, ":haze_power", 25, 65),
##                    (set_global_haze_amount, ":haze_power"),
##                    (set_rain, 2, ":rain_power"),                    
                (else_try),
                    (set_global_haze_amount, 0),
                    (set_rain, 0, 0),        
                (try_end),
   ])

#ordenes rapidas chief
##multiplayer_critical_strike =(
##  ti_on_agent_hit, 0, 0, [         
##],
##    [
##                        (multiplayer_send_int_to_server,multiplayer_event_sound_at_player, "snd_corazon_late"),
##
##    ])
##########multiplayer chief acaba


dplmc_battle_mode_triggers = [
      common_init_deathcam,
      common_start_deathcam,
      common_move_deathcam,
      common_rotate_deathcam,
   common_weapon_break,
   sp_shield_bash_1,
   sp_shield_bash_2,
   sp_shield_bash_3,
    common_weapon_use_spawn,
    common_weapon_use,
      rain,
    theoris_decapitation,
   custom_commander_hero_wounded,
      custom_commander_init_hero_begin_xp,
    custom_commander_give_hero_extra_xp,
    custom_commander_horse_speed,
    custom_commander_critical_strike,
##    spearwall_trigger_1,
##    spearwall_trigger_2,
##    spearwall_trigger_3,
##    spearwall_trigger_4,
##    spearwall_trigger_5,
##    spearwall_trigger_6,
##    spearwall_trigger_7,
##    spearwall_trigger_8,
##    spearwall_trigger_9,
     monitor_health,
     bleed,
#    common_rigale_legshot,
    common_andar_cae,
     WP_HR_on_death,
#common_performance_code,
sistema_fatiga,
recupera_fatiga,
      suma_fatigue,
resta_fatigue_porcorrer,
resta_fatigue,
      #common_damage_system_1,
      ]

dplmc_battle_mode_triggers2 = [
      common_init_deathcam,
      common_start_deathcam,
      common_move_deathcam,
      common_rotate_deathcam,
   common_weapon_break,
    common_weapon_use_spawn,
    common_weapon_use,
    theoris_decapitation,
    custom_commander_init_hero_begin_xp,
    custom_commander_give_hero_extra_xp,
    custom_commander_horse_speed,
    custom_commander_critical_strike,
     monitor_health,
     bleed,
   # common_rigale_legshot,
    common_andar_cae,
     WP_HR_on_death,
#common_performance_code,
sistema_fatiga,
recupera_fatiga,
suma_fatigue,
resta_fatigue_porcorrer,
resta_fatigue,
#common_damage_system_1,
      ]

dplmc_battle_mode_triggers3 = [
   common_weapon_break,
    common_weapon_use_spawn,
    common_weapon_use,
    custom_commander_critical_strike,
     monitor_health,
     bleed,
    common_andar_cae,
     WP_HR_on_death,
sistema_fatiga,
recupera_fatiga,
suma_fatigue,
resta_fatigue_porcorrer,
resta_fatigue,
#common_damage_system_1,
   ]
##diplomacy chief end
###multiplayer chief
multi_battle_mode_triggers3 = [
mp_shield_bash_1,
mp_shield_bash_2,
banner_heal_multi,
siege_multi_items,
multi_warcry,
hunt_taunting,
rain_multi,
#multiplayer_critical_strike,
respiracion_moribunda,
sistema_fatiga_multi,
recupera_fatiga_multi,
suma_fatigue_multi,
resta_fatigue_porcorrer_multi,
resta_fatigue_multi,
]

####sea battles phaiak chief
###############################
#### BEGIN OF KLABAUTERMANN ###
###############################

KLABAUTERMANN_1_weather =(            
  ti_before_mission_start, 0, 0, [],
  [    
        # RANDOMIZE WEATHER
        (store_random_in_range, "$weather", 1, 5),
        (try_begin),
          (eq, "$weather", 1),                            # very bad
          (store_random_in_range, ":value", 80, 101),
          (set_global_haze_amount, ":value"),
          (set_global_cloud_amount, ":value"),
          (set_rain, 1, ":value"),
          (store_random_in_range, ":value", 100, 200),
          (set_fog_distance, ":value", 0xFF8A8A5C),
          (store_random_in_range, "$wind_strange", 0, 2),
        (else_try),
          (eq, "$weather", 2),                            # bad
          (store_random_in_range, ":value", 50, 81),
          (set_global_haze_amount, ":value"),
          (set_global_cloud_amount, ":value"),
          (set_rain, 1, ":value"),
          (store_random_in_range, ":value", 200, 500),
          (set_fog_distance, ":value", 0xFFECECC6),
          (store_random_in_range, "$wind_strange", 0, 2),
        (else_try),
          (eq, "$weather", 3),                            # normal
          (store_random_in_range, ":value", 10, 51),
          (set_global_haze_amount, ":value"),
          (set_global_cloud_amount, ":value"),
          (set_rain, 1, 0),
          (store_random_in_range, ":value", 500, 1000),
          (set_fog_distance, ":value", 0xFFFFDBB8),
          (store_random_in_range, "$wind_strange", 0, 3),
        (else_try),            
          (store_random_in_range, ":value", 0, 10),        # good
          (set_global_haze_amount, ":value"),
          (set_global_cloud_amount, ":value"),
          (set_rain, 1, 0),
          (store_random_in_range, ":value", 1000, 2000),
          (set_fog_distance, ":value", 0xFFDBEDFF),
          (store_random_in_range, "$wind_strange", 0, 3),
        (try_end),    
        # RANDOMIZE WIND-ANGLE
        (store_random_in_range, "$wind_angle", 0, 360),

        # SHOW INFORMATION
        #(display_message,"@Press_'U'_for_informations_about_the_ship-battle.", 0xFF3D9EFF),
        (display_message,"str_klabautermann_info", 0xFF3D9EFF),
    ])

    
KLABAUTERMANN_2_prepare =(    
  0.1, 0, ti_once, [],        ### THE PREPARE-EVERYTHING-TRIGGER    
   [
     (call_script, "script_set_ships_and_crew"),
     
     # ACCORDING REINFORCEMENT
     (assign,"$defender_reinforcement_stage",0),
     (assign,"$attacker_reinforcement_stage",0),
     
##     # ACCORDING WEATHER
##        (try_begin),
##          (eq, "$weather", 1),                            # very bad
##          (store_random_in_range, ":value", 80, 101),
##          (set_global_haze_amount, ":value"),
##          (store_random_in_range, ":value", 100, 200),
##        (else_try),
##          (eq, "$weather", 2),                            # bad
##          (store_random_in_range, ":value", 50, 81),
##          (set_global_haze_amount, ":value"),
##          (store_random_in_range, ":value", 200, 500),
##        (else_try),
##          (eq, "$weather", 3),                            # normal
##          (store_random_in_range, ":value", 10, 51),
##          (set_global_haze_amount, ":value"),
##          (store_random_in_range, ":value", 500, 1000),
##        (else_try),            
##          (store_random_in_range, ":value", 0, 10),        # good
##          (set_global_haze_amount, ":value"),
##          (store_random_in_range, ":value", 1000, 2000),
##        (try_end),    
     ])

KLABAUTERMANN_3_kill_offboard =(                # changed !!!
  1.2, 0, 0, [],[            ### THE KILL-OFFBOARD-TRIGGER    
          (try_for_agents,":agent"),
            (agent_is_alive,":agent"),
            (agent_is_human,":agent"),
            (agent_get_position,pos6,":agent"),
            (try_begin),      
              (position_get_z, ":deep", pos6),
              (lt, ":deep", -200),
             (set_show_messages, 0),    #MOTO prevent "agent killed self" messages

              (agent_deliver_damage_to_agent,":agent" ,":agent" ,1000),
              (set_show_messages, 1),
          (end_try),
          (end_try),    
         ])         

KLABAUTERMANN_4_normal_commands =(             
  0, 0, 0, [],[            ### THE NORMAL-COMMAND-TRIGGER

          (try_begin),
            (key_clicked, key_back_space),                        ### camera command
            (try_begin),
              (eq, "$cam_mode", 0),
              (assign, "$cam_mode", 1),
              (mission_cam_set_mode, 1, 100, 0),
            (else_try),
              (eq, "$cam_mode", 1),
              (assign, "$cam_mode", 0),
              (mission_cam_set_mode, 0, 2000, 0),
            (try_end),          
          (try_end),
         ])

KLABAUTERMANN_5_ship_commands =(        
  0, 0, 0, [],[            ### THE PLAYER-SHIP-CONTROL-TRIGGER
        (try_begin),
          (gt, "$player_ship_number", -1),
          (get_player_agent_no, ":agent"),
          (agent_is_alive,":agent"),
          (scene_prop_get_instance, ":ship_instance", "spr_klabautermann_ship1", "$player_ship_number"),
          (scene_prop_get_slot, ":sail", ":ship_instance", 6),
          (scene_prop_get_slot, ":rowing", ":ship_instance", 7),
          (scene_prop_get_slot, ":rudder", ":ship_instance", 8),
          (scene_prop_get_slot, ":boarding_wanted", ":ship_instance", 12),
          (scene_prop_get_slot, ":landing_wanted", ":ship_instance", 13),
          (try_begin),
            (key_clicked, key_enter),                        ### Sail
            (try_begin),
              (eq, ":sail", 0),
              (assign, ":sail", 1),
              (display_message,"str_set_sail", 0xFFADD6FF),
            (else_try),
              #(eq, ":sail", 1),
              (assign, ":sail", 0),
              (display_message,"str_get_sail", 0xFFADD6FF),
            (try_end),
          (try_end),
          (try_begin),
            (key_clicked, key_down),                ### Rowing down
            (gt, ":rowing", 0),
            (val_add, ":rowing", -1),
            (display_message,"str_less_rowing", 0xFFADD6FF),
          (else_try),
            (key_clicked, key_up),                    ### Rowing up    
            (lt, ":rowing", 5),
            (val_add, ":rowing", 1),
            (display_message,"str_more_rowing", 0xFFADD6FF),
          (try_end),
          (try_begin),
            (key_clicked, key_right),                ### rudder right
            (gt, ":rudder", -3),
            (val_add, ":rudder", -1),
            (display_message,"str_starbord", 0xFFADD6FF),
          (else_try),
            (key_clicked, key_left),                ### rudder left
            (lt, ":rudder", 3),
            (val_add, ":rudder", 1),
            (display_message,"str_port", 0xFFADD6FF),
          (try_end),
          (try_begin),
            (key_clicked, key_k),                        ### Boarding command
            (try_begin),
              (eq, ":boarding_wanted", -1),
              (assign, ":boarding_wanted", 0),
              (display_message,"str_try_to_bord", 0xFFADD6FF),
            (else_try),
              (eq, ":boarding_wanted", 0),
              (assign, ":boarding_wanted", 1),
              (display_message,"str_bord_even_friendly_ships", 0xFFADD6FF),
            (else_try),
              (eq, ":boarding_wanted", 1),
              (assign, ":boarding_wanted", -1),
              (display_message,"str_avoid_boarding", 0xFFADD6FF),
            (try_end),
          (try_end),
          (try_begin),
            (key_clicked, key_j),                        ### Landing command
            (try_begin),
              (eq, ":landing_wanted", 0),
              (assign, ":landing_wanted", 1),
              (display_message,"str_try_to_land", 0xFFADD6FF),
            (else_try),
              (eq, ":landing_wanted", 1),
              (assign, ":landing_wanted", 0),
              (display_message,"str_avoid_landing", 0xFFADD6FF),
            (try_end),
          (try_end),
          
          (try_begin),
            (key_clicked, key_right_shift),                        ### Situation report
            (display_message,"str_situation_report", 0xFF7ABDFF),
            (try_begin),
              (gt, "$wind_strange", 0),
              (try_begin),
                (eq, "$wind_strange", 1),
                (str_store_string, s1, "str_light"),
              (else_try),
                (eq, "$wind_strange", 2),
                (str_store_string, s1, "@str_strong"),
              (try_end),
              
              (try_begin),
                (this_or_next|is_between, "$wind_angle", 0, 20),
                (is_between, "$wind_angle", 340, 360),
                (str_store_string, s2, "str_north"),
              (else_try),
                (is_between, "$wind_angle", 20, 70),
                (str_store_string, s2, "str_north-east"),
              (else_try),
                (is_between, "$wind_angle", 70, 110),
                (str_store_string, s2, "str_east"),
              (else_try),
                (is_between, "$wind_angle", 110, 160),
                (str_store_string, s2, "str_south-east"),
              (else_try),
                (is_between, "$wind_angle", 160, 200),
                (str_store_string, s2, "str_south"),
              (else_try),
                (is_between, "$wind_angle", 200, 250),
                (str_store_string, s2, "str_south-west"),
              (else_try),
                (is_between, "$wind_angle", 250, 290),
                (str_store_string, s2, "str_west"),
              (else_try),
                (is_between, "$wind_angle", 290, 340),
                (str_store_string, s2, "str_north-west"),
              (try_end),
              (display_message,"str_wind_comes_from", 0xFF7ABDFF),
            (else_try),
              (display_message,"str_doldrums", 0xFF7ABDFF),
            (try_end),
            
            (try_begin),
              (scene_prop_get_instance, ":ship_instance", "spr_klabautermann_ship1", "$player_ship_number"),
              (scene_prop_get_slot, reg1, ":ship_instance", 9),
                 (val_mul, reg1, 2),
              (display_message,"str_speed_report", 0xFF7ABDFF),
            (try_end),
          
            (try_begin),
              (eq, "$weather", 1),
              (str_store_string, s1, "str_very_bad"),
            (else_try),
              (eq, "$weather", 2),
              (str_store_string, s1, "str_bad"),
            (else_try),
              (eq, "$weather", 3),
              (str_store_string, s1, "str_normal"),
            (else_try),
              (str_store_string, s1, "str_good"),
            (try_end),
            (display_message,"str_weather_report", 0xFF7ABDFF),
          (try_end),
          
          (scene_prop_set_slot, ":ship_instance", 6, ":sail"),  
          (scene_prop_set_slot, ":ship_instance", 7, ":rowing"), 
          (scene_prop_set_slot, ":ship_instance", 8, ":rudder"), 
          (scene_prop_set_slot, ":ship_instance", 12, ":boarding_wanted"),  
          (scene_prop_set_slot, ":ship_instance", 13, ":landing_wanted"), 
          
        (try_end), 
         ])
         
KLABAUTERMANN_6_camera =(        
  0, 0, 0, [],                ### THE CAMERA TRIGGER
       [   
        (try_begin),
          (eq, "$cam_mode", 1),
          (neg|eq, "$player_ship_number", -1),
          (scene_prop_get_instance, ":ship_instance", "spr_klabautermann_ship1", "$player_ship_number"),
          (prop_instance_get_position, pos8, ":ship_instance"),
          (position_move_z, pos8, 500),
          (get_player_agent_no, ":agent"),
          (agent_get_look_position, pos9, ":agent"),
          (position_copy_rotation, pos8, pos9),
          (position_move_y, pos8, -1500),
          (try_begin),
            (position_get_z, ":z", pos8),
            (lt, ":z", 0),
            (position_set_z, pos8, 0),
          (end_try),
          (mission_cam_set_position, pos8),
        (try_end),
         ])

KLABAUTERMANN_7_wind =(         
  180, 0, 0, [],                ### THE WIND TRIGGER
       [   
        (try_begin),
          (store_random_in_range, ":chance", 1, 4),
          (try_begin),
            (eq, ":chance", 1),
            (store_random_in_range, "$wind_angle", 0, 360),
          (try_end),
        (try_end),
         ])

KLABAUTERMANN_8_main =(         
  1, 0.2, 0, [],                ### THE KLABAUTERMANN TRIGGER
       [
        (call_script, "script_put_the_klabautermann_into_the_ships"),
         ]) 

KLABAUTERMANN_9_reinforcement_A =(         
  1, 0, 5, [],                ### THE REINFORCE TRIGGER
       [
        (try_begin),
          (lt,"$attacker_reinforcement_stage",2),
          (store_mission_timer_a,":mission_time"),
          (ge,":mission_time",10),
          (store_normalized_team_count,":num_attackers", 1),
          (lt,":num_attackers",10),#gdw6
          (entry_point_get_position, pos5,0),            # Entry Point is next spawnpoint
          (set_spawn_position, pos5),
          (assign, "$last_reinforcement_ship", 0),
          (add_reinforcements_to_entry,0,7),
          (val_add,"$attacker_reinforcement_stage",1),
        (try_end),
        
        (try_begin),
          (lt,"$defender_reinforcement_stage",2),
          (store_mission_timer_a,":mission_time"),
          (ge,":mission_time",10),
          (store_normalized_team_count,":num_attackers", 0),
          (lt,":num_attackers",10),#gdw6
          (entry_point_get_position, pos5, 10),            # Entry Point is next spawnpoint
          (set_spawn_position, pos5),      
          (assign, "$last_reinforcement_ship", 0),
          (add_reinforcements_to_entry,3,7),
          (val_add,"$defender_reinforcement_stage",1),
        (try_end),    
         ]) 

KLABAUTERMANN_10_reinforcement_B =(         
  ti_on_agent_spawn, 0, 0, [],
  [
    (store_mission_timer_a,":mission_time"),
    (ge,":mission_time",10),
    (try_begin),
      (eq, "$last_reinforcement_ship", 0), ### then spawn ship with all instances...
      (spawn_scene_prop, "spr_klabautermann_ship1"),
      (assign, "$last_reinforcement_ship", reg0),
      (scene_prop_set_visibility, "$last_reinforcement_ship", 0),
      (spawn_scene_prop, "spr_klabautermann_ship1_sail_off"),
      (scene_prop_set_slot, "$last_reinforcement_ship", 17, reg0), # assigns sail-off-instance to the other instance
      #(scene_prop_set_team, "$last_reinforcement_ship", 1),
      (spawn_scene_prop, "spr_klabautermann_ship1_planks_a"),
      (scene_prop_set_slot, "$last_reinforcement_ship", 18, reg0), # assigns plank-instance to the ship-instance
      (scene_prop_set_visibility, reg0, 0),
      (spawn_scene_prop, "spr_klabautermann_ship1_planks_b"),
      (scene_prop_set_slot, "$last_reinforcement_ship", 19, reg0), # assigns plank-instance to the ship-instance
      (scene_prop_set_visibility, reg0, 0),
    (try_end),
    (store_trigger_param_1, ":agent"),
    (prop_instance_get_position, pos7, "$last_reinforcement_ship"),
    (position_move_z, pos7, 200),    
    (agent_set_position, ":agent", pos7),
    (agent_set_slot, ":agent", 23, "$last_reinforcement_ship"),
  ])

KLABAUTERMANN_11_sound =(         
  1, 0, 0, [],                ### THE SOUND TRIGGER
       [
        (try_begin),
          (eq, "$player_ship_number", -1),
          (try_begin),
            (eq, "$move_sound", 0),
            (stop_all_sounds),
            (assign, "$move_sound", -1),
          (try_end),
        (else_try),   
          (scene_prop_get_instance, ":player_ship_instance", "spr_klabautermann_ship1", "$player_ship_number"),
          (scene_prop_get_slot, ":speed", ":player_ship_instance", 9),
          (try_begin),
            (gt, ":speed", 0),
            (le, "$move_sound", 0),
            (stop_all_sounds),
            (play_sound, "snd_ship_drive", 1),
            (assign, "$move_sound", 1),
          (else_try),
            (le, ":speed", 0),
            (eq, "$move_sound", 1),
            (stop_all_sounds),
            #(prop_instance_get_position, pos7, ":player_ship_instance"),
            (play_sound, "snd_ship_stay", 1),
            (assign, "$move_sound", 0),        
          (try_end),
        (try_end),
         ])          

#############################
#### END OF KLABAUTERMANN ###
############################# Phaiak chief acaba sea battles



#order skirsmih a tropas chief caba'drin, incluido el tema de ordenes tambien
order_skirmish_triggers = [
    (0, 0, 1, [(key_clicked, key_for_skirmish)], [(call_script, "script_order_skirmish_begin_end")]),
    (0.5, 0, 0, [(call_script, "script_cf_order_skirmish_check")], [(call_script, "script_order_skirmish_skirmish")]),
    (ti_before_mission_start, 0, ti_once, [], [
        (try_for_range, ":i", slot_party_cabadrin_order_d0, slot_party_cabadrin_order_d8 + 1),
           (party_set_slot, "p_main_party", ":i", 33), #0?
        (try_end),
    ]),

    #a partir de esto es tema de ordenes
   (0, 0, 1, [(key_clicked, key_for_onehand)], [(call_script, "script_order_weapon_type_switch", onehand)]),
   (0, 0, 1, [(key_clicked, key_for_bothhands)], [(call_script, "script_order_weapon_type_switch", bothhands)]), 
   (0, 0, 1, [(key_clicked, key_for_ranged)], [(call_script, "script_order_weapon_type_switch", ranged)]),
   (0, 0, 1, [(key_clicked, key_for_shield)], [(call_script, "script_order_weapon_type_switch", shield)]),
   #(0, 0, 1, [(key_clicked, key_for_polearms)], [(call_script, "script_switch_to_noswing_weapons", ":agent")]),
   #gdwnew test above
    (0, 0, 0, [(game_key_clicked, gk_order_4)], [
            (eq, "$gk_order", gk_order_3),    #ANY WEAPON
            (call_script, "script_order_set_slot", clear),]),
   
    (ti_before_mission_start, 0, ti_once, [], [(assign, "$gk_order", 0)]),
     ]
#caba'drin acaba

############Habilidades de chel warcry y battlecry chief##########################
       #EGIII WARCRY
warcry_chel = [
     (0, 0, 60, [(key_clicked, key_b),(neg|main_hero_fallen)
   
    ], [
                 
#(play_sound,"snd_man_victory"),
             
  (get_player_agent_no, ":player_agent"),
  (agent_get_horse,":agent_mounted",":player_agent"),
  (try_begin),
     (eq,":agent_mounted",-1),
     (agent_set_animation, ":player_agent", "anim_cheer"),
  (try_end),
  (agent_play_sound,":player_agent","snd_man_victory"),
  (agent_get_position, pos1, ":player_agent"),
  (store_character_level,":level","trp_player"),
  (val_mul,":level",2),
  (val_add,":level",1),

  (try_for_agents,":agent"),
     (set_fixed_point_multiplier, 1),
        (agent_is_alive,":agent"),
        (agent_is_human,":agent"),
      (neg|agent_is_ally,":agent"),

      (agent_get_troop_id,":trp_agent", ":agent"),
      (store_character_level,":troop_level",":trp_agent"),
      (ge,":level",":troop_level"),
      (agent_get_position, pos2, ":agent"),
      (get_distance_between_positions,":distance",pos2,pos1),
      (lt,":distance",500),

      (set_fixed_point_multiplier, 10),

      (position_get_x,":player_x",pos1),
      (position_get_y,":player_y",pos1),
      (position_get_x,":enemy_x",pos2),
      (position_get_y,":enemy_y",pos2),

      (store_sub,":difference_x",":enemy_x",":player_x"),
      (val_mul,":difference_x",12),

      (store_sub,":difference_y",":enemy_y",":player_y"),
      (val_mul,":difference_y",12),

      (val_add,":enemy_x",":difference_x"),
      (val_add,":enemy_y",":difference_y"),

      (position_set_x,pos2,":enemy_x"),
      (position_set_y,pos2,":enemy_y"),

      (agent_set_scripted_destination,":agent",pos2,1),
  (try_end),

  (display_message,"@You unleash a fearsome cry!",0x6495ed),
       (set_fixed_point_multiplier, 1),
  (call_script, "script_focus_exp_penalty"),
        ]),
     
 # (0, 5, 60, [(key_clicked, key_b),(neg|main_hero_fallen)    MOTO duplicate

   # ], [

  # #(display_message,"@Enemies regain their courage!",0x6495ed),
  # (try_for_agents,":agent"),
   # (agent_is_alive,":agent"),
        # (agent_is_human,":agent"),
      # (neg|agent_is_ally,":agent"),
# (agent_clear_scripted_mode,":agent"),
  # (try_end),

        # ]),

  (0, 7, 60, [(key_clicked, key_b),(neg|main_hero_fallen)

   ], [

  (try_for_agents,":agent"),
   (agent_is_alive,":agent"),
        (agent_is_human,":agent"),
      (neg|agent_is_ally,":agent"),
(agent_clear_scripted_mode,":agent"),
  (try_end),

        ]),
# battlecry

  (0, 0, 60, [(key_clicked, key_u),(store_attribute_level,"$attribute","trp_player",3),(neg|main_hero_fallen),
  ], [
  (get_player_agent_no, ":player_agent"),
  (try_begin),
     (agent_get_horse,":agent_mounted",":player_agent"),
     (eq,":agent_mounted",-1),
     (agent_set_animation, ":player_agent", "anim_taunt"),
   #  (agent_set_animation, ":player_agent", "anim_cheer"),
  (try_end),
  (agent_play_sound,":player_agent","snd_man_warcry"),
  (agent_play_sound,":player_agent","snd_shield_hit_metal_wood"),
  ]),
   (0, 2, 60, [(key_clicked, key_u),(store_attribute_level,"$attribute","trp_player",3),(neg|main_hero_fallen),

#    (get_player_agent_no, ":player_agent")
   ], [

  (store_skill_level,":leadership","skl_leadership","trp_player"),
    (get_player_agent_no, ":player_agent"),
  (store_sub,":cha_bonus","$attribute",0),
  (val_mul,":leadership",3),
  (try_for_agents,":agent"),


        (agent_is_alive,":agent"),
        (agent_is_human,":agent"),
      (agent_is_ally,":agent"),
      (neg|eq,":agent",":player_agent"),
      (store_agent_hit_points,":life",":agent",0),
      (try_begin),
     (agent_get_class ,":blah", ":agent"),
     (neq,":blah",grc_cavalry),
       (agent_set_animation, ":agent", "anim_cheer"),
      (try_end),

  (val_add,":life",":cha_bonus"),
  (val_add,":life",":leadership"),
  (agent_set_hit_points,":agent",":life",0),
  #(agent_get_horse,":horse",":agent"),
  (agent_play_sound, ":agent", "snd_man_victory"),
       #(agent_set_animation, ":agent", "anim_cheer"),
      (try_end),
      (store_add,":recovery",":leadership",":cha_bonus"),
      (assign,reg1,":recovery"),
(display_message,"@You rally your men! (wounded troops recover {reg1} % hitpoints)",0x6495ed),
  (call_script, "script_rage_exp_penalty"),
        ]),
     ]
#terminado habilidades de chel
#heridas de chel chief empieza
heridas_chel = [
       (0,
        2,
        ti_once,
        [
            (main_hero_fallen)
        ],
        [
            (display_message,"@You have received a serious blow. The pain is unbearable.")
        ]
    ),
    
    (0,
        4,
        ti_once,
        [
            (main_hero_fallen)
        ],
        [
            (display_message,"@Breathe in...")
        ]
    ),
    
    (0,
        6,
        ti_once,
        [
            (main_hero_fallen)
        ],
        [
            (display_message,"@Breathe out...")
        ]
    ),
    
    (0,
        8,
        ti_once,
        [
   (eq, "$g_heridas_chel", 1),
            (main_hero_fallen)
        ],
        [
            (display_message,"@You make an effort to take another breath... "),
            (store_random_in_range,":wound_chance_roll",1,101),  ## chance
            (store_random_in_range,":wound_type_roll",1,101),  ## wound type
            (store_skill_level,":skill_ironflesh",skl_ironflesh,"trp_player"),
            (store_skill_level,":skill_first_aid",skl_first_aid,"trp_player"),
            (store_skill_level,":skill_wound_treatment",skl_wound_treatment,"trp_player"),
            (store_skill_level,":skill_surgery",skl_surgery,"trp_player"),
            (store_attribute_level,":attrib_charisma","trp_player",ca_charisma),
            ## bonuses to outcome of knockout
            (val_sub,":attrib_charisma",10),
            (store_add,":modifier",":attrib_charisma",":skill_ironflesh"),
            (val_add,":wound_chance_roll",":modifier"),
            ## decide outcome
                (try_begin),
                    (is_between,":wound_chance_roll",31,100), # complete recovery, scratches bruises, no wounds
                    (display_message,"@You will recover from this blow completely."),
                (else_try),
                    (is_between,":wound_chance_roll",11,30), # 26-50 light wound
                    (store_current_day,":currentday"),
                    (assign,":healtime",31),
                    (val_sub,":healtime",":skill_first_aid"),
                    (val_sub,":healtime",":skill_wound_treatment"),
                    (val_sub,":healtime",":skill_surgery"),
                    (store_add,"$heal_day",":currentday",":healtime"),
                        # wound type
                        (try_begin),
                            (is_between,":wound_type_roll",76,100),
                            (display_message,"@You suffer a deep cut on your arm. (-1 strength)",0xFFFFAAAA),
                            (assign,"$wound_type",1),
                            (troop_raise_attribute,"trp_player",ca_strength,-1),
                        (else_try),
                            (is_between,":wound_type_roll",51,75),
                            (display_message,"@You suffer a nasty cut on your torso. (-1 strength, -1 agility)",0xFFFFAAAA),
                            (assign,"$wound_type",2),
                            (troop_raise_attribute,"trp_player",ca_strength,-1),
                            (troop_raise_attribute,"trp_player",ca_agility,-1),
                        (else_try),
                            (is_between,":wound_type_roll",26,50),
                            (display_message,"@You suffer a blow to the head. (-1 intelligence)",0xFFFFAAAA),
                            (assign,"$wound_type",3),
                            (troop_raise_attribute,"trp_player",ca_intelligence,-1),
                        (else_try),
                            (display_message,"@You suffer a severe blow to your leg. (-1 agility)",0xFFFFAAAA),
                            (assign,"$wound_type",4),
                            (troop_raise_attribute,"trp_player",ca_agility,-1),
                        (try_end),
                (else_try),
                    (is_between,":wound_chance_roll",0,10), ## 0-25 serious wound
                    (store_current_day,":currentday"),
                    (assign,":healtime",41),
                    (val_sub,":healtime",":skill_first_aid"),
                    (val_sub,":healtime",":skill_wound_treatment"),
                    (val_sub,":healtime",":skill_surgery"),
                    (store_add,"$heal_day",":currentday",":healtime"),
                        (try_begin),
                            (is_between,":wound_type_roll",76,100),
                            (display_message,"@You suffer a broken arm. (-3 strength, -1 power strike, -1 power draw)",0xFFFFAAAA),
                            (assign,"$wound_type",5),
                            (troop_raise_attribute,"trp_player",ca_strength,-2),
                            (troop_raise_skill, "trp_player",skl_power_strike,-1),
                            (troop_raise_skill, "trp_player",skl_power_draw,-1),
                        (else_try),
                            (is_between,":wound_type_roll",51,75),
                            (display_message,"@You suffer a broken rib. (-2 strength, -2 agility, -1 ironflesh)",0xFFFFAAAA),
                            (assign,"$wound_type",6),
                            (troop_raise_attribute,"trp_player",ca_strength,-1),
                            (troop_raise_attribute,"trp_player",ca_agility,-2),
                            (troop_raise_skill, "trp_player",skl_ironflesh,-1),
                        (else_try),
                            (is_between,":wound_type_roll",26,50),
                            (display_message,"@You suffer a heavy blow to the head. (-2 intelligence, -1 leadership, -1 tactics)",0xFFFFAAAA),
                            (assign,"$wound_type",7),
                            (troop_raise_attribute,"trp_player",ca_intelligence,-2),
                            (troop_raise_skill, "trp_player",skl_leadership,-1),
                            (troop_raise_skill, "trp_player",skl_tactics,-1),
                        (else_try),
                            (display_message,"@You suffer a broken leg. (-3 agility, -1 athletics, -1 riding)",0xFFFFAAAA),
                            (assign,"$wound_type",8),
                            (troop_raise_attribute,"trp_player",ca_agility,-2),
                            (troop_raise_skill, "trp_player",skl_riding,-1),
                            (troop_raise_skill, "trp_player",skl_athletics,-1),
                        (try_end),
                (try_end),
        ]
    ),
     ]
#chel chief heridas end

#chief dano caida de caballo
rider_damage = [
   (0, 1, ti_once,
    [
    ],
      [
#       (assign, "$ridernum", 0),     # reset variable at battle start
        (try_for_agents, ":agent"),
          (agent_is_alive, ":agent"),
          (agent_is_human,":agent"),
#          (agent_get_troop_id, ":troop", ":agent"),
#          (troop_is_mounted, ":troop"),   
          (assign, ":agent_horse", 0),
          (agent_get_horse, ":agent_horse", ":agent"),
          (agent_set_slot, ":agent", slot_agent_horse, ":agent_horse"),
          (agent_set_slot, ":agent", slot_agent_got_damage, 0),    # reset variable at battle start
#          (val_add, "$ridernum", 1),
        (try_end),
#        (display_message,"@debug-horse1"),
      ]),


    (1, 0, 0,
    [
#    (gt, "$ridernum", 0), 
    ],
      [
        (try_for_agents, ":agent"),
          (agent_is_alive, ":agent"),
          (agent_is_human,":agent"),
          (agent_slot_eq, ":agent", slot_agent_got_damage, 0),   # agent haven't got damage
#          (agent_get_troop_id, ":troop", ":agent"),
#          (troop_is_mounted, ":troop"),
          (assign, ":agent_horse", 0),
          (agent_get_horse, ":agent_horse", ":agent"),
          (le, ":agent_horse", 0),              # agent doesn't have horse
          (agent_get_slot, ":agent_horse", ":agent", slot_agent_horse),
          (gt, ":agent_horse", 0),            # but he had horse at battle start
          (neg|agent_is_human,":agent_horse"),     
          (neg|agent_is_alive, ":agent_horse"),            # and his horse is dead
          (store_agent_hit_points, ":agent_hp", ":agent", 1),
          (gt, ":agent_hp", 1),         # avoid die by deal damage
#          (store_mul, ":hp_mul", ":agent_hp", 2),
#          (store_div, ":hp_high", ":hp_mul", 3),
          (store_div, ":hp_high", ":agent_hp", 2),     
          (store_div, ":hp_low", ":agent_hp", 3),
          (store_random_in_range, ":damage", ":hp_low", ":hp_high"),      # damage is 33%~50% of current agent HP.
          (agent_deliver_damage_to_agent, ":agent", ":agent", ":damage"),     # deal damage to agent
          (agent_set_slot, ":agent", slot_agent_got_damage, 1),     # agent have got damage
#          (val_sub, "$ridernum", 1),
          #(display_message,"@debug-horse2"),    # I inserted debug message, but this message doesn't shown and agent haven't got damage
        (try_end),
     ])
]
#dano caida de caballo acaba

multiplayer_server_check_belfry_movement = (
  0, 0, 0, [],
  [
    (multiplayer_is_server),
    (set_fixed_point_multiplier, 100),

    (try_for_range, ":belfry_kind", 0, 2),
      (try_begin),
        (eq, ":belfry_kind", 0),
        (assign, ":belfry_body_scene_prop", "spr_belfry_a"),
      (else_try),
        (assign, ":belfry_body_scene_prop", "spr_belfry_b"),
      (try_end),
    
      (scene_prop_get_num_instances, ":num_belfries", ":belfry_body_scene_prop"),
      (try_for_range, ":belfry_no", 0, ":num_belfries"),
        (scene_prop_get_instance, ":belfry_scene_prop_id", ":belfry_body_scene_prop", ":belfry_no"),
        (prop_instance_get_position, pos1, ":belfry_scene_prop_id"), #pos1 holds position of current belfry 
        (prop_instance_get_starting_position, pos11, ":belfry_scene_prop_id"),

        (store_add, ":belfry_first_entry_point_id", 11, ":belfry_no"), #belfry entry points are 110..119 and 120..129 and 130..139
        (try_begin),
          (eq, ":belfry_kind", 1),
          (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),
          (val_add, ":belfry_first_entry_point_id", ":number_of_belfry_a"),
        (try_end),        
                
        (val_mul, ":belfry_first_entry_point_id", 10),
        (store_add, ":belfry_last_entry_point_id", ":belfry_first_entry_point_id", 10),
    
        (try_for_range, ":entry_point_id", ":belfry_first_entry_point_id", ":belfry_last_entry_point_id"),
          (entry_point_is_auto_generated, ":entry_point_id"),
          (assign, ":belfry_last_entry_point_id", ":entry_point_id"),
        (try_end),
        
        (assign, ":belfry_last_entry_point_id_plus_one", ":belfry_last_entry_point_id"),
        (val_sub, ":belfry_last_entry_point_id", 1),
        (assign, reg0, ":belfry_last_entry_point_id"),
        (neg|entry_point_is_auto_generated, ":belfry_last_entry_point_id"),

        (try_begin),
          (get_sq_distance_between_positions, ":dist_between_belfry_and_its_destination", pos1, pos11),
          (ge, ":dist_between_belfry_and_its_destination", 4), #0.2 * 0.2 * 100 = 4 (if distance between belfry and its destination already less than 20cm no need to move it anymore)

          (assign, ":max_dist_between_entry_point_and_belfry_destination", -1), #should be lower than 0 to allow belfry to go last entry point
          (assign, ":belfry_next_entry_point_id", -1),
          (try_for_range, ":entry_point_id", ":belfry_first_entry_point_id", ":belfry_last_entry_point_id_plus_one"),
            (entry_point_get_position, pos4, ":entry_point_id"),
            (get_sq_distance_between_positions, ":dist_between_entry_point_and_belfry_destination", pos11, pos4),
            (lt, ":dist_between_entry_point_and_belfry_destination", ":dist_between_belfry_and_its_destination"),
            (gt, ":dist_between_entry_point_and_belfry_destination", ":max_dist_between_entry_point_and_belfry_destination"),
            (assign, ":max_dist_between_entry_point_and_belfry_destination", ":dist_between_entry_point_and_belfry_destination"),
            (assign, ":belfry_next_entry_point_id", ":entry_point_id"),
          (try_end),

          (try_begin),
            (ge, ":belfry_next_entry_point_id", 0),
            (entry_point_get_position, pos5, ":belfry_next_entry_point_id"), #pos5 holds belfry next entry point target during its path
          (else_try),
            (copy_position, pos5, pos11),    
          (try_end),
        
          (get_distance_between_positions, ":belfry_next_entry_point_distance", pos1, pos5),
        
          #collecting scene prop ids of belfry parts
          (try_begin),
            (eq, ":belfry_kind", 0),
            #belfry platform_a
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_platform_a", ":belfry_no"),
            #belfry platform_b
            (scene_prop_get_instance, ":belfry_platform_b_scene_prop_id", "spr_belfry_platform_b", ":belfry_no"),
          (else_try),
            #belfry platform_a
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_b_platform_a", ":belfry_no"),
          (try_end),
    
          #belfry wheel_1
          (store_mul, ":wheel_no", ":belfry_no", 3),
          (try_begin),
            (eq, ":belfry_body_scene_prop", "spr_belfry_b"),
            (scene_prop_get_num_instances, ":number_of_belfry_a", "spr_belfry_a"),    
            (store_mul, ":number_of_belfry_a_wheels", ":number_of_belfry_a", 3),
            (val_add, ":wheel_no", ":number_of_belfry_a_wheels"),
          (try_end),
          (scene_prop_get_instance, ":belfry_wheel_1_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
          #belfry wheel_2
          (val_add, ":wheel_no", 1),
          (scene_prop_get_instance, ":belfry_wheel_2_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),
          #belfry wheel_3
          (val_add, ":wheel_no", 1),
          (scene_prop_get_instance, ":belfry_wheel_3_scene_prop_id", "spr_belfry_wheel", ":wheel_no"),

          (init_position, pos17),
          (position_move_y, pos17, -225),
          (position_transform_position_to_parent, pos18, pos1, pos17),
          (position_move_y, pos17, -225),
          (position_transform_position_to_parent, pos19, pos1, pos17),

          (assign, ":number_of_agents_around_belfry", 0),
          (get_max_players, ":num_players"),
          (try_for_range, ":player_no", 0, ":num_players"),
            (player_is_active, ":player_no"),
            (player_get_agent_id, ":agent_id", ":player_no"),
            (ge, ":agent_id", 0),
            (agent_get_team, ":agent_team", ":agent_id"),
            (eq, ":agent_team", 1), #only team2 players allowed to move belfry (team which spawns outside the castle (team1 = 0, team2 = 1))
            (agent_get_horse, ":agent_horse_id", ":agent_id"),
            (eq, ":agent_horse_id", -1),
            (agent_get_position, pos2, ":agent_id"),
            (get_sq_distance_between_positions_in_meters, ":dist_between_agent_and_belfry", pos18, pos2),

            (lt, ":dist_between_agent_and_belfry", multi_distance_sq_to_use_belfry), #must be at most 10m * 10m = 100m away from the player
            (neg|scene_prop_has_agent_on_it, ":belfry_scene_prop_id", ":agent_id"),
            (neg|scene_prop_has_agent_on_it, ":belfry_platform_a_scene_prop_id", ":agent_id"),

            (this_or_next|eq, ":belfry_kind", 1), #there is this_or_next here because belfry_b has no platform_b
            (neg|scene_prop_has_agent_on_it, ":belfry_platform_b_scene_prop_id", ":agent_id"),
    
            (neg|scene_prop_has_agent_on_it, ":belfry_wheel_1_scene_prop_id", ":agent_id"),#can be removed to make faster
            (neg|scene_prop_has_agent_on_it, ":belfry_wheel_2_scene_prop_id", ":agent_id"),#can be removed to make faster
            (neg|scene_prop_has_agent_on_it, ":belfry_wheel_3_scene_prop_id", ":agent_id"),#can be removed to make faster
            (neg|position_is_behind_position, pos2, pos19),
            (position_is_behind_position, pos2, pos1),
            (val_add, ":number_of_agents_around_belfry", 1),        
          (try_end),

          (val_min, ":number_of_agents_around_belfry", 16),

          (try_begin),
            (scene_prop_get_slot, ":pre_number_of_agents_around_belfry", ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing),
            (scene_prop_get_slot, ":next_entry_point_id", ":belfry_scene_prop_id", scene_prop_next_entry_point_id),
            (this_or_next|neq, ":pre_number_of_agents_around_belfry", ":number_of_agents_around_belfry"),
            (neq, ":next_entry_point_id", ":belfry_next_entry_point_id"),

            (try_begin),
              (eq, ":next_entry_point_id", ":belfry_next_entry_point_id"), #if we are still targetting same entry point subtract 
              (prop_instance_is_animating, ":is_animating", ":belfry_scene_prop_id"),
              (eq, ":is_animating", 1),

              (store_mul, ":sqrt_number_of_agents_around_belfry", "$g_last_number_of_agents_around_belfry", 100),
              (store_sqrt, ":sqrt_number_of_agents_around_belfry", ":sqrt_number_of_agents_around_belfry"),
              (val_min, ":sqrt_number_of_agents_around_belfry", 300),
              (assign, ":distance", ":belfry_next_entry_point_distance"),
              (val_mul, ":distance", ":sqrt_number_of_agents_around_belfry"),
              (val_div, ":distance", 100), #100 is because of fixed_point_multiplier
              (val_mul, ":distance", 4), #multiplying with 4 to make belfry pushing process slower, 
                                                                 #with 16 agents belfry will go with 4 / 4 = 1 speed (max), with 1 agent belfry will go with 1 / 4 = 0.25 speed (min)    
            (try_end),

            (try_begin),
              (ge, ":belfry_next_entry_point_id", 0),

              #up down rotation of belfry's next entry point
              (init_position, pos9),
              (position_set_y, pos9, -500), #go 5.0 meters back
              (position_set_x, pos9, -300), #go 3.0 meters left
              (position_transform_position_to_parent, pos10, pos5, pos9), 
              (position_get_distance_to_terrain, ":height_to_terrain_1", pos10), #learn distance between 5 meters back of entry point(pos10) and ground level at left part of belfry
      
              (init_position, pos9),
              (position_set_y, pos9, -500), #go 5.0 meters back
              (position_set_x, pos9, 300), #go 3.0 meters right
              (position_transform_position_to_parent, pos10, pos5, pos9), 
              (position_get_distance_to_terrain, ":height_to_terrain_2", pos10), #learn distance between 5 meters back of entry point(pos10) and ground level at right part of belfry

              (store_add, ":height_to_terrain", ":height_to_terrain_1", ":height_to_terrain_2"),
              (val_mul, ":height_to_terrain", 100), #because of fixed point multiplier

              (store_div, ":rotate_angle_of_next_entry_point", ":height_to_terrain", 24), #if there is 1 meters of distance (100cm) then next target position will rotate by 2 degrees. #ac sonra
              (init_position, pos20),    
              (position_rotate_x_floating, pos20, ":rotate_angle_of_next_entry_point"),
              (position_transform_position_to_parent, pos23, pos5, pos20),

              #right left rotation of belfry's next entry point
              (init_position, pos9),
              (position_set_x, pos9, -300), #go 3.0 meters left
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in -x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_left", pos10), #learn distance between 3.0 meters left of entry point(pos10) and ground level
              (init_position, pos9),
              (position_set_x, pos9, 300), #go 3.0 meters left
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_right", pos10), #learn distance between 3.0 meters right of entry point(pos10) and ground level
              (store_sub, ":height_to_terrain_1", ":height_to_terrain_at_left", ":height_to_terrain_at_right"),

              (init_position, pos9),
              (position_set_x, pos9, -300), #go 3.0 meters left
              (position_set_y, pos9, -500), #go 5.0 meters forward
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in -x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_left", pos10), #learn distance between 3.0 meters left of entry point(pos10) and ground level
              (init_position, pos9),
              (position_set_x, pos9, 300), #go 3.0 meters left
              (position_set_y, pos9, -500), #go 5.0 meters forward
              (position_transform_position_to_parent, pos10, pos5, pos9), #applying 3.0 meters in x to position of next entry point target, final result is in pos10
              (position_get_distance_to_terrain, ":height_to_terrain_at_right", pos10), #learn distance between 3.0 meters right of entry point(pos10) and ground level
              (store_sub, ":height_to_terrain_2", ":height_to_terrain_at_left", ":height_to_terrain_at_right"),

              (store_add, ":height_to_terrain", ":height_to_terrain_1", ":height_to_terrain_2"),    
              (val_mul, ":height_to_terrain", 100), #100 is because of fixed_point_multiplier
              (store_div, ":rotate_angle_of_next_entry_point", ":height_to_terrain", 24), #if there is 1 meters of distance (100cm) then next target position will rotate by 25 degrees. 
              (val_mul, ":rotate_angle_of_next_entry_point", -1),

              (init_position, pos20),
              (position_rotate_y_floating, pos20, ":rotate_angle_of_next_entry_point"),
              (position_transform_position_to_parent, pos22, pos23, pos20),
            (else_try),
              (copy_position, pos22, pos5),      
            (try_end),
              
            (try_begin),
              (ge, ":number_of_agents_around_belfry", 1), #if there is any agents pushing belfry

              (store_mul, ":sqrt_number_of_agents_around_belfry", ":number_of_agents_around_belfry", 100),
              (store_sqrt, ":sqrt_number_of_agents_around_belfry", ":sqrt_number_of_agents_around_belfry"),
              (val_min, ":sqrt_number_of_agents_around_belfry", 300),
              (val_mul, ":belfry_next_entry_point_distance", 100), #100 is because of fixed_point_multiplier
              (val_mul, ":belfry_next_entry_point_distance", 3), #multiplying with 3 to make belfry pushing process slower, 
                                                                 #with 9 agents belfry will go with 3 / 3 = 1 speed (max), with 1 agent belfry will go with 1 / 3 = 0.33 speed (min)    
              (val_div, ":belfry_next_entry_point_distance", ":sqrt_number_of_agents_around_belfry"),
              #calculating destination coordinates of belfry parts
              #belfry platform_a
              (prop_instance_get_position, pos6, ":belfry_platform_a_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos1, pos6),
              (position_transform_position_to_parent, pos8, pos22, pos7),
              (prop_instance_animate_to_position, ":belfry_platform_a_scene_prop_id", pos8, ":belfry_next_entry_point_distance"),    
              #belfry platform_b
              (try_begin),
                (eq, ":belfry_kind", 0),
                (prop_instance_get_position, pos6, ":belfry_platform_b_scene_prop_id"),
                (position_transform_position_to_local, pos7, pos1, pos6),
                (position_transform_position_to_parent, pos8, pos22, pos7),
                (prop_instance_animate_to_position, ":belfry_platform_b_scene_prop_id", pos8, ":belfry_next_entry_point_distance"),
              (try_end),
              #wheel rotation
              (store_mul, ":belfry_wheel_rotation", ":belfry_next_entry_point_distance", -25),
              #(val_add, "$g_belfry_wheel_rotation", ":belfry_wheel_rotation"),
              (assign, "$g_last_number_of_agents_around_belfry", ":number_of_agents_around_belfry"),

              #belfry wheel_1
              #(prop_instance_get_starting_position, pos13, ":belfry_wheel_1_scene_prop_id"),
              (prop_instance_get_position, pos13, ":belfry_wheel_1_scene_prop_id"),
              (prop_instance_get_position, pos20, ":belfry_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos20, pos13),
              (position_transform_position_to_parent, pos21, pos22, pos7),
              (prop_instance_rotate_to_position, ":belfry_wheel_1_scene_prop_id", pos21, ":belfry_next_entry_point_distance", ":belfry_wheel_rotation"),
      
              #belfry wheel_2
              #(prop_instance_get_starting_position, pos13, ":belfry_wheel_2_scene_prop_id"),
              (prop_instance_get_position, pos13, ":belfry_wheel_2_scene_prop_id"),
              (prop_instance_get_position, pos20, ":belfry_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos20, pos13),
              (position_transform_position_to_parent, pos21, pos22, pos7),
              (prop_instance_rotate_to_position, ":belfry_wheel_2_scene_prop_id", pos21, ":belfry_next_entry_point_distance", ":belfry_wheel_rotation"),
      
              #belfry wheel_3
              (prop_instance_get_position, pos13, ":belfry_wheel_3_scene_prop_id"),
              (prop_instance_get_position, pos20, ":belfry_scene_prop_id"),
              (position_transform_position_to_local, pos7, pos20, pos13),
              (position_transform_position_to_parent, pos21, pos22, pos7),
              (prop_instance_rotate_to_position, ":belfry_wheel_3_scene_prop_id", pos21, ":belfry_next_entry_point_distance", ":belfry_wheel_rotation"),

              #belfry main body
              (prop_instance_animate_to_position, ":belfry_scene_prop_id", pos22, ":belfry_next_entry_point_distance"),    
            (else_try),
              (prop_instance_is_animating, ":is_animating", ":belfry_scene_prop_id"),
              (eq, ":is_animating", 1),

              #belfry platform_a
              (prop_instance_stop_animating, ":belfry_platform_a_scene_prop_id"),
              #belfry platform_b
              (try_begin),
                (eq, ":belfry_kind", 0),
                (prop_instance_stop_animating, ":belfry_platform_b_scene_prop_id"),
              (try_end),
              #belfry wheel_1
              (prop_instance_stop_animating, ":belfry_wheel_1_scene_prop_id"),
              #belfry wheel_2
              (prop_instance_stop_animating, ":belfry_wheel_2_scene_prop_id"),
              #belfry wheel_3
              (prop_instance_stop_animating, ":belfry_wheel_3_scene_prop_id"),
              #belfry main body
              (prop_instance_stop_animating, ":belfry_scene_prop_id"),
            (try_end),
        
            (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_number_of_agents_pushing, ":number_of_agents_around_belfry"),    
            (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_next_entry_point_id, ":belfry_next_entry_point_id"),
          (try_end),
        (else_try),
          (le, ":dist_between_belfry_and_its_destination", 4),
          (scene_prop_slot_eq, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 0),
      
          (scene_prop_set_slot, ":belfry_scene_prop_id", scene_prop_belfry_platform_moved, 1),    

          (try_begin),
            (eq, ":belfry_kind", 0),
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_platform_a", ":belfry_no"),
          (else_try),
            (scene_prop_get_instance, ":belfry_platform_a_scene_prop_id", "spr_belfry_b_platform_a", ":belfry_no"),
          (try_end),
    
          (prop_instance_get_starting_position, pos0, ":belfry_platform_a_scene_prop_id"),
          (prop_instance_animate_to_position, ":belfry_platform_a_scene_prop_id", pos0, 400),    
        (try_end),
      (try_end),
    (try_end),
    ])

multiplayer_server_spawn_bots = (
  0, 0, 0, [    
           ],
  [

          (multiplayer_is_server),
    (eq, "$g_multiplayer_ready_for_spawning_agent", 1),
    (store_add, ":total_req", "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_required_team_2"), #aqui suma todos los bots
    (try_begin),
      (gt, ":total_req", 0),

      (try_begin),
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),

        (team_get_score, ":team_1_score", 0),
        (team_get_score, ":team_2_score", 1),

        (store_add, ":current_round", ":team_1_score", ":team_2_score"),
        (eq, ":current_round", 0),

        (store_mission_timer_a, ":round_time"),
        (val_sub, ":round_time", "$g_round_start_time"),
        (lt, ":round_time", 20),

        (assign, ":rounded_game_first_round_time_limit_past", 0),
      (else_try),
        (assign, ":rounded_game_first_round_time_limit_past", 1),
      (try_end),
    
      (eq, ":rounded_game_first_round_time_limit_past", 1),
    
      (store_random_in_range, ":random_req", 0, ":total_req"), 
      (val_sub, ":random_req", "$g_multiplayer_num_bots_required_team_1"), 
      (try_begin),
        (lt, ":random_req", 0), 
        #add to team 1
        (assign, ":selected_team", 0),
      (else_try),
        #add to team 2
        (assign, ":selected_team", 1),
      (try_end),

      (try_begin),
        (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
        (eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),

        (store_mission_timer_a, ":round_time"),
        (val_sub, ":round_time", "$g_round_start_time"),

        (try_begin),
          (le, ":round_time", 20),
          (assign, ":look_only_actives", 0),
        (else_try),
          (assign, ":look_only_actives", 1),
        (try_end),
      (else_try),
        (assign, ":look_only_actives", 1),
      (try_end),
    
      (call_script, "script_multiplayer_find_bot_troop_and_group_for_spawn", ":selected_team", ":look_only_actives"),
      (assign, ":selected_troop", reg0),
      (assign, ":selected_group", reg1),

      (team_get_faction, ":team_faction", ":selected_team"),
      (assign, ":num_ai_troops", 0),
      (try_for_range, ":cur_ai_troop", multiplayer_ai_troops_begin, multiplayer_ai_troops_end),
        (store_troop_faction, ":ai_troop_faction", ":cur_ai_troop"),
        (eq, ":ai_troop_faction", ":team_faction"),
        (val_add, ":num_ai_troops", 1),
      (try_end),

      (assign, ":number_of_active_players_wanted_bot", 0),

      (get_max_players, ":num_players"),
      (try_for_range, ":player_no", 0, ":num_players"),
        (player_is_active, ":player_no"),
        (player_get_team_no, ":player_team_no", ":player_no"),
        (eq, ":selected_team", ":player_team_no"),

        (assign, ":ai_wanted", 0),
        (store_add, ":end_cond", slot_player_bot_type_1_wanted, ":num_ai_troops"),
        (try_for_range, ":bot_type_wanted_slot", slot_player_bot_type_1_wanted, ":end_cond"),
          (player_slot_ge, ":player_no", ":bot_type_wanted_slot", 1),
          (assign, ":ai_wanted", 1),
          (assign, ":end_cond", 0), 
        (try_end),

        (ge, ":ai_wanted", 1),

        (val_add, ":number_of_active_players_wanted_bot", 1),
      (try_end),

      (try_begin),
        (this_or_next|ge, ":selected_group", 0),
        (eq, ":number_of_active_players_wanted_bot", 0),

        (troop_get_inventory_slot, ":has_item", ":selected_troop", ek_horse),
        (try_begin),
          (ge, ":has_item", 0),
          (assign, ":is_horseman", 1),
        (else_try),
          (assign, ":is_horseman", 0),
        (try_end),

        (try_begin),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),

          (store_mission_timer_a, ":round_time"),
          (val_sub, ":round_time", "$g_round_start_time"),

          (try_begin),
            (lt, ":round_time", 20), #at start of game spawn at base entry point
            (try_begin),
              (eq, ":selected_team", 0),
              (call_script, "script_multiplayer_find_spawn_point", ":selected_team", 1, ":is_horseman"), 
            (else_try),
              (assign, reg0, multi_initial_spawn_point_team_2),
            (try_end),
          (else_try),
            (call_script, "script_multiplayer_find_spawn_point", ":selected_team", 0, ":is_horseman"), 
          (try_end),
        (else_try),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
      
          (try_begin),
            (eq, ":selected_team", 0),
            (assign, reg0, 0),
          (else_try),
            (assign, reg0, 32),
          (try_end),

        (else_try),
          (call_script, "script_multiplayer_find_spawn_point", ":selected_team", 0, ":is_horseman"), 
        (try_end),
      
        (store_current_scene, ":cur_scene"),
        (modify_visitors_at_site, ":cur_scene"),
        (add_visitors_to_current_scene, reg0, ":selected_troop", 1, ":selected_team", ":selected_group"),
        (assign, "$g_multiplayer_ready_for_spawning_agent", 0),

        (try_begin),
          (eq, ":selected_team", 0),
          (val_sub, "$g_multiplayer_num_bots_required_team_1", 1), 
        (else_try), 
          (eq, ":selected_team", 1),
          (val_sub, "$g_multiplayer_num_bots_required_team_2", 1),
        (try_end),
      (try_end),
    (try_end),  
    ])

###chief capitan cuando es el modo de batalla de lords
multiplayer_server_spawn_bots2 = (
  0, 0, 0, [#(eq, "$g_round_tropas", 1), #chief capitan
           ],
  [
         (multiplayer_is_server),
         (eq, "$g_round_tropas", 2), #chief capitan
      (try_begin),
         (eq, "$g_multiplayer_ready_for_spawning_agent", 1),
         (try_begin),
        (team_get_score, ":team_1_score", 0),
        (team_get_score, ":team_2_score", 1),

        (store_add, ":current_round", ":team_1_score", ":team_2_score"),
        (eq, ":current_round", 0),

        (store_mission_timer_a, ":round_time"),
        (val_sub, ":round_time", "$g_round_start_time"),
        (lt, ":round_time", 20),

        (assign, ":rounded_game_first_round_time_limit_past", 0),
      (else_try),
        (assign, ":rounded_game_first_round_time_limit_past", 1),
      (try_end),
      (try_begin),

      (eq, ":rounded_game_first_round_time_limit_past", 1),

         (get_max_players, ":num_players"),
         (try_for_range, ":player", 0, ":num_players"),

#      (multiplayer_get_my_player, ":player"),
            (player_is_active, ":player"),
           (neg|player_is_busy_with_menus, ":player"),
          (multiplayer_get_my_troop, ":troop_no"),
        (player_get_team_no, ":player_team_no", ":player"),

          (player_get_slot, ":basic_dinero", ":player", slot_agent_dinerotropas),
             (try_begin), #chief capitan
                  (eq, ":basic_dinero", 1),

##           (player_get_gold, ":player_gold", ":player_no"),
         (assign, ":per_round_gold_addition", 1000),

                  (try_begin), #chief capitan
           (eq, ":player_team_no", 0),
         (val_mul, ":per_round_gold_addition", "$g_multiplayer_battle_earnings_multiplier"),
         (val_div, ":per_round_gold_addition", 100),
             (assign, ":player_gold", ":per_round_gold_addition"), 
              (else_try),
           (eq, ":player_team_no", 1),
         (val_mul, ":per_round_gold_addition", "$g_multiplayer_round_earnings_multiplier"),
         (val_div, ":per_round_gold_addition", 100),
             (assign, ":player_gold", ":per_round_gold_addition"), 
                (try_end), #chief capitan acaba
           (player_set_gold, ":player", ":player_gold", multi_max_gold_that_can_be_stored),
                 (player_set_slot, ":player", slot_agent_dinerotropas, 0),
                (try_end), #chief capitan acaba

          (player_get_gold, ":player_gold", ":player"), #chief capitan
       (neq, ":troop_no", "trp_tropa1"),
       (neq, ":troop_no", "trp_tropa2"),
       (neq, ":troop_no", "trp_tropa3"),
       (neq, ":troop_no", "trp_tropa4"),
       (neq, ":troop_no", "trp_tropa5"),
       (neq, ":troop_no", "trp_tropa6"),
       (neq, ":troop_no", "trp_tropa7"),
       (neq, ":troop_no", "trp_tropa8"),
       (neq, ":troop_no", "trp_tropa9"),
       (neq, ":troop_no", "trp_tropa10"),
       (neq, ":troop_no", "trp_tropa11"),
       (neq, ":troop_no", "trp_tropa12"),
       (neq, ":troop_no", "trp_tropa13"),
       (neq, ":troop_no", "trp_tropa14"),
       (neq, ":troop_no", "trp_tropa15"),
       (neq, ":troop_no", "trp_tropa16"),
       (neq, ":troop_no", "trp_tropa17"),
       (neq, ":troop_no", "trp_tropa18"),
       (neq, ":troop_no", "trp_tropa19"),
       (neq, ":troop_no", "trp_tropa20"),
       (neq, ":troop_no", "trp_tropa21"),
       (neq, ":troop_no", "trp_tropa22"),
       (neq, ":troop_no", "trp_tropa23"),
       (neq, ":troop_no", "trp_tropa24"),
       (neq, ":troop_no", "trp_tropa25"),
       (neq, ":troop_no", "trp_tropa26"),
       (neq, ":troop_no", "trp_tropa27"),
       (neq, ":troop_no", "trp_tropa28"),
       (neq, ":troop_no", "trp_tropa29"),
       (neq, ":troop_no", "trp_tropa30"),
       (neq, ":troop_no", "trp_tropa32"),

    (store_add, ":total_req", "$g_multiplayer_num_bots_required_team_1", "$g_multiplayer_num_bots_required_team_2"),
      (store_random_in_range, ":random_req", 0, ":total_req"),
      (val_sub, ":random_req", "$g_multiplayer_num_bots_required_team_1"),

      (try_begin), #EQUIPO 1 EMpieza
        (eq, ":player_team_no", 0),
          (gt, ":player_gold", 250), #chief capitan #si la suma de todos esta por encima de 0, sigue en tigger hasta que se agoten los bots. Podemos poner aqui que para el player sin dinero tampoco continue
        (lt, ":random_req", 0),
    
        (assign, ":selected_team", 0), #EQUIPO 1

      (try_begin),
        (store_mission_timer_a, ":round_time"),
        (val_sub, ":round_time", "$g_round_start_time"),

        (try_begin),
          (le, ":round_time", 20),
          (assign, ":look_only_actives", 0),
        (else_try),
          (assign, ":look_only_actives", 1),
        (try_end),
      (else_try),
        (assign, ":look_only_actives", 1),
      (try_end),

      (call_script, "script_multiplayer_find_bot_troop_and_group_for_spawn", ":selected_team", ":look_only_actives"),
      (assign, ":selected_troop", reg0),
      (assign, ":selected_group", reg1),

      (team_get_faction, ":team_faction", ":selected_team"),
      (assign, ":num_ai_troops", 0),
      (try_for_range, ":cur_ai_troop", multiplayer_ai_troops_begin, multiplayer_ai_troops_end),
        (store_troop_faction, ":ai_troop_faction", ":cur_ai_troop"),
        (eq, ":ai_troop_faction", ":team_faction"),
        (val_add, ":num_ai_troops", 1),
      (try_end),

      (assign, ":number_of_active_players_wanted_bot", 0),


       (assign, ":unidad_cost", 50), #chief capitan
                # (player_set_slot, ":player_no", slot_agent_dinerotropas, ":player_gold"),
        # (player_slot_ge, ":player_no", slot_agent_dinerotropas, 250),

      (try_begin),
        (eq, ":selected_team", 0),
        (assign, ":ai_wanted", 0),
        (store_add, ":end_cond", slot_player_bot_type_1_wanted, ":num_ai_troops"),
        (try_for_range, ":bot_type_wanted_slot", slot_player_bot_type_1_wanted, ":end_cond"),
          (player_slot_ge, ":player", ":bot_type_wanted_slot", 1),
          (assign, ":ai_wanted", 1),
          (assign, ":end_cond", 0), 
        (try_end),

    #  (try_begin),
        (ge, ":ai_wanted", 1),

        (val_add, ":number_of_active_players_wanted_bot", 1),
      (try_end),
      (try_begin),
       (neq, ":number_of_active_players_wanted_bot", 0),

            (store_random_in_range, reg0, 0, 2), #EQUIPO 1
##          (else_try),
##            (store_random_in_range, reg0, 32, 34),
##          (try_end),

        (store_current_scene, ":cur_scene"),
        (modify_visitors_at_site, ":cur_scene"),
        (add_visitors_to_current_scene, reg0, ":selected_troop", 1, ":selected_team", ":selected_group"),
        (assign, "$g_multiplayer_ready_for_spawning_agent", 0),
#        (try_end),

        (troop_get_inventory_slot, ":has_item", ":selected_troop", ek_horse),
        (try_begin),
          (ge, ":has_item", 0),
        #  (assign, ":is_horseman", 1),
       (val_add, ":unidad_cost", 50), #chief capitan
        (else_try),
      (val_add, ":unidad_cost", 1), #chief capitan
        #  (assign, ":is_horseman", 0),
        (try_end),

#chief capitan para tropas de nivel alto
        (store_character_level, ":troop_level", ":selected_troop"),
        (try_begin),
        (gt, ":troop_level", 21),
       (val_add, ":unidad_cost", 50), #chief capitan
        (try_end), #chief capitan
        (try_begin),
        (gt, ":troop_level", 25),
       (val_add, ":unidad_cost", 20), #chief capitan
        (try_end), #chief capitan
        (try_begin),
        (gt, ":troop_level", 26),
       (val_add, ":unidad_cost", 20), #chief capitan
        (try_end), #chief capitan
        (try_begin),
        (gt, ":troop_level", 27),
       (val_add, ":unidad_cost", 30), #chief capitan
        (try_end), #chief capitan
        (try_begin),
        (gt, ":troop_level", 28),
       (val_add, ":unidad_cost", 30), #chief capitan
        (try_end), #chief capitan

        (try_begin), #equipo 1
          (val_sub, "$g_multiplayer_num_bots_required_team_1", 1), #aqui se va restando un bot cada vez que spawn, quizas podemos poner otro limite en el dinero del player
          (val_sub, ":player_gold", ":unidad_cost"), #chief capitan
         (player_set_gold, ":player", ":player_gold", multi_max_gold_that_can_be_stored),
       (try_end),
    (try_end),    

        (else_try), #EQUIPO 2    
        (eq, ":player_team_no", 1),
          (gt, ":player_gold", 250), #chief capitan #si la suma de todos esta por encima de 0, sigue en tigger hasta que se agoten los bots. Podemos poner aqui que para el player sin dinero tampoco continue
        (gt, ":random_req", 0),
        (assign, ":selected_team", 1), #EQUIPO 2

      (try_begin),
        (store_mission_timer_a, ":round_time"),
        (val_sub, ":round_time", "$g_round_start_time"),

        (try_begin),
          (le, ":round_time", 20),
          (assign, ":look_only_actives", 0),
        (else_try),
          (assign, ":look_only_actives", 1),
        (try_end),
      (else_try),
        (assign, ":look_only_actives", 1),
      (try_end),

      (call_script, "script_multiplayer_find_bot_troop_and_group_for_spawn", ":selected_team", ":look_only_actives"),
      (assign, ":selected_troop", reg0),
      (assign, ":selected_group", reg1),

      (team_get_faction, ":team_faction", ":selected_team"),
      (assign, ":num_ai_troops", 0),
      (try_for_range, ":cur_ai_troop", multiplayer_ai_troops_begin, multiplayer_ai_troops_end),
        (store_troop_faction, ":ai_troop_faction", ":cur_ai_troop"),
        (eq, ":ai_troop_faction", ":team_faction"),
        (val_add, ":num_ai_troops", 1),
      (try_end),

      (assign, ":number_of_active_players_wanted_bot", 0),


       (assign, ":unidad_cost", 50), #chief capitan

      (try_begin),
        (eq, ":selected_team", 1), #team2 equipo 2
        (assign, ":ai_wanted", 0),
        (store_add, ":end_cond", slot_player_bot_type_1_wanted, ":num_ai_troops"),
        (try_for_range, ":bot_type_wanted_slot", slot_player_bot_type_1_wanted, ":end_cond"),
          (player_slot_ge, ":player", ":bot_type_wanted_slot", 1),
          (assign, ":ai_wanted", 1),
          (assign, ":end_cond", 0), 
        (try_end),

        (ge, ":ai_wanted", 1),

        (val_add, ":number_of_active_players_wanted_bot", 1),
      (try_end),
      (try_begin),
       (neq, ":number_of_active_players_wanted_bot", 0),

            (store_random_in_range, reg0, 32, 34), #equipo 2

        (store_current_scene, ":cur_scene"),
        (modify_visitors_at_site, ":cur_scene"),
        (add_visitors_to_current_scene, reg0, ":selected_troop", 1, ":selected_team", ":selected_group"),
        (assign, "$g_multiplayer_ready_for_spawning_agent", 0),

        (troop_get_inventory_slot, ":has_item", ":selected_troop", ek_horse),
        (try_begin),
          (ge, ":has_item", 0),
       (val_add, ":unidad_cost", 50), #chief capitan
        (else_try),
      (val_add, ":unidad_cost", 1), #chief capitan
        (try_end),

#chief capitan para tropas de nivel alto
        (store_character_level, ":troop_level", ":selected_troop"),
        (try_begin),
        (gt, ":troop_level", 21),
       (val_add, ":unidad_cost", 50), #chief capitan
        (try_end), #chief capitan
        (try_begin),
        (gt, ":troop_level", 25),
       (val_add, ":unidad_cost", 20), #chief capitan
        (try_end), #chief capitan
        (try_begin),
        (gt, ":troop_level", 26),
       (val_add, ":unidad_cost", 20), #chief capitan
        (try_end), #chief capitan
        (try_begin),
        (gt, ":troop_level", 27),
       (val_add, ":unidad_cost", 30), #chief capitan
        (try_end), #chief capitan
        (try_begin),
        (gt, ":troop_level", 28),
       (val_add, ":unidad_cost", 30), #chief capitan
        (try_end), #chief capitan

        (try_begin), #equipo 2
          (val_sub, "$g_multiplayer_num_bots_required_team_2", 1),
         (val_sub, ":player_gold", ":unidad_cost"), #chief capitan
         (player_set_gold, ":player", ":player_gold", multi_max_gold_that_can_be_stored),      
       (try_end),
    (try_end),    

      (try_end), #chief capitan
      (try_end), #chief capitan
      (try_end), #chief capitan
      (try_end), #chief capitan
    ])




multiplayer_server_manage_bots = (
  3, 0, 0, [],
  [
    (multiplayer_is_server),
    (try_for_agents, ":cur_agent"),
      (agent_is_non_player, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
      (agent_is_alive, ":cur_agent"),
      (agent_get_group, ":agent_group", ":cur_agent"),
      (try_begin),
        (neg|player_is_active, ":agent_group"),
        (call_script, "script_multiplayer_change_leader_of_bot", ":cur_agent"),
      (else_try),
        (player_get_team_no, ":leader_team_no", ":agent_group"),
        (agent_get_team, ":agent_team", ":cur_agent"),
        (neq, ":leader_team_no", ":agent_team"),
        (call_script, "script_multiplayer_change_leader_of_bot", ":cur_agent"),
      (try_end),
    (try_end),
    ])

multiplayer_server_check_polls = (
  1, 5, 0,
  [
    (multiplayer_is_server),
    (eq, "$g_multiplayer_poll_running", 1),
    (eq, "$g_multiplayer_poll_ended", 0),
    (store_mission_timer_a, ":mission_timer"),
    (store_add, ":total_votes", "$g_multiplayer_poll_no_count", "$g_multiplayer_poll_yes_count"),
    (this_or_next|eq, ":total_votes", "$g_multiplayer_poll_num_sent"),
    (gt, ":mission_timer", "$g_multiplayer_poll_end_time"),
    (call_script, "script_cf_multiplayer_evaluate_poll"),
    ],
  [
    (assign, "$g_multiplayer_poll_running", 0),
    (try_begin),
      (this_or_next|eq, "$g_multiplayer_poll_to_show", 0), #change map
      (eq, "$g_multiplayer_poll_to_show", 3), #change map with factions
      (call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
      (start_multiplayer_mission, reg0, "$g_multiplayer_poll_value_to_show", 1),
      (call_script, "script_game_set_multiplayer_mission_end"),
    (try_end),
    ])
    
multiplayer_server_check_end_map = ( 
  1, 0, 0, [],
  [
    (multiplayer_is_server),
    #checking for restarting the map
    (assign, ":end_map", 0),
    (try_begin),
      (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
      (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_lords_battle), #chief capitan
      (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
      (eq, "$g_multiplayer_game_type", multiplayer_game_type_siege),
    
      (try_begin),
        (eq, "$g_round_ended", 1),

        (store_mission_timer_a, ":seconds_past_till_round_ended"),
        (val_sub, ":seconds_past_till_round_ended", "$g_round_finish_time"),
        (store_sub, ":multiplayer_respawn_period_minus_one", "$g_multiplayer_respawn_period", 1),
        (ge, ":seconds_past_till_round_ended", ":multiplayer_respawn_period_minus_one"),
  
        (store_mission_timer_a, ":mission_timer"),    
        (try_begin),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_battle),
          (this_or_next|eq, "$g_multiplayer_game_type", multiplayer_game_type_lords_battle), #chief capitan
          (eq, "$g_multiplayer_game_type", multiplayer_game_type_destroy),
          (assign, ":reduce_amount", 90),
        (else_try),
          (assign, ":reduce_amount", 120),
        (try_end),
    
        (store_mul, ":game_max_seconds", "$g_multiplayer_game_max_minutes", 60),
        (store_sub, ":game_max_seconds_min_n_seconds", ":game_max_seconds", ":reduce_amount"), #when round ends if there are 60 seconds to map change time then change map without completing exact map time.
        (gt, ":mission_timer", ":game_max_seconds_min_n_seconds"),
        (assign, ":end_map", 1),
      (try_end),
      
      (eq, ":end_map", 1),
    (else_try),
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_battle), #battle mod has different end map condition by time
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_lords_battle), #chief capitan
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_destroy), #fight and destroy mod has different end map condition by time
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_siege), #siege mod has different end map condition by time
      (neq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters), #in headquarters mod game cannot limited by time, only can be limited by score.
      (store_mission_timer_a, ":mission_timer"),
      (store_mul, ":game_max_seconds", "$g_multiplayer_game_max_minutes", 60),
      (gt, ":mission_timer", ":game_max_seconds"),
      (assign, ":end_map", 1),
    (else_try),
      #assuming only 2 teams in scene
      (team_get_score, ":team_1_score", 0),
      (team_get_score, ":team_2_score", 1),
      (try_begin),
        (neq, "$g_multiplayer_game_type", multiplayer_game_type_headquarters), #for not-headquarters mods
        (try_begin),
          (this_or_next|ge, ":team_1_score", "$g_multiplayer_game_max_points"),
          (ge, ":team_2_score", "$g_multiplayer_game_max_points"),
          (assign, ":end_map", 1),
        (try_end),
      (else_try),
        (assign, ":at_least_one_player_is_at_game", 0),
        (get_max_players, ":num_players"),
        (try_for_range, ":player_no", 0, ":num_players"),
          (player_is_active, ":player_no"),
          (player_get_agent_id, ":agent_id", ":player_no"),
          (ge, ":agent_id", 0),
          (neg|agent_is_non_player, ":agent_id"),
          (assign, ":at_least_one_player_is_at_game", 1),
          (assign, ":num_players", 0),
        (try_end),
    
        (eq, ":at_least_one_player_is_at_game", 1),

        (this_or_next|le, ":team_1_score", 0), #in headquarters game ends only if one team has 0 score.
        (le, ":team_2_score", 0),
        (assign, ":end_map", 1),
      (try_end),
    (try_end),
    (try_begin),
      (eq, ":end_map", 1),
      (call_script, "script_game_multiplayer_get_game_type_mission_template", "$g_multiplayer_game_type"),
      (start_multiplayer_mission, reg0, "$g_multiplayer_selected_map", 0),
      (call_script, "script_game_set_multiplayer_mission_end"),           
    (try_end),
    ])

multiplayer_once_at_the_first_frame = (
  0, 0, ti_once, [], [
    (start_presentation, "prsnt_multiplayer_welcome_message"),
       (play_sound, "snd_marchingdrums", 1), #multiplayer chief sonido efectua sonido de empiece
    ])

multiplayer_battle_window_opened = (
  ti_battle_window_opened, 0, 0, [], [
    (start_presentation, "prsnt_multiplayer_team_score_display"),
    ])


common_battle_mission_start = (
  ti_before_mission_start, 0, 0, [],
  [
    (team_set_relation, 0, 2, 1),
    (team_set_relation, 1, 3, 1),
    (call_script, "script_change_banners_and_chest"),
    ])

#chief diplomacy cambiado para camara despues de muerto

common_battle_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (try_begin),
      (eq, "$g_battle_won", 1),
      (call_script, "script_count_mission_casualties_from_agents"),
      (finish_mission,0),
#Diplomacy chief begin
   (else_try),
      (eq, "$g_dplmc_battle_continuation", 0),
      (this_or_next|main_hero_fallen),   #CABA EDIT/FIX FOR DEATH CAM
      (eq, "$pin_player_fallen", 1),
      (question_box,"str_do_you_want_to_retreat"),
##      (call_script, "script_simulate_retreat", 5, 20),
##      (str_store_string, s5, "str_retreat"),
##      (call_script, "script_count_mission_casualties_from_agents"),
##      (set_mission_result, -1),
##      (finish_mission,0),
    #diplomacy chief acaba
#TEMPERED CHANGES FOR ENTRENCHMENT 
    (else_try),
        (party_get_slot,":entrenched","p_main_party",slot_party_entrenched),
        (ge,":entrenched",1),
        (display_message,"str_can_not_retreat"),
#TEMPERED CHANGES END
    ##diplomacy begin   
    (else_try),
      (call_script, "script_cf_check_enemies_nearby"),
      (question_box,"str_do_you_want_to_retreat"),
    (else_try),
      (display_message,"str_can_not_retreat"),
    (try_end),
    ])
#chief cambiado acaba

common_battle_init_banner = (
  ti_on_agent_spawn, 0, 0, [],
  [
    (store_trigger_param_1, ":agent_no"),
    (agent_get_troop_id, ":troop_no", ":agent_no"),
    (call_script, "script_force_weapon", ":agent_no"), #anadido para forzar jabalinas chief
    (call_script, "script_troop_agent_set_banner", "tableau_game_troop_label_banner", ":agent_no", ":troop_no"),
####    # Distributed Pheno BEGIN dunde para alturas chief, activar si queremos adiferentes alturas en batalla
    (try_begin),
        (eq, "$sp_alturas", 1),
      (troop_get_type, ":type", ":troop_no"),
    (val_mod, ":type", 2),    #MOTO chief gender fix
     (neq,":type",tf_female),
    (neg|troop_is_hero, ":troop_no"),
    (call_script, "script_troop_random_type", ":troop_no"),
    (try_end),
##    # Distributed Pheno END
    ])


common_arena_fight_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (question_box,"str_give_up_fight"),
    ])

common_custom_battle_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (try_begin),
      (neq, "$g_battle_result", 0),
      (call_script, "script_custom_battle_end"),
      (finish_mission),
    (else_try),
      (question_box,"str_give_up_fight"),
    (try_end),
    ])

custom_battle_check_victory_condition = (
  1, 60, ti_once,
  [
    (store_mission_timer_a,reg(1)),
    (ge,reg(1),10),
    (all_enemies_defeated, 2),
    ##diplomacy chief begin
    (this_or_next|eq, "$g_dplmc_battle_continuation", 0),
    (neg|main_hero_fallen, 0),
    ##diplomacy end
    (set_mission_result,1),
    (display_message,"str_msg_battle_won"),
    (assign, "$g_battle_won",1),
    (assign, "$g_battle_result", 1),
    ],
  [
    (call_script, "script_custom_battle_end"),
    (finish_mission, 1),
    ])

custom_battle_check_defeat_condition = (
  1, 4, 
##diplomacy chief begin  
0,
##diplomacy end
  [
    (main_hero_fallen),
    ##diplomacy chief begin
    (try_begin),
      (eq, "$g_dplmc_battle_continuation", 0),
        (assign, ":num_allies", 0),
        (try_for_agents, ":agent"),
         (agent_is_ally, ":agent"),
         (agent_is_alive, ":agent"),
         (val_add, ":num_allies", 1),
        (try_end),  
        (gt, ":num_allies", 0),  
      (try_begin),
        (eq, "$g_dplmc_cam_activated", 0),
        #(store_mission_timer_a, "$g_dplmc_main_hero_fallen_seconds"),
        (assign, "$g_dplmc_cam_activated", 1),      
      (display_message, "@You have been knocked out by the enemy. Watch your men continue the fight without you or press Tab to retreat."),
        (display_message, "@To watch the fight you can use 'w, a, s, d', and rotate the cam."),
      (try_end),
    (else_try),
    ##diplomacy end
    (assign,"$g_battle_result",-1),
    ##diplomacy chief begin
    (try_end),
    ##diplomacy end
    ],
  [
    (call_script, "script_custom_battle_end"),
    (finish_mission),
    ])

common_battle_victory_display = (
  10, 0, 0, [],
  [
    (eq,"$g_battle_won",1),
    (display_message,"str_msg_battle_won"),
    ])

common_siege_question_answered = (
  ti_question_answered, 0, 0, [],
   [
     (store_trigger_param_1,":answer"),
     (eq,":answer",0),
     (assign, "$pin_player_fallen", 0),
     (get_player_agent_no, ":player_agent"),
     (agent_get_team, ":agent_team", ":player_agent"),
     (try_begin),
       (neq, "$attacker_team", ":agent_team"),
       (neq, "$attacker_team_2", ":agent_team"),
       (str_store_string, s5, "str_siege_continues"),
       (call_script, "script_simulate_retreat", 8, 15, 0),
     (else_try),
       (str_store_string, s5, "str_retreat"),
       (call_script, "script_simulate_retreat", 5, 20, 0),
     (try_end),
     (call_script, "script_count_mission_casualties_from_agents"),
     (finish_mission,0),
     ])

common_custom_battle_question_answered = (
   ti_question_answered, 0, 0, [],
   [
     (store_trigger_param_1,":answer"),
     (eq,":answer",0),
     (assign, "$g_battle_result", -1),
     (call_script, "script_custom_battle_end"),
     (finish_mission),
     ])

common_custom_siege_init = (
  0, 0, ti_once, [],
  [
    (assign, "$g_battle_result", 0),
    (call_script, "script_music_set_situation_with_culture", mtf_sit_siege),
    ])

common_siege_init = (
  0, 0, ti_once, [],
  [
    (assign,"$g_battle_won",0),
    (assign,"$defender_reinforcement_stage",0),
    (assign,"$attacker_reinforcement_stage",0),
    (call_script, "script_music_set_situation_with_culture", mtf_sit_siege),
    ])

common_music_situation_update = (
  30, 0, 0, [],
  [
    (call_script, "script_combat_music_set_situation_with_culture"),
    ])

common_siege_ai_trigger_init = (
  0, 0, ti_once,
  [
    (assign, "$defender_team", 0),
    (assign, "$attacker_team", 1),
    (assign, "$defender_team_2", 2),
    (assign, "$attacker_team_2", 3),
    ], [])

common_siege_ai_trigger_init_2 = (
  0, 0, ti_once,
  [
    (set_show_messages, 1),#gdw was 0
    (entry_point_get_position, pos10, 10),
    (try_for_range, ":cur_group", 0, grc_everyone),
      (neq, ":cur_group", grc_archers),
      (team_give_order, "$defender_team", ":cur_group", mordr_hold),
      (team_give_order, "$defender_team", ":cur_group", mordr_stand_closer),
      (team_give_order, "$defender_team", ":cur_group", mordr_stand_closer),
      (team_give_order, "$defender_team_2", ":cur_group", mordr_hold),
      (team_give_order, "$defender_team_2", ":cur_group", mordr_stand_closer),
      (team_give_order, "$defender_team_2", ":cur_group", mordr_stand_closer),
    (try_end),
    (team_give_order, "$defender_team", grc_archers, mordr_stand_ground),
    (team_set_order_position, "$defender_team", grc_everyone, pos10),
    (team_give_order, "$defender_team_2", grc_archers, mordr_stand_ground),
    (team_set_order_position, "$defender_team_2", grc_everyone, pos10),
    #(set_show_messages, 1),
    ], [])

common_siege_ai_trigger_init_after_2_secs = (
  0, 2, ti_once, [],
  [
    (try_for_agents, ":agent_no"),
      (agent_set_slot, ":agent_no", slot_agent_is_not_reinforcement, 1),
    (try_end),
    ])

## CC custom commander chief cambia entero
common_siege_defender_reinforcement_check = (
  3, 0, 0, [],
  ## CC
  [
    (store_mission_timer_a,":mission_time"),
    (ge,":mission_time",10),
    (try_begin),
      (store_mul, ":attacker_reinf_stage_mul_2", "$attacker_reinforcement_stage", 2),
      (this_or_next|lt, "$defender_reinforcement_stage", 14),
      (le, "$defender_reinforcement_stage", ":attacker_reinf_stage_mul_2"),
      (store_normalized_team_count, ":num_defenders_normalized", 0),
      (lt, ":num_defenders_normalized", 13),#gdw
      (add_reinforcements_to_entry,4, 7),
      (val_add,"$defender_reinforcement_stage",1),
    (try_end),
    ## CC
    (try_begin),
      (ge, "$defender_reinforcement_stage", 3), ## CC
      (set_show_messages, 0),
      (team_give_order, "$defender_team", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
      (team_give_order, "$defender_team_2", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
      (set_show_messages, 1),
      (ge, "$defender_reinforcement_stage", 6), ## CC
      (set_show_messages, 0),
      (team_give_order, "$defender_team", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
      (team_give_order, "$defender_team_2", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
      (set_show_messages, 1),
    (try_end),
   ])
## CC chief acaba
#viejo chief sustituitdo por arriba
##common_siege_defender_reinforcement_check = (
##  3, 0, 5, [],
##  [(lt, "$defender_reinforcement_stage", 7),
##   (store_mission_timer_a,":mission_time"),
##   (ge,":mission_time",10),
##   (store_normalized_team_count,":num_defenders",0),
##   (lt,":num_defenders",8),
##   (add_reinforcements_to_entry,4, 7),
##   (val_add,"$defender_reinforcement_stage",1),
##   (try_begin),
##     (gt, ":mission_time", 300), #5 minutes, don't let small armies charge
##     (get_player_agent_no, ":player_agent"),
##     (agent_get_team, ":player_team", ":player_agent"),
##     (neq, ":player_team", "$defender_team"), #player should be the attacker
##     (neq, ":player_team", "$defender_team_2"), #player should be the attacker
##     (ge, "$defender_reinforcement_stage", 2),
##     (set_show_messages, 0),
##     (team_give_order, "$defender_team", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
##     (team_give_order, "$defender_team_2", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
##     (team_give_order, "$defender_team", grc_cavalry, mordr_charge), #AI desperate charge:cavalry!!!
##     (team_give_order, "$defender_team_2", grc_cavalry, mordr_charge), #AI desperate charge:cavalry!!!
##     (set_show_messages, 1),
##     (ge, "$defender_reinforcement_stage", 4),
##     (set_show_messages, 0),
##     (team_give_order, "$defender_team", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
##     (team_give_order, "$defender_team_2", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
##     (set_show_messages, 1),
##   (try_end),
##   ])

common_siege_defender_reinforcement_archer_reposition = (
  2, 0, 0,
  [
    (gt, "$defender_reinforcement_stage", 0),
    ],
  [
    (call_script, "script_siege_move_archers_to_archer_positions"),
    ])

#Xenoargh BandS changes
common_siege_defender_infantry_patrol = (
  60, 0, 0,
  [
    (gt, "$defender_reinforcement_stage", 0),
    ],
  [
  #This script cycles infantry / cavalry between positions, so that they can not just stand and get slaughtered by missile fire at the ladder.
  #It would be better to have a true point-to-point patrol route, but that would involve complex scripts that would tend to work less well than letting them defend their positions once they arrive, so it uses simple orders instead, but splits between cavalry and infantry and the defending 'teams'.
  #pos1 / entry-point 10 is usually the spawn point, center of the courtyard, etc.
  #pos3 / entry-point 11 and 15 are the two 'ladder points'.
  #In general, Blood and Steel cycles through these points, and in general, these points have been moved away from the ladder / belfry, to prevent pointless slaughter of AI troops.
  #However, most infantry now have at least thrown weapons as "backups", and there's the obvious problems with the Khergits, where their "cavalry" are actually archers, for all intents and purposes, but the engine doesn't make this distinction, since there is no "mounted archer" class... so they're put on Stand Ground, which seems to trigger shooting behaviors and the ability to re-position, instead of just standing around.
  #Lastly, I am sure somebody reading this will ask, 'Why not just copy the archer order script for infantry?'
  #The answer's simple: Stand Ground with archers works, because no distance in a typical siege is out of archer range.  With infantry, you are asking for Bad Things to happen, because they aren't "smart" enough to "know" when to charge, other than the limit placed in the AI.  It's annoying, and I'd like to give orders to specific Agents to fix this problem more easily... but it's how the engine works.
  
  #(display_message, "@Running Patrol Positions Script"),
  (store_random_in_range, ":random_no", 1,3),
          (entry_point_get_position, pos1, 10),
        (entry_point_get_position, pos2, 11),
        (entry_point_get_position, pos3, 15),
    (try_begin),
        (eq, ":random_no", 1),

        # (team_set_order_position, "$defender_team", grc_infantry, pos1),
        # (team_set_order_position, "$defender_team_2", grc_infantry, pos2),
          # (team_give_order, "$defender_team", grc_infantry, mordr_stand_ground),
        # (team_give_order, "$defender_team_2", grc_infantry, mordr_stand_ground),
        
        # (team_set_order_position, "$defender_team", grc_infantry, pos2),
        # (team_set_order_position, "$defender_team_2", grc_infantry, pos3),
        # (team_give_order, "$defender_team", grc_cavalry, mordr_stand_ground),
        # (team_give_order, "$defender_team_2", grc_cavalry, mordr_stand_ground),
    (try_end),
    (try_begin),
        (eq, ":random_no", 2),

        # (team_set_order_position, "$defender_team", grc_infantry, pos2),
        # (team_set_order_position, "$defender_team_2", grc_infantry, pos3),
          # (team_give_order, "$defender_team", grc_infantry, mordr_stand_ground),
        # (team_give_order, "$defender_team_2", grc_infantry, mordr_stand_ground),
        
        # (team_set_order_position, "$defender_team", grc_infantry, pos3),
        # (team_set_order_position, "$defender_team_2", grc_infantry, pos1),
        # (team_give_order, "$defender_team", grc_cavalry, mordr_stand_ground),
        # (team_give_order, "$defender_team_2", grc_cavalry, mordr_stand_ground),
    (try_end),
        (try_begin),
        (eq, ":random_no", 1),

        # (team_set_order_position, "$defender_team", grc_infantry, pos3),
        # (team_set_order_position, "$defender_team_2", grc_infantry, pos1),
          # (team_give_order, "$defender_team", grc_infantry, mordr_stand_ground),
        # (team_give_order, "$defender_team_2", grc_infantry, mordr_hold),
        
        # (team_set_order_position, "$defender_team", grc_infantry, pos1),
        # (team_set_order_position, "$defender_team_2", grc_infantry, pos2),
        # (team_give_order, "$defender_team", grc_cavalry, mordr_hold),
        # (team_give_order, "$defender_team_2", grc_cavalry, mordr_stand_ground),
    (try_end),    
    ])

####Xenoargh BandS acaba

## CC cambia entero chief
common_siege_attacker_reinforcement_check = (
  3, 0, 0,
  [
    (assign, ":continue", 1),
    (try_begin),
      (ge,"$attacker_reinforcement_stage",10),
      (store_mul, ":defender_reinf_stage_mul_2", "$defender_reinforcement_stage", 2),
      (gt, "$attacker_reinforcement_stage", ":defender_reinf_stage_mul_2"),
      (assign, ":continue", 0),
    (try_end),
    (eq, ":continue", 1),
    (store_mission_timer_a,":mission_time"),
    (ge,":mission_time",10),
    (store_normalized_team_count,":num_attackers",1),
    (lt,":num_attackers",10),#gdw6
    ],
  [
    (add_reinforcements_to_entry, 1, 8),
    (val_add,"$attacker_reinforcement_stage", 1),
    ])
## CC chief termina

# chief CC pone off por arriba
##common_siege_attacker_reinforcement_check = (
##  1, 0, 5,
##  [
##    (lt,"$attacker_reinforcement_stage",5),
##    (store_mission_timer_a,":mission_time"),
##    (ge,":mission_time",10),
##    (store_normalized_team_count,":num_attackers",1),
##    (lt,":num_attackers",6)
##    ],
##  [
##    (add_reinforcements_to_entry, 1, 8),
##    (val_add,"$attacker_reinforcement_stage", 1),
##    ])

common_siege_attacker_do_not_stall = (
  5, 0, 0, [],
  [ #Make sure attackers do not stall on the ladders...
    (try_for_agents, ":agent_no"),
      (agent_is_human, ":agent_no"),
      (agent_is_alive, ":agent_no"),
      (agent_get_team, ":agent_team", ":agent_no"),
      (this_or_next|eq, ":agent_team", "$attacker_team"),
      (eq, ":agent_team", "$attacker_team_2"),
      (agent_ai_set_always_attack_in_melee, ":agent_no", 1),
    (try_end),
    ])

common_battle_check_friendly_kills = (
  2, 0, 0, [],
  [
    (call_script, "script_check_friendly_kills"),
    ])

common_battle_check_victory_condition = (
  1, 60, ti_once,
  [
    (store_mission_timer_a,reg(1)),
    (ge,reg(1),10),
    (all_enemies_defeated, 5),
    ##diplomacy chief begin
    (this_or_next|eq, "$g_dplmc_battle_continuation", 0),
    (neg|main_hero_fallen),
    ##diplomacy end
    (set_mission_result,1),
    (display_message,"str_msg_battle_won"),
    (assign,"$g_battle_won",1),
    (assign, "$g_battle_result", 1),
    (call_script, "script_play_victorious_sound"),
    ],
  [
    (call_script, "script_count_mission_casualties_from_agents"),
    (finish_mission, 1),
    ])

common_battle_victory_display = (
  10, 0, 0, [],
  [
    (eq,"$g_battle_won",1),
    (display_message,"str_msg_battle_won"),
    ])

common_siege_refill_ammo = (
  120, 0, 0, [],
  [#refill ammo of defenders every two minutes.
    (get_player_agent_no, ":player_agent"),
    (try_for_agents,":cur_agent"),
      (neq, ":cur_agent", ":player_agent"),
      (agent_is_alive, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
##      (agent_is_defender, ":cur_agent"),
    #Tempered added for siege camps chief
      (try_begin),
        (party_slot_eq,"p_main_party",slot_party_siege_camp,1),
        (agent_refill_ammo, ":cur_agent"),
      (else_try),
        (agent_get_team, ":agent_team", ":cur_agent"),
        (this_or_next|eq, ":agent_team", "$defender_team"),
        (eq, ":agent_team", "$defender_team_2"),
        (agent_refill_ammo, ":cur_agent"),
      (try_end),
#Tempered changes end

      (agent_get_team, ":agent_team", ":cur_agent"),
      (this_or_next|eq, ":agent_team", "$defender_team"),
      (eq, ":agent_team", "$defender_team_2"),
      (agent_refill_ammo, ":cur_agent"),
    (try_end),
    ])

common_siege_check_defeat_condition = (
  1, 4, 
##diplomacy chief begin
0,
##diplomacy end
  [
    (main_hero_fallen)
    ],
  [
    ##diplomacy chief begin
    (try_begin),
      (eq, "$g_dplmc_battle_continuation", 0),
      (assign, ":num_allies", 0),
      (try_for_agents, ":agent"),
       (agent_is_ally, ":agent"),
       (agent_is_alive, ":agent"),
       (val_add, ":num_allies", 1),
      (try_end),  
      (gt, ":num_allies", 0),        
     (try_begin),
        (eq, "$g_dplmc_cam_activated", 0),
        #(store_mission_timer_a, "$g_dplmc_main_hero_fallen_seconds"),
        (assign, "$g_dplmc_cam_activated", 1),      
      (display_message, "@You have been knocked out by the enemy. Watch your men continue the fight without you or press Tab to retreat."),
        (display_message, "@To watch the fight you can use 'w, a, s, d', and rotate the cam."),
      (try_end),
    (else_try),
    ##diplomacy end
    (get_player_agent_no, ":player_agent"),
    (agent_get_team, ":agent_team", ":player_agent"),
    (try_begin),
      (neq, "$attacker_team", ":agent_team"),
      (neq, "$attacker_team_2", ":agent_team"),
      (str_store_string, s5, "str_siege_continues"),
      (call_script, "script_simulate_retreat", 8, 15, 0),
    (else_try),
      (str_store_string, s5, "str_retreat"),
      (call_script, "script_simulate_retreat", 5, 20, 0),
    (try_end),
    (assign, "$g_battle_result", -1),
    (set_mission_result,-1),
    (call_script, "script_count_mission_casualties_from_agents"),
    (finish_mission,0),
    ##diplomacy chief begin
    (try_end),
    ##diplomacy end
    ])

common_battle_order_panel = (
  0, 0, 0, [],
  [
    (game_key_clicked, gk_view_orders),
    ##diplomacy chief begin
    (neg|main_hero_fallen),
    ##diplomacy end
    (neg|is_presentation_active, "prsnt_battle"),
    (start_presentation, "prsnt_battle"),
    ])

common_battle_order_panel_tick = (
  0.1, 0, 0, [],
  [
    (is_presentation_active, "prsnt_battle"),
    (call_script, "script_update_order_panel_statistics_and_map"),
    ])

common_battle_inventory = (
  ti_inventory_key_pressed, 0, 0, [],
  [
    (display_message,"str_use_baggage_for_inventory"),
    ])

common_inventory_not_available = (
  ti_inventory_key_pressed, 0, 0,
  [
    (display_message, "str_cant_use_inventory_now"),
    ], [])

common_siege_init_ai_and_belfry = (
  0, 0, ti_once,
  [
    (call_script, "script_siege_init_ai_and_belfry"),
    ], [])

common_siege_move_belfry = (
  0, 0, ti_once,
  [
    (call_script, "script_cf_siege_move_belfry"),
    ], [])

common_siege_rotate_belfry = (
  0, 2, ti_once,
  [
    (call_script, "script_cf_siege_rotate_belfry_platform"),
    ],
  [
    (assign, "$belfry_positioned", 3),
    ])

common_siege_assign_men_to_belfry = (
  0, 0, ti_once,
  [
    (call_script, "script_cf_siege_assign_men_to_belfry"),
    ], [])

#########siege warfare ram chief cdvader
common_siege_init_ai_and_ram = (
  0, 0, ti_once,
  [
    (call_script, "script_siege_init_ai_and_ram"),
    ], [])

common_siege_move_ram = (
  0, 0, ti_once,
  [
    (call_script, "script_cf_siege_move_ram"),
    ], [])

##common_siege_rotate_ram = (
##  0, 2, ti_once,
##  [
##    (call_script, "script_cf_siege_rotate_ram_platform"),
##    ],
##  [
##    (assign, "$ram_positioned", 3),
##    ])


common_siege_assign_men_to_ram = (
  0, 0, ti_once,
  [
    (call_script, "script_cf_siege_assign_men_to_ram"),
    ], [])
    
#~ This requires you to have "Towngate Rectangle Door Right and Left" as doors. ~#
#~ If you want to make new doors, etc, then change the scene_prop_get_instance part
# to your mods doors OR create a new common_ram_move_ram_shaft_2 for example,
# and copy all the stuff and rename the :door_objects. 
# You probably also need to adjust the timers and stuff. ~#
common_ram_move_ram_shaft = (
    1, 0, 0, # Needs to be 1 second check interval for the $ram_timer.
        [(eq, "$ram_positioned", 1)], # Begins checking when the ram is positioned near the gate.
        [(scene_prop_get_instance, ":ram_object", "spr_ram_shaft", 0),
         (scene_prop_get_instance, ":door_1_object", "spr_towngate_rectangle_door_right", 0),
         (scene_prop_get_instance, ":door_2_object", "spr_towngate_rectangle_door_left", 0),
         (prop_instance_get_position, pos1, ":ram_object"),
         (prop_instance_get_position, pos2, ":door_1_object"),
         (prop_instance_get_position, pos3, ":door_2_object"),
         (val_add, "$ram_timer", 1), # Add 1 to $ram_timer each time it checks the timer.
         
         #Shaft backwards:
         (try_begin),
            (eq, "$ram_timer", 1),
            (position_move_y, pos1, -150),
            (prop_instance_animate_to_position, ":ram_object", pos1, 600), #6 seconds.
         (else_try),
            (eq, "$ram_timer", 13),
            (position_move_y, pos1, -350),
            (prop_instance_animate_to_position, ":ram_object", pos1, 600), #6 seconds.
         (else_try),
            (eq, "$ram_timer", 24),
            (position_move_y, pos1, -550),
            (prop_instance_animate_to_position, ":ram_object", pos1, 600), #6 seconds.
         (else_try),
            (eq, "$ram_timer", 35),
            (position_move_y, pos1, -450),
            (prop_instance_animate_to_position, ":ram_object", pos1, 600), #6 seconds.
            (assign, "$ram_positioned", 3),
         (try_end),
         
         #Shaft forwards:
         (try_begin),
            (eq, "$ram_timer", 9),
            (position_move_y, pos1, 450),
            (prop_instance_animate_to_position, ":ram_object", pos1, 200), #2 seconds.
         (else_try),
            (eq, "$ram_timer", 20),
            (position_move_y, pos1, 450),
            (prop_instance_animate_to_position, ":ram_object", pos1, 200), #2 seconds.
         (else_try),
            (eq, "$ram_timer", 31),
            (position_move_y, pos1, 550),
            (prop_instance_animate_to_position, ":ram_object", pos1, 200), #2 seconds.
         (try_end),
         
         #Doors:
         (try_begin),
            (eq, "$ram_timer", 11),
            (position_rotate_z, pos2, -10),
            (prop_instance_animate_to_position, ":door_1_object", pos2, 50), #0.5 seconds.
            (particle_system_burst, "psys_dummy_smoke", pos2, 100),
            (position_rotate_z, pos3, 10),
            (prop_instance_animate_to_position, ":door_2_object", pos3, 50), #0.5 seconds.
            (particle_system_burst, "psys_gourd_smoke", pos3, 50),
            (play_sound, "snd_dummy_hit"),
         (else_try),
            (eq, "$ram_timer", 22),
            (position_rotate_z, pos2, -10),
            (prop_instance_animate_to_position, ":door_1_object", pos2, 50), #0.5 seconds.
            (particle_system_burst, "psys_dummy_smoke", pos2, 100),
            (position_rotate_z, pos3, 10),
            (prop_instance_animate_to_position, ":door_2_object", pos3, 50), #0.5 seconds.
            (particle_system_burst, "psys_gourd_smoke", pos3, 50),
            (play_sound, "snd_dummy_hit"),
         (else_try),
            (eq, "$ram_timer", 33),
            (position_rotate_z, pos2, -100), #Move right.
            (prop_instance_animate_to_position, ":door_1_object", pos2, 100), #1 second.
            (particle_system_burst, "psys_dummy_smoke", pos2, 500),
            (position_rotate_z, pos3, 100), #Move left.
            (prop_instance_animate_to_position, ":door_2_object", pos3, 100), #1 second.
            (particle_system_burst, "psys_gourd_smoke", pos3, 250),
            (play_sound, "snd_dummy_hit"),
         (try_end),
        ])
####siege warfare chief acaba
#1 fire arrow chief empieza siege warfare
fire_arrow_initialize = (0, 0, ti_once, [],[
        (set_fixed_point_multiplier, 100),
        (get_scene_boundaries, pos20, pos21),
        (position_get_x, "$g_min_x", pos20),
        (position_get_y, "$g_min_y", pos20),
        (position_get_x, "$g_max_x", pos21),
        (position_get_y, "$g_max_y", pos21),
        (assign, "$g_min_z", 5),
        (assign, "$g_max_z", 6000),
        (val_add, "$g_min_x", 6),
        (val_add, "$g_min_x", 6),
        (val_sub, "$g_max_x", 6),
        (val_sub, "$g_max_y", 6),
        #(assign, reg1, "$g_min_x"),
        #(assign, reg2, "$g_max_x"),
        #(assign, reg3, "$g_min_y"),
        #(assign, reg4, "$g_max_y"),
        #(assign, reg5, "$g_min_z"),
        #(assign, reg6, "$g_max_z"),
        #(display_message, "@DEBUG: x({reg1}-{reg2}) y({reg3}-{reg4}) z({reg5}-{reg6})"),
])

fire_arrow_routine = (0.01, 0, 0,
  [ ],#(troop_slot_ge, "trp_global_value", slot_gloval_max_fire_arrow, 1),
  [
    (call_script, "script_fire_arrow_routine"),
  ])
  
toggle_fire_arrow_mode = (0, 0, 0, [],
  [
    (troop_get_slot, ":key", "trp_global_value", slot_gloval_fire_arrow_key), 
    (key_clicked, ":key"), ###tecla T chief
    (call_script,"script_toggle_fire_arrow_mode"),
  ])
  
fire_element_life = (3, 0, 0,
  [],#(troop_slot_ge, "trp_global_value", slot_gloval_max_flame_slot, 1),
  [(call_script, "script_flame_routine")])
  
destructible_object_initialize  = (
  ti_before_mission_start, 0, 0, [],[
      (call_script,"script_initialize_agents_use_fire_arrow"),
      (call_script, "script_destructible_object_initialize")])
###fire arrow acaba


#TEMPERED chief DROWNING TRIGGER ASSUMES A WATER LEVEL OF -0.5, TOGGLE IN CAMP ACTIONS MENU TO DISABLE/ENABLE        
common_drowning = (
        6,0,0,[(eq,"$drowning",1)],
        [    (set_fixed_point_multiplier, 10),
            (try_for_agents,":cur_agent"),
                (agent_is_alive,":cur_agent"),
                (agent_is_human,":cur_agent"),
                (agent_get_position,pos3,":cur_agent"),
                (position_get_z,":cur_z_position",pos3),
                (agent_get_horse,":horse",":cur_agent"),
                (try_begin),#unmounted agent
                    (le,":cur_z_position",-19),
                    (eq,":horse",-1),
                    (store_agent_hit_points,":cur_agent_hp",":cur_agent",1),
                    (store_sub,":damage",":cur_agent_hp",10),
                    (agent_set_hit_points,":cur_agent",":damage",1),
                    (try_begin),
                        (le,":damage",0),

                        (set_show_messages, 0),    #MOTO prevent "agent killed self" messages

                        (agent_deliver_damage_to_agent,":cur_agent",":cur_agent"),

                        (set_show_messages, 1),
                    (try_end),

                (else_try), #mounted agent
                    (neq,":horse",-1),
                    (le,":cur_z_position",-32),
                    (store_agent_hit_points,":cur_agent_hp",":cur_agent",1),
                    (store_sub,":damage",":cur_agent_hp",10),
                    (agent_set_hit_points,":cur_agent",":damage",1),
                    (try_begin),
                        (le,":damage",0),

                        (set_show_messages, 0),    #MOTO prevent "agent killed self" messages

                        (agent_deliver_damage_to_agent,":cur_agent",":cur_agent"),

                        (set_show_messages, 1),
                    (try_end),

                (try_end),
            (try_end),
        ])
#TEMPERED   CAMP OVER RUN, SUPPLY LOSS
common_camp_supply = ( 5,0,0,[(ge,"$camp_supply",1)],
                        [
                            (set_fixed_point_multiplier, 100),
                            (scene_prop_get_instance,":inventory_tent", "spr_bell_tent_inventory",0),
                            (prop_instance_get_position,pos1,":inventory_tent"),
                            (scene_prop_get_instance,":replacement_tent", "spr_bell_tent_noinventory",0),
                            (prop_instance_get_position,pos4,":replacement_tent"),
                            (assign,":in_range",0),
                            (try_for_agents,":cur_agent"),                            
                                (agent_is_alive,":cur_agent"),
                                (agent_is_human,":cur_agent"),
                                (agent_get_team, ":agent_team", ":cur_agent"),
                                (try_begin),
                                    (this_or_next|eq, ":agent_team", "$attacker_team"),
                                    (eq, ":agent_team", "$attacker_team_2"),                                
                                    (agent_get_position,pos2,":cur_agent"),
                                    (get_distance_between_positions, ":cur_distance", pos1, pos2),
                                    (le,":cur_distance",800),                                    
                                    (val_add,":in_range",1),
                                (try_end),
                            (try_end),
                            (try_begin),
                                (ge,":in_range",3),
                                (val_sub,"$camp_supply",1),                                
                                (prop_instance_animate_to_position,":replacement_tent",pos1,0),
                                (prop_instance_animate_to_position,":inventory_tent",pos4,0),
                                (scene_prop_get_instance,":supply_cart", "spr_cart",0),
                                (prop_instance_get_position,pos3,":supply_cart"),
                                (particle_system_burst, "psys_village_fire_big", pos3,400),
                                (particle_system_burst, "psys_village_fire_smoke_big", pos3, 9999),
                                (call_script,"script_loot_camp"),
                            (try_end),                            
                        ]
                     )

#TEMPERED  wilderness duel cheer
common_duel_cheer_winner = ( 1,0,3,[    (this_or_next|main_hero_fallen),
                                            (num_active_teams_le,3),],
                                
                        [    (try_for_agents,":cur_agent"),                        
                                (agent_is_alive,":cur_agent"),
                                (agent_is_human,":cur_agent"),
                                (agent_get_team, ":agent_team", ":cur_agent"),
                                (try_begin),
                                    (eq,":agent_team", 1),
                                    (main_hero_fallen),                                    
                                    (agent_set_animation, ":cur_agent", "anim_cheer"),
                                    (play_sound, "snd_man_yell"),
                                (else_try),
                                    (eq,":agent_team",3),
                                    (neg|main_hero_fallen, 1),
                                    (agent_set_animation, ":cur_agent", "anim_cheer"),
                                    (play_sound, "snd_man_victory"),
                                (try_end),
                            (try_end),
                        ]
                     )
      
#tempered chief acaba
###############################################
#dunde torneo chief
#reduce dano causado por player y aumenta el recibido por player en torneos para hacerlos mas dificiles
torneo_aumenta_dano = (
    ti_on_agent_hit, 0, 0, [(eq, "$g_mt_mode", abm_tournament),(eq, "$g_avdificultad", 1),],
   [(store_trigger_param_1, ":victim_id"),
    (store_trigger_param_2, ":attacker_id"),   
    (store_trigger_param_3, ":damage"),
    (agent_is_human, ":victim_id"),
    (agent_is_human, ":attacker_id"),
    (get_player_agent_no, ":player_agent"),  # it's for single player, is'nt it?
    (try_begin),
       (eq, ":victim_id", ":player_agent"),
       (store_mul, ":new_damage", ":damage", 2),
        (set_trigger_result,  ":new_damage"),   
    (else_try),
       (eq, ":attacker_id", ":player_agent"),
       (store_div, ":new_damage", ":damage", 2),
        (set_trigger_result,  ":new_damage"),     
    (else_try),
       (set_trigger_result, -1),   
    (try_end),
    ])
  #dunde torneo acaba

###############################################    

tournament_triggers = [
  (ti_before_mission_start, 0, 0, [], [(call_script, "script_change_banners_and_chest"),
                                       (assign, "$g_arena_training_num_agents_spawned", 0)]),

  (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_arena")], []),
#chief anadido Commander
sp_shield_bash_1,
sp_shield_bash_2,
sp_shield_bash_3,
    common_weapon_use_spawn,
    common_weapon_use,
      rain,
    custom_commander_init_hero_begin_xp,
    custom_commander_give_hero_extra_xp,
    custom_commander_horse_speed,
    custom_commander_critical_strike,
     monitor_health,
     bleed,
  #  common_rigale_legshot,
    common_andar_cae,
torneo_aumenta_dano, #dunde torneo chief
sistema_fatiga,
suma_fatigue,
resta_fatigue_porcorrer,
resta_fatigue,
  #chief acaba
  (ti_tab_pressed, 0, 0, [],
   [(try_begin),
      (eq, "$g_mt_mode", abm_visit),
      (set_trigger_result, 1),
     (else_try),
     (question_box,"str_give_up_fight"),
     (try_end),
    ]),
  (ti_question_answered, 0, 0, [],
   [(store_trigger_param_1,":answer"),
    (eq,":answer",0),
    (try_begin),
     (eq, "$g_mt_mode", abm_tournament),
      (call_script, "script_end_tournament_fight", 0),
    (else_try),
      (eq, "$g_mt_mode", abm_training),
      (get_player_agent_no, ":player_agent"),
      (agent_get_kill_count, "$g_arena_training_kills", ":player_agent", 1),#use this for conversation
    (try_end),
    (finish_mission,0),
    ]),

  (1, 0, ti_once, [], [
      (eq, "$g_mt_mode", abm_visit),
      (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
      (store_current_scene, reg(1)),
      (scene_set_slot, reg(1), slot_scene_visited, 1),
      (mission_enable_talk),
      (get_player_agent_no, ":player_agent"),
      (assign, ":team_set", 0),
      (try_for_agents, ":agent_no"),
        (neq, ":agent_no", ":player_agent"),
        (agent_get_troop_id, ":troop_id", ":agent_no"),
        (is_between, ":troop_id", regular_troops_begin, regular_troops_end),
        (eq, ":team_set", 0),
        (agent_set_team, ":agent_no", 1),
        (assign, ":team_set", 1),
      (try_end),
    ]),
  
  (0, 0, ti_once, [],
   [
     (eq, "$g_mt_mode", abm_tournament),
     (play_sound, "snd_arena_ambiance", sf_looping),
     (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
     ]),

  (1, 4, ti_once, [(eq, "$g_mt_mode", abm_tournament),
                   (this_or_next|main_hero_fallen),
                   (num_active_teams_le, 1)],
   [
       (try_begin),
         (neg|main_hero_fallen),
         (call_script, "script_end_tournament_fight", 1),
         (call_script, "script_play_victorious_sound"),
         (finish_mission),
       (else_try),
         (call_script, "script_end_tournament_fight", 0),
         (finish_mission),
       (try_end),
       ]),
  
  (ti_battle_window_opened, 0, 0, [], [(eq, "$g_mt_mode", abm_training),(start_presentation, "prsnt_arena_training")]),
  
  (0, 0, ti_once, [], [(eq, "$g_mt_mode", abm_training),
                       (assign, "$g_arena_training_max_opponents", 40),
                       (assign, "$g_arena_training_num_agents_spawned", 0),
                       (assign, "$g_arena_training_kills", 0),
                       (assign, "$g_arena_training_won", 0),
                       (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
                       ]),

  (1, 4, ti_once, [(eq, "$g_mt_mode", abm_training),
                   (store_mission_timer_a, ":cur_time"),
                   (gt, ":cur_time", 3),
                   (assign, ":win_cond", 0),
                   (try_begin),
                     (ge, "$g_arena_training_num_agents_spawned", "$g_arena_training_max_opponents"),#spawn at most 40 agents
                     (num_active_teams_le, 1),
                     (assign, ":win_cond", 1),
                   (try_end),
                   (this_or_next|eq, ":win_cond", 1),
                   (main_hero_fallen)],
   [
       (get_player_agent_no, ":player_agent"),
       (agent_get_kill_count, "$g_arena_training_kills", ":player_agent", 1),#use this for conversation
       (assign, "$g_arena_training_won", 0),
       (try_begin),
         (neg|main_hero_fallen),
         (assign, "$g_arena_training_won", 1),#use this for conversation
       (try_end),
       (assign, "$g_mt_mode", abm_visit),
       (set_jump_mission, "mt_arena_melee_fight"),
       (party_get_slot, ":arena_scene", "$current_town", slot_town_arena),
       (modify_visitors_at_site, ":arena_scene"),
       (reset_visitors),
       (set_visitor, 35, "trp_veteran_fighter"),
       (set_visitor, 36, "trp_merc_infantryt5"),
       (set_jump_entry, 50),
       (jump_to_scene, ":arena_scene"),
       ]),


  (0.2, 0, 0,
   [
       (eq, "$g_mt_mode", abm_training),
       (assign, ":num_active_fighters", 0),
       (try_for_agents, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_is_alive, ":agent_no"),
         (agent_get_team, ":team_no", ":agent_no"),
         (is_between, ":team_no", 0 ,7),
         (val_add, ":num_active_fighters", 1),
       (try_end),
       (lt, ":num_active_fighters", 7),
       (neg|main_hero_fallen),
       (store_mission_timer_a, ":cur_time"),
       (this_or_next|ge, ":cur_time", "$g_arena_training_next_spawn_time"),
       (this_or_next|lt, "$g_arena_training_num_agents_spawned", 6),
       (num_active_teams_le, 1),
       (lt, "$g_arena_training_num_agents_spawned", "$g_arena_training_max_opponents"),
      ],
    [
       (assign, ":added_troop", "$g_arena_training_num_agents_spawned"),
       (store_div,  ":added_troop", "$g_arena_training_num_agents_spawned", 6),
       (assign, ":added_troop_sequence", "$g_arena_training_num_agents_spawned"),
       (val_mod, ":added_troop_sequence", 6),
       (val_add, ":added_troop", ":added_troop_sequence"),
       (val_min, ":added_troop", 9),
       (val_add, ":added_troop", "trp_arena_training_fighter_1"),
       (assign, ":end_cond", 10000),
       (get_player_agent_no, ":player_agent"),
       (agent_get_position, pos5, ":player_agent"),
       (try_for_range, ":unused", 0, ":end_cond"),
         (store_random_in_range, ":random_entry_point", 32, 40),
         (neq, ":random_entry_point", "$g_player_entry_point"), # make sure we don't overwrite player
         (entry_point_get_position, pos1, ":random_entry_point"),
         (get_distance_between_positions, ":dist", pos5, pos1),
         (gt, ":dist", 1200), #must be at least 12 meters away from the player
         (assign, ":end_cond", 0),
       (try_end),
       (add_visitors_to_current_scene, ":random_entry_point", ":added_troop", 1),
       (store_add, ":new_spawned_count", "$g_arena_training_num_agents_spawned", 1),
       (store_mission_timer_a, ":cur_time"),
       (store_add, "$g_arena_training_next_spawn_time", ":cur_time", 14),
       (store_div, ":time_reduction", ":new_spawned_count", 3),
       (val_sub, "$g_arena_training_next_spawn_time", ":time_reduction"),
       ]),

  (0, 0, 0,
   [
       (eq, "$g_mt_mode", abm_training)
       ],
    [
       (assign, ":max_teams", 6),
       (val_max, ":max_teams", 1),
       (get_player_agent_no, ":player_agent"),
       (try_for_agents, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_is_alive, ":agent_no"),
         (agent_slot_eq, ":agent_no", slot_agent_arena_team_set, 0),
         (agent_get_team, ":team_no", ":agent_no"),
         (is_between, ":team_no", 0 ,7),
         (try_begin),
           (eq, ":agent_no", ":player_agent"),
           (agent_set_team, ":agent_no", 6), #player is always team 6.
         (else_try),
           (store_random_in_range, ":selected_team", 0, ":max_teams"),
          # find strongest team
           (try_for_range, ":t", 0, 6),
             (troop_set_slot, "trp_temp_array_a", ":t", 0),
           (try_end),
           (try_for_agents, ":other_agent_no"),
             (agent_is_human, ":other_agent_no"),
             (agent_is_alive, ":other_agent_no"),
             (neq, ":agent_no", ":player_agent"),
             (agent_slot_eq, ":other_agent_no", slot_agent_arena_team_set, 1),
             (agent_get_team, ":other_agent_team", ":other_agent_no"),
             (troop_get_slot, ":count", "trp_temp_array_a", ":other_agent_team"),
             (val_add, ":count", 1),
             (troop_set_slot, "trp_temp_array_a", ":other_agent_team", ":count"),
           (try_end),
           (assign, ":strongest_team", 0),
           (troop_get_slot, ":strongest_team_count", "trp_temp_array_a", 0),
           (try_for_range, ":t", 1, 6),
             (troop_slot_ge, "trp_temp_array_a", ":t", ":strongest_team_count"),
             (troop_get_slot, ":strongest_team_count", "trp_temp_array_a", ":t"),
             (assign, ":strongest_team", ":t"),
           (try_end),
           (store_random_in_range, ":rand", 5, 100),
           (try_begin),
             (lt, ":rand", "$g_arena_training_num_agents_spawned"),
             (assign, ":selected_team", ":strongest_team"),
           (try_end),
           (agent_set_team, ":agent_no", ":selected_team"),
         (try_end),
         (agent_set_slot, ":agent_no", slot_agent_arena_team_set, 1),
         (try_begin),
           (neq, ":agent_no", ":player_agent"),
           (val_add, "$g_arena_training_num_agents_spawned", 1),
         (try_end),
       (try_end),
       ]),
  ]
