from source.header_dialogs import anyone, plyr
from source.header_operations import *

dialogs = [
    # todo: make this with different sums of money
    [anyone | plyr, "village_elder_talk", [
        (store_troop_gold, ":money", "trp_player"),
        (ge, ":money", 500)
    ],
     "I want help to you with 500 scillingas if you speak well of me to "
     "farmers here.", "villageelder_agree", [
         (troop_remove_gold, "trp_player", 500),
         (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
     ]],

    [anyone, "villageelder_agree", [],
     "Sure (his eyes shine).", "village_elder_pretalk", [
         (change_screen_trade, "$g_talk_troop")
     ]],
]
