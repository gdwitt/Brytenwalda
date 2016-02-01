from source.header_operations import *
from source.header_common import *

from source.header_dialogs import *

from source.module_constants import towns_begin, castles_end


dialog_option = \
    [anyone | plyr, "dplmc_constable_security", [],
     "I want to move troops to an another location.", "dplmc_constable_move_troops", [
        (party_clear, "p_temp_party"),
        (assign, "$g_move_heroes", 1),
        (call_script, "script_party_add_party", "p_temp_party", "p_main_party"),
        (party_clear, "p_main_party"),
        (party_remove_members, "p_main_party", "trp_player", 1),
        (change_screen_exchange_members, 1),
    ]]

dialogs = [

    [anyone, "dplmc_constable_move_troops", [],
     "Where do you want to move the troops?", "dplmc_constable_move_troops_location", []
    ],

    [anyone | plyr | repeat_for_parties, "dplmc_constable_move_troops_location", [
        (store_repeat_object, ":party_no"),
        (is_between, ":party_no", towns_begin, castles_end),
        (neq, ":party_no", "$current_town"),
        (store_faction_of_party, ":party_faction", ":party_no"),
        (eq, ":party_faction", "$players_kingdom"),
        (str_store_party_name, s11, ":party_no"),
        ], "{!}{s11}.", "dplmc_constable_move_troops_location_confirm_ask", [

        (store_repeat_object, "$diplomacy_var"),
        (party_clear, "p_temp_party_2"),
        (try_begin),
            (store_party_size, ":party_size", "p_main_party"),
            (gt, ":party_size", 0),
            (call_script, "script_party_add_party", "p_temp_party_2", "p_main_party"),
            (party_clear, "p_main_party"),
            (party_stack_get_troop_id, ":troop_id", "p_main_party", 0),

            (try_begin),
                (ge, ":troop_id", 0),
                (party_stack_get_size, ":troop_size", "p_main_party", 0),
                (party_remove_members, "p_main_party", ":troop_id", ":troop_size"),
            (try_end),

            (party_stack_get_troop_id, ":troop_id", "p_main_party", 1),
            (try_begin),
                (ge, ":troop_id", 0),
                (party_stack_get_size, ":troop_size", "p_main_party", 1),
                (party_remove_members, "p_main_party", ":troop_id", ":troop_size"),
            (try_end),
        (try_end),

        (call_script, "script_party_add_party", "p_main_party", "p_temp_party"),
        (assign, "$g_move_heroes", 0),
    ]],

    [anyone | plyr, "dplmc_constable_move_troops_location", [],
     "Nowhere.", "dplmc_constable_pretalk", [
        (party_clear, "p_temp_party_2"),
        (try_begin),
            (store_party_size, ":party_size", "p_main_party"),
            (gt, ":party_size", 0),
            (call_script, "script_party_add_party", "p_temp_party_2", "p_main_party"),
            (party_clear, "p_main_party"),
            (party_stack_get_troop_id, ":troop_id", "p_main_party", 0),

            (try_begin),
                (ge, ":troop_id", 0),
                (party_stack_get_size, ":troop_size", "p_main_party", 0),
                (party_remove_members, "p_main_party", ":troop_id", ":troop_size"),
            (try_end),
            (party_stack_get_troop_id, ":troop_id", "p_main_party", 1),
            (try_begin),
                (ge, ":troop_id", 0),
                (party_stack_get_size, ":troop_size", "p_main_party", 1),
                (party_remove_members, "p_main_party", ":troop_id", ":troop_size"),
            (try_end),
        (try_end),

        (call_script, "script_party_add_party", "p_main_party", "p_temp_party"),
        (assign, "$g_move_heroes", 0),

        # reset town party
        (call_script, "script_party_add_party", "$current_town", "p_temp_party_2"),
        (party_clear, "p_temp_party_2"),
    ]],

    [anyone, "dplmc_constable_move_troops_location_confirm_ask", [
        (store_party_size, ":party_size", "p_temp_party_2"),

        (assign, ":prisoner_size", 0),
        (party_get_num_prisoner_stacks, ":num_prisoner_stacks", "p_temp_party_2"),
        (try_for_range_backwards, ":stack_no", 0, ":num_prisoner_stacks"),
            (party_prisoner_stack_get_size, ":stack_size", "p_temp_party_2", ":stack_no"),
            (val_add, ":prisoner_size", ":stack_size"),
        (try_end),

        (le, ":party_size", ":prisoner_size"),
        ], "You didn't choose any soldiers. Seems like you changed your mind.",
        "dplmc_constable_pretalk", []
    ],

    [anyone, "dplmc_constable_move_troops_location_confirm_ask", [
        (str_store_party_name, s9, "$diplomacy_var"),
        (store_party_size, ":party_size", "p_temp_party_2"),
        (store_mul, reg5, ":party_size", 5),
        ], "Do you really want to send the troops to {s9}? This will cost us {reg5} scillingas.",
        "dplmc_constable_move_troops_location_confirm", []
    ],

    [anyone | plyr, "dplmc_constable_move_troops_location_confirm", [
        (store_troop_gold, ":player_wealth", "trp_household_possessions"),
        (ge, ":player_wealth", reg5),
        ], "Yes.", "dplmc_constable_pretalk", [

        (call_script, "script_dplmc_withdraw_from_treasury", reg5),
        (call_script, "script_dplmc_move_troops_party", "$current_town", "$diplomacy_var", "p_temp_party_2", "fac_player_faction", "trp_player"), #FLORIS BUGFIX adds "trp_player" argument
        (party_clear, "p_temp_party_2"),
    ]],

    [anyone | plyr, "dplmc_constable_move_troops_location_confirm", [],
     "No. Let me check if we can afford that.", "dplmc_constable_pretalk", [

        (call_script, "script_party_add_party", "$current_town", "p_temp_party_2"),
        (party_clear, "p_temp_party_2"),
    ]],
]
