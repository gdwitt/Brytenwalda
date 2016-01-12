from ..module_constants import *
from ..header_mission_templates import *


simple_triggers = [

   (72,
   [
       # Updating trade good prices according to the productions
       (call_script, "script_update_trade_good_prices"),
       # Updating player odds
       (try_for_range, ":cur_center", centers_begin, centers_end),
         (party_get_slot, ":player_odds", ":cur_center", slot_town_player_odds),
         (try_begin),
           (gt, ":player_odds", 1000),
           (val_mul, ":player_odds", 95),
           (val_div, ":player_odds", 100),
           (val_max, ":player_odds", 1000),
         (else_try),
           (lt, ":player_odds", 1000),
           (val_mul, ":player_odds", 105),
           (val_div, ":player_odds", 100),
           (val_min, ":player_odds", 1000),
         (try_end),
         (party_set_slot, ":cur_center", slot_town_player_odds, ":player_odds"),
       (try_end),
    ]),
]
