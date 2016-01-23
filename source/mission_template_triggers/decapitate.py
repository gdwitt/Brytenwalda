from source.header_mission_templates import *
from source.header_items import *

from source.module_constants import *


theoris_decapitation = (
    ti_on_agent_hit, 0, 0, [(eq, "$sp_decapitation", 1),
],
    [
       (store_trigger_param_1, ":agent"),
      (agent_is_human, ":agent"),
      (agent_get_troop_id, ":troop", ":agent"),
      (neg|troop_is_hero,":troop"),
       (store_trigger_param_3, ":damage"),
             (set_trigger_result, -1),
      (ge, ":damage", 50), #strong blow golpe para decapitar necesario. If the damage is greater than or equal to 30.
      (set_trigger_result, ":damage"),
      (store_agent_hit_points, ":hp", ":agent", 1), #Stores agent hp to :hp
#      (val_sub, ":hp", 5), #vida que le resta al keko para decapitar. Subtracts 5 from :hp (hp = hp -5)
      (lt, ":hp", 10), #strong blow golpe para decapitar necesario. If the damage is greater than or equal to 30.
#      (ge, ":damage", ":hp"), #If ( damage >= hp) (after hp - 5) (ie if damage >= hp-5)
      (agent_get_position, pos1, ":agent"),
      (get_distance_between_positions, ":distance", pos1, pos0),
      (is_between, ":distance", 150, 185), # *zing*
      (agent_get_item_slot, ":item", ":agent", 4), #head slot
      (try_begin),
          (ge, ":item", 1),
         (agent_unequip_item, ":agent", ":item"),
##         (le, ":hp", 0),
##         (set_position_delta, 0, 0, -10), #center of head is somewhere above stump?
##         (particle_system_add_new, "psys_game_blood"),
##         (particle_system_emit, "psys_game_blood" , 100000, 100),
      (try_end),
      (agent_equip_item, ":agent", "itm_noheadhelm"),
      (particle_system_burst, "psys_game_blood_4", pos0, 125), #Yeah..
      (agent_set_hit_points,":agent",0,1),#insta-death, muerte fija al decapitar
#(prop_instance_enable_physics, spr_head_a_dynamic, 1),
       #(set_spawn_position, pos1),
      #(spawn_scene_prop, "spr_physics_head"),
   ])
