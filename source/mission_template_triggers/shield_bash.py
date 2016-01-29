from source.header_operations import *
from source.header_common import pos1, pos2, rpw_shield_bash_server
from source.header_troops import tf_male
from source.header_items import itp_type_shield
from source.header_triggers import gk_defend, gk_attack

from source.module_constants import *


sp_shield_bash_1 = (
   0, 0, 0,
   [
       (eq, "$sp_shield_bash", 1),
        (game_key_is_down, gk_defend),
        (game_key_clicked, gk_attack),
   ],
   [
       (get_player_agent_no, ":agent"),
      (agent_is_active, ":agent"),
      (agent_is_alive, ":agent"),
      (neg|agent_slot_ge, ":agent", sp_agent_shield_bash_timer, 1), #Less than.
      (agent_get_wielded_item, ":item", ":agent", 1), #Offhand.
      (gt, ":item", 0),
      (item_get_type, ":type", ":item"),
      (eq, ":type", itp_type_shield), #Shield equipped.
      (agent_get_defend_action, ":action", ":agent"),
      (eq, ":action", 2), #Blocking.
      (agent_get_horse, ":horse", ":agent"),
      (eq, ":horse", -1), #No horse.
      (agent_set_slot, ":agent", sp_agent_shield_bash_timer, 15), #tiempo ampliado chief entre cada shield bash
      (agent_set_animation, ":agent", "anim_shield_bash"),

      #MOTO just use $character_gender
            # (agent_get_troop_id, ":troop", ":agent"),
            # (troop_get_type, ":type", ":troop"),
            (try_begin),
           # (this_or_next|eq,"$character_gender",tf_male),
           # (this_or_next|eq,"$character_gender",tf_alto),
           # (this_or_next|eq,"$character_gender",tf_bajo),
           # (eq,"$character_gender",tf_oso),
                (eq, "$character_gender", tf_male),
               (agent_play_sound, ":agent", "snd_man_yell"),
            (else_try),
                # (eq, ":type", tf_female),
               (agent_play_sound, ":agent", "snd_woman_yell"),
            (try_end),
            #MOTO end just use $character_gender

      (agent_get_position, pos1, ":agent"),
      (assign, ":victim", -1),
      (assign, ":minimum_distance", 150),
      (try_for_agents, ":suspect"),
          (agent_is_alive, ":suspect"),
         (agent_is_human, ":suspect"),
         (neg|agent_is_ally, ":suspect"),
         (agent_get_position, pos2, ":suspect"),
         (neg|position_is_behind_position, pos2, pos1), #Suspect can't be behind basher.
         (get_distance_between_positions, ":distance", pos1, pos2),
         (le, ":distance", ":minimum_distance"),
         (assign, ":minimum_distance", ":distance"),
         (assign, ":victim", ":suspect"),
      (try_end),
      (ge, ":victim", 0),
      (agent_play_sound, ":victim", "snd_wooden_hit_low_armor_high_damage"),
      (agent_get_defend_action, ":action", ":victim"),
      (try_begin),
          (eq, ":action", 2), #Blocking.
         (neg|position_is_behind_position, pos1, pos2), #If basher isn't behind victim.
         (agent_get_wielded_item, ":item", ":victim", 1), #Offhand.
         (gt, ":item", 0),
         (item_get_type, ":type", ":item"),
         (eq, ":type", itp_type_shield),
         (agent_set_animation, ":victim", "anim_shield_bash"),
      (else_try),
          (agent_set_animation, ":victim", "anim_shield_strike"),
      (try_end),
   ])
sp_shield_bash_2 = (
   1, 0, 0, [(eq, "$sp_shield_bash", 1)],
   [
       (get_player_agent_no, ":agent"),
      (agent_is_active, ":agent"),
      (agent_is_alive, ":agent"),
      (agent_get_slot, ":timer", ":agent", sp_agent_shield_bash_timer),
      (val_sub, ":timer", 1),
      (val_max, ":timer", 0),
      (agent_set_slot, ":agent", sp_agent_shield_bash_timer, ":timer"),
   ])
sp_shield_bash_3 = (
   0.25, 0, 0, [(eq, "$sp_shield_bash_ai", 1)],
   [
       (get_player_agent_no, ":player_agent"),
       (try_for_agents, ":agent"),
          (neq, ":agent", ":player_agent"),
          (agent_is_alive, ":agent"),
         (agent_is_human, ":agent"),
         (try_begin),
             (neg|agent_slot_ge, ":agent", sp_agent_shield_bash_timer, 1), #Less than.
            (agent_slot_eq, ":agent", slot_agent_is_running_away, 0), #Isn't routing.
             (agent_get_wielded_item, ":item", ":agent", 1), #Offhand.
            (gt, ":item", 0),
             (item_get_type, ":type", ":item"),
             (eq, ":type", itp_type_shield), #Shield equipped.
             (agent_get_attack_action, ":action", ":agent"),
             (eq, ":action", 0), #Free.
             (agent_get_horse, ":horse", ":agent"),
             (eq, ":horse", -1), #No horse.
            (agent_get_team, ":team", ":agent"),
            (agent_get_position, pos1, ":agent"),
            (assign, ":victim", -1),
            (assign, ":minimum_distance", 125),
            (try_for_agents, ":suspect"),
                (agent_is_alive, ":suspect"),
               (agent_is_human, ":suspect"),
             (neg|agent_is_ally, ":suspect"), #anadido chief para ia no ataque aliados
               (agent_get_position, pos2, ":suspect"),
               (neg|position_is_behind_position, pos2, pos1), #Suspect can't be behind basher.
               (agent_get_team, ":suspect_team", ":suspect"),
               (neq, ":suspect_team", ":team"),
               (get_distance_between_positions, ":distance", pos1, pos2),
               (le, ":distance", ":minimum_distance"),
               (assign, ":minimum_distance", ":distance"),
               (assign, ":victim", ":suspect"),
            (try_end),
            (ge, ":victim", 0),
            (agent_get_horse, ":horse", ":victim"),
            (eq, ":horse", -1),
            (store_random_in_range, ":rand", 145, 156), #ampliado chief
             (agent_set_slot, ":agent", sp_agent_shield_bash_timer, ":rand"), #20 is 20*0.25=5seconds.
            (agent_set_animation, ":agent", "anim_shield_bash"),

            #MOTO just use $character_gender
                  # (agent_get_troop_id, ":troop", ":agent"),
                  # (troop_get_type, ":type", ":troop"),
                  (try_begin),
           # (this_or_next|eq,"$character_gender",tf_male),
           # (this_or_next|eq,"$character_gender",tf_alto),
           # (this_or_next|eq,"$character_gender",tf_bajo),
           # (eq,"$character_gender",tf_oso),
                     (eq, "$character_gender", tf_male),
                     (agent_play_sound, ":agent", "snd_man_yell"),
                  (else_try),
                      # (eq, ":type", tf_female),
                     (agent_play_sound, ":agent", "snd_woman_yell"),
                  (try_end),
                  #MOTO end just use $character_gender

            (agent_play_sound, ":victim", "snd_wooden_hit_low_armor_high_damage"),
            (agent_get_defend_action, ":action", ":victim"),
            (try_begin),
                (eq, ":action", 2), #Blocking.
               (neg|position_is_behind_position, pos1, pos2), #If basher isn't behind victim.
               (agent_get_wielded_item, ":item", ":victim", 1), #Offhand.
                 (gt, ":item", 0),
               (item_get_type, ":type", ":item"),
               (eq, ":type", itp_type_shield),
               (agent_set_animation, ":victim", "anim_shield_bash"),
            (else_try),
                (agent_set_animation, ":victim", "anim_shield_strike"),
            (try_end),
         (try_end),
         (agent_get_slot, ":timer", ":agent", sp_agent_shield_bash_timer),
         (val_sub, ":timer", 1),
         (val_max, ":timer", 0),
         (agent_set_slot, ":agent", sp_agent_shield_bash_timer, ":timer"),
      (try_end),
])



mp_shield_bash_1 = (
    0, 0, 0,
    [
        #Get player input for shield bash.
        (game_key_is_down, gk_defend),
        (game_key_clicked, gk_attack),
    ],
    [
        #If input is given, then initialize a bash.
        (multiplayer_send_message_to_server, rpw_shield_bash_server),
    ])
mp_shield_bash_2 = (
    2.5, 0, 0, [],
    [
        #Update each players shield bash timer.
        #Do this every 2.5 seconds for optimization issues.
        (multiplayer_is_server),
        (get_max_players, ":max"),
        (try_for_range, ":player", 0, ":max"),
            (player_is_active, ":player"),
            (player_get_slot, ":value", ":player", rpw_shield_bash_timer),
            (val_sub, ":value", 1),
            (val_max, ":value", 0),
            (player_set_slot, ":player", rpw_shield_bash_timer, ":value"),
        (try_end),
    ])
