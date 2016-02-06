from source.header_operations import *
from source.header_common import *
from source.header_dialogs import anyone

from source.module_constants import active_npcs_begin, active_npcs_end, slto_kingdom_hero


dialogs = [

    [anyone, "village_elder_ask_enemies", [
        (assign, ":give_report", 0),
        (party_get_slot, ":original_faction", "$g_encountered_party", "slot_center_original_faction"),
        (store_relation, ":original_faction_relation", ":original_faction", "fac_player_supporters_faction"),
        (try_begin),
            (gt, ":original_faction_relation", 0),
            (party_slot_ge, "$g_encountered_party", "slot_center_player_relation", 0),
            (assign, ":give_report", 1),
        (else_try),
            (party_slot_ge, "$g_encountered_party", "slot_center_player_relation", 30),
            (assign, ":give_report", 1),
        (try_end),
        (eq, ":give_report", 0),

         ], "I am sorry, {sir/madam}. We have neither seen nor heard of any "
            "war parties in this area.", "village_elder_pretalk", []],

    [anyone, "village_elder_ask_enemies", [],
     "Hmm. Let me think about it...", "village_elder_tell_enemies", [
        (assign, "$temp", 0),
     ]],

    [anyone, "village_elder_tell_enemies", [
        # $temp is the total number of parties found so far.
        (assign, ":start", "$temp"),

        (val_add, ":start", active_npcs_begin),

        (assign, ":found", 0),
        (try_for_range, ":cur_troop", ":start", active_npcs_end),
            (troop_slot_eq, ":cur_troop", "slot_troop_occupation", slto_kingdom_hero),
            (troop_get_slot, ":cur_party", ":cur_troop", "slot_troop_leaded_party"),
            (gt, ":cur_party", 0),
            (store_troop_faction, ":cur_faction", ":cur_troop"),
            (store_relation, ":reln", ":cur_faction", "fac_player_supporters_faction"),
            (lt, ":reln", 0),
            (store_distance_to_party_from_party, ":dist", "$g_encountered_party", ":cur_party"),
            (lt, ":dist", 10),

            (call_script, "script_get_information_about_troops_position", ":cur_troop", 0),
            # this scripts outputs `s1`
            (eq, reg0, 1),  # Troop's location is known.

            # when found, break the for
            (assign, ":found", 1),
            (assign, ":cur_troop", active_npcs_end),
            (val_add, ":cur_troop", 1),

            (str_store_string, s2, "@He is not commanding any men at the moment."),

            (assign, ":num_troops", 0),
            (assign, ":num_wounded_troops", 0),
            (party_get_num_companion_stacks, ":num_stacks", ":cur_party"),
            (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
                (party_stack_get_troop_id, ":stack_troop", ":cur_party", ":i_stack"),
                (neg | troop_is_hero, ":stack_troop"),
                (party_stack_get_size, ":stack_size", ":cur_party", ":i_stack"),
                (party_stack_get_num_wounded, ":num_wounded", ":cur_party", ":i_stack"),
                (val_add, ":num_troops", ":stack_size"),
                (val_add, ":num_wounded_troops", ":num_wounded"),
            (try_end),

            (try_begin),
                (gt, ":num_troops", 0),
                (call_script, "script_round_value", ":num_wounded_troops"),
                (assign, reg1, reg0),
                (call_script, "script_round_value", ":num_troops"),
                (str_store_string, s2, "@He currently commands {reg0} men{reg1?, "
                                       "of which around {reg1} are wounded:}."),
            (try_end),
        (try_end),

        (eq, ":found", 1),
        (val_add, "$temp", 1),
     ],
     "{s1} {s2}", "village_elder_tell_enemies", []],

    [anyone, "village_elder_tell_enemies",
     [(eq, "$temp", 0)],
     "No, {sir/madam}. We haven't seen any war parties in this area for some time.",
     "village_elder_pretalk", []
     ],

    [anyone, "village_elder_tell_enemies", [],
     "Well, I guess that was all.", "village_elder_pretalk", []
     ],
]
