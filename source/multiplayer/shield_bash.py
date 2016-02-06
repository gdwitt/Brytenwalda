from source.header_operations import *
from source.header_common import rpw_shield_bash_server
from source.header_triggers import gk_defend, gk_attack

from source.module_constants import *


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
            (player_get_slot, ":value", ":player", "slot_player_rpw_shield_bash_timer"),
            (val_sub, ":value", 1),
            (val_max, ":value", 0),
            (player_set_slot, ":player", "slot_player_rpw_shield_bash_timer", ":value"),
        (try_end),
    ])
