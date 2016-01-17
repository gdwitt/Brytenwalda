

dialogs = [

  [anyone|plyr, "member_intel_liaison", [],
   "What have you discovered?", "member_intel_liaison_results", []],


  [anyone, "start", [(is_between, "$g_talk_troop", companions_begin, companions_end),
                     (eq, "$talk_context", tc_tavern_talk),
                     (troop_slot_eq, "$g_talk_troop", slot_troop_current_mission, npc_mission_gather_intel)],
   "Greetings, stranger.", "member_intel_liaison", []],

  [anyone|plyr, "member_intel_liaison", [
],
   "What have you discovered?", "member_intel_liaison_results", []],

  [anyone|plyr, "member_intel_liaison", [],
   "It's time to pull you out. Let's leave town separately, but join me soon after", "close_window", [
   (assign, "$npc_to_rejoin_party", "$g_talk_troop"),
   ]],

  [anyone|plyr, "member_intel_liaison", [],
   "You're doing good work. Stay here for a little longer", "close_window", []],

  [anyone, "member_intel_liaison_results", [
		(store_faction_of_party, ":town_faction", "$g_encountered_party"),
		(call_script, "script_update_faction_political_notes", ":town_faction"),
		(assign, ":instability_index", reg0),
		(val_add, ":instability_index", reg0),
		(val_add, ":instability_index", reg1),

		(try_for_range, ":lord", active_npcs_begin, active_npcs_end),
			(troop_slot_eq, ":lord", slot_troop_occupation, slto_kingdom_hero),
			(store_faction_of_troop, ":lord_faction", ":lord"),
			(eq, ":lord_faction", ":town_faction"),
			(call_script, "script_update_troop_political_notes", ":lord"),
		(try_end),

		(str_store_faction_name, s12, ":town_faction"),
		(try_begin),
			(gt, ":instability_index", 60),
			(str_store_string, s11, "str_the_s12_is_a_labyrinth_of_rivalries_and_grudges_lords_ignore_their_lieges_summons_and_many_are_ripe_to_defect"),
		(else_try),
			(is_between, ":instability_index", 40, 60),
			(str_store_string, s11, "str_the_s12_is_shaky_many_lords_do_not_cooperate_with_each_other_and_some_might_be_tempted_to_defect_to_a_liege_that_they_consider_more_worthy"),
		(else_try),
			(is_between, ":instability_index", 20, 40),
			(str_store_string, s11, "str_the_s12_is_fairly_solid_some_lords_bear_enmities_for_each_other_but_they_tend_to_stand_together_against_outside_enemies"),
		(else_try),
			(lt, ":instability_index", 20),
			(str_store_string, s11, "str_the_s12_is_a_rock_of_stability_politically_speaking_whatever_the_lords_may_think_of_each_other_they_fight_as_one_against_the_common_foe"),
		(try_end),

],
   "{s11} I noticed that you have been keeping some notes about individual lords. I have annotated those with my findings.", "member_intel_liaison", []],

]