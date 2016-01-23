from source.header_mission_templates import *
from source.header_items import *

from source.module_constants import *


WP_HR_on_death =(
  ti_on_agent_killed_or_wounded, 0, 0, [],
    [
      (store_trigger_param_1, ":agent_victim"),
      (store_trigger_param_2, ":agent_killer"),

      # Is this a valid kill worth gaining morale?
      (agent_is_human, ":agent_victim"),

      # Determine health amount to regenerate
      (try_begin), # Is it the player?
          (get_player_agent_no, ":agent_player"),
          (eq, ":agent_killer", ":agent_player"),
          (assign, ":health_regeneration", wp_hr_player_rate),
      (else_try), # Is it a companion?
          (is_between, ":agent_killer", companions_begin, companions_end),
          (assign, ":health_regeneration", wp_hr_companion_rate),
      (else_try), # Is it a lord?
          (is_between, ":agent_killer", lords_begin, lords_end),
          (assign, ":health_regeneration", wp_hr_lord_rate),
      (else_try), # Is it a king?
          (is_between, ":agent_killer", kings_begin, kings_end),
          (assign, ":health_regeneration", wp_hr_king_rate),
      (else_try), # This should catch all common soldiers, horses, etc.
          (assign, ":health_regeneration", wp_hr_common_rate),
          # This adds a small bonus to all non-heroes based on the leadership of their owner.
          (agent_get_team, ":team_killer", ":agent_killer"),
          (team_get_leader, ":agent_leader", ":team_killer"),
          (agent_get_troop_id, ":troop_leader", ":agent_leader"),
          (store_skill_level, ":leadership", "skl_leadership", ":troop_leader"),
          (assign, reg4, ":leadership"), # stored for debug display purposes.
          (val_div, ":leadership", wp_hr_leadership_factor),
          (val_add, ":health_regeneration", ":leadership"),
      (try_end),

      # Adds in Strength as a bonus or penalty.  (STR - 10) / wp_hr_strength_factor
      (agent_get_troop_id, ":troop_killer", ":agent_killer"),
      (store_attribute_level, ":strength", ":troop_killer", ca_strength),
      (val_sub, ":strength", 10),
      (val_div, ":strength", wp_hr_strength_factor),
      (val_add, ":health_regeneration", ":strength"),

      # Changes health regeneration based on this factor.
      (try_begin),
          (eq, wp_hr_factor_difficulty, 1),  # Is this difficulty script even being used.
          (assign, ":bonus_difficulty", 2),
          (try_begin),
              (agent_is_ally, ":agent_killer"),
              (val_mul, ":bonus_difficulty", wp_hr_diff_ally_penalty),
          (else_try),
              (val_mul, ":bonus_difficulty", wp_hr_diff_enemy_bonus),
          (try_end),
          (val_add, ":health_regeneration", ":bonus_difficulty"),
      (try_end),

      (val_max, ":health_regeneration", 0), # We don't want a negative health regeneration.

      # Displays debug messages if turned on.
      (try_begin),
          (eq, wp_hr_debug, 1),
          (str_store_troop_name, s1, ":troop_killer"),
          (assign, reg0, ":health_regeneration"),
          (assign, reg1, ":strength"),
          (try_begin), (ge, ":leadership", 10), (assign, ":leadership", -1), (try_end), # If no leadership bonus exists put in a default value.
          (assign, reg2, ":leadership"),
         # (display_message, "@DEBUG (Health Regen): Agent leadership skill is {reg4}."),
          (try_begin), (eq, wp_hr_factor_difficulty, 1),(assign, reg3, ":bonus_difficulty"), (else_try), (assign, reg3, 0), (try_end),  # Get difficulty bonus OR use 0.
       #   (display_message, "@DEBUG (Health Regen): {s1} regains {reg0}% health.  = +{reg1}% STR +{reg2}% Lead + {reg3}% Difficulty."),
      (try_end),

      # Regenerates the given health amount.
      (ge, ":health_regeneration", 1),
      (store_agent_hit_points, ":current_health", ":agent_killer", 0),
      (val_add, ":current_health", ":health_regeneration"),
      (agent_set_hit_points, ":agent_killer", ":current_health", 0),
    ])
