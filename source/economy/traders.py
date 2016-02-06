from source.header_operations import *
from source.header_common import reg0, reg6

from source.header_items import *

from source.module_constants import *


simple_triggers = [
    # Refresh traders inventories
    # the times are different to avoid calling all at once.
    (24*7,
     [
         (call_script, "script_refresh_center_stables"),
         (call_script, "script_refresh_special_merchants"),
         (call_script, "script_cf_refresh_bandit_merchants"),
     ]),
    (24*7 + 1,
    [
        (try_for_range, ":village_no", villages_begin, villages_end),
           (call_script, "script_refresh_village_merchant_inventory", ":village_no"),
        (try_end),
    ]),
    (24*7 + 2,
    [
        (call_script, "script_refresh_center_inventories"),
        (call_script, "script_refresh_center_armories"),
        (call_script, "script_refresh_center_weaponsmiths"),
    ]),
]


scripts = [
  # script_refresh_village_merchant_inventory
  # Input: arg1 = village_no
  # Output: none
  ("refresh_village_merchant_inventory",
    [
      (store_script_param_1, ":village_no"),
      (party_get_slot, ":merchant_troop", ":village_no", "slot_town_elder"),
      (reset_item_probabilities,0),

      (party_get_slot, ":bound_center", ":village_no", "slot_village_bound_center"),

      (assign, ":total_probability", 0),
      (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),        
        (call_script, "script_center_get_production", ":village_no", ":cur_good"),
        (assign, ":cur_probability", reg0),

        (call_script, "script_center_get_production", ":bound_center", ":cur_good"),
        (val_div, reg0, 4), #also add 1/5 of bound center production to village's #inventory.gdw from 5 increase vill inv
        (val_add, ":cur_probability", reg0),

        (val_max, ":cur_probability", 5),            
        (val_add, ":total_probability", ":cur_probability"),
      (try_end),
      
      (try_begin),
        (party_get_slot, ":prosperity", ":village_no", "slot_town_prosperity"),
        (val_div, ":prosperity", 15), #up to 6
        (store_add, ":number_of_items_in_village", ":prosperity", 1),
      (try_end),

      (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
        (call_script, "script_center_get_production", ":village_no", ":cur_good"),
        (assign, ":cur_probability", reg0),

        (call_script, "script_center_get_production", ":bound_center", ":cur_good"),
        (val_div, reg0, 4), #also add 1/5 of bound center production to village's inventory.gdw
        (val_add, ":cur_probability", reg0),

        (val_max, ":cur_probability", 5),
        (val_mul, ":cur_probability", ":number_of_items_in_village"),
        (val_mul, ":cur_probability", 100),
        (val_div, ":cur_probability", ":total_probability"),

        (set_item_probability_in_merchandise, ":cur_good", ":cur_probability"),
      (try_end),

      (troop_clear_inventory, ":merchant_troop"),
      (troop_add_merchandise, ":merchant_troop", itp_type_goods, ":number_of_items_in_village"),
      (troop_ensure_inventory_space, ":merchant_troop", 80),

      #Adding 1 prosperity to the village while reducing each 3000 gold from the elder
      (store_troop_gold, ":gold", ":merchant_troop"),

      # todo: move this code to a property update script
      (try_begin),
        (gt, ":gold", 3500),
        (store_div, ":prosperity_added", ":gold", 3000),
        (store_mul, ":gold_removed", ":prosperity_added", 3000),
        (troop_remove_gold, ":merchant_troop", ":gold_removed"),
        (call_script, "script_change_center_prosperity", ":village_no", ":prosperity_added"),
      (try_end),
  ]),

  # script_refresh_center_inventories
  ("refresh_center_inventories",
  [
    (set_merchandise_modifier_quality,150),
    (reset_item_probabilities,100),

    # Add trade goods to merchant inventories
    (try_for_range,":cur_center",towns_begin, towns_end),
      (party_get_slot,":cur_merchant",":cur_center","slot_town_merchant"),
      (reset_item_probabilities,100),
      (assign, ":total_production", 0),
      (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
        (call_script, "script_center_get_production", ":cur_center", ":cur_goods"),
        (assign, ":cur_production", reg0),

        (try_for_range, ":cur_village", villages_begin, villages_end),
          (party_slot_eq, ":cur_village", "slot_village_bound_center", ":cur_center"),
          (call_script, "script_center_get_production", ":cur_village", ":cur_goods"),
          (val_div, reg0, 3),
          (val_add, ":cur_production", reg0),
        (try_end),

        (val_max, ":cur_production", 1),
        (val_mul, ":cur_production", 4),

        (val_add, ":total_production", ":cur_production"),
      (try_end),

      (party_get_slot, ":town_prosperity", ":cur_center", "slot_town_prosperity"),
      (assign, ":number_of_items_in_town", 25),

      (try_begin), #1.0x - 2.0x (50 - 100 prosperity)
        (ge, ":town_prosperity", 50),
        (store_sub, ":ratio", ":town_prosperity", 50),
        (val_mul, ":ratio", 2),
        (val_add, ":ratio", 100),
        (val_mul, ":number_of_items_in_town", ":ratio"),
        (val_div, ":number_of_items_in_town", 100),
      (else_try), #0.5x - 1.0x (0 - 50 prosperity)
        (store_sub, ":ratio", ":town_prosperity", 50),
        (val_add, ":ratio", 100),
        (val_mul, ":number_of_items_in_town", ":ratio"),
        (val_div, ":number_of_items_in_town", 100),
      (try_end),

      (val_clamp, ":number_of_items_in_town", 10, 40),

      (try_begin),
        (is_between, ":cur_center", castles_begin, castles_end),
        (val_div, ":number_of_items_in_town", 2),
      (try_end),

      (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
        (call_script, "script_center_get_production", ":cur_center", ":cur_goods"),
        (assign, ":cur_production", reg0),

        (try_for_range, ":cur_village", villages_begin, villages_end),
          (party_slot_eq, ":cur_village", "slot_village_bound_center", ":cur_center"),
          (call_script, "script_center_get_production", ":cur_village", ":cur_goods"),
          (val_div, reg0, 3),
          (val_add, ":cur_production", reg0),
        (try_end),

        (val_max, ":cur_production", 1),
        (val_mul, ":cur_production", 4),

        (val_mul, ":cur_production", ":number_of_items_in_town"),
        (val_mul, ":cur_production", 100),
        (val_div, ":cur_production", ":total_production"),
        (set_item_probability_in_merchandise, ":cur_goods", ":cur_production"),
      (try_end),

      (troop_clear_inventory, ":cur_merchant"),
      (troop_add_merchandise, ":cur_merchant", itp_type_goods, ":number_of_items_in_town"),

      (troop_ensure_inventory_space, ":cur_merchant", 20),
      (troop_sort_inventory, ":cur_merchant"),
      (store_troop_gold, ":cur_gold", ":cur_merchant"),
      (lt, ":cur_gold", 1700),#gdw
      (store_random_in_range,":new_gold", 2300, 3300),
      (call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
    (try_end),
  ]),

  # script_refresh_center_armories
  ("refresh_center_armories",
  [
    (reset_item_probabilities, 100),
    (set_merchandise_modifier_quality, 140),
    (try_for_range, ":cur_merchant", armor_merchants_begin, armor_merchants_end),
      (store_sub, ":cur_town", ":cur_merchant", armor_merchants_begin),
      (val_add, ":cur_town", towns_begin),
      (troop_clear_inventory, ":cur_merchant"),
      (party_get_slot, ":cur_faction", ":cur_town", "slot_center_original_faction"),
      (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_body_armor, 17),#gdw
      (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_head_armor, 16),
      (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_foot_armor, 7),#gdw
      (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_hand_armor, 4),#gdw
      (troop_ensure_inventory_space, ":cur_merchant", merchant_inventory_space),
      (troop_sort_inventory, ":cur_merchant"),
      (store_troop_gold, reg6, ":cur_merchant"),
      (lt, reg6, 1400),#gdw
                        (store_random_in_range,":new_gold",1300,2300), #oro inicial chief cambiado#gdw
      (call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
    (end_try),
  ]),

  # script_refresh_center_weaponsmiths
  ("refresh_center_weaponsmiths",
  [
    (reset_item_probabilities, 100),
    (set_merchandise_modifier_quality, 140),
    (try_for_range, ":cur_merchant", weapon_merchants_begin, weapon_merchants_end),
      (store_sub, ":cur_town", ":cur_merchant", weapon_merchants_begin),
      (val_add, ":cur_town", towns_begin),
      (troop_clear_inventory, ":cur_merchant"),
      (party_get_slot, ":cur_faction", ":cur_town", "slot_center_original_faction"),
      (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_one_handed_wpn, 6),
      (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_two_handed_wpn, 6),
      (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_polearm, 5),
      (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_shield, 5),
      (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_bow, 3),
      (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_crossbow, 3),
      (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_thrown, 5),
      (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_arrows, 2),
      (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_bolts, 2),
      (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_pistol,1),
      (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_bullets,1),
      (troop_ensure_inventory_space, ":cur_merchant", merchant_inventory_space),
      (troop_sort_inventory, ":cur_merchant"),
      (store_troop_gold, reg6, ":cur_merchant"),
      (lt, reg6, 1500),
      (store_random_in_range,":new_gold", 1300, 2300),
      (call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
    (try_end),
  ]),

  # script_refresh_center_stables
  ("refresh_center_stables",
  [
    (reset_item_probabilities, 100),
    (set_merchandise_modifier_quality, 150),
    (try_for_range, ":cur_merchant", horse_merchants_begin, horse_merchants_end),
      (troop_clear_inventory, ":cur_merchant"),
      (store_sub, ":cur_town", ":cur_merchant", horse_merchants_begin),
      (val_add, ":cur_town", towns_begin),
      (party_get_slot, ":cur_faction", ":cur_town", "slot_center_original_faction"),
      (troop_add_merchandise_with_faction, ":cur_merchant", ":cur_faction", itp_type_horse, 9),
      (troop_ensure_inventory_space, ":cur_merchant", 65),
      (troop_sort_inventory, ":cur_merchant"),
      (store_troop_gold, ":cur_gold", ":cur_merchant"),
      (lt, ":cur_gold", 1200),#gdw
                        (store_random_in_range,":new_gold",1400,2400), #oro inicial chief cambiado#gdw
      (call_script, "script_troop_add_gold", ":cur_merchant", ":new_gold"),
    (try_end),
  ]),

  ("refresh_special_merchants",
  [
    (reset_item_probabilities, 100),
    (set_merchandise_modifier_quality, 230),

    (troop_clear_inventory, "trp_specialmerch1"),
    (troop_add_items, "trp_specialmerch1", "itm_noblearmor11res",2),
    (troop_add_items, "trp_specialmerch1", "itm_noblearmor14res",1),
    (troop_add_items, "trp_specialmerch1", "itm_noblearmor15res",1),
    (troop_add_items, "trp_specialmerch1", "itm_noblearmor18res",1),
    (troop_add_items, "trp_specialmerch1", "itm_saxonhelmt4face",1),
    (troop_add_items, "trp_specialmerch1_chest", "itm_noblearmor1res", 4),
    (troop_add_items, "trp_specialmerch1", "itm_flailsteel_blunt", 1),

    (troop_clear_inventory, "trp_specialmerch2"),
    (troop_add_items, "trp_specialmerch2", "itm_longmail_coat_kingred",1),
    (troop_add_items, "trp_specialmerch2", "itm_noblearmor8res", 1),
    (troop_add_items, "trp_specialmerch2", "itm_goat_nobleman_helm", 1),
    (troop_add_items, "trp_specialmerch2", "itm_resanglehelmet_gold",1),
    (troop_add_items, "trp_specialmerch2", "itm_noblearmor21res",1),
    (troop_add_items, "trp_specialmerch2", "itm_flailsteel_blunt", 1),

    (troop_clear_inventory, "trp_specialmerch3"),
    (troop_add_items, "trp_specialmerch3", "itm_noblearmor9res",1),
    (troop_add_items, "trp_specialmerch3", "itm_noblearmor1res",1),
    (troop_add_items, "trp_specialmerch3", "itm_noblearmor5res",1),##5 is purple lightscalar
    (troop_add_items, "trp_specialmerch3", "itm_noblearmor7res",1),
    (troop_add_items, "trp_specialmerch3", "itm_szpadelhelm5engravedt3",1),
    (troop_add_items, "trp_specialmerch3", "itm_flailsteel_blunt", 1),

    (troop_clear_inventory, "trp_specialmerch4"),
    (troop_add_items, "trp_specialmerch4", "itm_noblearmor16res",1),
    (troop_add_items, "trp_specialmerch4", "itm_scale_greyvestelite",1),
    (troop_add_items, "trp_specialmerch4", "itm_scale_greykhergitfemale",1),
    (troop_add_items, "trp_specialmerch4", "itm_scale_greywhitefemale",1),
    (troop_add_items, "trp_specialmerch4", "itm_noblearmor24res",1),
    (troop_add_items, "trp_specialmerch4", "itm_black_nordichelmwboar",1),
    (troop_add_items, "trp_specialmerch4", "itm_flailsteel_blunt", 1),

    (troop_clear_inventory, "trp_specialmerch5"),
    (troop_add_items, "trp_specialmerch5", "itm_noblearmor4res", 1),#pengwern
    (troop_add_items, "trp_specialmerch5", "itm_noblearmor6res", 1),
    (troop_add_items, "trp_specialmerch5", "itm_noblearmor13res", 1),
    (troop_add_items, "trp_specialmerch5", "itm_noblemanshirt1", 1),
    (troop_add_items, "trp_specialmerch5", "itm_scale_goldlongtunicwcape", 1),
    (troop_add_items, "trp_specialmerch5", "itm_helmbascinet_boar", 1),
    (troop_add_items, "trp_specialmerch5", "itm_flailsteel_blunt", 1),

    (troop_clear_inventory, "trp_specialmerch6"),
    (troop_add_items, "trp_specialmerch6", "itm_noblearmor7res", 1),
    (troop_add_items, "trp_specialmerch6", "itm_noblearmor2res", 1),
    (troop_add_items, "trp_specialmerch6", "itm_noblearmor5res", 1),
    (troop_add_items, "trp_specialmerch6", "itm_noblearmor10res", 1),
    (troop_add_items, "trp_specialmerch6", "itm_noblearmor23res",1),
    (troop_add_items, "trp_specialmerch6", "itm_szpadelhelmnoble", 1),
    (troop_add_items, "trp_specialmerch6", "itm_flailsteel_blunt", 1),

    (troop_clear_inventory, "trp_specialmerch7"),##ireland
    (troop_add_items, "trp_specialmerch7", "itm_noblearmor3res", 1),
    (troop_add_items, "trp_specialmerch7", "itm_noblearmor12res", 1),
    (troop_add_items, "trp_specialmerch7", "itm_noblearmor22res", 1),
    (troop_add_items, "trp_specialmerch7", "itm_noblemanshirt2", 1),
    (troop_add_items, "trp_specialmerch7", "itm_longmail_coat_king1", 1),
    (troop_add_items, "trp_specialmerch7", "itm_flailsteel_blunt", 1),
  ]),

  ("cf_refresh_bandit_merchants",
  [
    (reset_item_probabilities, 100),
    (set_merchandise_modifier_quality, 100),
      (troop_clear_inventory, "trp_brigand_hideout_merchant"),
      (troop_add_merchandise_with_faction, "trp_brigand_hideout_merchant", "fac_outlaws", itp_type_one_handed_wpn, 5),
      (troop_add_merchandise_with_faction, "trp_brigand_hideout_merchant", "fac_outlaws", itp_type_two_handed_wpn, 5),
      (troop_add_merchandise_with_faction, "trp_brigand_hideout_merchant", "fac_outlaws", itp_type_polearm, 5),
      (troop_add_merchandise_with_faction, "trp_brigand_hideout_merchant", "fac_outlaws", itp_type_shield, 6),
      (troop_add_merchandise_with_faction, "trp_brigand_hideout_merchant", "fac_outlaws", itp_type_bow, 4),
      (troop_add_merchandise_with_faction, "trp_brigand_hideout_merchant", "fac_outlaws", itp_type_crossbow, 1),
      (troop_add_merchandise_with_faction, "trp_brigand_hideout_merchant", "fac_outlaws", itp_type_thrown, 5),
      (troop_add_merchandise_with_faction, "trp_brigand_hideout_merchant", "fac_outlaws", itp_type_arrows, 2),
      (troop_add_merchandise_with_faction, "trp_brigand_hideout_merchant", "fac_outlaws", itp_type_bolts, 1),
      (troop_add_merchandise_with_faction, "trp_brigand_hideout_merchant", "fac_outlaws", itp_type_pistol,1),
      (troop_add_merchandise_with_faction, "trp_brigand_hideout_merchant", "fac_outlaws", itp_type_bullets,1),
      (troop_add_merchandise_with_faction, "trp_brigand_hideout_merchant", "fac_outlaws", itp_type_body_armor, 6),
      (troop_add_merchandise_with_faction, "trp_brigand_hideout_merchant", "fac_outlaws", itp_type_head_armor, 6),
      (troop_add_merchandise_with_faction, "trp_brigand_hideout_merchant", "fac_outlaws", itp_type_foot_armor, 6),
      (troop_add_merchandise_with_faction, "trp_brigand_hideout_merchant", "fac_outlaws", itp_type_hand_armor, 3),
      (troop_add_merchandise_with_faction, "trp_brigand_hideout_merchant", "fac_outlaws", itp_type_horse, 5),
      (troop_add_merchandise_with_faction, "trp_brigand_hideout_merchant", "fac_outlaws", itp_type_goods, 5),
      (troop_sort_inventory, "trp_brigand_hideout_merchant"),
      (store_troop_gold, reg6, "trp_brigand_hideout_merchant"),
      (lt, reg6, 1000),
      (store_random_in_range,":new_gold",1000,2000), #oro inicial chief cambiado
      (call_script, "script_troop_add_gold", "trp_brigand_hideout_merchant", ":new_gold"),
  ]),

]