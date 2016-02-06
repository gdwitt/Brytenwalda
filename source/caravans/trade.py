from ..header_operations import *
from ..header_common import *
from ..header_parties import ai_bhvr_travel_to_party, ai_bhvr_travel_to_point, \
    pf_default_behavior

from ..module_constants import *


simple_triggers = [
  # Troop AI: Caravans
  (8, [
       (try_for_parties, ":party_no"),
         # It is a land trader and it is in town.
         (party_slot_eq, ":party_no", "slot_party_type", spt_kingdom_caravan),
         (party_is_in_any_town, ":party_no"),

         (store_faction_of_party, ":merchant_faction", ":party_no"),
         (faction_get_slot, ":num_towns", ":merchant_faction", "slot_faction_num_towns"),

         (try_begin),
           # remove merchant if faction has no towns
           (le, ":num_towns", 0),
           (remove_party, ":party_no"),
         (else_try),
           (party_get_cur_town, ":cur_center", ":party_no"),

           (assign, ":tariff_succeed_limit", 45),
           (try_begin),
             # player tariffs depend on difficulty.
             (party_slot_eq, ":cur_center", "slot_town_lord", "trp_player"),

             (options_get_campaign_ai, ":reduce_campaign_ai"),
             (try_begin),
               # hard (less money)
               (eq, ":reduce_campaign_ai", 0),
               (assign, ":tariff_succeed_limit", 35),
             (else_try),
               # medium (normal money)
               (eq, ":reduce_campaign_ai", 1),
               (assign, ":tariff_succeed_limit", 45),
             (else_try),
               # easy (more money)
               (eq, ":reduce_campaign_ai", 2),
               (assign, ":tariff_succeed_limit", 60),
             (try_end),
           (try_end),

           # don't trade if below tariff_succeed_limit
           # todo: why such hard constraint?
           (store_random_in_range, ":random_no", 0, 100),
           (lt, ":random_no", ":tariff_succeed_limit"),

           # If town is besieged, don't trade nor leave town.
           (assign, ":can_leave", 1),
           (try_begin),
             (is_between, ":cur_center", walled_centers_begin, walled_centers_end),
             (neg|party_slot_eq, ":cur_center", "slot_center_is_besieged_by", -1),
             (assign, ":can_leave", 0),
           (try_end),
           (eq, ":can_leave", 1),

           # only trade if it is in correct state and town.
           (assign, ":do_trade", 0),
           (try_begin),
             (party_get_slot, ":cur_ai_state", ":party_no", "slot_party_ai_state"),
             (eq, ":cur_ai_state", spai_trading_with_town),
             (party_get_slot, ":cur_ai_object", ":party_no", "slot_party_ai_object"),
             (eq, ":cur_center", ":cur_ai_object"),
             (assign, ":do_trade", 1),
           (try_end),

           # select next location to travel to.
           (assign, ":target_center", -1),
           (try_begin),
             # Make sure that when the caravan is escorted by the player,
             # it continues to the original destination.
             (eq, "$caravan_escort_party_id", ":party_no"),
             (neg|party_is_in_town, ":party_no", "$caravan_escort_destination_town"),
             (assign, ":target_center", "$caravan_escort_destination_town"),
           (else_try),
             # else, get best new town.
             (call_script, "script_cf_select_most_profitable_town_at_peace_with_faction_in_trade_route", ":cur_center", ":merchant_faction"),
             (assign, ":target_center", reg0),
           (try_end),
           # abort if no new target town found or next town is this town.
           (is_between, ":target_center", towns_begin, towns_end),
           (neg|party_is_in_town, ":party_no", ":target_center"),

           # and finally, TRADE!
           (try_begin),
             (eq, ":do_trade", 1),
             (str_store_party_name, s7, ":cur_center"),
             (call_script, "script_do_merchant_town_trade", ":party_no", ":cur_center"),
           (try_end),

           # travel to next location.
           (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
           (party_set_ai_object, ":party_no", ":target_center"),
           (party_set_flags, ":party_no", pf_default_behavior, 0),
           (party_set_slot, ":party_no", "slot_party_ai_state", spai_trading_with_town),
           (party_set_slot, ":party_no", "slot_party_ai_object", ":target_center"),

        (else_try),
         # todo: refactor this part as it is an almost copy of the previous try.
         (party_slot_eq, ":party_no", "slot_party_type", spt_merchant_caravan),
         (get_party_ai_object, ":object_town", ":party_no"),
         (party_slot_ge, ":object_town", "slot_town_is_coastal", 1),
         (store_distance_to_party_from_party, ":dist", ":party_no", ":object_town"),
         (party_get_position, pos0, ":object_town"),
         (party_get_slot, ":radius", ":object_town", "slot_town_is_coastal"),
         (val_add, ":radius", 3),
         (lt, ":dist", ":radius"),
         (assign, ":cur_center", ":object_town"),
         (store_faction_of_party, ":merchant_faction", ":party_no"),
         (faction_get_slot, ":num_towns", ":merchant_faction", "slot_faction_num_towns"),
         (try_begin),
           (le, ":num_towns", 0),
           (remove_party, ":party_no"),
         (else_try),
           (store_random_in_range, ":random_no", 0, 100),

           (try_begin),
             (party_slot_eq, ":cur_center", "slot_town_lord", "trp_player"),

             (game_get_reduce_campaign_ai, ":reduce_campaign_ai"),
             (try_begin),
               (eq, ":reduce_campaign_ai", 0), #hard (less money from tariffs)
               (assign, ":tariff_succeed_limit", 35),
             (else_try),
               (eq, ":reduce_campaign_ai", 1), #medium (normal money from tariffs)
               (assign, ":tariff_succeed_limit", 45),
             (else_try),
               (eq, ":reduce_campaign_ai", 2), #easy (more money from tariffs)
               (assign, ":tariff_succeed_limit", 60),
             (try_end),
           (else_try),
             (assign, ":tariff_succeed_limit", 45),
           (try_end),

           (lt, ":random_no", ":tariff_succeed_limit"),

           (assign, ":can_leave", 1),
           (try_begin),
             (is_between, ":cur_center", walled_centers_begin, walled_centers_end),
             (neg|party_slot_eq, ":cur_center", "slot_center_is_besieged_by", -1),
             (assign, ":can_leave", 0),
           (try_end),
           (eq, ":can_leave", 1),

           (assign, ":do_trade", 0),
           (try_begin),
             (party_get_slot, ":cur_ai_state", ":party_no", "slot_party_ai_state"),
             (eq, ":cur_ai_state", spai_trading_with_town),
             (party_get_slot, ":cur_ai_object", ":party_no", "slot_party_ai_object"),
             (eq, ":cur_center", ":cur_ai_object"),
             (assign, ":do_trade", 1),
           (try_end),

           (assign, ":target_center", -1),

           (try_begin), #Make sure escorted caravan continues to its original destination.
             #(eq, "$caravan_escort_party_id", ":party_no"),
             #(neg|party_is_in_town, ":party_no", "$caravan_escort_destination_town"),
             #(assign, ":target_center", "$caravan_escort_destination_town"),
           #(else_try),                                 #Calling altered script for seatrade
             (call_script, "script_cf_select_most_profitable_coastal_town_at_peace_with_faction_in_trade_route", ":cur_center", ":merchant_faction"),
             (assign, ":target_center", reg0),
           (try_end),
           (is_between, ":target_center", towns_begin, towns_end),
           (store_distance_to_party_from_party, ":target_dist", ":party_no", ":target_center"),
           (party_get_position, pos0, ":target_center"),
           (party_get_slot, ":radius", ":target_center", "slot_town_is_coastal"),
           (map_get_water_position_around_position, pos1, pos0, ":radius"),
           (val_add, ":radius", 2),
           (gt, ":target_dist", ":radius"), #was 5 #Ensures that they aren't already at the target party...just a redundancy check, as there is with caravans

           (try_begin),
             (eq, ":do_trade", 1),
             (str_store_party_name, s7, ":cur_center"),
             (call_script, "script_do_merchant_town_trade", ":party_no", ":cur_center"),
           (try_end),

           (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_point),
           (party_set_ai_target_position, ":party_no", pos1),
           # (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
           (party_set_ai_object, ":party_no", ":target_center"),
           (party_set_flags, ":party_no", pf_default_behavior, 0),
           (party_set_slot, ":party_no", "slot_party_ai_state", spai_trading_with_town),
           (party_set_slot, ":party_no", "slot_party_ai_object", ":target_center"),
         (try_end),
        (try_end),
       (try_end),
    ]),
]


scripts = [

  #the following is a very simple adjustment - it measures the difference in prices between two towns
  #all goods are weighted equally except for luxuries
  #it does not take into account the prices of the goods, nor cargo capacity
  #to do that properly, a merchant would have to virtually fill his baggage, slot by slot, for each town
  #is also found that one needed to introduce demand inelasticity -- prices should vary a lot for grain,  relatively little for iron
  #
  #Added a third parameter, the caravan party, for use in distance calculations and perhaps
  #other things in the future.  This may be -1, in which case the script attempts to find a
  #general answer without referring to any specific attributes.  It may also be a town,
  #in which case its position is used for distance calculations.
  ("cf_select_most_profitable_town_at_peace_with_faction_in_trade_route",
    [
      (store_script_param, ":town_no", 1),
      (store_script_param, ":faction_no", 2),

      (assign, ":result", -1),
      (assign, ":best_town_score", 0),
      (store_sub, ":item_to_price_slot", "slot_town_trade_good_prices_begin", trade_goods_begin),

      (try_for_range, ":cur_slot", "slot_town_trade_routes_begin", "slot_town_trade_routes_end"),
        (party_get_slot, ":cur_town", ":town_no", ":cur_slot"),
        (gt, ":cur_town", 0),

        (store_faction_of_party, ":cur_faction", ":cur_town"),
        (store_relation, ":reln", ":cur_faction", ":faction_no"),
        (ge, ":reln", 0),

        (assign, ":cur_town_score", 0),
        (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
          (neq, ":cur_goods", "itm_butter"), #Don't count perishables
          (neq, ":cur_goods", "itm_cattle_meat"),
          (neq, ":cur_goods", "itm_chicken"),
          (neq, ":cur_goods", "itm_pork"),
          (neq, ":cur_goods", "itm_deer_meat"),
          (neq, ":cur_goods", "itm_boar_meat"),
          (neq, ":cur_goods", "itm_wolf_meat"),
          (neq, ":cur_goods", "itm_goat_meat"),
          (neq, ":cur_goods", "itm_goatb_meat"),
          (neq, ":cur_goods", "itm_wilddonkey_meat"),

          (store_add, ":cur_goods_price_slot", ":cur_goods", ":item_to_price_slot"),
          (party_get_slot, ":origin_price", ":town_no", ":cur_goods_price_slot"),
          (party_get_slot, ":destination_price", ":cur_town", ":cur_goods_price_slot"),

          (gt, ":destination_price", ":origin_price"),
          (store_sub, ":price_dif", ":destination_price", ":origin_price"),

          (try_begin), #weight luxury goods double
            (this_or_next|eq, ":cur_goods", "itm_spice"),
            (eq, ":cur_goods", "itm_velvet"),
            (val_mul, ":price_dif", 2),
          (try_end),
          (val_add, ":cur_town_score", ":price_dif"),
        (try_end),
        (gt, ":cur_town_score", ":best_town_score"),
        (assign, ":best_town_score", ":cur_town_score"),
        (assign, ":result", ":cur_town"),
      (try_end),

      (gt, ":result", -1), # Fail if there are no towns

      (assign, reg0, ":result"),
    ]),

  #script_do_merchant_town_trade
  # INPUT: arg1 = party_no (of the merchant), arg2 = center_no
  # OUTPUT: reg1 (total_change), s1 (party_no), s2 (center_no)
  ("do_merchant_town_trade",
    [
      (store_script_param_1, ":party_no"),
      (store_script_param_2, ":center_no"),

      (party_get_slot, ":origin", ":party_no", "slot_party_last_traded_center"),

      # logging
      (try_begin),
        (eq, "$cheat_mode", 2),
        (str_store_party_name, s4, ":center_no"),
        (str_store_party_name, s5, ":origin"),
        (display_message, "@{!}DEBUG -- Caravan trades in {s4}, originally from {s5}"),
      (try_end),
      (call_script, "script_add_log_entry", logent_party_traded, ":party_no", ":origin", ":center_no", -1),

      # trade
      (call_script, "script_do_party_center_trade", ":party_no", ":center_no", 4),

      # Add the earnings to the wealth (maximum changed price is the earning)
      # todo: why divide by 2?
      (assign, ":total_change", reg0),
      (val_div, ":total_change", 2),
      (str_store_party_name, s1, ":party_no"),
      (str_store_party_name, s2, ":center_no"),
      (assign, reg1, ":total_change"),

      ### Add tariffs to the town
      (party_get_slot, ":accumulated_tariffs", ":center_no", "slot_center_accumulated_tariffs"),
      (party_get_slot, ":prosperity", ":center_no", "slot_town_prosperity"),

      (assign, ":tariffs_generated", ":total_change"),
      (val_mul, ":tariffs_generated", ":prosperity"),

      (assign, ":percent", 100),
      (try_begin),
        # trade agreement boost tariffs by 30%
        (store_faction_of_party, ":party_faction", ":party_no"),
        (store_faction_of_party, ":center_faction", ":center_no"),

        (store_add, ":truce_slot", ":party_faction", "slot_faction_truce_days_with_factions_begin"),
        (val_sub, ":truce_slot", kingdoms_begin),
        (faction_get_slot, ":truce_days", ":center_faction", ":truce_slot"),
        (gt, ":truce_days", dplmc_treaty_trade_days_expire),
        (val_add, ":percent", 30),
      (try_end),

      # If economic changes are enabled, divide the tariffs between the source and destination.
      (try_begin),
        # Economic changes are enabled
        (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),

        # verify the origin is a real town or village and not a placeholder value
        (ge, ":origin", 0),
        (this_or_next|is_between, ":origin", towns_begin, towns_end),
        (this_or_next|is_between, ":origin", villages_begin, villages_end),
        (this_or_next|party_slot_eq, ":origin", "slot_party_type", spt_town),
        (party_slot_eq, ":origin", "slot_party_type", spt_village),

        # give half the tariffs to the origin
        (ge, ":tariffs_generated", 0),
        (party_get_slot, ":origin_accumulated_tariffs", ":origin", "slot_center_accumulated_tariffs"),
        (store_div, ":origin_tariffs_generated", ":tariffs_generated", 2),
        (val_sub, ":tariffs_generated", ":origin_tariffs_generated"),

        # apply plutocracy/aristocracy modifier and trade treaty boost
        (store_faction_of_party, ":origin_faction", ":center_no"),
        (faction_get_slot, ":aristocracy", ":origin_faction", "slot_faction_aristocracy"),
        (val_mul, ":aristocracy", -5),
        (store_add, ":origin_percent", ":percent", ":aristocracy"),
        # Otg = :origin_tariffs_generated, Op = :origin_percent
        # ([(Otg * Op + 50) / 100] + 50) / 100
        # todo: why this complication? Consider simplifing.
        (val_mul, ":origin_tariffs_generated", ":origin_percent"),
        (val_add, ":origin_tariffs_generated", 50),
        (val_div, ":origin_tariffs_generated", 100),
        #apply the delayed division from before (leaving the steps separated for clarity)
        (val_add, ":origin_tariffs_generated", 50),
        (val_div, ":origin_tariffs_generated", 100),
        (val_add, ":origin_tariffs_generated", 5),
        (val_div, ":origin_tariffs_generated", 10),
        # now we have the final value of origin_tariffs_generated
        (val_add, ":origin_accumulated_tariffs", ":origin_tariffs_generated"),
        (party_set_slot, ":origin", "slot_center_accumulated_tariffs", ":origin_accumulated_tariffs"),

        #print economic debug message if enabled
        (try_begin),
          (ge, "$cheat_mode", 3),
          (assign, reg4, ":origin_tariffs_generated"),
          (str_store_party_name, s4, ":origin"),
          (assign, reg5, ":origin_accumulated_tariffs"),
          (display_message, "@{!}New tariffs at {s4} = {reg4}, total = {reg5}"),
        (try_end),
      (try_end),

      #For this town: apply the faction plutocracy/aristocracy modifier
      (faction_get_slot, ":aristocracy", ":center_faction", "slot_faction_aristocracy"),
      (val_mul, ":aristocracy", -5),
      (val_add, ":percent", ":aristocracy"),
      (val_mul, ":tariffs_generated", ":percent"),
      (val_add, ":tariffs_generated", 50),
      (val_div, ":tariffs_generated", 100),
      #apply the delayed division from before (leaving the steps separated for clarity)
      (val_add, ":tariffs_generated", 50),
      (val_div, ":tariffs_generated", 100),
      (val_add, ":tariffs_generated", 5),
      (val_div, ":tariffs_generated", 10), #10 for caravans, 20 for villages
      (val_add, ":accumulated_tariffs", ":tariffs_generated"),
      (party_set_slot, ":center_no", "slot_center_accumulated_tariffs", ":accumulated_tariffs"),

      (try_begin),
        (ge, "$cheat_mode", 3),
        (assign, reg4, ":tariffs_generated"),
        (str_store_party_name, s4, ":center_no"),
        (assign, reg5, ":accumulated_tariffs"),
        (display_message, "@{!}New tariffs at {s4} = {reg4}, total = {reg5}"),
      (try_end),

      (assign, ":benefit_center", ":center_no"),

      # If economic changes are enabled, 50% chance that the origin rather than
      # the destination will receive the chance for prosperity increase.
      (try_begin),
        (ge, "$g_dplmc_gold_changes", DPLMC_GOLD_CHANGES_LOW),

        # verify the origin is a real town or village and not a placeholder value
        (ge, ":origin", 0),
        (this_or_next|is_between, ":origin", towns_begin, towns_end),
        (this_or_next|is_between, ":origin", villages_begin, villages_end),
        (this_or_next|party_slot_eq, ":origin", "slot_party_type", spt_town),
            (party_slot_eq, ":origin", "slot_party_type", spt_village),

        (ge, ":tariffs_generated", 0),
        # 50% chance
        (store_random_in_range, ":rand", 0, 64),
        (lt, ":rand", 32),
        (assign, ":benefit_center", ":origin"),
      (try_end),

      # Prosperity increase
      (try_begin),
        (store_random_in_range, ":rand", 0, 80),

        (call_script, "script_center_get_goods_availability", ":benefit_center"),
        (assign, ":hardship_index", reg0),
        (gt, ":rand", ":hardship_index"),

        (try_begin),
          (store_random_in_range, ":rand", 0, 100),
          (gt, ":rand", 82),
          (call_script, "script_change_center_prosperity", ":benefit_center", 1),
          (val_add, "$newglob_total_prosperity_from_caravan_trade", 1),
        (try_end),
      (try_end),
  ]),

  ("cf_select_most_profitable_coastal_town_at_peace_with_faction_in_trade_route",
  [
        (store_script_param, ":town_no", 1),
        (store_script_param, ":faction_no", 2),

        (assign, ":result", -1),
        (assign, ":best_town_score", 0),
        (store_sub, ":item_to_price_slot", "slot_town_trade_good_prices_begin", trade_goods_begin),

        (try_for_range, ":cur_slot", "slot_town_trade_routes_begin", "slot_town_trade_routes_end"),
          (party_get_slot, ":cur_town", ":town_no", ":cur_slot"),
          (gt, ":cur_town", 0),
          (party_slot_ge, ":cur_town", "slot_town_is_coastal", 1), #Seatrade

          (store_faction_of_party, ":cur_faction", ":cur_town"),
          (store_relation, ":reln", ":cur_faction", ":faction_no"),
          (ge, ":reln", 0),

          (assign, ":cur_town_score", 0),
          (try_for_range, ":cur_goods", trade_goods_begin, trade_goods_end),
            (neq, ":cur_goods", "itm_butter"), #Don't count perishables
            (neq, ":cur_goods", "itm_cattle_meat"),
            (neq, ":cur_goods", "itm_chicken"),
            (neq, ":cur_goods", "itm_pork"),

            (store_add, ":cur_goods_price_slot", ":cur_goods", ":item_to_price_slot"),
            (party_get_slot, ":origin_price", ":town_no", ":cur_goods_price_slot"),
            (party_get_slot, ":destination_price", ":cur_town", ":cur_goods_price_slot"),

            (gt, ":destination_price", ":origin_price"),
            (store_sub, ":price_dif", ":destination_price", ":origin_price"),

            (try_begin), #weight luxury goods double
              (this_or_next|eq, ":cur_goods", "itm_spice"),
              (eq, ":cur_goods", "itm_velvet"),
              (val_mul, ":price_dif", 2),
            (try_end),
            (val_add, ":cur_town_score", ":price_dif"),
          (try_end),

          ##        (try_begin),
          ##            (eq, "$cheat_mode", 1),
          ##            (str_store_party_name, s10, ":town_no"),
          ##            (str_store_party_name, s11, ":cur_town"),
          ##            (assign, reg3, ":cur_town_score"),
          ##            (display_message, "str_caravan_in_s10_considers_s11_total_price_dif_=_reg3"),
          ##        (try_end),

          (gt, ":cur_town_score", ":best_town_score"),
          (assign, ":best_town_score", ":cur_town_score"),
          (assign, ":result", ":cur_town"),

        (try_end),

        (gt, ":result", -1), #Fail if there are no towns

        (assign, reg0, ":result"),

        #      (store_current_hours, ":hour"),
        #      (party_set_slot, ":result", "slot_town_caravan_last_visit", ":hour"),

        # (try_begin),
        ###(eq, "$cheat_mode", 1),
        # (assign, reg3, ":best_town_score"),
        # (str_store_party_name, s3, ":town_no"),
        # (str_store_party_name, s4, ":result"),
        # (display_message, "str_test__caravan_in_s3_selects_for_s4_trade_score_reg3"),
        # (try_end),
  ]),
]
