from source.header_operations import *
from source.header_common import *
from source.header_triggers import *

from source.module_constants import *


################from flail osp gdw
flail_trigger = (
    0, 0, 0, [
    (neg|multiplayer_is_dedicated_server),],
        [
            (try_for_agents, ":agent_no"),
                (agent_is_active, ":agent_no"),
                (agent_is_alive, ":agent_no"),
                (agent_slot_eq, ":agent_no", slot_agent_flail_using, 1),
                (agent_get_wielded_item, ":wielded_weapon", ":agent_no", 0),
                (try_begin),
                    (this_or_next|eq, ":wielded_weapon", "itm_flail1_blunt"),
                    (this_or_next|eq, ":wielded_weapon", "itm_flail2_blunt"),
                    (eq, ":wielded_weapon", "itm_flailsteel_blunt"),
                    (agent_get_wielded_item_slot_no, ":slot_no", ":agent_no"),
                    (val_add, ":slot_no", bmm_item_1),
                    (agent_get_animation, ":upper_anim", ":agent_no", 1),
                    (try_begin),
                        (this_or_next|eq, ":upper_anim", "anim_release_slashright_onehanded"),
                        (this_or_next|eq, ":upper_anim", "anim_release_slashright_onehanded_continue"),
                        #(this_or_next|eq, ":upper_anim", "anim_release_slashleft_onehanded_continue"),
                        (this_or_next|eq, ":upper_anim", "anim_release_slashleft_onehanded"),
                        (this_or_next|eq, ":upper_anim", "anim_release_overswing_onehanded"),
                        (this_or_next|eq, ":upper_anim", "anim_release_slash_horseback_right"),
                        (eq, ":upper_anim", "anim_release_slash_horseback_left"),

                        (agent_get_animation_progress, ":animation_progress", ":agent_no", 1),
                        (store_mul, ":vertex_animation_time", 55, ":animation_progress"),
                        (val_div, ":vertex_animation_time", 100),
                        (val_add, ":vertex_animation_time", 10),
                        (agent_body_meta_mesh_set_vertex_keys_time_point, ":agent_no", ":slot_no", ":vertex_animation_time"),
                    (else_try),
                        (agent_body_meta_mesh_set_vertex_keys_time_point, ":agent_no", ":slot_no", 65),
                        (agent_set_slot, ":agent_no", slot_agent_flail_using, 0),
                    (try_end),
                (else_try),
                    (agent_set_slot, ":agent_no", slot_agent_flail_using, 0),
                (try_end),
            (try_end),
        ])

flail_wielding_trigger = (
    ti_on_item_wielded, 0, 0, [
    (neg|multiplayer_is_dedicated_server),],
    [
        (store_trigger_param_1, ":agent_no"),
        (store_trigger_param_2, ":item_no"),
        #(eq, ":item_no", "itm_flail"),
        (this_or_next|eq, ":item_no", "itm_flail1_blunt"),
        (this_or_next|eq, ":item_no", "itm_flail2_blunt"),
        (eq, ":item_no", "itm_flailsteel_blunt"),
        (agent_get_bone_position,pos1,":agent_no",hb_item_r, 1),##this was used for 1st flail pack -multiplayer
        #(play_sound_at_position, "snd_draw_flail", pos1),
        (agent_play_sound, ":agent_no", "snd_draw_flail"),
    ])

flail_triggers = [flail_trigger, flail_wielding_trigger]