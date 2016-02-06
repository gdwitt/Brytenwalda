
slots = [
    ["team_flag_situation", 1],
    ["team_faction", 1],
    ["team_starting_x", 1],
    ["team_starting_y", 1],
    ["team_reinforcement_stage", 1],

    ["team_reset_stats_begin", 0],  # reset on store_battlegroup_data
    ["team_size", 1],
    ["team_adj_size", 1],  # cavalry double counted for AI considerations
    ["team_num_infantry", 1],  # class counts
    ["team_num_archers", 1],
    ["team_num_cavalry", 1],
    ["team_level", 1],
    ["team_avg_x", 1],
    ["team_avg_y", 1],

    # Battlegroup slots (1 for each of 9 divisions)
    ["team_d0_size", 9],
    ["team_d0_percent_ranged", 9],
    ["team_d0_percent_throwers", 9],
    ["team_d0_low_ammo", 9],
    ["team_d0_level", 9],
    ["team_d0_armor", 9],
    ["team_d0_weapon_length", 9],
    ["team_d0_swung_weapon_length", 9],
    ["team_d0_front_weapon_length", 9],
    ["team_d0_front_agents", 9],  # for calculating team_d0_front_weapon_length
    ["team_d0_in_melee", 9],
    ["team_d0_enemy_supporting_melee", 9],
    ["team_d0_closest_enemy", 9],
    ["team_d0_closest_enemy_dist", 9],  # for calculating team_d0_closest_enemy
    ["team_d0_closest_enemy_special", 9],  # tracks non-cavalry for AI infantry division, infantry for AI archer division
    ["team_d0_closest_enemy_special_dist", 9],  # for calculating team_d0_closest_enemy_special
    ["team_d0_avg_x", 9],
    ["team_d0_avg_y", 9],
    ["team_reset_stats_end", 0],  # end reset on store_battlegroup_data

    ["team_d0_type", 9],
    ["team_d0_formation", 9],
    ["team_d0_formation_space", 9],
    ["team_d0_move_order", 9],  # now used only for player divisions
    ["team_d0_fclock", 9],  # now used only for player divisions
    ["team_d0_first_member", 9],
    ["team_d0_prev_first_member", 9],
    ["team_d0_speed_limit", 9],
    ["team_d0_percent_in_place", 9],
    ["team_d0_destination_x", 9],
    ["team_d0_destination_y", 9],
    ["team_d0_destination_zrot", 9],
    ["team_d0_target_team", 9],  # targeted battlegroup (team ID)
    ["team_d0_target_division", 9],  # targeted battlegroup (division ID)
    ["team_d0_order_volley", 9],
    ["team_d0_order_volley_end", 0],
    # Battlegroup slots end
]
