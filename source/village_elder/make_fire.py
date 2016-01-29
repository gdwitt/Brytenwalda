from source.header_operations import *
from source.header_common import s4, pos0, pos1, pos2

from source.header_dialogs import anyone, plyr

from source.module_constants import slot_village_bound_center, \
    slot_town_last_nearby_fire_time, villages_begin, villages_end, \
    village_elders_begin, village_elders_end, fire_duration, slot_village_smoke_added

from source.statement import StatementBlock


village_elder_talk_condition = StatementBlock(
    (party_get_slot, ":bound_center", "$current_town", slot_village_bound_center),

    (assign, ":num_heroes_in_dungeon", 0),
    (assign, ":num_heroes_given_parole", 0),

    (party_get_num_prisoner_stacks, ":num_stacks", ":bound_center"),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
        (party_prisoner_stack_get_troop_id, ":stack_troop", ":bound_center", ":i_stack"),
        (troop_is_hero, ":stack_troop"),
        (try_begin),
            (call_script, "script_cf_prisoner_offered_parole", ":stack_troop"),
            (party_add_members, "p_temp_party_2", ":stack_troop", 1),
            (val_add, ":num_heroes_given_parole", 1),
        (else_try),
            (party_add_members, "p_temp_party", ":stack_troop", 1),
            (val_add, ":num_heroes_in_dungeon", 1),
        (try_end),
    (try_end),

    (ge, ":num_heroes_in_dungeon", 1),
)


dialogs = [

    [anyone, "village_elder_ask_set_fire", [
        (eq, "$g_village_elder_did_not_liked_money_offered", 0),
        (party_get_slot, ":bound_center", "$current_town", slot_village_bound_center),
        (party_get_slot, ":fire_time", ":bound_center", slot_town_last_nearby_fire_time),
        (store_current_hours, ":cur_time"),
        (ge, ":fire_time", ":cur_time"),
    ],
     "We have already agreed upon this, {sir/my lady}. I will do my best. You can trust me.",
     "close_window", []],

    [anyone, "village_elder_ask_set_fire", [
        (eq, "$g_village_elder_did_not_liked_money_offered", 0),
    ],
     "A fire, {sir/madam}! Fires are dangerous! Why would you want such a thing?",
     "village_elder_ask_set_fire_1", []],

    # elder did not accepted 100 scillingas before
    [anyone, "village_elder_ask_set_fire", [
        (eq, "$g_village_elder_did_not_liked_money_offered", 1),
    ],
     "I believe that we have already discussed this issue, {sir/my lady}.",
     "village_elder_ask_set_fire_5", []],

    # elder did not accepted 100 and 200 scillingas before
    [anyone, "village_elder_ask_set_fire", [
        (eq, "$g_village_elder_did_not_liked_money_offered", 2),
    ],
     "We talked about this {sir/madam} before and your previous offers were low compared to risk you want me to take.",
     "village_elder_ask_set_fire_5", []],

    [anyone | plyr, "village_elder_ask_set_fire_1", [],
     "I have my reasons, and you will have yours -- a purse of silver. Will you do it, or not?",
     "village_elder_ask_set_fire_2", []],

    [anyone | plyr, "village_elder_ask_set_fire_1", [],
     "Given the risk you are taking, you are entitled to know my plan.",
     "village_elder_ask_set_fire_explain_plan", []],

    [anyone | plyr, "village_elder_ask_set_fire_explain_plan", [
        (party_get_slot, ":bound_center", "$g_encountered_party", slot_village_bound_center),
        (str_store_party_name, s4, ":bound_center"),
    ],
     "I wish to rescue a prisoner from {s4}. When you light the fire, the guards in {s4} will see the smoke, and some of them will rush outside to see what is going on. ",
     "village_elder_ask_set_fire_2", []],

    [anyone, "village_elder_ask_set_fire_2", [
        (gt, "$g_talk_troop_effective_relation", 9),
    ],
     "As you wish, {sir/my lady}. You have been a good friend to this village, and, even though there is a risk, we should be glad to return the favor. When do you want this fire to start?",
     "village_elder_ask_set_fire_9", []],

    [anyone, "village_elder_ask_set_fire_2", [
        (lt, "$g_talk_troop_relation", 0),
    ],
     "I'm sorry, {sir/my lady}. You will forgive me for saying this, but we don't exactly have good reason to trust you. This is too dangerous.",
     "close_window", []],

    [anyone, "village_elder_ask_set_fire_2", [],
     "As you say, {sir/my lady}. But in doing this, we are taking a very great risk. What's in it for us?",
     "village_elder_ask_set_fire_3", []],

    [anyone | plyr, "village_elder_ask_set_fire_3", [
        (store_troop_gold, ":cur_gold", "trp_player"),
        (ge, ":cur_gold", 100),
    ],
     "I can give you 100 scillingas.", "village_elder_ask_set_fire_4",
     [(assign, "$g_last_money_offer_to_elder", 100)]
     ],

    [anyone | plyr, "village_elder_ask_set_fire_3", [
        (store_troop_gold, ":cur_gold", "trp_player"),
        (ge, ":cur_gold", 200),
    ],
     "I can give you 200 scillingas.", "village_elder_ask_set_fire_6", [
         (assign, "$g_last_money_offer_to_elder", 200)]
     ],

    [anyone | plyr, "village_elder_ask_set_fire_3", [
        (store_troop_gold, ":cur_gold", "trp_player"),
        (ge, ":cur_gold", 300),
    ],
     "I can give you 300 scillingas.", "village_elder_ask_set_fire_6", [
         (assign, "$g_last_money_offer_to_elder", 300)]
     ],

    [anyone | plyr, "village_elder_ask_set_fire_3", [],
     "Never mind.", "close_window", []],

    [anyone, "village_elder_ask_set_fire_4", [
        (eq, "$g_village_elder_did_not_liked_money_offered", 0),
    ],
     "This is madness. I cannot take such a risk.", "village_elder_talk", [
         (assign, "$g_village_elder_did_not_liked_money_offered", 1),
     ]],

    [anyone | plyr, "village_elder_ask_set_fire_5", [
        (eq, "$g_village_elder_did_not_liked_money_offered", 1),
        (store_troop_gold, ":cur_gold", "trp_player"),
        (ge, ":cur_gold", 200),
    ],
     "Then let's increase your reward to 200 scillingas.",
     "village_elder_ask_set_fire_7", [
         (assign, "$g_last_money_offer_to_elder", 200)]
     ],

    [anyone | plyr, "village_elder_ask_set_fire_5", [
        (eq, "$g_village_elder_did_not_liked_money_offered", 1),
        (store_troop_gold, ":cur_gold", "trp_player"),
        (ge, ":cur_gold", 300),
    ],
     "Then let's increase your reward to 300 scillingas.",
     "village_elder_ask_set_fire_6",
     [(assign, "$g_last_money_offer_to_elder", 300)]],

    [anyone | plyr, "village_elder_ask_set_fire_5", [
        (eq, "$g_village_elder_did_not_liked_money_offered", 2),
        (store_troop_gold, ":cur_gold", "trp_player"),
        (ge, ":cur_gold", 300),
    ],
     "Then let's increase your reward to 300 scillingas. This is my last offer.",
     "village_elder_ask_set_fire_6",
     [(assign, "$g_last_money_offer_to_elder", 300)]],

    [anyone | plyr, "village_elder_ask_set_fire_5", [],
     "Never mind.", "close_window", []],

    [anyone, "village_elder_ask_set_fire_6", [],
     "Very well. You are asking me to take a very great risk, but I will do it. "
     "When do you want this fire to start?", "village_elder_ask_set_fire_9", [
         (troop_remove_gold, "trp_player", "$g_last_money_offer_to_elder"),
     ]],

    [anyone, "village_elder_ask_set_fire_7", [],
     "I cannot do such a dangerous thing for 200 scillingas.",
     "village_elder_talk", [
         (assign, "$g_village_elder_did_not_liked_money_offered", 2),
     ]],

    [anyone | plyr, "village_elder_ask_set_fire_9", [],
     "Continue with your preparations. One hour from now, I need that fire.",
     "village_elder_ask_set_fire_10", [
         (party_get_slot, ":bound_center", "$current_town", slot_village_bound_center),
         (store_current_hours, ":cur_time"),
         (val_add, ":cur_time", 1),
         (assign, ":fire_time", ":cur_time"),
         (party_set_slot, ":bound_center", slot_town_last_nearby_fire_time, ":fire_time"),
         (try_begin),
             (is_between, "$next_center_will_be_fired", villages_begin, villages_end),
             (party_get_slot, ":is_there_already_fire", "$next_center_will_be_fired", slot_village_smoke_added),
             (eq, ":is_there_already_fire", 0),
             (party_get_slot, ":fire_time", "$next_center_will_be_fired", slot_town_last_nearby_fire_time),
             (store_current_hours, ":cur_hours"),
             (store_sub, ":cur_time_sub_fire_duration", ":cur_hours", fire_duration),
             (val_sub, ":cur_time_sub_fire_duration", 1),
             (ge, ":fire_time", ":cur_time_sub_fire_duration"),
             (party_clear_particle_systems, "$next_center_will_be_fired"),
         (try_end),
         (assign, "$next_center_will_be_fired", "$current_town"),
         (assign, "$g_village_elder_did_not_liked_money_offered", 0),
     ]],

    [anyone | plyr, "village_elder_ask_set_fire_9", [
        (store_time_of_day, ":cur_day_hour"),
        (ge, ":cur_day_hour", 6),
        (lt, ":cur_day_hour", 23),
    ],
     "Do this in at the stroke of midnight. I will wait exactly one hour.",
     "village_elder_ask_set_fire_11", [
         (party_get_slot, ":bound_center", "$current_town",
          slot_village_bound_center),
         (store_time_of_day, ":cur_day_hour"),
         (store_current_hours, ":cur_time"),
         (store_sub, ":difference", 24, ":cur_day_hour"),
         # fire will be at 24 midnight today
         (store_add, ":fire_time", ":cur_time", ":difference"),
         (party_set_slot, ":bound_center", slot_town_last_nearby_fire_time, ":fire_time"),

         (try_begin),
             (is_between, "$next_center_will_be_fired", villages_begin, villages_end),
             (party_get_slot, ":is_there_already_fire", "$next_center_will_be_fired", slot_village_smoke_added),
             (eq, ":is_there_already_fire", 0),
             (party_get_slot, ":fire_time", "$next_center_will_be_fired", slot_town_last_nearby_fire_time),
             (store_current_hours, ":cur_hours"),
             (store_sub, ":cur_time_sub_fire_duration", ":cur_hours", fire_duration),
             (val_sub, ":cur_time_sub_fire_duration", 1),
             (ge, ":fire_time", ":cur_time_sub_fire_duration"),
             (party_clear_particle_systems, "$next_center_will_be_fired"),
         (try_end),

         (assign, "$next_center_will_be_fired", "$current_town"),
         (assign, "$g_village_elder_did_not_liked_money_offered", 0),
     ]],

    [anyone, "village_elder_ask_set_fire_10", [],
     "Very well, {sir/my lady}. We will make our preparations. Now you make yours.",
     "close_window", [
         (assign, ":maximum_distance", -1),
         (try_for_agents, ":cur_agent"),
             (agent_get_troop_id, ":troop_id", ":cur_agent"),
             (is_between, ":troop_id", village_elders_begin, village_elders_end),
             (agent_get_position, pos0, ":cur_agent"),
             (try_for_range, ":entry_point_id", 0, 64),
                 (entry_point_get_position, pos1, ":entry_point_id"),
                 (get_distance_between_positions, ":dist", pos0, pos1),
                 (gt, ":dist", ":maximum_distance"),
                 (assign, ":maximum_distance", ":dist"),
                 (copy_position, pos2, pos1),
                 (assign, ":village_elder_agent", ":cur_agent"),
             (try_end),

             (try_begin),
                (gt, ":maximum_distance", -1),
                (agent_set_scripted_destination, ":village_elder_agent", pos2),
             (try_end),
         (try_end),
     ]],

    [anyone, "village_elder_ask_set_fire_11", [],
     "As you wish, {sir/my lady}. May the heavens protect you.", "close_window", []
     ],
]
