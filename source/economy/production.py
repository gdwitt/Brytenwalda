from ..header_mission_templates import *
from ..header_map_icons import *
from ..module_constants import *


simple_triggers = [
    (72,
     [
         # Update trade good prices
         (call_script, "script_update_trade_good_prices"),
     ])
]


scripts = [

  #script_update_trade_good_prices
  # INPUT: none
  ("update_trade_good_prices",
    [
      (try_for_range, ":center_no", centers_begin, centers_end),
        (this_or_next|is_between, ":center_no", towns_begin, towns_end),
        (is_between, ":center_no", villages_begin, villages_end),
        (call_script, "script_update_trade_good_price_for_party", ":center_no"),
      (try_end),

      (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
        (assign, ":total_price", 0),
        (assign, ":total_constants", 0),

        (try_for_range, ":center_no", centers_begin, centers_end),
          (this_or_next|is_between, ":center_no", towns_begin, towns_end),
          (is_between, ":center_no", villages_begin, villages_end),

          (store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
          (val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
          (party_get_slot, ":cur_price", ":center_no", ":cur_good_price_slot"),

          (try_begin),
            (is_between, ":center_no", towns_begin, towns_end),
            (assign, ":constant", 5),
          (else_try),
            (assign, ":constant", 1),
          (try_end),

          (val_mul, ":cur_price", ":constant"),

          (val_add, ":total_price", ":cur_price"),
          (val_add, ":total_constants", ":constant"),
        (try_end),

        (try_for_range, ":center_no", centers_begin, centers_end),
          (this_or_next|is_between, ":center_no", towns_begin, towns_end),
          (is_between, ":center_no", villages_begin, villages_end),

          (store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
          (val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
          (party_get_slot, ":cur_price", ":center_no", ":cur_good_price_slot"),

          (val_mul, ":cur_price", 1000),
          (val_mul, ":cur_price", ":total_constants"),
          (val_div, ":cur_price", ":total_price"),          

          (val_clamp, ":cur_price", minimum_price_factor, maximum_price_factor),
          (party_set_slot, ":center_no", ":cur_good_price_slot", ":cur_price"),
        (try_end),
      (try_end),
  ]),

  #script_update_trade_good_price_for_party
  # INPUT: arg1 = party_no
  ("update_trade_good_price_for_party",
    [
      (store_script_param, ":center_no", 1),
      (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
        (store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
        (val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
        (party_get_slot, ":cur_price", ":center_no", ":cur_good_price_slot"),
        
        (call_script, "script_center_get_production", ":center_no", ":cur_good"),
        (assign, ":production", reg0),
        
        (call_script, "script_center_get_consumption", ":center_no", ":cur_good"),
        (assign, ":consumption", reg0),

        (val_sub, ":production", ":consumption"),
        
        #Change average production x 2(1+random(2)) (was 4, random(8)) for excess demand
        (try_begin),
          #supply is greater than demand
          (gt, ":production", 0), 
          (store_mul, ":change_factor", ":production", 6), #price      will be decreased by his factor    MOTO chief increase 20% (from 1)
                (val_div, ":change_factor", 5),    #MOTO chief increase 20%
      #(store_mul, ":change_factor", ":production", 1), #price will be decreased by his factor
          (store_random_in_range, ":random_change", 0, ":change_factor"),
          (val_add, ":random_change", ":change_factor"),
          (val_add, ":random_change", ":change_factor"),          

          #simulation starts
          (store_sub, ":final_price", ":cur_price", ":random_change"),
          (val_clamp, ":final_price", minimum_price_factor, maximum_price_factor),                              
          (try_begin), #Excess of supply decelerates over time, as low price reduces output
            #if expected final price is 100 then it will multiply random_change by 0.308x ((100+300)/(1300) = 400/1300).
            (lt, ":final_price", 1000),
            (store_add, ":final_price_plus_300", ":final_price", 300),
            (val_mul, ":random_change", ":final_price_plus_300"),
            (val_div, ":random_change", 1300),
          (try_end),
          (val_sub, ":cur_price", ":random_change"),
        (else_try),
          (lt, ":production", 0), 
          (store_sub, ":change_factor", 0, ":production"), #price will be increased by his factor
                (val_mul, ":change_factor", 6),    #MOTO chief increase 20%      (from 1)
                (val_div, ":change_factor", 5),    #MOTO chief increase 20%
                (store_random_in_range, ":random_change", 0, ":change_factor"),
          (val_add, ":random_change", ":change_factor"),
          (val_add, ":random_change", ":change_factor"),
          (val_add, ":cur_price", ":random_change"),
        (try_end),
            
        #Move price towards average by 3%...
        #Equilibrium is 33 cycles, or 100 days
        #Change per cycle is Production x 4
        #Thus, max differential = -5 x 4 x 33 = -660 for -5
        (try_begin),
          (is_between, ":center_no", villages_begin, villages_end),
          (store_sub, ":price_difference", ":cur_price", average_price_factor),
          (val_mul, ":price_difference", 96),
          (val_div, ":price_difference", 100),
          (store_add, ":new_price", average_price_factor, ":price_difference"),
        (else_try),
          (store_sub, ":price_difference", ":cur_price", average_price_factor),
          (val_mul, ":price_difference", 96),
          (val_div, ":price_difference", 100),
          (store_add, ":new_price", average_price_factor, ":price_difference"),
        (try_end),
        
        #Price of manufactured goods drift towards primary raw material 
        (try_begin),
            (item_get_slot, ":raw_material", ":cur_good", slot_item_primary_raw_material),
            (neq, ":raw_material", 0),
            (store_sub, ":raw_material_price_slot", ":raw_material", trade_goods_begin),
            (val_add, ":raw_material_price_slot", slot_town_trade_good_prices_begin),

            (party_get_slot, ":total_raw_material_price", ":center_no", ":raw_material_price_slot"),
            (val_mul, ":total_raw_material_price", 3),
            (assign, ":number_of_centers", 3),

            (try_for_range, ":village_no", villages_begin, villages_end),
              (party_slot_eq, ":village_no", slot_village_bound_center, ":center_no"),
              (party_get_slot, ":raw_material_price", ":village_no", ":raw_material_price_slot"),
              (val_add, ":total_raw_material_price", ":raw_material_price"),
              (val_add, ":number_of_centers", 1),
            (try_end),

            (store_div, ":average_raw_material_price", ":total_raw_material_price", ":number_of_centers"),                    

            (gt, ":average_raw_material_price", ":new_price"),
            (store_sub, ":raw_material_boost", ":average_raw_material_price", ":new_price"),
            (val_div, ":raw_material_boost", 10), 
            (val_add, ":new_price", ":raw_material_boost"),
        (try_end),
        
        (val_clamp, ":new_price", minimum_price_factor, maximum_price_factor),
        (party_set_slot, ":center_no", ":cur_good_price_slot", ":new_price"),
      (try_end),
  ]),
  
  ("center_get_production",
    [
        #Actually, this could be reset somewhat to yield supply and demand as raw numbers
        #Demand could be set values for rural and urban
        #Supply could be based on capital goods -- head of cattle, head of sheep, fish ponds, fishing fleets, acres of grain fields, olive orchards, olive presses, wine presses, mills, smithies, salt pans, potters' kilns, etc
        #Prosperity would increase both demand and supply
        (store_script_param_1, ":center_no"),
        (store_script_param_2, ":cur_good"),
  
        (assign, ":base_production", 0),

        #Grain products
        (try_begin),
            (eq, ":cur_good", "itm_bread"), #Demand = 3000 across Calradia
            (party_get_slot, ":base_production", ":center_no", slot_center_mills),
            (val_mul, ":base_production", 20), #one mills per village, five mills per town = 160 mills 
        (else_try),
            (eq, ":cur_good", "itm_grain"), #Demand =  3200+, 1600 to mills, 1500 on its own, extra to breweries
            (party_get_slot, ":base_production", ":center_no", slot_center_acres_grain),
            (val_div, ":base_production", 125), #10000 acres is the average across Calradia, extra in Swadia, less in snows and steppes, a bit from towns 
        (else_try),
            (eq, ":cur_good", "itm_ale"), #
            (party_get_slot, ":base_production", ":center_no", slot_center_breweries),
            (val_mul, ":base_production", 25), 
        (else_try),
            (eq, ":cur_good", "itm_mead"), #
            (party_get_slot, ":base_production", ":center_no", slot_center_breweries),
            (val_mul, ":base_production", 20), 

        (else_try),
            (eq, ":cur_good", "itm_smoked_fish"), #Demand = 20
            (party_get_slot, ":base_production", ":center_no", slot_center_fishing_fleet),
            (val_mul, ":base_production", 4), #was originally 5
        (else_try),
            (eq, ":cur_good", "itm_salt"), 
            (party_get_slot, ":base_production", ":center_no", slot_center_salt_pans),
            (val_mul, ":base_production", 35),

        #Cattle products    
        (else_try),
            (eq, ":cur_good", "itm_cattle_meat"), #Demand = 5
            (party_get_slot, ":base_production", ":center_no", slot_center_head_cattle),
            (val_div, ":base_production", 4), #was 9
        (else_try),
            (eq, ":cur_good", "itm_dried_meat"), #Demand = 15
            (party_get_slot, ":base_production", ":center_no", slot_center_head_cattle),
            (val_div, ":base_production", 2), #was 3
        (else_try),
            (eq, ":cur_good", "itm_cheese"),      #Demand = 10
            (party_get_slot, ":base_production", ":center_no", slot_center_head_cattle),
            (party_get_slot, ":sheep_addition", ":center_no", slot_center_head_sheep),
            (val_div, ":sheep_addition", 2),
            (val_add, ":base_production", ":sheep_addition"),
            (party_get_slot, ":gardens", ":center_no", slot_center_household_gardens),
            (val_mul, ":base_production", ":gardens"),
            (val_div, ":base_production", 10), 
        (else_try),
            (eq, ":cur_good", "itm_butter"),      #Demand = 2
            (party_get_slot, ":base_production", ":center_no", slot_center_head_cattle),
            (party_get_slot, ":gardens", ":center_no", slot_center_household_gardens),
            (val_mul, ":base_production", ":gardens"),
            (val_div, ":base_production", 15),
            
        (else_try),
            (eq, ":cur_good", "itm_raw_leather"),      #Demand = ??
            (party_get_slot, ":base_production", ":center_no", slot_center_head_cattle),
            (val_div, ":base_production", 6),
            (party_get_slot, ":sheep_addition", ":center_no", slot_center_head_sheep),
            (val_div, ":sheep_addition", 12),
            (val_add, ":base_production", ":sheep_addition"),
            
        (else_try),
            (eq, ":cur_good", "itm_leatherwork"),      #Demand = ??
            (party_get_slot, ":base_production", ":center_no", slot_center_tanneries),
            (val_mul, ":base_production", 20),
            

        (else_try),
            (eq, ":cur_good", "itm_honey"),      #Demand = 5
            (party_get_slot, ":base_production", ":center_no", slot_center_apiaries),
            (val_mul, ":base_production", 6),
        (else_try),
            (eq, ":cur_good", "itm_cabbages"),      #Demand = 7
            (party_get_slot, ":base_production", ":center_no", slot_center_household_gardens),
            (val_mul, ":base_production", 10),
        (else_try),
            (eq, ":cur_good", "itm_apples"),      #Demand = 7
            (party_get_slot, ":base_production", ":center_no", slot_center_household_gardens),
            (val_mul, ":base_production", 10),
            
        #Sheep products    
        (else_try),
            (eq, ":cur_good", "itm_sausages"),      #Demand = 5
            (party_get_slot, ":base_production", ":center_no", slot_center_head_sheep), #average of 90 sheep
            (val_div, ":base_production", 15),
        (else_try),
            (eq, ":cur_good", "itm_wool"),      #(Demand = 0, but 15 averaged out perhaps)
            (party_get_slot, ":base_production", ":center_no", slot_center_head_sheep), #average of 90 sheep
            (val_div, ":base_production", 5),
        (else_try),
            (eq, ":cur_good", "itm_wool_cloth"),      #(Demand = 1500 across Calradia)
            (party_get_slot, ":base_production", ":center_no", slot_center_wool_looms),
            (val_mul, ":base_production", 5), #300 across Calradia
        (else_try),
            (this_or_next|eq, ":cur_good", "itm_pork"),      
            (eq, ":cur_good", "itm_chicken"),      
            (try_begin),
              (is_between, ":center_no", villages_begin, villages_end),
              (assign, ":base_production", 30), 
            (else_try),
              (assign, ":base_production", 0), 
            (try_end),
        (else_try),
            (eq, ":cur_good", "itm_iron"),      #Demand = 5, one supplies three smithies
            (party_get_slot, ":base_production", ":center_no", slot_center_iron_deposits),
            (val_mul, ":base_production", 10),
        (else_try), #silver
            (eq, ":cur_good", "itm_silver"),      #Demand = 5, one supplies three smithies
            (party_get_slot, ":base_production", ":center_no", slot_center_iron_deposits),
            (val_mul, ":base_production", 10),
        (else_try),
            (eq, ":cur_good", "itm_mineral"),      #Demand = 5, one supplies three smithies
            (party_get_slot, ":base_production", ":center_no", slot_center_iron_deposits),
            (val_mul, ":base_production", 10),
        (else_try),
            (eq, ":cur_good", "itm_tools"),      #Demand = 560 across Calradia
            (party_get_slot, ":base_production", ":center_no", slot_center_smithies),
            (val_mul, ":base_production", 3),

        #Other artisanal goods    
        (else_try),
            (eq, ":cur_good", "itm_pottery"), #560 is total demand     
            (party_get_slot, ":base_production", ":center_no", slot_center_pottery_kilns),
            (val_mul, ":base_production", 5),

        (else_try),
            (eq, ":cur_good", "itm_raw_grapes"),      
            (party_get_slot, ":base_production", ":center_no", slot_center_acres_vineyard),
            (val_div, ":base_production", 100),
        (else_try),
            (eq, ":cur_good", "itm_wine"),      
            (party_get_slot, ":base_production", ":center_no", slot_center_wine_presses),
            (val_mul, ":base_production", 10), #chief cambiado
            
            
        (else_try),
            (eq, ":cur_good", "itm_raw_olives"),      
            (party_get_slot, ":base_production", ":center_no", slot_center_acres_olives),
            (val_div, ":base_production", 150),
        (else_try),
            (eq, ":cur_good", "itm_oil"),      
            (party_get_slot, ":base_production", ":center_no", slot_center_olive_presses),
            (val_mul, ":base_production", 12),
            
        #Flax and linen    
        (else_try),
            (eq, ":cur_good", "itm_linen"),      
            (party_get_slot, ":base_production", ":center_no", slot_center_linen_looms),
            (val_mul, ":base_production", 5),
        (else_try),
            (eq, ":cur_good", "itm_raw_flax"),      
            (party_get_slot, ":base_production", ":center_no", slot_center_acres_flax),
            (val_div, ":base_production", 80),
            

        (else_try),
            (eq, ":cur_good", "itm_velvet"),      
            (party_get_slot, ":base_production", ":center_no", slot_center_silk_looms),
            (val_mul, ":base_production", 5),
        (else_try), #tile
            (eq, ":cur_good", "itm_rare_fabric"),      
            (party_get_slot, ":base_production", ":center_no", slot_center_silk_farms),
            (val_div, ":base_production", 20),
        (else_try),
            (eq, ":cur_good", "itm_raw_dyes"),      
            (party_get_slot, ":base_production", ":center_no", slot_center_kirmiz_farms),
            (val_div, ":base_production", 20),

##            
##        (else_try),
##            (eq, ":cur_good", "itm_silver"),      
##            (party_get_slot, ":base_production", ":center_no", slot_center_acres_dates),
##            (val_div, ":base_production", 120),
        (else_try),
            (eq, ":cur_good", "itm_furs"),      #Demand = 90 across Calradia
            (party_get_slot, ":base_production", ":center_no", slot_center_fur_traps),
            (val_mul, ":base_production", 25),
        (else_try),
            (eq, ":cur_good", "itm_spice"),
            (try_begin),
                (eq, ":center_no", "p_town_1"), #Cantwaraburh
                (assign, ":base_production", 30), #chief cambia
            (else_try),
                (eq, ":center_no", "p_town_2"), #Seals-ey
                (assign, ":base_production", 20), #chief cambiado
            (else_try),
                (eq, ":center_no", "p_town_12"), #Lundenwic
                (assign, ":base_production", 10), #chief cambia
            (else_try),
                (eq, ":center_no", "p_town_17"), #Uisc
                (assign, ":base_production", 10), #chief cambiado
            (else_try),
                (this_or_next|eq, ":center_no", "p_village_11"), #Dusturil (village of Tulga)
                (eq, ":center_no", "p_village_25"), #Dashbigha (village of Tulga)
                (assign, ":base_production", 50),
            (else_try),
                (this_or_next|eq, ":center_no", "p_village_37"), #Ada Kulun (village of Ichlamur)
                (this_or_next|eq, ":center_no", "p_village_42"), #Dirigh Aban (village of Ichlamur)
                (this_or_next|eq, ":center_no", "p_village_99"), #Fishara (village of Bariyye)
                (eq, ":center_no", "p_village_100"), #Iqbayl (village of Bariyye)
                (assign, ":base_production", 25),
            (try_end),    
        (try_end),

        #Modify production by other goods
        (assign, ":modified_production", ":base_production"),
        (try_begin),
            (eq, ":cur_good", "itm_bread"),
            (call_script, "script_good_price_affects_good_production", ":center_no", "itm_grain", ":base_production", 1),
            (assign, ":modified_production", reg0),
        (else_try),
            (eq, ":cur_good", "itm_ale"),
            (call_script, "script_good_price_affects_good_production", ":center_no", "itm_grain", ":base_production", 2),
            (assign, ":modified_production", reg0),
        (else_try), #chief
            (eq, ":cur_good", "itm_mead"),
            (call_script, "script_good_price_affects_good_production", ":center_no", "itm_honey", ":base_production", 2),
            (assign, ":modified_production", reg0),
        (else_try),
            (eq, ":cur_good", "itm_dried_meat"),
            (call_script, "script_good_price_affects_good_production", ":center_no", "itm_salt", ":base_production", 2),
            (assign, ":modified_production", reg0),
        (else_try),
            (eq, ":cur_good", "itm_smoked_fish"),
            (call_script, "script_good_price_affects_good_production", ":center_no", "itm_salt", ":base_production", 2),
            (assign, ":modified_production", reg0),
        (else_try),    
            (eq, ":cur_good", "itm_tools"),
            (call_script, "script_good_price_affects_good_production", ":center_no", "itm_iron", ":base_production", 1),
            (assign, ":modified_production", reg0),
        (else_try),    
            (eq, ":cur_good", "itm_wool_cloth"),
            (call_script, "script_good_price_affects_good_production", ":center_no", "itm_wool", ":base_production", 1),
            (assign, ":modified_production", reg0),
        (else_try),    
            (eq, ":cur_good", "itm_wine"),
            (call_script, "script_good_price_affects_good_production", ":center_no", "itm_raw_grapes", ":base_production", 1),
            (assign, ":modified_production", reg0),
        (else_try),    
            (eq, ":cur_good", "itm_oil"),
            (call_script, "script_good_price_affects_good_production", ":center_no", "itm_raw_olives", ":base_production", 1),
            (assign, ":modified_production", reg0),
        (else_try),    
            (eq, ":cur_good", "itm_velvet"),
            (call_script, "script_good_price_affects_good_production", ":center_no", "itm_rare_fabric", ":base_production", 1),
            (assign, ":initially_modified_production", reg0),
            
            (call_script, "script_good_price_affects_good_production", ":center_no", "itm_raw_dyes", ":initially_modified_production", 2),
            (assign, ":modified_production", reg0),
        (else_try),    
            (eq, ":cur_good", "itm_leatherwork"),
            (call_script, "script_good_price_affects_good_production", ":center_no", "itm_raw_leather", ":base_production", 1),
            (assign, ":modified_production", reg0),
        (else_try),    
            (eq, ":cur_good", "itm_linen"),
            (call_script, "script_good_price_affects_good_production", ":center_no", "itm_raw_flax", ":base_production", 1),
            (assign, ":modified_production", reg0),
        (try_end),
        

        (assign, ":base_production_modded_by_raw_materials", ":modified_production"), #this is just logged for the report screen

        #Increase both positive and negative production by the center's prosperity
        #Richer towns have more people and consume more, but also produce more 
        (try_begin),
            (party_get_slot, ":prosperity_plus_75", ":center_no", slot_town_prosperity),
            (val_add, ":prosperity_plus_75", 75),
            (val_mul, ":modified_production", ":prosperity_plus_75"),
            (val_div, ":modified_production", 125),
        (try_end),
  
        (try_begin),
            (this_or_next|party_slot_eq, ":center_no", slot_village_state, svs_being_raided),
                (party_slot_eq, ":center_no", slot_village_state, svs_looted),
            (assign, ":modified_production", 0),    
        (try_end),
 
        (assign, reg0, ":modified_production"), #modded by prosperity
        (assign, reg1, ":base_production_modded_by_raw_materials"),
        (assign, reg2, ":base_production"),
      
    ]),

  ("center_get_consumption",
    [
        (store_script_param_1, ":center_no"),
        (store_script_param_2, ":cur_good"),

        (assign, ":consumer_consumption", 0),
        (try_begin),
            (this_or_next|is_between, ":center_no", "p_town_19", "p_castle_1"),        
                (ge, ":center_no", "p_village_91"),
            (item_slot_ge, ":cur_good", slot_item_desert_demand, 0), #Otherwise use rural or urban
            (item_get_slot, ":consumer_consumption", ":cur_good", slot_item_desert_demand),
        (else_try),
            (is_between, ":center_no", villages_begin, villages_end),
            (item_get_slot, ":consumer_consumption", ":cur_good", slot_item_rural_demand),
        (else_try),
            (is_between, ":center_no", towns_begin, towns_end),
            (item_get_slot, ":consumer_consumption", ":cur_good", slot_item_urban_demand),
        (try_end),
        
        
        (assign, ":raw_material_consumption", 0),
        (try_begin),
            (eq, ":cur_good", "itm_grain"),
            (party_get_slot, ":grain_for_bread", ":center_no", slot_center_mills),
            (val_mul, ":grain_for_bread", 20),
            
            (party_get_slot, ":grain_for_ale", ":center_no", slot_center_breweries),
            (val_mul, ":grain_for_ale", 5),
            
            (store_add, ":raw_material_consumption", ":grain_for_bread", ":grain_for_ale"),
            
        (else_try),    
            (eq, ":cur_good", "itm_iron"),
            (party_get_slot, ":raw_material_consumption", ":center_no", slot_center_smithies),
            (val_mul, ":raw_material_consumption", 3),
            
        (else_try),    
            (eq, ":cur_good", "itm_wool"),
            (party_get_slot, ":raw_material_consumption", ":center_no", slot_center_wool_looms),
            (val_mul, ":raw_material_consumption", 5),

        (else_try),    
            (eq, ":cur_good", "itm_raw_flax"),
            (party_get_slot, ":raw_material_consumption", ":center_no", slot_center_linen_looms),
            (val_mul, ":raw_material_consumption", 5),

        (else_try),    
            (eq, ":cur_good", "itm_raw_leather"),
            (party_get_slot, ":raw_material_consumption", ":center_no", slot_center_tanneries),
            (val_mul, ":raw_material_consumption", 20),

        (else_try),    
            (eq, ":cur_good", "itm_raw_grapes"),
            (party_get_slot, ":raw_material_consumption", ":center_no", slot_center_wine_presses),
            (val_mul, ":raw_material_consumption", 30),

        (else_try),    
            (eq, ":cur_good", "itm_raw_olives"),
            (party_get_slot, ":raw_material_consumption", ":center_no", slot_center_olive_presses),
            (val_mul, ":raw_material_consumption", 12),

            
        (else_try),    
            (eq, ":cur_good", "itm_raw_dyes"),
            (party_get_slot, ":raw_material_consumption", ":center_no", slot_center_silk_looms),
            (val_mul, ":raw_material_consumption", 1),
        (else_try),    
            (eq, ":cur_good", "itm_rare_fabric"),
            (party_get_slot, ":raw_material_consumption", ":center_no", slot_center_silk_looms),
            (val_mul, ":raw_material_consumption", 5),
            

        (else_try),    
            (eq, ":cur_good", "itm_salt"),
            (party_get_slot, ":salt_for_beef", ":center_no", slot_center_head_cattle),
            (val_div, ":salt_for_beef", 10),
            
            (party_get_slot, ":salt_for_fish", ":center_no", slot_center_fishing_fleet),
            (val_div, ":salt_for_fish", 5),
            
            (store_add, ":raw_material_consumption", ":salt_for_beef", ":salt_for_fish"),
        (try_end),
        
        (try_begin), #Reduce consumption of raw materials if their cost is high
            (gt, ":raw_material_consumption", 0),
            (store_sub, ":item_to_price_slot", slot_town_trade_good_prices_begin, trade_goods_begin),
            (store_add, ":cur_good_price_slot", ":cur_good", ":item_to_price_slot"),
            (party_get_slot, ":cur_center_price", ":center_no", ":cur_good_price_slot"),
            ##diplomacy start+ chief
            (gt, ":cur_center_price", average_price_factor),#replace the hardcoded constant 1000 with average_price_factor
            (val_mul, ":raw_material_consumption", average_price_factor),#again replace the hardcoded constant 1000 with average_price_factor
            ##diplomacy end+
            (val_div, ":raw_material_consumption", ":cur_center_price"),
        (try_end),
        
    
        
        (store_add, ":modified_consumption", ":consumer_consumption", ":raw_material_consumption"),
        (try_begin),
            (party_get_slot, ":prosperity_plus_75", ":center_no", slot_town_prosperity),
            (val_add, ":prosperity_plus_75", 75),
            (val_mul, ":modified_consumption", ":prosperity_plus_75"),
            (val_div, ":modified_consumption", 125),
        (try_end),
        

        (assign, reg0, ":modified_consumption"), #modded by prosperity
        (assign, reg1, ":raw_material_consumption"),
        (assign, reg2, ":consumer_consumption"),                
    ]),

    # output: reg0 = hardship_index
    ("center_get_goods_availability", 
    [
        (store_script_param, ":center_no", 1),

        (assign, ":hardship_index", 0),
        (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),

            # Must have consumption of at least 4 to be relevant
            # This prevents perishables and raw materials from having a major impact
            (try_begin),
                (is_between, ":center_no", villages_begin, villages_end),
                (item_get_slot, ":consumer_consumption", ":cur_good", slot_item_rural_demand),
            (else_try),
                (item_get_slot, ":consumer_consumption", ":cur_good", slot_item_urban_demand),
            (try_end),
            (gt, ":consumer_consumption", 2),

            (store_div, ":max_impact", ":consumer_consumption", 4),

            # High-demand items like grain tend to have much more dramatic price differentiation,
            # so they yield substantially higher results than low-demand items
            (store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
            (val_add, ":cur_good_price_slot", slot_town_trade_good_prices_begin),
            (party_get_slot, ":price", ":center_no", ":cur_good_price_slot"),

            # (store_sub, ":price_differential", ":price", 950),       #MOTO chief adjust game prosperity levels
            (store_sub, ":price_differential", ":price", 1000),
            (gt, ":price_differential", 200), #was 100

            (val_div, ":price_differential", 200),
            (val_min, ":price_differential", ":max_impact"),

            (val_add, ":hardship_index", ":price_differential"),
        (try_end),

        (assign, reg0, ":hardship_index"),

        (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_party_name, s4, ":center_no"),
            (display_message, "@{!}DEBUG -- hardship index for {s4} = {reg0}"),
        (try_end),
    ]),

  # output: reg0 = production
  ("good_price_affects_good_production",
  [
    (store_script_param, ":center", 1),     
    (store_script_param, ":input_item_no", 2),     
    (store_script_param, ":production", 3),     
    (store_script_param, ":impact_divisor", 4),

    #(assign, reg4, ":production"),

    (try_begin),
        (gt, ":production", 0), # let's take -20 as the zero production rate, although in actuality production can go lower, representing increased demand
    
        (store_sub, ":input_good_price_slot", ":input_item_no", trade_goods_begin),
        (val_add, ":input_good_price_slot", slot_town_trade_good_prices_begin),
        (party_get_slot, ":input_price", ":center", ":input_good_price_slot"),
    
        (try_begin),
          (is_between, ":center", towns_begin, towns_end),

          (val_mul, ":input_price", 4),
          (assign, ":number_of_villages", 4),
          (try_for_range, ":village_no", villages_begin, villages_end),
            (party_slot_eq, ":village_no", slot_village_bound_center, ":center"),
            (party_get_slot, ":input_price_at_village", ":village_no", ":input_good_price_slot"),
            (val_add, ":input_price", ":input_price_at_village"),
            (val_add, ":number_of_villages", 1),
          (try_end),          

          (val_div, ":input_price", ":number_of_villages"),
        (try_end),

        # 1/2 impact for low prices
        (try_begin),
            (lt, ":input_price", average_price_factor),
            (val_mul, ":impact_divisor", 2),
        (try_end),

        (try_begin),
            (gt, ":impact_divisor", 1),
            (val_sub, ":input_price", average_price_factor),
            (val_div, ":input_price", ":impact_divisor"),
            (val_add, ":input_price", average_price_factor),
        (try_end),

        (val_mul, ":production", average_price_factor),
        (val_div, ":production", ":input_price"),

        #(assign, reg5, ":production"),
        #(assign, reg3, ":input_price"),
        #(str_store_item_name, s4, ":input_item_no"),
        #(display_message, "@{s4} price of {reg3} reduces production from {reg4} to {reg5}"),
    (try_end),
            
    (assign, reg0, ":production"),    
  ]),
]
