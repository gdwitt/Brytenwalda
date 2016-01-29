from source.header_operations import *
from source.header_common import s5, reg0

from source.header_dialogs import anyone, plyr
from source.header_troops import ca_intelligence
from source.statement import StatementBlock

from ..module_constants import *


trigger_event_block = StatementBlock(

    (try_begin),
        (main_party_has_troop, ":npc"),

        (try_begin),
            (call_script, "script_npc_morale", ":npc"),
            (assign, ":npc_morale", reg0),
            # todo: this never happens: P[x < a] = 0 when x ~ U(a, 1+a)
            (lt, ":npc_morale", 20),
            # random ~ U(0, 1)
            (store_random_in_range, ":random", 0, 100),
            # random ~ U(a, 1 + a)
            (val_add, ":npc_morale", ":random"),
            # random < a never happens
            (lt, ":npc_morale", 20),
            (assign, "$npc_is_quitting", ":npc"),
        (try_end),
    (try_end),
)

trigger_dialog_block = StatementBlock(
    (gt, "$npc_is_quitting", 0),
    (eq, "$g_infinite_camping", 0),
    (try_begin),
        (main_party_has_troop, "$npc_is_quitting"),
        (neq, "$g_player_is_captive", 1),

        (start_map_conversation, "$npc_is_quitting", -1),
    (else_try),
        # todo: why this?
        (assign, "$npc_is_quitting", 0),
    (try_end),
)


dialogs = [
    [anyone, "event_triggered", [
        (eq, "$g_infinite_camping", 0),
        (store_conversation_troop, "$map_talk_troop"),
        (is_between, "$map_talk_troop", companions_begin, companions_end),
        (eq, "$map_talk_troop", "$npc_is_quitting"),
        (troop_get_slot, ":honorific", "$map_talk_troop", slot_troop_honorific),
        (str_store_string, s5, ":honorific")],

     "Excuse me {s5} -- there is something I need to tell you.",
     "companion_quitting", [
         (assign, "$npc_is_quitting", 0),
         (assign, "$player_can_persuade_npc", 1),
         (assign, "$player_can_refuse_npc_quitting", 1),
     ]],

    [anyone, "companion_quitting", [
        (store_conversation_troop, "$map_talk_troop"),
        (troop_get_slot, ":speech", "$map_talk_troop", slot_troop_retirement_speech),
        (str_store_string, s5, ":speech")],
     "{s5}", "companion_quitting_2", []
     ],

    # The companion explains his/her reasons for quitting
    [anyone, "companion_quitting_2", [
        (call_script, "script_npc_morale", "$map_talk_troop"),
    ],
     "To tell you the truth, {s21}", "companion_quitting_response", []
     ],

    [anyone|plyr, "companion_quitting_response", [],
     "Very well. You be off, then.", "companion_quitting_yes", []
     ],

    [anyone|plyr, "companion_quitting_response", [
        (eq, "$player_can_persuade_npc", 1)],
    "Perhaps I can persuade you to change your mind.", "dplmc_companion_quitting_persuasion_start", [
        (assign, "$player_can_persuade_npc", 0),
     ]],

    # Response in more formal diction.
    [anyone, "dplmc_companion_quitting_persuasion_start", [
        (troop_get_slot, ":personality", "$map_talk_troop", slot_lord_reputation_type),
        (assign, ":formal_response", 0), # accept or reject
        (try_begin),
            # Nobles and well-educated commoners answer this way.
            (this_or_next|ge, ":personality", lrep_benefactor), # includes lrep_benefactor and all kingdom lady personalities
            (is_between, ":personality", lrep_none, lrep_roguish),

            # Exclude quarrelsome and debauched. They are not inclined to mince words when they're discontent.
            (neq, ":personality", lrep_quarrelsome),
            (neq, ":personality", lrep_debauched),
            (assign, ":formal_response", 1),
        (else_try),
            # "Well-educated commoners" includes some custodians but not others.
            # (For example, in Native compare Katrin with Artimenner.)
            (eq, ":personality", lrep_custodian),

            # Checking intelligence by itself isn't enough, since there isn't all
            # that much variation at the starting levels, and many companions
            # will have their intelligence raised for party skills regardless of
            # their background.
            (store_attribute_level, ":intelligence", "$map_talk_troop", ca_intelligence),
            (ge, ":intelligence", 12),

            # As the lesser of several evils, I'll add a secondary check for Engineer,
            # which is obviously arbitrary somewhat targeted but may catch Artimenner-like
            # characters in other mods.
            (store_skill_level, ":engineer", "$map_talk_troop", "skl_engineer"),
            (ge, ":engineer", 4),
            (assign, ":formal_response", 1),
        (try_end),
        (neq, ":formal_response", 0),
    ], "Very well, I shall hear you out.", "dplmc_companion_quitting_persuasion_1", []
     ],

    # Normal response
    [anyone, "dplmc_companion_quitting_persuasion_start", [],
     "I'm listening.", "dplmc_companion_quitting_persuasion_1", []
     ],

    # This goes to the standard persuasion dialog.
    [anyone|plyr, "dplmc_companion_quitting_persuasion_1", [
    ], "We've had some good times. Things might not be going to your liking now, "
       "but stay with me a while longer and the situation will turn around.",
     "companion_quitting_persuasion", [
     ]],

    # Bribe to stay
    [anyone|plyr, "dplmc_companion_quitting_persuasion_1", [
        # The same calculation as ransoming a companion from a ransom broker.
        # (From a game balance perspective, the effect is similar: you are
        # paying to avoid losing access to your companion.)

        # cost = (20 + lvl)*lvl*5
        (store_character_level, ":companion_level", "$map_talk_troop"),
        (store_add, ":cost", ":companion_level", 20),
        (val_mul, ":cost", ":companion_level"),
        (val_mul, ":cost", 5),

        # Persuasion and leadership reduces cost
        (store_skill_level, ":persuasion", "skl_persuasion", "trp_player"),
        (store_skill_level, ":leadership", "skl_leadership", "trp_player"),
        (val_max, ":persuasion", ":leadership"),

        # cost = cost*(1 - min(persuasion, 19)/20)
        # i.e. each lvl of persuasion/leadership decreases cost by 5%
        (val_min, ":persuasion", 19),
        (store_sub, ":reduction", 20, ":persuasion"),
        (val_mul, ":cost", ":reduction"),
        (val_div, ":cost", 20),

        # Check if the player can afford it.
        (store_troop_gold, ":treasury", "trp_household_possessions"),
        (store_troop_gold, ":purse", "trp_player"),
        (store_add, ":available_funds", ":treasury", ":purse"),
        (ge, ":available_funds", ":cost"),

        (assign, reg0, ":cost"),
        (assign, "$temp", ":cost"),  # store for the next dialog
     ], "Would {reg0} denars convince you to remain a while longer?",
     "dplmc_companion_quitting_persuasion_bribe", [
         (assign, "$player_can_persuade_npc", 0),
     ]],

    # Return to previous dialog
    [anyone|plyr, "dplmc_companion_quitting_persuasion_1", [],
     "Actually, nevermind. I meant to say something else.", "companion_quitting_response", [
        (assign, "$player_can_persuade_npc", 1),
     ]],

    # Player bribed companion to stay
    [anyone, "dplmc_companion_quitting_persuasion_bribe", [],
        "Hm. When you put it like that, I suppose I can stay a while longer, see if "
        "things improve.", "close_window", [

        (assign, ":cost", "$temp"),

        # Remove the gold from the player
        (store_troop_gold, ":funds", "trp_player"),
        (assign, ":remove_from_funds", ":cost"),
        (try_begin),
            (gt, ":remove_from_funds", ":funds"),
            (assign, ":remove_from_funds", ":funds"),
        (try_end),
        (troop_remove_gold, "trp_player", ":remove_from_funds"),

        # Remove any remaining gold from the treasury
        (val_sub, ":cost", ":remove_from_funds"),
        (try_begin),
            (gt, ":cost", 0),
            (call_script, "script_dplmc_withdraw_from_treasury", ":cost"),
        (try_end),

        # Reduce penalties per a successful persuasion attempt
        (troop_get_slot, ":morality_penalties", "$map_talk_troop", slot_troop_morality_penalties),
        (val_div, ":morality_penalties", 2),
        (troop_set_slot, "$map_talk_troop", slot_troop_morality_penalties, ":morality_penalties"),

        (troop_get_slot, ":personalityclash_penalties", "$map_talk_troop", slot_troop_personalityclash_penalties),
        (val_div, ":personalityclash_penalties", 2),
        (troop_set_slot, "$map_talk_troop", slot_troop_personalityclash_penalties, ":personalityclash_penalties"),
     ]],

    # Player persuaded companion to stay
    [anyone, "companion_quitting_persuasion", [
        (store_random_in_range, ":random", -2, 13),
        (store_skill_level, ":persuasion", "skl_persuasion", "trp_player"),
        (store_skill_level, ":leadership", "skl_leadership", "trp_player"),
        (val_max, ":persuasion", ":leadership"),

        (le, ":random", ":persuasion"),
     ], "Hm. When you put it like that, I suppose I can stay a while longer, see if "
       "things improve.", "close_window", [
        # Reduce penalties per a successful persuasion attempt
        (troop_get_slot, ":morality_penalties", "$map_talk_troop", slot_troop_morality_penalties),
        (val_div, ":morality_penalties", 2),
        (troop_set_slot, "$map_talk_troop", slot_troop_morality_penalties, ":morality_penalties"),

        (troop_get_slot, ":personalityclash_penalties", "$map_talk_troop", slot_troop_personalityclash_penalties),
        (val_div, ":personalityclash_penalties", 2),
        (troop_set_slot, "$map_talk_troop", slot_troop_personalityclash_penalties, ":personalityclash_penalties"),
     ]],

    # Player failed to persuade companion to stay => companion leaves
    [anyone, "companion_quitting_persuasion", [],
     "I'm sorry, but I don't see your point. I am leaving whether you like it "
     "or not.", "companion_quitting_response", []],

    # Cheat exception.
    [anyone|plyr, "companion_quitting_response", [
        (ge, "$cheat_mode", 1),
        (eq, "$player_can_refuse_npc_quitting", 1),
        ], "CHEAT -- We hang deserters in this company.", "companion_quitting_no", []
     ],

    # Response to cheat.
    [anyone, "companion_quitting_no", [
        (troop_get_slot, ":talk_troop_personality", "$g_talk_troop", slot_lord_reputation_type),
        (this_or_next|eq, ":talk_troop_personality", lrep_martial),
        (this_or_next|eq, ":talk_troop_personality", lrep_selfrighteous),
        (eq, ":talk_troop_personality", lrep_quarrelsome),
     ], "I believe I misheard you. You certainly could not have been threatening me.",
     "companion_quitting_no_confirm", []
     ],

    # Default response to cheat.
    [anyone, "companion_quitting_no", [],
     "Oh... Right... Do you mean that?", "companion_quitting_no_confirm", []
     ],

    # Threaten npc and take the consequences
    [anyone|plyr, "companion_quitting_no_confirm", [],
     "Absolutely. You either leave this shield wall by my command, or are "
     "carried out on your shield.", "companion_quitting_no_confirmed", [

        (call_script, "script_dplmc_get_troop_morality_value", "$g_talk_troop", tmt_egalitarian),
        (try_begin),
            (lt, reg0, 0),
            # I am adding an exception. If you know who this applies to in Native, you
            # might agree with this character interpretation. My reasons for adding this
            # are:
            # (1) I like it when companions react to circumstances differently.
            # (2) I find this possible scenario funny.
            (call_script, "script_change_player_relation_with_troop", "$g_talk_troop", 1),
        (else_try),
            (call_script, "script_change_player_relation_with_troop", "$g_talk_troop", -5),
        (try_end),

        ## Approval/disapproval from other NPCs
        (try_for_range, ":npc", companions_begin, companions_end),
            (neq, ":npc", "$g_talk_troop"),
            (main_party_has_troop, ":npc"),
            (call_script, "script_dplmc_get_troop_morality_value", ":npc", tmt_egalitarian),
            (try_begin),
                (lt, reg0, 0),
                (call_script, "script_change_player_relation_with_troop", ":npc", 1),
            (else_try),
                (gt, reg0, 0),
                (call_script, "script_change_player_relation_with_troop", ":npc", -1),
            (try_end),
        (try_end),
     ]],

    # Regret using cheat
    [anyone|plyr, "companion_quitting_no_confirm", [],
     "No, actually I don't mean that. You are free to leave.", "companion_quitting_yes", []
     ],

    # Companion leaves.
    [anyone, "companion_quitting_yes", [],
     "Then this is farewell. Perhaps I'll see you around, {playername}.", "close_window", [
         (troop_set_slot, "$map_talk_troop", slot_troop_playerparty_history, pp_history_quit),
         (call_script, "script_retire_companion", "$map_talk_troop", 100),
     ]],

    # Cheat => Companion does not leave.
    [anyone, "companion_quitting_no_confirmed", [],
     "Hm. I suppose I'm staying, then.", "close_window", []
     ],
]
