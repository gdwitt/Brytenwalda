from source.header_operations import *
from source.header_common import *

from source.module_constants import slot_town_lord, slot_center_volunteer_troop_amount


menus = [

    ("force_recruit", 0,
     "Your men taken from their homes by force all villagers.", "none", [
        (call_script, "script_party_count_members_with_full_health", "p_main_party"),
        (assign, ":player_party_size", reg0),
        (call_script, "script_party_count_members_with_full_health", "$current_town"),
        (assign, ":villagers_party_size", reg0),

        (try_begin),
            # todo: this does not make sense as village wins for sure.
            (lt, ":player_party_size", 6),
            (ge, ":villagers_party_size", 40),
            (neg | party_slot_eq, "$current_town", slot_town_lord, "trp_player"),
            (jump_to_menu, "mnu_village_start_attack"),
        (try_end),
        ], [
            ("let_them_keep_it", [], "Continue",
                [(jump_to_menu, "mnu_force_recruit_decision")
        ]),
    ]),

    ("force_recruit_decision", 0, "{s18}", "none", [

        (try_begin),
            (eq, reg0, 0),
            (str_store_string, s18, "@Others Lords have gone through here, "
                                    "there are only old people and children."),
        (else_try),
            (str_store_troop_name_by_count, s3, reg1, reg0),
            (try_begin),
                (eq, reg5, 1),
                (str_store_string, s18, "@One {s3} will join you reluctantly."),
            (else_try),
                (str_store_string, s18, "@{reg5} {s3} will join you reluctantly."),
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
            ], "Recruit them all ({reg6} scillingas).", [
                (call_script, "script_change_player_honor", -5),
                (call_script, "script_change_player_party_morale", -5),
                (call_script, "script_change_player_relation_with_center", "$current_town", -10),
                (call_script, "script_village_recruit_volunteers", reg5, 1),
                (jump_to_menu, "mnu_village"),
        ]),

        ("forget_it", [
            (ge, reg5, 1),
            ], "Forget it.", [
                (jump_to_menu, "mnu_village"),
        ]),
    ]),
]
