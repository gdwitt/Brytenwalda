from ..module_constants import *
from ..header_parties import *
from ..header_mission_templates import *
from ..header_map_icons import *


scripts = [
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
