from source.header_operations import *
from source.header_common import *
from source.header_items import itp_type_one_handed_wpn, itp_type_polearm, \
    itp_type_two_handed_wpn, ek_item_0, ek_head
from source.header_item_modifiers import *


#chief Brytenwalda -Baron Conrad script- armas se rompen
common_weapon_break = (0.4, 0, 0, [(eq, "$g_weapon_breaking", 0)], [
   (try_for_agents, ":agent_id"),
       (agent_get_attack_action, reg0, ":agent_id"),
       (eq,reg0,3),    #completing attack
#Cruger MODIFICATION BEGIN----------------------------------------------------------------------------
       #break only if agent has another weapon to use

       (assign, ":num_agent_items", 0),

       (try_for_range, ":item_slot", ek_item_0, ek_head),
           (agent_get_item_slot,  ":item", ":agent_id", ":item_slot"),

           (gt, ":item", "itm_no_item"),
           (item_get_type, reg0, ":item"),
           (this_or_next|eq,itp_type_one_handed_wpn,reg0),
           (this_or_next|eq,itp_type_two_handed_wpn,reg0),
           (eq,itp_type_polearm,reg0),

           (val_add, ":num_agent_items", 1),
       (try_end),

       (ge, ":num_agent_items", 2),
#Cruger MODIFICATION END------------------------------------------------------------------------------

       (agent_get_wielded_item,":breakweapon",":agent_id",0),
       (gt,":breakweapon", "itm_no_item"),

       (item_get_type, ":weapontype", ":breakweapon"),

       (store_random_in_range,":weaponbreakchance",1,100),
       (try_begin),

           (eq,itp_type_polearm,":weapontype"),
           #       (display_message, "@Polearm"),

           (val_mul,":weaponbreakchance",1.01),
       # (else_try),
           # (eq,itp_type_two_handed_wpn,":weapontype"),
           # #       (display_message, "@2 hander"),
           # (val_mul,":weaponbreakchance",1),
       # (else_try),
           # (eq,itp_type_one_handed_wpn,":weapontype"),

           # #       (display_message, "@1 hander"),
           # (val_mul,":weaponbreakchance",1),
       (try_end),


       (agent_get_horse,":agent_mounted",":agent_id"),
       (try_begin),
           (ge,":agent_mounted",0),
           #      (display_message, "@Mounted."),
           (val_mul,":weaponbreakchance",1.01),

           (eq,itp_type_polearm,":weapontype"),

           (val_mul,":weaponbreakchance",1.03),

       (try_end),

#--Cabadrin imod Quality Modifier

       (agent_get_troop_id, ":troop_id", ":agent_id"),
       (try_begin),    #only heroes have item modifications
           (troop_is_hero, ":troop_id"),
           (try_for_range, ":item_slot", ek_item_0, ek_head),    # heroes have only 4 possible weapons (equipped)
               (troop_get_inventory_slot, reg0, ":troop_id", ":item_slot"),  #Find Item Slot with same item ID as Equipped Weapon
               (eq, reg0, ":breakweapon"),
               (troop_get_inventory_slot_modifier, ":imod", ":troop_id", ":item_slot"),
           (try_end),
       (else_try),
           (assign, ":imod", imodbit_plain),
       (try_end),

   #Better than Average
       (try_begin),
           # (eq, imodbit_masterwork, ":imod"),

           # (val_mul,":weaponbreakchance",1),
       # (else_try),
           (eq, imodbit_tempered, ":imod"),
           (val_mul,":weaponbreakchance",1.01),
       (else_try),
           (eq, imodbit_balanced, ":imod"),
           (val_mul,":weaponbreakchance",1.02),
       (else_try),
           (eq, imodbit_heavy, ":imod"),
           (val_mul,":weaponbreakchance",1.03),
       (else_try),
           (eq, imodbit_plain, ":imod"),
           (val_mul,":weaponbreakchance",1.04),
   #Worse than Average
       (else_try),
           (eq, imodbit_bent, ":imod"),
           (val_mul,":weaponbreakchance",1.06),
       (else_try),
           (eq, imodbit_rusty, ":imod"),
           (val_mul,":weaponbreakchance",1.08),
       (else_try),
           (eq, imodbit_chipped, ":imod"),
           (val_mul,":weaponbreakchance",1.11),
       (else_try),
           (eq, imodbit_cracked, ":imod"),
           (val_mul,":weaponbreakchance",1.13),
       (try_end),
       # (assign, reg8, ":weaponbreakchance"),

       # (display_message, "@{reg8}"),
#--End imod Quality Modifier
       (try_begin),
           (ge,":weaponbreakchance",99), #chief cambiado#gdw99

           (agent_unequip_item,":agent_id",":breakweapon"),
#Cruger MODIFICATION BEGIN----------------------------------------------------------------------------
           (get_player_agent_no, ":player_agent_id"),
           (try_begin),
               (eq, ":agent_id", ":player_agent_id"),

               (play_sound,"snd_shield_broken",),

               (display_message, "@Hah! Your weapon broke. This can not be repaired until the end of the battle"),
           (try_end),
#Cruger MODIFICATION END------------------------------------------------------------------------------

           (lt,":agent_mounted",0),
           (agent_set_animation, ":agent_id", "anim_strike_chest_front"),
       (try_end),
   (try_end),
])
