from source.header_operations import *
from source.header_common import *
from source.header_triggers import ti_on_order_issued, ti_on_item_wielded, \
    gk_toggle_weapon_mode
from source.header_items import itp_type_one_handed_wpn, itp_type_arrows, \
    ek_item_0, ek_head
from source.header_mission_templates import mordr_use_any_weapon, \
    mordr_use_blunt_weapons, wordr_use_blunt_weapons

from source.module_constants import *


common_ai_order_toggle = (ti_on_order_issued, 0, 0, [
    (store_trigger_param_1, ":order_no"),
    (this_or_next | eq, ":order_no", mordr_use_any_weapon),
    (eq, ":order_no", mordr_use_blunt_weapons),
    ], [
    (store_trigger_param_1, ":order_no"),
    (store_trigger_param_2, ":agent_id"),
    # probably the player
    (agent_get_team, ":team_id", ":agent_id"),

    (try_for_agents, ":agent_no"),
        (agent_is_active, ":agent_no"),
        (agent_is_human, ":agent_no"),
        (agent_is_non_player, ":agent_no"),
        (agent_is_alive, ":agent_no"),
        (agent_get_team, ":team_no", ":agent_no"),
        (eq, ":team_no", ":team_id"),

        (agent_get_class, ":class_no", ":agent_no"),
        (class_is_listening_order, ":team_no", ":class_no"),
        (agent_get_wielded_item, ":item_no", ":agent_no", 0),
        # (assign, reg10, ":agent_no"),
        # (str_store_agent_name, s1, ":agent_no"),
        # (try_begin),
        # (le, ":item_no", 0),
        # (str_store_string, s2, "@nothing"),
        # (else_try),
        # (str_store_item_name, s2, ":item_no"),
        # (try_end),
        # (str_store_string, s1, "@{reg10}:{s1} holding {s2}:"),
        # (try_for_range, ":item_slot", ek_item_0, ek_head),
        # (agent_get_item_slot, ":item_id", ":agent_no", ":item_slot"),
        # (gt, ":item_id", 0),
        # (neq, ":item_id", ":item_no"),
        # (str_store_item_name, s0, ":item_id"),
        # (str_store_string, s1, "@{s1}, {s0}"),
        # (try_end),
        # (display_message, s1),

        (gt, ":item_no", 0),
        (assign, ":swap_no", 0),

        # here we assume a weapon with alternate mode has been found already - it is rare that two item types will be equipped that can be swapped with different damage modes
        (try_begin),  # make use of the other item slots
            (eq, ":order_no", mordr_use_any_weapon),
            # just plain swapping
            (item_get_slot, ":swap_no", ":item_no", "slot_item_alternate"),
            (gt, ":swap_no", 1),
            (agent_unequip_item, ":agent_no", ":item_no"),
            (agent_equip_item, ":agent_no", ":swap_no"),
            (agent_set_wielded_item, ":agent_no", ":swap_no", 0),
            # (store_mission_timer_a, ":timer_a"),
            # (val_add, ":timer_a", 1000),
            # (agent_set_slot, ":agent_no", "slot_agent_last_weapon_toggled", ":timer_a"),
        (else_try),
            (eq, ":order_no", mordr_use_blunt_weapons),
            # switching to blunt modes only
            (neg | item_slot_ge, ":item_no", "slot_item_swing_damage", 513),
            # not already holding blunt
            # check inventory to see if weapon can be toggled
            (assign, ":end", ek_head),
            # (str_store_agent_name, s10, ":agent_no"),
            # (assign, reg10, ":agent_no"),
            # (str_store_string, s10, "@{reg10}={s10}:blunt"),
            (try_for_range, ":item_slot", ek_item_0, ":end"),
                (agent_get_item_slot, ":item_id", ":agent_no", ":item_slot"),
                (gt, ":item_id", 0),

                (item_get_type, ":item_itp", ":item_id"),
                (is_between, ":item_itp", itp_type_one_handed_wpn, itp_type_arrows),
                (neg | item_slot_ge, ":item_id", "slot_item_swing_damage", 513),
                # let engine set wielded
                # (str_store_item_name, s1, ":item_id"),
                # (item_get_slot, reg9, ":item_id", "slot_item_swing_damage"),
                # (str_store_string, s10, "@{s10},checking {s1} with {reg9} dmg"),
                (item_get_slot, ":swap_id", ":item_id", "slot_item_alternate"),
                (gt, ":swap_id", 1),
                # (str_store_string, s10, "@{s10} and alt"),

                (try_begin),
                    # (item_get_slot, ":damage", ":swap_id", "slot_item_swing_damage"),
                    # (gt, ":damage", 512),
                    (item_slot_ge, ":swap_id", "slot_item_swing_damage", 513),
                    (item_get_slot, ":damage", ":item_id", "slot_item_thrust_damage"),
                    (this_or_next | eq, ":damage", 0),
                    # no thrust capability
                    (this_or_next | eq, ":damage", 256),
                    # defined as (0, flag)
                    (gt, ":damage", 512),

                    # (assign, ":item_no", ":item_id"),
                    (assign, ":end", -1),
                    (agent_unequip_item, ":agent_no", ":item_id"),
                    (agent_equip_item, ":agent_no", ":swap_id"),
                    (agent_force_rethink, ":agent_no"),
                (try_end),
            (try_end),

            (try_begin),
                (eq, ":end", ek_head),
                (assign, ":swap_no", -1),
                (assign, ":item_no", -1),
                (assign, ":color", 0xFF0000),
                (display_message, "@{reg10}: switch to nothing", ":color"),
            (else_try),
                (item_get_slot, ":swap_no", ":item_no", "slot_item_alternate"),
                (assign, ":color", 0x00FF00),
                (str_store_item_name, s2, ":swap_no"),
                (display_message, "@{reg10}: switch to {s2}", ":color"),
            (try_end),
        (else_try),
            (assign, ":swap_no", 0),
        (try_end),

        (gt, ":item_no", 0),
        (gt, ":swap_no", 0),

        (agent_unequip_item, ":agent_no", ":item_no"),
        (agent_unequip_item, ":agent_no", ":swap_no"),
        (agent_equip_item, ":agent_no", ":swap_no"),
        # (agent_set_wielded_item, ":agent_no", ":swap_no"),
        (str_store_item_name, s3, ":item_no"),
        (str_store_item_name, s2, ":swap_no"),
        (str_store_agent_name, s1, ":agent_no"),
        (display_message, "@{reg10}:{s1} switching to {s2} from {s3}", ":color"),
        (agent_force_rethink, ":agent_no"),
    (try_end),
])

common_ai_sanity_check = (ti_on_item_wielded, 0, 0, [
    (store_trigger_param_2, ":item_no"),
    (eq, ":item_no", 0),
    ], [
    (store_trigger_param_1, ":agent_no"),
    # (str_store_agent_name, s11, ":agent_no"),
    # (assign, reg11, ":agent_no"),
    # (str_store_string, s11, "@{reg11}+{s11}"),
    # (try_for_range, ":item_slot", 0, ek_head),
    # (agent_get_item_slot, reg11, ":agent_no", ":item_slot"),
    # (str_store_string, s11, "@{s11}; {reg11}"),
    # (try_end),
    # (display_message, s11),
    (agent_unequip_item, ":agent_no", 0),
    (agent_force_rethink, ":agent_no"),
])

common_ai_random_toggle = (1, 0, 0, [], [
    (store_mission_timer_a, ":timer_a"),
    (try_for_agents, ":agent_no"),
        (assign, ":swap_no", -1),
        # check valid agent candidates
        (agent_is_active, ":agent_no"),
        (agent_is_human, ":agent_no"),
        (agent_is_non_player, ":agent_no"),
        (agent_is_alive, ":agent_no"),
        (agent_get_combat_state, ":cs", ":agent_no"),
        (this_or_next | eq, ":cs", 0),  # cs_free
        (this_or_next | eq, ":cs", 7),  # cs_still
        (eq, ":cs", 3),  # cs_wield

        (agent_get_team, ":agent_team", ":agent_no"),
        (agent_get_class, ":agent_class", ":agent_no"),
        # should probably cache this inside team slots
        (team_get_weapon_usage_order, ":order_no", ":agent_team", ":agent_class"),
        (neq, ":order_no", wordr_use_blunt_weapons),
        # check validity of weapon
        (agent_get_wielded_item, ":item_no", ":agent_no", 0),
        (gt, ":item_no", 1),
        (item_get_slot, ":swap_no", ":item_no", "slot_item_alternate"),

        (gt, ":swap_no", 1),
        (item_get_type, ":itp", ":item_no"),
        (is_between, ":itp", itp_type_one_handed_wpn, itp_type_arrows),
        # weapon mastery increases chance of toggling
        (agent_get_troop_id, ":troop_no", ":agent_no"),
        (store_skill_level, ":skill", "skl_weapon_master", ":troop_no"),
        (store_random_in_range, ":random_no", 0, 100),

        # most native troops do NOT have weapon mastery - adjust as needed
        (ge, ":skill", ":random_no"),

        (store_mission_timer_a, ":timer_a"),
        # check timing
        (agent_get_slot, ":last_switched", ":agent_no", "slot_agent_last_weapon_toggled"),
        (lt, ":last_switched", ":timer_a"),

        (store_sub, ":wpt", ":itp", 2),
        (store_proficiency_level, ":prof", ":troop_no", ":wpt"),
        (assign, reg9, ":prof"),
        # proficiency decreases time between toggle
        (val_mul, ":random_no", 8),  # from 0 to 160
        (val_add, ":random_no", 1600),  # delay
        (store_sub, ":prof", ":random_no", ":prof"),
        # between 1500 to 600 usually
        (val_div, ":prof", 80),  # between 12s to 7.5s

        # store timing
        (store_add, ":last_switched", ":timer_a", ":prof"),
        (agent_set_slot, ":agent_no", "slot_agent_last_weapon_toggled", ":last_switched"),

        # actual switching
        (agent_unequip_item, ":agent_no", ":item_no"),
        (agent_equip_item, ":agent_no", ":swap_no"),
        (agent_set_wielded_item, ":agent_no", ":swap_no"),

        # (assign, reg10, ":last_switched"),
        # (str_store_item_name, s3, ":item_no"),
        # (str_store_item_name, s2, ":swap_no"),
        # (str_store_agent_name, s1, ":agent_no"),
        # (display_message, "@{reg10}:{s1} with {reg9} wpx switching to {s2} from {s3}"),
    (try_end),
])

# side effects may include cleaning the weapon automatically, improper carry
# positions, and items not corresponding to stats when switched between
# trigger checks using native behaviour
common_player_toggle = (0, 0, 1, [
    (neg | main_hero_fallen),
    (game_key_clicked, gk_toggle_weapon_mode),
    (get_player_agent_no, "$g_player_agent"),
    (agent_get_wielded_item, ":item", "$g_player_agent", 0),
    (gt, ":item", 0),
    (item_slot_ge, ":item", "slot_item_alternate", 1),
    ], [
    (agent_get_wielded_item, ":item", "$g_player_agent", 0),
    (item_get_slot, ":alternate", ":item", "slot_item_alternate"),
    (gt, ":alternate", 1),
    (agent_unequip_item, "$g_player_agent", ":alternate"),
    (agent_unequip_item, "$g_player_agent", ":item"),
    (agent_equip_item, "$g_player_agent", ":alternate"),
    (agent_set_wielded_item, "$g_player_agent", ":alternate"),
])

common_wpn_swapping = [common_ai_order_toggle, common_ai_sanity_check,
                       common_player_toggle]
