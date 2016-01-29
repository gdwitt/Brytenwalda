from source.header_operations import *
from source.header_triggers import key_left_shift, gk_move_backward
from source.header_troops import tf_male, tf_female


## Beaver - Mission Template for tripping when walking backwards - SP ONLY
common_andar_cae = (1, 0, 5, [ #Check every second, if conditions pass, only re-run after 5 sec
         (eq, "$sp_caer_andar", 1),
    (game_key_is_down,gk_move_backward), #Player moving backwards
    (neg|key_is_down,key_left_shift), #Don't trip if walking
        (neg|main_hero_fallen)
],
[

       (get_player_agent_no, ":player"),
       (agent_get_horse,":agent_mounted",":player"),
           (eq,":agent_mounted",-1),
      (store_skill_level, ":athletics_level", "skl_athletics", "trp_player"),
    (store_random_in_range,":percentage",0,100), #Get random percentage
   (try_begin),    #MOTO amounts to even 20% chance for athletics < 6...
##       (lt,":percentage",2), #10% risk of tripping
##      (agent_set_animation, ":player", "anim_strike_fall_back_rise"),
##      (display_message, "@You walk backwards without looking, you stumble and fall."),
##       (try_begin),
##       (eq,"$character_gender",tf_male),
##         (agent_play_sound, ":player", "snd_man_yell"),
##      (else_try),
##          (eq, "$character_gender", tf_female),
##         (agent_play_sound, ":player", "snd_woman_yell"),
##      (try_end),
##      (else_try),
##        (lt, ":athletics_level", 2),
##       (gt, ":percentage", 2),
##       (lt, ":percentage", 4),
##      (agent_set_animation, ":player", "anim_strike_fall_back_rise"),
##      (display_message, "@You stumble and fall."),
##       (try_begin),
##       (eq,"$character_gender",tf_male),
##         (agent_play_sound, ":player", "snd_man_yell"),
##      (else_try),
##          (eq, "$character_gender", tf_female),
##         (agent_play_sound, ":player", "snd_woman_yell"),
##      (try_end),
##      (else_try),
##        (lt, ":athletics_level", 4),
##       (gt, ":percentage", 4),
##       (lt, ":percentage", 6),
##      (agent_set_animation, ":player", "anim_strike_fall_back_rise"),
##      (display_message, "@You stumble and fall."),
##       (try_begin),
##       (eq,"$character_gender",tf_male),
##         (agent_play_sound, ":player", "snd_man_yell"),
##      (else_try),
##          (eq, "$character_gender", tf_female),
##         (agent_play_sound, ":player", "snd_woman_yell"),
##      (try_end),
##      (else_try),
##        (lt, ":athletics_level", 6),
##       (gt, ":percentage", 6),
##       (lt, ":percentage", 8),
##      (agent_set_animation, ":player", "anim_strike_fall_back_rise"),
##      (display_message, "@You stumble and fall."),
##       (try_begin),
##       (eq,"$character_gender",tf_male),
##         (agent_play_sound, ":player", "snd_man_yell"),
##      (else_try),
##          (eq, "$character_gender", tf_female),
##         (agent_play_sound, ":player", "snd_woman_yell"),
##      (try_end),
##      (else_try),
##        (display_message, "@"),
       (val_mul, ":athletics_level", 3),
       (store_sub, ":chance_trip", 23, ":athletics_level"),
       (lt, ":percentage", ":chance_trip"),    #chance to trip 20% athletics 0 down to 2% athletics 6 (0 above that)
       (agent_set_animation, ":player", "anim_strike_fall_back_rise"),
       (display_message, "@You stumble and fall."),
       (try_begin),
           (eq,"$character_gender",tf_male),
           (agent_play_sound, ":player", "snd_man_yell"),
       (else_try),
           (eq, "$character_gender", tf_female),
           (agent_play_sound, ":player", "snd_woman_yell"),
       (else_try),
           (agent_play_sound, ":player", "snd_man_yell"),
       (try_end),
       (try_end),
])
###andar hacia atras se cae chief acaba
