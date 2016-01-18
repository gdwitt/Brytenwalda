from source.header_dialogs import anyone, plyr
from source.header_operations import *
from source.module_constants import *
from source.header_parties import *


dialogs = [

    # answer to attack
    [anyone, "merchant_attack_begin", [],
     "Are you robbing us?{s11}", "merchant_attack_verify", [
         (str_clear, s11),
         (try_begin),
            (faction_slot_ge, "$g_encountered_party_faction", slot_faction_truce_days_with_factions_begin, 1),
            (str_store_string, s11, "str__have_you_not_signed_a_truce_with_our_lord"),
         (try_end),
     ]],

    # cancel attack
    [anyone | plyr, "merchant_attack_verify", [],
     "Robbing you? No, no! It was a joke.", "merchant_attack_verify_norob", []
     ],

    # answer to cancel attack
    [anyone, "merchant_attack_verify_norob", [],
     "God, don't joke about that, {lad/lass}. For a moment I thought we were in "
     "real trouble.", "close_window", [
         (assign, "$g_leave_encounter", 1)
        ]
     ],

    # confirm attack
    [anyone | plyr, "merchant_attack_verify", [],
     "Of course I'm robbing you. Now hand over your goods.", "merchant_attack", [
         (call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$g_encountered_party"),
        ]
     ],

    # answer confirm attack, attack starts
    [anyone, "merchant_attack", [],
     "Damn you, you won't get anything from us without a fight!", "close_window", [

        (store_relation, ":relation", "$g_encountered_party_faction", "fac_player_supporters_faction"),
        (try_begin),
            (gt, ":relation", 0),
            (val_sub, ":relation", 50),
        (try_end),
        (val_sub, ":relation", 10),
        (call_script, "script_set_player_relation_with_faction", "$g_encountered_party_faction", ":relation"),
        (call_script, "script_diplomacy_party_attacks_neutral", "p_main_party", "$g_encountered_party"),

        (assign, "$encountered_party_hostile", 1),
        (assign, "$encountered_party_friendly", 0),
      ]],
]