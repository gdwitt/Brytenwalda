from source.header_operations import *
from source.header_common import reg6
from source.header_dialogs import anyone, plyr

from source.module_constants import *

dialogs = [

    [anyone, "merchant_demand_toll", [
        (gt, "$g_strength_ratio", 70),
        (store_div, reg6, "$g_ally_strength", 2),
        (val_add, reg6, 40),
        (assign, "$temp", reg6),
        ], "Please, I don't want any trouble. I can give you {reg6} scillingas, "
           "just let us go.", "merchant_demand_toll_2", []
     ],

    [anyone, "merchant_demand_toll", [
        (store_div, reg6, "$g_ally_strength", 4),
        (val_add, reg6, 10),
        (assign, "$temp", reg6),
        ], "I don't want any trouble. I can give you {reg6} scillingas if "
           "you'll let us go.", "merchant_demand_toll_2", []
     ],

    [anyone | plyr, "merchant_demand_toll_2", [],
     "Agreed, hand it over and you may go in peace.",
     "merchant_demand_toll_accept", []
     ],

    [anyone, "merchant_demand_toll_accept", [
        (assign, reg6, "$temp")
        ],
     "Very well then. Here's {reg6} scillingas. ", "close_window", [
        (assign, "$g_leave_encounter", 1),
        (call_script, "script_troop_add_gold", "trp_player", "$temp"),

        (store_add, ":toll_finish_time", "$g_current_hours", merchant_toll_duration),
        (party_set_slot, "$g_encountered_party", slot_party_last_toll_paid_hours, ":toll_finish_time"),

        (try_begin),
            (ge, "$g_encountered_party_relation", -5),
            (store_relation, ":rel", "$g_encountered_party_faction", "fac_player_supporters_faction"),

            (try_begin),
                (gt, ":rel", 0),
                (val_sub, ":rel", 1),
            (try_end),

            (val_sub, ":rel", 1),
            (call_script, "script_set_player_relation_with_faction", "$g_encountered_party_faction", ":rel"),
        (try_end),

        (call_script, "script_add_log_entry", logent_caravan_accosted, "trp_player", -1, -1, "$g_encountered_party_faction"),
        (assign, reg6, "$temp"),
      ]
     ],

    [anyone | plyr, "merchant_demand_toll_2", [],
     "I changed my mind, I can't take your money.", "merchant_pretalk", []
     ],

    [anyone | plyr, "merchant_demand_toll_2", [],
     "No, I want everything you have! [Attack]", "merchant_attack_begin", []
     ],
]
