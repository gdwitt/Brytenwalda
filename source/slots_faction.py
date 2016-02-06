

slots = [
    ["faction_ai_state", 1],
    ["faction_ai_object", 1],

    ["faction_marshall", 1],
    ["faction_ai_offensive_max_followers", 1],
    
    ["faction_culture", 1],
    ["faction_leader", 1],
    
    ["faction_temp_slot", 1],

    ["faction_banner", 1],

    ["faction_number_of_parties", 1],
    ["faction_state", 1],

    ["faction_adjective", 1],

    ["faction_player_alarm", 1],
    ["faction_last_mercenary_offer_time", 1],
    ["faction_recognized_player", 1],

    # troop info for factions in quick start mode.
    ["faction_quick_battle_tier_1_infantry", 1],
    ["faction_quick_battle_tier_2_infantry", 1],
    ["faction_quick_battle_tier_1_archer", 1],
    ["faction_quick_battle_tier_2_archer", 1],
    ["faction_quick_battle_tier_1_cavalry", 1],
    ["faction_quick_battle_tier_2_cavalry", 1],

    ["faction_tier_1_troop", 1],
    ["faction_tier_2_troop", 1],
    ["faction_tier_3_troop", 1],
    ["faction_tier_4_troop", 1],
    ["faction_tier_5_troop", 1],

    ["faction_deserter_troop", 1],
    ["faction_guard_troop", 1],
    ["faction_messenger_troop", 1],
    ["faction_prison_guard_troop", 1],
    ["faction_castle_guard_troop", 1],

    ["faction_town_walker_male_troop", 1],
    ["faction_town_walker_female_troop", 1],
    ["faction_village_walker_male_troop", 1],
    ["faction_village_walker_female_troop", 1],
    ["faction_town_spy_male_troop", 1],
    ["faction_town_spy_female_troop", 1],

    ["faction_has_rebellion_chance", 1],

    ["faction_instability", 1],  # last time measured

    ["faction_political_issue", 1],  # Center or marshal appointment
    ["faction_political_issue_time", 1],

    ["faction_reinforcements_a", 1],
    ["faction_reinforcements_b", 1],
    ["faction_reinforcements_c", 1],

    ["faction_num_armies", 1],
    ["faction_num_castles", 1],
    ["faction_num_towns", 1],

    ["faction_last_attacked_center", 1],
    ["faction_last_attacked_hours", 1],
    ["faction_last_safe_hours", 1],

    ["faction_num_routed_agents", 1],

    # Faction AI states
    ["faction_last_feast_start_time", 1],

    ["faction_last_offensive_concluded", 1],

    # the last time that the faction has had default or feast AI --
    # this determines lords' dissatisfaction with the campaign. Set during faction_ai script
    ["faction_ai_last_rest_time", 1],
    ["faction_ai_current_state_started", 1],

    ["faction_ai_last_decisive_event", 1],  # capture a fortress or declaration of war

    ["faction_morale_of_player_troops", 1],

    # number of factions < 50
    ["faction_truce_days_with_factions_begin", 50],
    ["faction_provocation_days_with_factions_begin", 50],
    ["faction_war_damage_inflicted_on_factions_begin", 50],

    ["faction_neighbors_begin", 50],

    ["faction_policy_time", 1],
    ["faction_centralization", 1],
    ["faction_aristocracy", 1],
    ["faction_serfdom", 1],
    ["faction_quality", 1],
    ["faction_patrol_time", 1],

    ["faction_mercantilism", 1],  # + mercantilism / - free trade
    
    # stores the formation of each group
    # todo: why is it stored in the faction?
    ["faction_d0_mem_formation", 8],
    ["faction_d0_mem_formation_space", 8],
    ["faction_d0_mem_relative_x_flag", 8],
    ["faction_d0_mem_relative_y", 8],

    ["faction_freelancer_troop", 1],
]
