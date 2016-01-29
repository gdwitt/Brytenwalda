from source.header_operations import *
from source.header_common import *

from source.module_constants import slot_village_state, slot_village_infested_by_bandits, \
    slot_center_volunteer_troop_amount, slot_center_volunteer_troop_type, \
    slot_center_player_relation, svs_looted, svs_being_raided


menus = [
    ("recruit_volunteers", 0, "{s18}", "none", [
        (call_script, "script_compute_village_recruits", -1),

        (try_begin),
            (eq, reg0, 0),
            (str_store_string, s18, "@No one here seems to be willing to join your party."),
        (else_try),
            (str_store_troop_name_by_count, s3, reg1, reg0),
            (try_begin),
                (eq, reg5, 1),
                (str_store_string, s18, "@One {s3} volunteer follows you."),
            (else_try),
                (str_store_string, s18, "@{reg5} {s3} volunteers are willing follow you."),
            (try_end),
            (set_background_mesh, "mesh_pic_recruits"),
        (try_end),

        ], [

        ("continue", [
            (lt, reg0, 1),
            ], "[Leave]", [
            (party_set_slot, "$current_town", slot_center_volunteer_troop_amount, -1),
                (jump_to_menu, "mnu_village"),
        ]),

        ("continue_not_enough_space", [
            (ge, reg0, 1),
            (lt, reg3, 1),
            ], "I don't have enough space in your party...", [
                (jump_to_menu, "mnu_village"),
        ]),

        ("continue_not_enough_gold", [
            (ge, reg0, 1),
            (ge, reg3, 1),
            (lt, reg4, 1),
            ], "I don't have enough money...", [
                (jump_to_menu, "mnu_village"),
        ]),

        ("recruit_them", [
            (ge, reg5, 1),
            (store_mul, reg6, reg5, reg2),
            ], "Recruit all I can ({reg6} scillingas).", [
                (call_script, "script_village_recruit_volunteers", reg5, -1),
                (jump_to_menu, "mnu_village"),
        ]),

        ("forget_it", [
            (ge, reg5, 1),
            ], "Forget it.", [
                (jump_to_menu, "mnu_village"),
        ]),
    ]),
]


scripts = [

    # condition for recruitment to be available
    ("cf_village_recruit_volunteers_condition", [
        (store_script_param, ":min_relation", 1),
        (store_script_param, ":min_faction_relation", 2),

        (neg | party_slot_eq, "$current_town", slot_village_state, svs_looted),
        (neg | party_slot_eq, "$current_town", slot_village_state, svs_being_raided),
        (neg | party_slot_ge, "$current_town", slot_village_infested_by_bandits, 1),

        (store_faction_of_party, ":village_faction", "$current_town"),
        (party_get_slot, ":center_relation", "$current_town", slot_center_player_relation),
        (store_relation, ":village_faction_relation", ":village_faction", "fac_player_faction"),

        (ge, ":center_relation", ":min_relation"),

        (try_begin),
            (eq, "$cheat_mode", 1),
            (display_message, "str_center_relation_at_least_zero"),
        (try_end),

        (this_or_next | eq, ":village_faction", "$players_kingdom"),
        (this_or_next | ge, ":village_faction_relation", ":min_faction_relation"),
        (this_or_next | eq, ":village_faction", "$supported_pretender_old_faction"),
        (eq, "$players_kingdom", 0),

        (try_begin),
            (eq, "$cheat_mode", 1),
            (display_message, "str_relationfaction_conditions_met"),
        (try_end),

        (party_slot_ge, "$current_town", slot_center_volunteer_troop_amount, 1),
        (party_slot_ge, "$current_town", slot_center_volunteer_troop_type, 1),

        (try_begin),
            (eq, "$cheat_mode", 1),
            (display_message, "str_troops_available"),
        (try_end),

        (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
        (ge, ":free_capacity", 1),

        (try_begin),
            (eq, "$cheat_mode", 1),
            (display_message, "str_party_has_capacity"),
        (try_end),
     ]),

    # input1: cost per recruit (-1 -> compute it)
    # number recruits -> reg0
    # troop type -> reg1
    # cost_per_recruit -> reg2
    # party capacity -> reg3
    # gold capacity -> reg4
    # max_amount -> reg5
    ("compute_village_recruits", [
        (store_script_param, ":cost_per_recruit", 1),

        (party_get_slot, ":troop_type", "$current_town", slot_center_volunteer_troop_type),
        (party_get_slot, ":recruits", "$current_town", slot_center_volunteer_troop_amount),
        (party_get_free_companions_capacity, ":capacity", "p_main_party"),

        # recruits += persuasion
        # todo: formula is wrong because it recruits even when :recruits = 0
        (store_skill_level, ":persuasion_lvl", "skl_persuasion", "trp_player"),
        (val_add, ":recruits", ":persuasion_lvl"),

        (store_troop_gold, ":gold", "trp_player"),
        (try_begin),
            (eq, ":cost_per_recruit", -1),
            (call_script, "script_cost_per_village_recruit"),
            (assign, ":cost_per_recruit", reg0),
        (try_end),
        (store_div, ":gold_capacity", ":gold", ":cost_per_recruit"),

        (assign, reg0, ":recruits"),
        (assign, reg1, ":troop_type"),
        (assign, reg2, ":cost_per_recruit"),
        (assign, reg3, ":capacity"),
        (assign, reg4, ":gold_capacity"),

        (assign, ":max_amount", ":recruits"),
        (val_min, ":max_amount", ":capacity"),
        (val_min, ":max_amount", ":gold_capacity"),
        (assign, reg5, ":max_amount"),
    ]),

    # cost_per_recruit -> reg0
    ("cost_per_village_recruit", [
        (party_get_slot, ":troop_id", "$current_town", slot_center_volunteer_troop_type),
        (store_character_level, ":troop_level", ":troop_id"),
        (try_begin),
            (is_between, ":troop_level", 0, 16),
            (assign, reg0, 10),
        (else_try),
            (is_between, ":troop_level", 16, 20),
            (assign, reg0, 25),
        (else_try),
            (is_between, ":troop_level", 20, 24),
            (assign, reg0, 75),
        (else_try),
            (is_between, ":troop_level", 24, 28),
            (assign, reg0, 200),
        (else_try),
            (is_between, ":troop_level", 28, 30),
            (assign, reg0, 400),
        (else_try),
            (is_between, ":troop_level", 30, 34),
            (assign, reg0, 500),
        (else_try),
            (assign, reg0, 1000),
        (try_end),
    ]),

    # input1: amount to recruit
    # input2: cost per recruit (-1 -> compute it)
    # recruited -> reg0
    ("village_recruit_volunteers", [
        (store_script_param, ":amount", 1),
        (store_script_param, ":cost_per_recruit", 2),

        (call_script, "script_compute_village_recruits", ":cost_per_recruit"),
        (assign, ":recruits", reg0),
        (assign, ":troop_type", reg1),
        (try_begin),
            (eq, ":cost_per_recruit", -1),
            (assign, ":cost_per_recruit", reg2),
        (try_end),
        (assign, ":max_amount", reg5),

        (val_min, ":amount", ":max_amount"),

        (party_add_members, "p_main_party", ":troop_type", ":amount"),

        (store_sub, ":recruits_left", ":recruits", ":amount"),
        (party_set_slot, "$current_town", slot_center_volunteer_troop_amount, ":recruits_left"),

        (store_mul, ":cost", ":amount", ":cost_per_recruit"),
        (troop_remove_gold, "trp_player", ":cost"),

        (assign, reg0, ":amount"),
    ]),
]
