"""
This file contains all party slots.

The first entry is the slot name (`slot_...`), the second entry is the number of slots
it actually allocates. For example,

    ['a', 10]

means that the slot `slot_a` actually requires 10 slots, implicitly declared by
    `slot_a` + i in the code.
"""

from source.module_constants import num_party_loot_slots


slots = [
    ['party_type', 1],  # spt_caravan, spt_town, spt_castle
    ['party_save_icon', 1],
    ['party_retreat_flag', 1],
    ['party_ignore_player_until', 1],
    ['party_ai_state', 1],
    ['party_ai_object', 1],

    ['town_lord', 1],
    ['party_ai_substate', 1],
    ['cattle_driven_by_player', 1],

    # scenes; set during game_start
    ['castle_exterior', 0],  # same id as town_center
    ['town_center', 1],
    ['town_castle', 1],
    ['town_prison', 1],
    ['town_tavern', 1],
    ['town_store', 1],
    ['town_arena', 1],
    ['town_alley', 1],
    ['town_walls', 1],

    ['center_culture', 1],

    # the troop used on each role
    ['town_tavernkeeper', 1],
    ['town_weaponsmith', 1],
    ['town_armorer', 1],
    ['town_merchant', 1],
    ['town_horse_merchant', 1],
    ['town_elder', 1],

    # player relation
    ['center_player_relation', 1],

    ['center_siege_with_belfry', 1],  # center requires siege tower (belfry)
    ['center_last_taken_by_troop', 1],

    # party will follow this party if set:
    ['party_commander_party', 1],
    ['party_following_player', 1],
    ['party_follow_player_until_time', 1],
    ['party_dont_follow_player_until_time', 1],

    ['village_raided_by', 1],
    ['village_state', 1],  # svs_normal, svs_being_raided, svs_looted, svs_recovering, svs_deserted
    ['village_raid_progress', 1],
    ['village_recover_progress', 1],
    ['village_smoke_added', 1],
    ['village_infested_by_bandits', 1],

    ['center_last_player_alarm_hour', 1],

    ['village_player_can_not_steal_cattle', 1],

    ['center_accumulated_rents', 1],  # collected automatically by NPC lords
    ['center_accumulated_tariffs', 1],  # collected automatically by NPC lords #TEMPERED chief USED ON LOOT WAGON TO STORE GOLD AFTER TOWN TRADE
    ['town_wealth', 1],  # total amount of accumulated wealth in the center, pays for the garrison
    ['town_prosperity', 1],  # affects the amount of wealth generated
    ['town_player_odds', 1],

    ['party_last_toll_paid_hours', 1],
    ['party_food_store', 1],  # used for sieges
    ['center_is_besieged_by', 1],  # used for sieges
    ['center_last_spotted_enemy', 1],

    ['party_cached_strength', 1],
    ['party_nearby_friend_strength', 1],
    ['party_nearby_enemy_strength', 1],
    ['party_follower_strength', 1],

    ['town_reinforcement_party_template', 1],
    ['center_original_faction', 1],
    ['center_ex_faction', 1],

    ['party_follow_me', 1],
    ['center_siege_begin_hours', 1],  # used for sieges
    ['center_siege_hardness', 1],

    ['center_sortie_strength', 1],
    ['center_sortie_enemy_strength', 1],

    ['party_last_in_combat', 1],  # used for AI
    ['party_last_in_home_center', 1],  # used for AI
    ['party_leader_last_courted', 1],  # used for AI
    ['party_last_in_any_center', 1],  # used for AI

    ['party_cabadrin_orders_begin', 8],
    ['party_cabadrin_orders_end', 0],

    ['center_npc_volunteer_troop_type', 1],
    ['center_npc_volunteer_troop_amount', 1],
    ['center_mercenary_troop_type', 1],
    ['center_mercenary_troop_amount', 1],
    ['center_mercenary_troop_type_2', 1],
    ['center_mercenary_troop_amount_2', 1],
    ['center_volunteer_troop_type', 1],
    ['center_volunteer_troop_amount', 1],

    # troop used as profession on center
    ['center_ransom_broker', 1],
    ['center_tavern_traveler', 1],
    ['center_traveler_info_faction', 1],
    ['center_tavern_bookseller', 1],
    ['center_tavern_minstrel', 1],

    ['party_next_looted_item_slot', 1],
    ['party_looted_item_1', num_party_loot_slots],
    ['party_looted_item_1_modifier', num_party_loot_slots],

    ['village_bound_center', 1],
    ['village_market_town', 1],
    ['village_farmer_party', 1],
    ['party_home_center', 1],

    ['center_current_improvement', 1],
    ['center_improvement_end_hour', 1],

    ['party_last_traded_center', 1],

    ['village_improvements_begin', 0],

    ['center_has_manor', 1],
    ['center_has_fish_pond', 1],
    ['center_has_watch_tower', 1],
    ['center_has_school', 1],

    ['center_has_temple1', 1],
    ['center_has_temple2', 1],
    ['center_has_temple3', 1],
    ['center_has_temple5', 1],

    ['walled_center_improvements_begin', 0],

    ['center_has_messenger_post', 1],  # town, castle, village

    ['village_improvements_end', 0],

    ['center_has_prisoner_tower', 1],  # town, castle

    ['center_has_monastery1', 1],
    ['center_has_monastery2', 1],
    ['center_has_monastery3', 1],
    ['center_has_chapel5', 1],
    ['center_has_blacksmith', 1],
    ['center_has_guild', 1],
    ['center_has_university', 1],
    ['center_has_shrine5', 1],

    ['walled_center_improvements_end', 0],

    ['center_player_enterprise', 1],  # the item produced in the center by the enterprise
    ['center_player_enterprise_production_order', 1],  # 0 = sell; 1 = store
    ['center_player_enterprise_days_until_complete', 1],

    ['center_last_reconnoitered_by_faction_time', 50],  # increase if kingdoms > 50
    ['center_has_bandits', 1],
    ['town_has_tournament', 1],
    ['town_tournament_max_teams', 1],
    ['town_tournament_max_team_size', 1],
    ['center_faction_when_oath_renounced', 1],

    # 10 slots for walkers
    ['center_walker_0_troop', 10],
    ['center_walker_0_dna', 10],
    ['center_walker_0_type', 10],

    ['town_trade_good_prices_begin', 100],  # 100 is an upper bound; change if num goods > 100

    ['town_trade_routes_begin', 14],
    ['town_trade_routes_end', 0],

    ['town_trade_route_last_arrivals_begin', 14],
    ['town_trade_route_last_arrivals_end', 0],

    ['village_number_of_cattle', 1],
    ['center_head_cattle', 1],  # dried meat, cheese, hides, butter
    ['center_head_sheep', 1],  # sausages, wool

    ['center_acres_pasture', 1],  # pasture area for grazing of cattles and sheeps, if this value is high then number of cattles and sheeps increase faster

    ['production_sources_begin', 0],
    ['center_acres_grain', 1],  # grain
    ['center_acres_olives', 1],  # olives
    ['center_acres_vineyard', 1],  # fruit
    ['center_acres_flax', 1],  # flax
    ['center_acres_dates', 1],  # dates

    ['center_fishing_fleet', 1],  # smoked fish
    ['center_salt_pans', 1],  # salt

    ['center_apiaries', 1],  # honey
    ['center_silk_farms', 1],  # silk
    ['center_kirmiz_farms', 1],  # dyes

    ['center_iron_deposits', 1],  # iron
    ['center_fur_traps', 1],  # furs

    ['center_mills', 1],  # bread
    ['center_breweries', 1],  # ale
    ['center_wine_presses', 1],  # wine
    ['center_olive_presses', 1],  # oil

    ['center_linen_looms', 1],  # linen
    ['center_silk_looms', 1],  # velvet
    ['center_wool_looms', 1],  # wool cloth

    ['center_pottery_kilns', 1],  # pottery
    ['center_smithies', 1],  # tools
    ['center_tanneries', 1],  # leatherwork

    ['center_household_gardens', 1],  # cabbages

    ['production_sources_end', 0],

    ['center_sod_local_faith', 1],  # how much religious the center is
    ['center_religion_pagan', 1],  # whether it is pagan or not

    ['town_last_nearby_fire_time', 1],
    ['town_port', 1],  # town has port
    ['town_is_coastal', 1],  # town is reachable by sea trade
    ['town_sacked', 1],
    ['town_lord_old', 1],  # MOTO tested in game_menus but never set...

    ['party_following_orders_of_troop', 1],
    ['party_orders_type', 1],
    ['party_orders_object', 1],
    ['party_orders_time', 1],

    ['party_temp_slot_1', 1],  # todo: what is this?
    ['party_under_player_suggestion', 1],  # todo: slot `set` but never `get`
    ['party_unrested_morale_penalty', 1],  # morale addition

    ['party_blind_to_other_parties', 1],

    ['spy_in_town', 1],  # number range from zero, used to check if spy is in a town and how long he has been there in hours.
    ['spy_sabotage', 1],  # sets a sabotage mission on a town equal to this number, used by spy update simple trigger
    ['well_poisoned', 1],  # tally of days a well has been poisoned
    ['spy_target_town', 1],  # the town the spy is associated with, used in simple trigger for entering town, also used by personal messenger to identify target of message
    ['spies_deployed', 1],  # tally of spy parties currently deployed
    ['party_entrenched', 1],  # 0 for not entrenched, 1 for entrenched. -1 for working on entrenchment.
    ['party_hired', 1],  # current time plus 24, party hired to aid for 24 hours
    ['party_nearby', 1],  # used to identify nearby parties. 0 for not nearby, party id for nearby
    ['message_content', 1],  # for personal messenger, holds number used for storing contents of a message, 0 for no message
    ['message_target', 1],  # for messenger scripts, stores message target party
    ['message_target_2', 1],  # for messenger scripts, stores 2nd party in message, such as a group to attack or town to meet at.
    ['party_loot_wagon', 1],  # used to store the party id of the players loot wagon, stored on p_main_party
    ['party_wagon_leader', 1],  # used to store leader id of loot wagon, stored on p_main_party
    ['loot_wagon_target', 1],  # used to store town that loot wagon will trade with, stored on p_main_party
    ['party_siege_camp', 1],  # 0 for no siege camp, 1 for siege camp, -1 for working on siege camp. player party slot
    ['center_siege_camp', 1],  # name of scene to use for sieges or sorties with a siege camp built. town or castle slot.

    ['center_blockaded', 1],
    ['center_port_blockaded', 1],
    ['center_siege_with_ram', 1],

    ['party_recruiter_needed_recruits', 1],  # Amount of recruits the employer ordered.
    ['party_recruiter_origin', 1],  # Walled center from where the recruiter was hired.
    ['village_reserved_by_recruiter', 1],  # This prevents recruiters from going to villages targeted by other recruiters.
    ['party_recruiter_needed_recruits_faction', 1],  # Alkhadias Master, you forgot this one from the PM you sent me :D
    ['party_mission_parameter_1', 1],

    ['party_mission_diplomacy', 1],

    ['party_orig_morale', 1],

    # only used for freelancer_party_backup
    ['freelancer_equip_number_items', 1],
    # todo: this 50 is arbitrary, see what this should depend on
    ['freelancer_equip_begin', 50],

    ['town_acres', 1],
    ['town_player_acres', 1],
    ['center_population', 1],
    ['town_bank_rent', 1],
    ['town_bank_upkeep', 1],
    ['town_bank_assets', 1],
    ['town_bank_debt', 1],
    ['town_bank_deadline', 1],

    ["town_arena_melee_1_num_teams", 1],
    ["town_arena_melee_1_team_size", 1],
    ["town_arena_melee_2_num_teams", 1],
    ["town_arena_melee_2_team_size", 1],
    ["town_arena_melee_3_num_teams", 1],
    ["town_arena_melee_3_team_size", 1],

    ['center_taxation', 1],
    ['village_trade_last_returned_from_market', 1],
    ['village_trade_last_arrived_to_market', 1],

    # seafare of Duh chief
    ['town_has_ship', 1],

    ["ship_center", 1],
    ["ship_time", 1],
]
