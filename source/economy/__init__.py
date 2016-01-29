from source.header_operations import *
from source.header_common import *

from source.header_parties import ai_bhvr_travel_to_party, pf_default_behavior

from source.module_constants import *

from . import traders, production, population


scripts = [

  #script_do_party_center_trade
  # INPUT: arg1 = party_no, arg2 = center_no, arg3 = percentage_change_in_center
  # OUTPUT: reg0 = total_change
  # todo: clean this code.
  ("do_party_center_trade",
    [
      (store_script_param, ":party_no", 1),
      (store_script_param, ":center_no", 2),

      (try_begin),
        (gt, "$cheat_mode", 0),
        (str_store_party_name, s1, ":center_no"),
        (display_message, "@{!}DEBUG : {s1} is trading with villagers"),
      (try_end),

      (store_script_param, ":percentage_change", 3), #this should probably always be a constant. Currently it is 25.
      (assign, ":percentage_change", 30),
      ##diplomacy start+ chief
      (party_get_slot, ":origin", ":party_no", slot_party_last_traded_center),
      #If optional economic changes are enabled, reduce the percentage change in order
      #to make prices feel less static.
      (try_begin),
        (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),
        #Only apply lessened price movements to towns.
        (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
            (is_between, ":center_no", towns_begin, towns_end),
        #This halves the average impact as well as making it more variable.
        (val_add, ":percentage_change", 1),
        (store_random_in_range, ":percentage_change", 0, ":percentage_change"),
        #Display economics diagnostic
        (ge, "$cheat_mode", 3),
        (str_store_party_name, s3, ":origin"),
        (str_store_party_name, s4, ":center_no"),
        (assign, reg4, ":percentage_change"),
        (display_message, "@{!}DEBUG -- Trade from {s3} to {s4}: rolled random impact of {reg4}"),
      (try_end),
      ##diplomacy end+

      (party_get_slot, ":origin", ":party_no", slot_party_last_traded_center),
      (party_set_slot, ":party_no", slot_party_last_traded_center, ":center_no"),
      ##diplomacy start+
      #Update the record of trade route arrival times
      (try_begin),
         (ge, ":origin", centers_begin),
      (this_or_next|party_slot_eq, ":origin", villages_begin, villages_end),
         (is_between, ":origin", villages_begin, villages_end),
         (store_current_hours, ":cur_hours"),
         (party_set_slot, ":origin", dplmc_slot_village_trade_last_arrived_to_market, ":cur_hours"),
      (try_end),
      (try_begin),
         (ge, ":origin", centers_begin),
         (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_town),
            (is_between, ":center_no", towns_begin, towns_end),
         (store_current_hours, ":cur_hours"),
         (try_for_range, ":trade_route_slot", slot_town_trade_routes_begin, slot_town_trade_routes_end),
            (party_slot_eq,  ":center_no", ":trade_route_slot", ":origin"),
            (store_sub, ":trade_route_arrival_slot", ":trade_route_slot", slot_town_trade_routes_begin),
            (val_add, ":trade_route_arrival_slot", dplmc_slot_town_trade_route_last_arrivals_begin),
            (is_between, ":trade_route_arrival_slot", dplmc_slot_town_trade_route_last_arrivals_begin, dplmc_slot_town_trade_route_last_arrivals_end),#this will always be true unless a modder increased the number of trade route slots without increasing the number of last arrival slots
            (party_set_slot, ":center_no", ":trade_route_arrival_slot", ":cur_hours"),
         (try_end),
         (else_try),
            (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_village),
               (is_between, ":center_no", villages_begin, villages_end),
         (store_current_hours, ":cur_hours"),
         (party_set_slot, ":center_no", dplmc_slot_village_trade_last_returned_from_market, ":cur_hours"),
      (try_end),
      ##diplomacy end+

      (assign, ":total_change", 0),
      (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
      (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
        (store_add, ":cur_good_price_slot", ":cur_good", ":item_to_price_slot"),
        (party_get_slot, ":cur_merchant_price", ":party_no", ":cur_good_price_slot"),
        (party_get_slot, ":cur_center_price", ":center_no", ":cur_good_price_slot"),
        (store_sub, ":price_dif", ":cur_merchant_price", ":cur_center_price"),
        (assign, ":cur_change", ":price_dif"),
        (val_abs, ":cur_change"),
        (val_add, ":total_change", ":cur_change"),
        (val_mul, ":cur_change", ":percentage_change"),
        (val_div, ":cur_change", 100),

        #This is to reconvert from absolute value
        (try_begin),
          (lt, ":price_dif", 0),
          (val_mul, ":cur_change", -1),
        (try_end),

        (assign, ":initial_price", ":cur_center_price"),

        #The new price for the caravan or peasant is set before the change,
        # so the prices in the trading town have full effect on the next center
        (party_set_slot, ":party_no", ":cur_good_price_slot", ":cur_center_price"),

        (val_add, ":cur_center_price", ":cur_change"),
        (party_set_slot, ":center_no", ":cur_good_price_slot", ":cur_center_price"),

        (try_begin),
            (gt, "$cheat_mode", 0),
            (str_store_party_name, s3, ":origin"),
            (str_store_party_name, s4, ":center_no"),
            (str_store_item_name, s5, ":cur_good"),
            (assign, reg4, ":initial_price"),
            (assign, reg5, ":cur_center_price"),
            (display_log_message, "@{!}DEBUG -- Trade of {s5} from {s3} to {s4} brings price from {reg4} to {reg5}"),
        (try_end),
      (try_end),
      (assign, reg0, ":total_change"),
  ]),

  # script_create_village_farmer_party
  # Input: arg1 = village_no
  # Output: reg0 = party_no
  ("create_village_farmer_party",
   [(store_script_param, ":village_no", 1),
    (party_get_slot, ":town_no", ":village_no", slot_village_market_town),
    (store_faction_of_party, ":party_faction", ":town_no"),

    (try_begin),
        (is_between, ":town_no", towns_begin, towns_end),
        (set_spawn_radius, 0),
        (spawn_around_party, ":village_no", "pt_village_farmers"),
        (assign, ":new_party", reg0),

        (party_set_faction, ":new_party", ":party_faction"),
        (party_set_slot, ":new_party", slot_party_home_center, ":village_no"),
        (party_set_slot, ":new_party", slot_party_last_traded_center, ":village_no"),

        (party_set_slot, ":new_party", slot_party_type, spt_village_farmer),
        (party_set_slot, ":new_party", slot_party_ai_state, spai_trading_with_town),
        (party_set_slot, ":new_party", slot_party_ai_object, ":town_no"),
        (party_set_slot, ":new_party", slot_party_hired, 0),
        (party_set_ai_behavior, ":new_party", ai_bhvr_travel_to_party),
        (party_set_ai_object, ":new_party", ":town_no"),
        (party_set_flags, ":new_party", pf_default_behavior, 0),
        (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),

        # move goods from village to party
        (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
          (store_add, ":cur_good_price_slot", ":cur_goods", ":item_to_price_slot"),
          (party_get_slot, ":cur_village_price", ":village_no", ":cur_good_price_slot"),
          (party_set_slot, ":new_party", ":cur_good_price_slot", ":cur_village_price"),
        (try_end),

        (assign, reg0, ":new_party"),
    (try_end),

    ]),
]

simple_triggers = [
  # Troop AI: Village Farmer
  (1,
   [
       (store_time_of_day, ":oclock"),
       (is_between, ":oclock", 4, 15),
       (try_for_parties, ":party_no"),
         (party_slot_eq, ":party_no", slot_party_type, spt_village_farmer),
         # todo: why this? maybe to ease CPU usage?
         (store_random_in_range, reg0, 0, 20),
         (eq, reg0, 0),
         (party_is_in_any_town, ":party_no"),
         (party_get_slot, ":home_center", ":party_no", slot_party_home_center),
         (party_get_cur_town, ":cur_center", ":party_no"),

         (assign, ":can_leave", 1),
         (try_begin),
           (is_between, ":cur_center", walled_centers_begin, walled_centers_end),
           (this_or_next|party_slot_eq, ":cur_center", centro_bloqueado, 1),  # center blockaded (by player) OR
           (party_slot_ge, ":cur_center", slot_center_is_besieged_by, 1), # center besieged by someone else siege warfare
           (assign, ":can_leave", 0),
         (try_end),
         (eq, ":can_leave", 1),

         (try_begin),
           # Trade in his village
           (eq, ":cur_center", ":home_center"),

           (call_script, "script_do_party_center_trade", ":party_no", ":cur_center", 3),

           # when a town flips faction, the farmer also flips faction.
              # todo: check that this is not done in the flip faction script.
           (store_faction_of_party, ":cur_faction", ":cur_center"),
           (party_set_faction, ":party_no", ":cur_faction"),

           # Send farmer to town market
           (party_get_slot, ":market_town", ":cur_center", slot_village_market_town),
           (party_set_slot, ":party_no", slot_party_ai_object, ":market_town"),
           (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
           (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
           (party_set_ai_object, ":party_no", ":market_town"),
         (else_try),
           (try_begin),
             # Trade in town
             (party_get_slot, ":cur_ai_object", ":party_no", slot_party_ai_object),
             (eq, ":cur_center", ":cur_ai_object"),

             (call_script, "script_do_party_center_trade", ":party_no", ":cur_center", 3),
             (assign, ":total_change", reg0),

             ### Add tariffs, food, and prosperity
             (party_get_slot, ":accumulated_tariffs", ":cur_center", slot_center_accumulated_tariffs),
             (party_get_slot, ":prosperity", ":cur_center", slot_town_prosperity),

             (assign, ":tariffs_generated", ":total_change"),
             (val_mul, ":tariffs_generated", ":prosperity"),
             (val_div, ":tariffs_generated", 100),
             (val_div, ":tariffs_generated", 20), #10 for caravans, 20 for villages
             (val_add, ":accumulated_tariffs", ":tariffs_generated"),

             # no tariffs from infested villages
             # todo: why `:cur_center`? maybe it should be `:home_center`.
             (try_begin),
               (party_slot_ge, ":cur_center", slot_village_infested_by_bandits, 1),
               (assign,":accumulated_tariffs", 0),
             (try_end),

             (try_begin),
               (ge, "$cheat_mode", 3),
               (assign, reg4, ":tariffs_generated"),
               (str_store_party_name, s4, ":cur_center"),
               (assign, reg5, ":accumulated_tariffs"),
               (display_message, "@{!}New tariffs at {s4} = {reg4}, total = {reg5}"),
             (try_end),

             # Store accumulated tariffs
             (party_set_slot, ":cur_center", slot_center_accumulated_tariffs, ":accumulated_tariffs"),

             # Increase food stocks
             (party_get_slot, ":town_food_store", ":cur_center", slot_party_food_store),
             (call_script, "script_center_get_food_store_limit", ":cur_center"),
             (assign, ":food_store_limit", reg0),
             (val_add, ":town_food_store", 1000),
             (val_min, ":town_food_store", ":food_store_limit"),
             (party_set_slot, ":cur_center", slot_party_food_store, ":town_food_store"),

             # 5% chance to increase prosperity of village by 1
             (try_begin),
               (store_random_in_range, ":rand", 0, 100),
               (lt, ":rand", 5),
               (call_script, "script_change_center_prosperity", ":home_center", 1),
               (val_add, "$newglob_total_prosperity_from_village_trade", 1),
             (try_end),
           (try_end),

           # Send farmer to its home village
           (party_set_slot, ":party_no", slot_party_ai_object, ":home_center"),
           (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
           (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
           (party_set_ai_object, ":party_no", ":home_center"),
         (try_end),
       (try_end),
    ]),

  # Spawn village farmer parties
  (24,
   [
       (try_for_range, ":village_no", villages_begin, villages_end),
         (party_slot_eq, ":village_no", slot_village_state, svs_normal),
         (party_get_slot, ":farmer_party", ":village_no", slot_village_farmer_party),
         (this_or_next|eq, ":farmer_party", 0),
         (neg|party_is_active, ":farmer_party"),
         (store_random_in_range, ":random_no", 0, 100),
         (lt, ":random_no", 60), # 60% changes of being created
         (call_script, "script_create_village_farmer_party", ":village_no"),
         (party_set_slot, ":village_no", slot_village_farmer_party, reg0),
         (try_begin),
           (gt, "$cheat_mode", 0),
           (store_time_of_day, ":cur_hour"),
           (assign, reg9, ":cur_hour"),
           (str_store_party_name, s1, ":village_no"),
           (display_message, "@{!}DEBUG Village farmers created at {s1}at {reg0} at {reg9} ."),
         (try_end),
       (try_end),
    ]),
]

scripts += traders.scripts + production.scripts + population.scripts

simple_triggers += traders.simple_triggers + production.simple_triggers + \
                   population.simple_triggers \
