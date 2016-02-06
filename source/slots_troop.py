

slots = [
    ["troop_occupation", 1],  # 0 = free, 1 = merchant	SEE troop occupations below

    ["troop_last_talk_time", 1],
    ["troop_met", 1],  # i also use this for the courtship state -- may become cumbersome
    ["troop_courtship_state", 1],  # 2 professed admiration, 3 agreed to seek a marriage, 4 ended relationship

    ["troop_renown", 1],

    ["troop_prisoner_of_party", 1],  # important for heroes only

    ["troop_present_at_event", 1],

    ["troop_leaded_party", 1],  # important for kingdom heroes only
    ["troop_wealth", 1],  # important for kingdom heroes only
    ["troop_cur_center", 1],  # important for royal family members only (non-kingdom heroes)

    ["troop_banner_scene_prop", 1],  # important for kingdom heroes and player only

    ["troop_original_faction", 1],  # for pretenders
    ["troop_original_faction2", 1],  # for pretenders en dialogo strings chief

    ["troop_age", 1],
    ["troop_age_appearance", 1],

    ["troop_does_not_give_quest", 1],
    ["troop_player_debt", 1],
    ["troop_player_relation", 1],

    ["troop_last_persuasion_time", 1],

    ["troop_spawned_before", 1],

    ["troop_last_comment_slot", 1],

    ["troop_spouse", 1],
    ["troop_father", 1],
    ["troop_mother", 1],
    ["troop_guardian", 1],  # Usually siblings are identified by a common parent.This is used for brothers if the father is not an active npc. At some point we might introduce geneologies
    ["troop_betrothed", 1],  # Obviously superseded once troop_spouse is filled

    ["troop_love_interest_1", 1],  # each unmarried lord has three love interests
    ["troop_love_interest_2", 1],
    ["troop_love_interest_3", 1],
    ["troop_love_interests_end", 0],
    ["lady_no_messages", 1],
    ["lady_last_suitor", 1],
    ["lord_granted_courtship_permission", 1],

    ["troop_betrothal_time", 1],  # used in scheduling the wedding

    ["lady_used_tournament", 1],

    ["troop_current_rumor", 1],
    ["troop_temp_slot", 1],
    ["troop_promised_fief", 1],

    ["troop_set_decision_seed", 1],  # Does not change
    ["troop_temp_decision_seed", 1],  # Resets at recalculate_ai
    ["troop_recruitment_random", 1],  # used in a number of different places in the intrigue procedures to overcome intermediate hurdles, although not for the final calculation, might be replaced at some point by the global decision seed
    # Decision seeds can be used so that some randomness can be added to NPC decisions, without allowing the player to spam the NPC with suggestions
    # The temp decision seed is reset 24 to 48 hours after the NPC last spoke to the player, while the set seed only changes in special occasions
    # The single seed is used with varying modula to give high/low outcomes on different issues, without using a separate slot for each issue
    
    ["troop_intrigue_impatience", 1],

    ["lord_reputation_type", 1],
    ["lord_recruitment_argument", 1],  # the last argument proposed by the player to the lord
    ["lord_recruitment_candidate", 1],  # the last candidate proposed by the player to the lord

    ["troop_change_to_faction", 1],

    ["troop_first_encountered", 1],
    ["troop_home", 1],
    
    ["troop_morality_state", 1],
    ["troop_morality_type", 1],
    ["troop_morality_value", 1],

    ["troop_2ary_morality_type", 1],
    ["troop_2ary_morality_state", 1],
    ["troop_2ary_morality_value", 1],

    ["troop_town_with_contacts", 1],

    ["troop_morality_penalties", 1],  # accumulated grievances from morality conflicts

    ["troop_personalityclash_object", 1],
    # (0 - they have no problem, 1 - they have a problem)

    # 1 = pclash_penalty_to_self, 2 = pclash_penalty_to_other, 3 = pclash_penalty_to_other,
    ["troop_personalityclash_state", 1],

    ["troop_personalityclash2_object", 1],  # a string
    ["troop_personalityclash2_state", 1],

    ["troop_personalitymatch_object", 1],
    ["troop_personalitymatch_state", 1],

    ["troop_personalityclash_penalties", 1],  # accumulated grievances from personality clash

    ["troop_home_speech_delivered", 1],  # only for companions
    ["troop_discussed_rebellion", 1],    # only for pretenders

    ["lady_courtship_heroic_recited", 1],
    ["lady_courtship_allegoric_recited", 1],
    ["lady_courtship_comic_recited", 1],
    ["lady_courtship_mystic_recited", 1],
    ["lady_courtship_tragic_recited", 1],

    # NPC history slots
    ["troop_met_previously", 1],
    ["troop_turned_down_twice", 1],
    ["troop_playerparty_history", 1],

    ["troop_return_renown", 1],
    
    ["troop_custom_banner_bg_color_1", 1],
    ["troop_custom_banner_bg_color_2", 1],
    ["troop_custom_banner_charge_color_1", 1],
    ["troop_custom_banner_charge_color_2", 1],
    ["troop_custom_banner_charge_color_3", 1],
    ["troop_custom_banner_charge_color_4", 1],
    ["troop_custom_banner_bg_type", 1],
    ["troop_custom_banner_charge_type_1", 1],
    ["troop_custom_banner_charge_type_2", 1],
    ["troop_custom_banner_charge_type_3", 1],
    ["troop_custom_banner_charge_type_4", 1],
    ["troop_custom_banner_flag_type", 1],
    ["troop_custom_banner_num_charges", 1],
    ["troop_custom_banner_positioning", 1],
    ["troop_custom_banner_map_flag_type", 1],

    # conversation strings -- must be in this order!
    ["troop_strings_begin", 0],
    ["troop_intro", 1],
    ["troop_intro_response_1", 1],
    ["troop_intro_response_2", 1],
    ["troop_backstory_a", 1],
    ["troop_backstory_b", 1],
    ["troop_backstory_c", 1],
    ["troop_backstory_delayed", 1],
    ["troop_backstory_response_1", 1],
    ["troop_backstory_response_2", 1],
    ["troop_signup", 1],
    ["troop_signup_2", 1],
    ["troop_signup_response_1", 1],
    ["troop_signup_response_2", 1],
    ["troop_mentions_payment", 1],
    ["troop_payment_response", 1],
    ["troop_morality_speech", 1],
    ["troop_2ary_morality_speech", 1],
    ["troop_personalityclash_speech", 1],
    ["troop_personalityclash_speech_b", 1],
    ["troop_personalityclash2_speech", 1],
    ["troop_personalityclash2_speech_b", 1],
    ["troop_personalitymatch_speech", 1],
    ["troop_personalitymatch_speech_b", 1],
    ["troop_retirement_speech", 1],
    ["troop_rehire_speech", 1],
    ["troop_home_intro", 1],
    ["troop_home_description", 1],
    ["troop_home_description_2", 1],
    ["troop_home_recap", 1],
    ["troop_honorific", 1],
    ["troop_kingsupport_string_1", 1],
    ["troop_kingsupport_string_2", 1],
    ["troop_kingsupport_string_2a", 1],
    ["troop_kingsupport_string_2b", 1],
    ["troop_kingsupport_string_3", 1],
    ["troop_kingsupport_objection_string", 1],
    ["troop_intel_gathering_string", 1],
    ["troop_fief_acceptance_string", 1],
    ["troop_woman_to_woman_string", 1],
    ["troop_turn_against_string", 1],
    ["troop_strings_end", 0],

    ["troop_payment_request", 1],

    ["troop_kingsupport_state", 1],
    ["troop_kingsupport_argument", 1],
    ["troop_kingsupport_opponent", 1],
    ["troop_kingsupport_objection_state", 1],  # 0, default, 1, needs to voice, 2, has voiced

    ["troop_days_on_mission", 1],
    ["troop_current_mission", 1],
    ["troop_mission_object", 1],

    # Number of routed agents after battle ends.
    ["troop_player_routed_agents", 1],
    ["troop_ally_routed_agents", 1],
    ["troop_enemy_routed_agents", 1],

    # Special quest slots
    ["troop_mission_participation", 1],

    # Below are some constants to expand the political system a bit.
    # The idea is to make quarrels less random, but instead make them
    # serve a rational purpose -- as a disincentive to lords to seek

    # CONTROVERSY
    # This is used to create a more "rational choice" model of faction politics, in which lords pick fights with other lords for gain, rather than simply because of clashing personalities
    # It is intended to be a limiting factor for players and lords in their ability to intrigue against each other.
    # It represents the embroilment of a lord in internal factional disputes. In contemporary media English,
    # a lord with high "controversy" would be described as "embattled."
    # The main effect of high controversy is that it disqualifies a lord from receiving a fief or an appointment
    # It is a key political concept because it provides incentive for much of the political activity. For example,
    # Lord Red Senior is worried that his rival, Lord Blue Senior, is going to get a fied which Lord Red wants.
    # So, Lord Red turns to his protege, Lord Orange Junior, to attack Lord Blue in public. The fief goes to
    # Lord Red instead of Lord Blue, and Lord Red helps Lord Orange at a later date.
    ["troop_controversy", 1],  # Determines whether or not a troop is likely to receive fief or marshalship

    ["troop_stance_on_faction_issue", 1],  # when it happened

    ["troop_will_join_prison_break", 1],

    ["troop_duel_won", 1],  # duel mod - how many duels player won against this troop
    ["troop_duel_lost", 1],  # duel mod - how many duels player lost against this troop
    ["troop_duel_started", 1],  # duel mod - if player started dueling with this troop

    ["troop_flirted_with", 1],  # Flirting chief companeros

    ["troop_cur_xp_for_wp", 1],
    ["troop_xp_limit_for_wp", 1],
    
    ["troop_kill_count", 1],
    ["troop_wound_count", 1],

    ["troop_extra_xp_limit", 1],
    ["troop_default_type", 1],  # for different heights in battle?
    ["troop_prisoner_agreed", 1],

    # troop-troop relations (200 < number of lords + ladies + pretenders)
    ["troop_relations_begin", 200],

    ["troop_duel_challenger", 1],  # indicates a lord that has challenged player to duel, stores time + 24 hours, indicating time player has to arrive at duel.
    ["troop_duel_challenged", 1],  # indicates a lord that was challenged by player to duel, stores time + 24 hours, indicating time player has to arrive at duel.
    ["troop_poisoner", 1],  # number of times the player has poisoned someone
    ["troop_poisoned", 1],  # indicates that the troop has been poisoned by the player previously, 1 for previously poisoned

    ["troop_mission_diplomacy", 1],
    ["troop_mission_diplomacy2", 1],
    ["troop_political_stance", 1],
    # todo: clarify note below
    # Though you may assume otherwise from the name,  troop_political_stance is
    # actually used as a temporary slot (it's overwritten every time you start a conversation
    # with your chancellor about who supports whom, and in Diplomacy 3.3.2 it isn't used
    # elsewhere).
    #   I'm giving it a new name to reflect its use, to avoid confusion.
    # troop_temp_slot                    = 165 #replaces troop_political_stance

    ["troop_affiliated", 1],  # 0 is default, 1 is asked; on newer games 3 is affiliated and 4 is betrayed

    ["troop_freelancer_start_xp", 1],  # only used for player
    ["troop_freelancer_start_date", 1],  # only used for player
]
