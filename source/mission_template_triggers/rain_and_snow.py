from source.header_mission_templates import *

from source.module_constants import *


rain = (
    ti_before_mission_start, 0, ti_once, [],
   [
                (store_random_in_range, ":rain_chance", 1,7),
                (try_begin),
                    (eq, ":rain_chance", 1),
          (this_or_next|eq, "$g_cur_month", 9),
          (this_or_next|eq, "$g_cur_month", 10),
          (this_or_next|eq, "$g_cur_month", 11),
          (this_or_next|eq, "$g_cur_month", 12),
          (this_or_next|eq, "$g_cur_month", 1),
          (this_or_next|eq, "$g_cur_month", 3),
          (this_or_next|eq, "$g_cur_month", 4),
          (eq, "$g_cur_month", 5),
                    (store_random_in_range, ":rain_power", 50, 100),
                    (store_random_in_range, ":haze_power", 25, 65),
                    (set_global_haze_amount, ":haze_power"),
                    (set_rain, 1, ":rain_power"),
                (else_try),
                    (eq, ":rain_chance", 2),
                    (store_random_in_range, ":rain_power", 50, 100),
                    (store_random_in_range, ":haze_power", 25, 65),
                    (set_global_haze_amount, ":haze_power"),
                    (set_rain, 1, ":rain_power"),
                (else_try),
                    (eq, ":rain_chance", 3),
          (this_or_next|eq, "$g_cur_month", 9),
          (this_or_next|eq, "$g_cur_month", 10),
          (this_or_next|eq, "$g_cur_month", 11),
          (this_or_next|eq, "$g_cur_month", 12),
          (this_or_next|eq, "$g_cur_month", 1),
          (eq, "$g_cur_month", 2),
                    (store_random_in_range, ":fog_distance", 50, 75),
                    (store_random_in_range, ":haze_power", 25, 65),
                    (set_global_haze_amount, ":haze_power"),
                                        (set_fog_distance, ":fog_distance", 0x333333),
                (else_try),
                    (eq, ":rain_chance", 4),
          (this_or_next|eq, "$g_cur_month", 11),
          (this_or_next|eq, "$g_cur_month", 12),
          (this_or_next|eq, "$g_cur_month", 1),
          (eq, "$g_cur_month", 2),
                    (store_random_in_range, ":rain_power", 50, 100),
                    (store_random_in_range, ":haze_power", 25, 65),
                    (set_global_haze_amount, ":haze_power"),
                    (set_rain, 1, ":rain_power"),
                                        (call_script, "script_change_rain_or_snow"),
                (else_try),
                    (eq, ":rain_chance", 5),
          (this_or_next|eq, "$g_cur_month", 11),
          (this_or_next|eq, "$g_cur_month", 12),
          (this_or_next|eq, "$g_cur_month", 1),
          (eq, "$g_cur_month", 2),
          (party_get_current_terrain,":terrain","p_main_party"),
         (this_or_next|eq,":terrain",4),
          (eq,":terrain",12),
                    (store_random_in_range, ":rain_power", 50, 100),
                    (store_random_in_range, ":haze_power", 25, 65),
                    (set_global_haze_amount, ":haze_power"),
                    (set_rain, 2, ":rain_power"),
                (else_try),
                    (set_global_haze_amount, 0),
                    (set_rain, 0, 0),
                (try_end),
   ])
