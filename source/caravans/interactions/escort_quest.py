from source.header_common import reg0, s1, reg2, s3, reg3, reg4
from source.header_dialogs import anyone, plyr
from source.header_operations import *
from source.module_constants import tc_party_encounter


dialogs = [

    [anyone, "caravan_offer_protection", [],
     "These roads are dangerous indeed. One can never have enough protection.",
     "caravan_offer_protection_2", [
        (get_party_ai_object, ":caravan_destination", "$g_encountered_party"),
        (store_distance_to_party_from_party, "$caravan_distance_to_target", ":caravan_destination", "$g_encountered_party"),
        (assign, "$caravan_escort_offer", "$caravan_distance_to_target"),
        (val_sub, "$caravan_escort_offer", 10),
        (call_script, "script_party_calculate_strength", "p_main_party", 0),
        (assign, ":player_strength", reg0),
        (val_min, ":player_strength", 200),
        (val_add, ":player_strength", 20),
        (val_mul, "$caravan_escort_offer", ":player_strength"),
        (val_div, "$caravan_escort_offer", 50),
        (val_max, "$caravan_escort_offer", 5),
      ]],

    # reject offer
    [anyone, "caravan_offer_protection_2", [
        (lt, "$caravan_distance_to_target", 10)
    ], "An escort? We're almost there already! Thank you for the offer, though.",
     "close_window", [
         (assign, "$g_leave_encounter", 1)
     ]],

    # suggest value offer
    [anyone, "caravan_offer_protection_2", [
        (get_party_ai_object, ":caravan_destination", "$g_encountered_party"),
        (str_store_party_name, 1, ":caravan_destination"),
        (assign, reg2, "$caravan_escort_offer"),

        ], "We are heading to {s1}. I will pay you {reg2} scillingas if you "
           "escort us there.", "caravan_offer_protection_3", []
     ],

    # player agrees to value
    [anyone | plyr, "caravan_offer_protection_3", [],
     "Agreed.", "caravan_offer_protection_4", []],

    # chat after accepting
    [anyone, "caravan_offer_protection_4", [],
     "I want you to stay close to us along the way. We'll need your help if "
     "we get ambushed by bandits.", "caravan_offer_protection_5", []
     ],

    # chat after accepting
    [anyone | plyr, "caravan_offer_protection_5", [],
     "Don't worry, you can trust me.", "caravan_offer_protection_6", []],

    # chat after accepting
    [anyone, "caravan_offer_protection_6", [
        (get_party_ai_object, ":caravan_destination", "$g_encountered_party"),
        (str_store_party_name, s1, ":caravan_destination")
        ], "Good. Come and collect your money when we're within sight of {s1}. "
           "For now, let's just get underway.", "close_window", [

        (get_party_ai_object, ":caravan_destination", "$g_encountered_party"),
        (assign, "$caravan_escort_destination_town", ":caravan_destination"),
        (assign, "$caravan_escort_party_id", "$g_encountered_party"),
        (assign, "$caravan_escort_agreed_reward", "$caravan_escort_offer"),
        (assign, "$caravan_escort_state", 1),
        (assign, "$g_leave_encounter", 1)
      ]],

    # player refuses with value
    [anyone | plyr, "caravan_offer_protection_3", [],
     "Forget it.", "caravan_offer_protection_4b", []
     ],

    # caravan replies to refusal
    [anyone, "caravan_offer_protection_4b", [],
     "Perhaps another time, then.", "close_window", [
         (assign, "$g_leave_encounter", 1)]
     ],
]

# dialogs triggered when `$caravan_escort_state = 1`
dialogs += [

    [anyone, "event_triggered", [
        (eq, "$caravan_escort_state", 1),
        (eq, "$g_encountered_party", "$caravan_escort_party_id"),
        (le, "$talk_context", tc_party_encounter),
        (store_distance_to_party_from_party, reg0, "$caravan_escort_destination_town", "$caravan_escort_party_id"),
        (lt, reg0, 5),
        (str_store_party_name, s3, "$caravan_escort_destination_town"),
        (assign, reg3, "$caravan_escort_agreed_reward"),
        ], "There! I can see the walls of {s3} in the distance. We've made it "
           "safely. Here, take this purse of {reg3} scillingas, as I promised. "
           "I hope we can travel together again someday.", "close_window", [
         (assign, "$caravan_escort_state", 0),
         (call_script, "script_troop_add_gold", "trp_player",
          "$caravan_escort_agreed_reward"),
         (assign, reg4, "$caravan_escort_agreed_reward"),
         (val_mul, reg4, 1),
         (add_xp_as_reward, reg4),
         (assign, "$g_leave_encounter", 1),
     ]],

    [anyone | plyr, "talk_caravan_escort", [],
     "There might be bandits nearby. Stay close.", "talk_caravan_escort_2a", []
     ],

    [anyone, "talk_caravan_escort_2a", [],
     "Trust me, {playername}, we're already staying as close to you as we can. "
     "Lead the way.", "close_window", [
         (assign, "$g_leave_encounter", 1),
     ]],

    [anyone | plyr, "talk_caravan_escort", [],
     "No sign of trouble, we can breathe easy.", "talk_caravan_escort_2b", []
     ],

    [anyone, "talk_caravan_escort_2b", [],
     "I'll breathe easy when we reach {s1} and not a moment sooner. Let's "
     "keep moving.", "close_window", [
        (str_store_party_name, s1, "$caravan_escort_destination_town"),
        (assign, "$g_leave_encounter", 1)
     ]],
]

simple_triggers = [
    (0, [
        # escort caravan quest auto dialog trigger
        (try_begin),
            (eq, "$caravan_escort_state", 1),
            (party_is_active, "$caravan_escort_party_id"),

            (store_distance_to_party_from_party, ":caravan_distance_to_destination", "$caravan_escort_destination_town", "$caravan_escort_party_id"),
            (lt, ":caravan_distance_to_destination", 2),

            (store_distance_to_party_from_party, ":caravan_distance_to_player", "p_main_party", "$caravan_escort_party_id"),
            (lt, ":caravan_distance_to_player", 5),

            (assign, "$talk_context", tc_party_encounter),
            (assign, "$g_encountered_party", "$caravan_escort_party_id"),
            (party_stack_get_troop_id, ":caravan_leader", "$caravan_escort_party_id", 0),
            (party_stack_get_troop_dna, ":caravan_leader_dna", "$caravan_escort_party_id", 0),

            (start_map_conversation, ":caravan_leader", ":caravan_leader_dna"),
        (try_end),
    ]),
]

triggers = [
    # cancel escort quest if caravan is no longer active
    (4.0, 0, 0.0, [
        (eq, "$caravan_escort_state", 1),
        (assign, ":cancel_quest", 0),
        (try_begin),
            (neg | party_is_active, "$caravan_escort_party_id"),
            (assign, ":cancel_quest", 1),
        (else_try),
            (get_party_ai_object, ":ai_object", "$caravan_escort_party_id"),
            (neq, ":ai_object", "$caravan_escort_destination_town"),
            (assign, ":cancel_quest", 1),
        (try_end),
        (eq, ":cancel_quest", 1),
        ],
     [(assign, "$caravan_escort_state", 0),
    ]),
]
