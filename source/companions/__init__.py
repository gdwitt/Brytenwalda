from source.header_common import s3, s4, s6, reg0
from source.statement import StatementBlock
from ..header_operations import *
from ..module_constants import *

import dialog_quit


dialogs = dialog_quit.dialogs


triggers = [
    # Move unemployed NPCs around taverns
    (24 * 15, 0, 0, [
        (call_script, "script_update_companion_candidates_in_taverns"),
    ], []),

    # Process morale and determine personality clashes
    (0, 0, 24, [], [

        # Count NPCs in party (npcs_in_party) and get the "grievance_divisor",
        # which determines how fast grievances go away.
        # grievance_divisor = 100 - npcs_in_party + trp_player.skl_persuasion
        (assign, ":npcs_in_party", 0),
        (assign, ":grievance_divisor", 100),

        (try_for_range, ":npc1", companions_begin, companions_end),
            (main_party_has_troop, ":npc1"),
            (val_add, ":npcs_in_party", 1),
        (try_end),
        (val_sub, ":grievance_divisor", ":npcs_in_party"),
        (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
        (val_add, ":grievance_divisor", ":persuasion_level"),

        # Activate personality clash from 24 hours ago
        # scheduled personality clashes require at least 24hrs together
        # todo: why isn't this scheduling already guaranteed by the trigger?
        (try_begin),
             (gt, "$personality_clash_after_24_hrs", 0),
             (eq, "$disable_npc_complaints", 0),
             (try_begin),
                  (troop_get_slot, ":other_npc", "$personality_clash_after_24_hrs", slot_troop_personalityclash_object),
                  (main_party_has_troop, "$personality_clash_after_24_hrs"),
                  (main_party_has_troop, ":other_npc"),
                  (assign, "$npc_with_personality_clash", "$personality_clash_after_24_hrs"),
             (try_end),
             (assign, "$personality_clash_after_24_hrs", 0),
        (try_end),

        (try_for_range, ":npc", companions_begin, companions_end),
            # Reset meeting variables
            # todo: what does this do exactly?
            (troop_set_slot, ":npc", slot_troop_turned_down_twice, 0),
            (try_begin),
                (troop_slot_eq, ":npc", slot_troop_met, 1),
                (troop_set_slot, ":npc", slot_troop_met_previously, 1),
            (try_end),

            # Check for coming out of retirement
            # todo: what does this do exactly?
            (troop_get_slot, ":occupation", ":npc", slot_troop_occupation),
            (try_begin),
                (eq, ":occupation", slto_retirement),
                (troop_get_slot, ":renown_min", ":npc", slot_troop_return_renown),

                (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),

                (gt, ":player_renown", ":renown_min"),
                (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, 0),
                (troop_set_slot, ":npc", slot_troop_morality_penalties, 0),
                (troop_set_slot, ":npc", slot_troop_occupation, 0),
            (try_end),

            # Check for political issues
            # todo: what does this do exactly?
            (try_begin),
                (troop_slot_ge, ":npc", slot_troop_days_on_mission, 5),
                (troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_kingsupport),

                (troop_get_slot, ":other_npc", ":npc", slot_troop_kingsupport_opponent),

                (troop_slot_eq, ":other_npc", slot_troop_kingsupport_objection_state, 0),
                (troop_set_slot, ":other_npc", slot_troop_kingsupport_objection_state, 1),

                (try_begin),
                    (eq, "$cheat_mode", 1),
                    (str_store_troop_name, s3, ":npc"),
                    (str_store_troop_name, s4, ":other_npc"),
                    (display_message, "str_s4_ready_to_voice_objection_to_s3s_mission_if_in_party"),
                (try_end),
            (try_end),

            # If npc in the party
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

                # Change grievance over time by the factor 90/grievance_divisor
                (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
                (val_mul, ":grievance", 90),
                (val_div, ":grievance", ":grievance_divisor"),
                (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),

                (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
                (val_mul, ":grievance", 90),
                (val_div, ":grievance", ":grievance_divisor"),
                (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),

                # Affect moral by personalityclash
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash_state, 1),
                    # todo: why == 1?
                    (eq, "$disable_npc_complaints", 1),

                    # if party contains the clashing npc
                    (troop_get_slot, ":object", ":npc", slot_troop_personalityclash_object),
                    (main_party_has_troop, ":object"),
                    # reduce moral
                    (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash_state),
                (try_end),

                # Affect moral by personalityclash2
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalityclash2_state, 1),
                    # todo: why == 1?
                    (eq, "$disable_npc_complaints", 1),

                    (troop_get_slot, ":object", ":npc", slot_troop_personalityclash2_object),
                    (main_party_has_troop, ":object"),
                    (call_script, "script_reduce_companion_morale_for_clash", ":npc", ":object", slot_troop_personalityclash2_state),
                (try_end),

                # Decrease grievance by 10% for personality matches
                (try_begin),
                    (this_or_next|troop_slot_ge, ":npc", slot_troop_personalitymatch_state, 1),
                    # todo: why == 1 and not == 0?
                    (eq, "$disable_npc_complaints", 1),

                    (troop_get_slot, ":object", ":npc", slot_troop_personalitymatch_object),
                    (main_party_has_troop, ":object"),
                    (troop_get_slot, ":grievance", ":npc", slot_troop_personalityclash_penalties),
                    (val_mul, ":grievance", 9),
                    (val_div, ":grievance", 10),
                    (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, ":grievance"),
                (try_end),

                # Active personality clash 1 if at least 24 hours have passed
                (try_begin),
                    (eq, "$disable_npc_complaints", 0),
                    (eq, "$npc_with_personality_clash", 0),
                    (eq, "$npc_with_personality_clash_2", 0),
                    (eq, "$personality_clash_after_24_hrs", 0),
                    (troop_slot_eq, ":npc", slot_troop_personalityclash_state, 0),
                    (troop_get_slot, ":other_npc", ":npc", slot_troop_personalityclash_object),
                    (main_party_has_troop, ":other_npc"),
                    (assign, "$personality_clash_after_24_hrs", ":npc"),
                (try_end),

                # todo: what does this do exactly?
                (try_begin),
                    (eq, "$npc_with_political_grievance", 0),

                    (troop_slot_eq, ":npc", slot_troop_kingsupport_objection_state, 1),
                    (assign, "$npc_with_political_grievance", ":npc"),
                (try_end),
            (else_try),
                # not in party and the troop is a companion
                # todo: this seems to be related with missions, not morale.
                # move it to another trigger.
                (eq, ":occupation", slto_player_companion),

                (troop_get_slot, ":days_on_mission", ":npc", slot_troop_days_on_mission),
                (try_begin),
                    (gt, ":days_on_mission", 0),
                    (val_sub, ":days_on_mission", 1),
                    (troop_set_slot, ":npc", slot_troop_days_on_mission, ":days_on_mission"),
                (else_try),
                    # return npc after spy mission
                    (troop_slot_eq, ":npc", slot_troop_current_mission, dplmc_npc_mission_spy_request),
                    (troop_slot_ge, ":npc", dplmc_slot_troop_mission_diplomacy, 1),

                    # trp_merc_infantryt5 is the troop for failed spy missions
                    (troop_set_slot, "trp_merc_infantryt5", slot_troop_mission_object, ":npc"),
                    (assign, "$npc_to_rejoin_party", "trp_merc_infantryt5"),
                (else_try),
                    # return npc after mission
                    (troop_slot_ge, ":npc", slot_troop_current_mission, 1),

                    #If the hero can join
                    (this_or_next|neg|troop_slot_eq, ":npc", slot_troop_current_mission, npc_mission_rejoin_when_possible),
                    (hero_can_join, "p_main_party"),

                    (assign, "$npc_to_rejoin_party", ":npc"),
                (try_end),
            (try_end),
        (try_end),
    ]),
]


def _affect_morality_by_action(slot, slot_state, slot_value):
    """
    :param slot: 
    :param slot_state: 
    :param slot_value: 
    :return: 
    """
    return StatementBlock(
        (troop_slot_eq, ":npc", slot, ":action_type"),
        (troop_get_slot, ":value", ":npc", slot_value),
        (try_begin),
            (troop_slot_eq, ":npc", slot_state, tms_acknowledged),
            # npc is betrayed, major penalty to player honor and morale
            (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
            (val_mul, ":value", 2),
            (val_add, ":grievance", ":value"),
            (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),
        (else_try),
            (this_or_next|troop_slot_eq, ":npc", slot_state, tms_dismissed),
            (eq, "$disable_npc_complaints", 1),
            # npc is quietly disappointed
            (troop_get_slot, ":grievance", ":npc", slot_troop_morality_penalties),
            (val_add, ":grievance", ":value"),
            (troop_set_slot, ":npc", slot_troop_morality_penalties, ":grievance"),
        (else_try),
            # npc raises the issue for the first time
            (troop_slot_eq, ":npc", slot_state, tms_no_problem),
            (gt, ":value", ":grievance_minimum"),
            (assign, "$npc_with_grievance", ":npc"),
            (assign, "$npc_grievance_string", ":action_string"),
            (assign, "$npc_grievance_slot", slot_state),
            (assign, ":grievance_minimum", ":value"),
            (assign, "$npc_praise_not_complaint", 0),
            (try_begin),
                (lt, ":value", 0),
                (assign, "$npc_praise_not_complaint", 1),
            (try_end),
        (try_end),
    )


scripts = [
    ('initialize_companions', [
        # todo: convert these lists of commands into a single Python function
        # that accepts the values

        # Osmund
        (troop_set_slot, "trp_npc1", slot_troop_morality_type, tmt_egalitarian),  #borcha
        (troop_set_slot, "trp_npc1", slot_troop_morality_value, 4),  #osmund
        (troop_set_slot, "trp_npc1", slot_troop_2ary_morality_type, tmt_aristocratic),  #borcha
        (troop_set_slot, "trp_npc1", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc1", slot_troop_personalityclash_object, "trp_npcpictlady"),  #borcha - deshavi
        (troop_set_slot, "trp_npc1", slot_troop_personalityclash2_object, "trp_npc16cleric"),  #borcha - klethi
        (troop_set_slot, "trp_npc1", slot_troop_personalitymatch_object, "trp_npc_tradecompanion"),  #borcha - marnid
        (troop_set_slot, "trp_npc1", slot_troop_home, "p_town_2"), #Dashbiga
        (troop_set_slot, "trp_npc1", slot_troop_payment_request, 300), 
        (troop_set_slot, "trp_npc1", slot_troop_kingsupport_argument, argument_ruler),
        (troop_set_slot, "trp_npc1", slot_troop_kingsupport_opponent, "trp_npc14"), #lezalit
        (troop_set_slot, "trp_npc1", slot_troop_town_with_contacts, "p_town_2"), #ichamur
        (troop_set_slot, "trp_npc1", slot_troop_original_faction, 0), #ichamur
        (troop_set_slot, "trp_npc1", slot_lord_reputation_type, lrep_roguish), #

        #aleifr
        (troop_set_slot, "trp_npc_tradecompanion", slot_troop_morality_type, tmt_humanitarian), #marnid
        (troop_set_slot, "trp_npc_tradecompanion", slot_troop_morality_value, 2),  
        (troop_set_slot, "trp_npc_tradecompanion", slot_troop_2ary_morality_type, tmt_honest),  
        (troop_set_slot, "trp_npc_tradecompanion", slot_troop_2ary_morality_value, 1),
        (troop_set_slot, "trp_npc_tradecompanion", slot_troop_personalityclash_object, "trp_npc5"), #marnid - beheshtur
        (troop_set_slot, "trp_npc_tradecompanion", slot_troop_personalityclash2_object, "trp_npc9"), #marnid - alayen
        (troop_set_slot, "trp_npc_tradecompanion", slot_troop_personalitymatch_object, "trp_npc1"),  #marnid - borcha
        (troop_set_slot, "trp_npc_tradecompanion", slot_troop_home, "p_town_1"), #Sargoth
        (troop_set_slot, "trp_npc_tradecompanion", slot_troop_payment_request, 0), 
        (troop_set_slot, "trp_npc_tradecompanion", slot_troop_kingsupport_argument, argument_victory),
        (troop_set_slot, "trp_npc_tradecompanion", slot_troop_kingsupport_opponent, "trp_npc16cleric"), #klethi
        (troop_set_slot, "trp_npc_tradecompanion", slot_troop_town_with_contacts, "p_town_1"), #Sargoth
        (troop_set_slot, "trp_npc_tradecompanion", slot_troop_original_faction, 0), #ichamur
        (troop_set_slot, "trp_npc_tradecompanion", slot_lord_reputation_type, lrep_custodian), #lrep_custodian

        #eithne
        (troop_set_slot, "trp_npclady1", slot_troop_morality_type, tmt_humanitarian), #Ymira
        (troop_set_slot, "trp_npclady1", slot_troop_morality_value, 4),  
        (troop_set_slot, "trp_npclady1", slot_troop_2ary_morality_type, tmt_aristocratic), 
        (troop_set_slot, "trp_npclady1", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npclady1", slot_troop_personalityclash_object, "trp_npc14"), #Ymira - artimenner
        (troop_set_slot, "trp_npclady1", slot_troop_personalityclash2_object, "trp_npc8"), #Ymira - matheld
        (troop_set_slot, "trp_npclady1", slot_troop_personalitymatch_object, "trp_npc9"), #Ymira - alayen
        (troop_set_slot, "trp_npclady1", slot_troop_home, "p_town_32"), #Veluca
        (troop_set_slot, "trp_npclady1", slot_troop_payment_request, 0), 
        (troop_set_slot, "trp_npclady1", slot_troop_kingsupport_argument, argument_lords),
        (troop_set_slot, "trp_npclady1", slot_troop_kingsupport_opponent, "trp_npc5"), #klethi
        (troop_set_slot, "trp_npclady1", slot_troop_town_with_contacts, "p_town_32"), #yalen
        (troop_set_slot, "trp_npclady1", slot_troop_original_faction, 0), #ichamur
        (troop_set_slot, "trp_npclady1", slot_lord_reputation_type, lrep_benefactor), #lrep_benefactor

        #athrwys
        (troop_set_slot, "trp_npc_noblebriton", slot_troop_morality_type, tmt_aristocratic), #Rolf
        (troop_set_slot, "trp_npc_noblebriton", slot_troop_morality_value, 4),  
        (troop_set_slot, "trp_npc_noblebriton", slot_troop_2ary_morality_type, tmt_honest), 
        (troop_set_slot, "trp_npc_noblebriton", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc_noblebriton", slot_troop_personalityclash_object, "trp_npc10"), #Rolf - bunduk
        (troop_set_slot, "trp_npc_noblebriton", slot_troop_personalityclash2_object, "trp_npcpictlady"), #Rolf - deshavi
        (troop_set_slot, "trp_npc_noblebriton", slot_troop_personalitymatch_object, "trp_npc5"), #Rolf - beheshtur
        (troop_set_slot, "trp_npc_noblebriton", slot_troop_home, "p_castle_49"), #Ehlerdah
        (troop_set_slot, "trp_npc_noblebriton", slot_troop_payment_request, 300), 
        (troop_set_slot, "trp_npc_noblebriton", slot_troop_kingsupport_argument, argument_claim),
        (troop_set_slot, "trp_npc_noblebriton", slot_troop_kingsupport_opponent, "trp_npc6"), #firentis
        (troop_set_slot, "trp_npc_noblebriton", slot_troop_town_with_contacts, "p_town_22"), #veluca
        (troop_set_slot, "trp_npc_noblebriton", slot_troop_original_faction, 0), #ichamur
        (troop_set_slot, "trp_npc_noblebriton", slot_lord_reputation_type, lrep_cunning), #lrep_cunning)

        #frioc
        (troop_set_slot, "trp_npc5", slot_troop_morality_type, tmt_egalitarian),  #beheshtur
        (troop_set_slot, "trp_npc5", slot_troop_morality_value, 3),  #beheshtur
        (troop_set_slot, "trp_npc5", slot_troop_2ary_morality_type, -1),
        (troop_set_slot, "trp_npc5", slot_troop_2ary_morality_value, 0),
        (troop_set_slot, "trp_npc5", slot_troop_personalityclash_object, "trp_npc_tradecompanion"),  #beheshtur - marnid
        (troop_set_slot, "trp_npc5", slot_troop_personalityclash2_object, "trp_npclady2"),  #beheshtur- katrin
        (troop_set_slot, "trp_npc5", slot_troop_personalitymatch_object, "trp_npc_noblebriton"),  #beheshtur - rolf
        (troop_set_slot, "trp_npc5", slot_troop_home, "p_village_64"), #Halmar
        (troop_set_slot, "trp_npc5", slot_troop_payment_request, 400),
        (troop_set_slot, "trp_npc5", slot_troop_kingsupport_argument, argument_ruler),
        (troop_set_slot, "trp_npc5", slot_troop_kingsupport_opponent, "trp_npc9"), #firentis
        (troop_set_slot, "trp_npc5", slot_troop_town_with_contacts, "p_town_17"), #tulga
        (troop_set_slot, "trp_npc5", slot_troop_original_faction, "fac_kingdom_8"), #khergit
        (troop_set_slot, "trp_npc5", slot_lord_reputation_type, lrep_cunning), #

        #bodero
        (troop_set_slot, "trp_npc6", slot_troop_morality_type, tmt_humanitarian), #firenz
        (troop_set_slot, "trp_npc6", slot_troop_morality_value, 2),  #beheshtur
        (troop_set_slot, "trp_npc6", slot_troop_2ary_morality_type, tmt_honest),
        (troop_set_slot, "trp_npc6", slot_troop_2ary_morality_value, 1),
        (troop_set_slot, "trp_npc6", slot_troop_personalityclash_object, "trp_npclady2"), #firenz
        (troop_set_slot, "trp_npc6", slot_troop_personalityclash2_object, "trp_npc13"), #firenz - nizar
        (troop_set_slot, "trp_npc6", slot_troop_personalitymatch_object, "trp_npc12"),  #firenz - jeremus
        (troop_set_slot, "trp_npc6", slot_troop_home, "p_town_10"), #Suno
        (troop_set_slot, "trp_npc6", slot_troop_payment_request, 0),
        (troop_set_slot, "trp_npc6", slot_troop_kingsupport_argument, argument_victory),
        (troop_set_slot, "trp_npc6", slot_troop_kingsupport_opponent, "trp_npc8"), #firentis
        (troop_set_slot, "trp_npc6", slot_troop_town_with_contacts, "p_town_27"), #uxkhal
        (troop_set_slot, "trp_npc6", slot_troop_original_faction, "fac_kingdom_13"), #swadia
        (troop_set_slot, "trp_npc6", slot_lord_reputation_type, lrep_upstanding), #

        
        #bridei
        (troop_set_slot, "trp_npcpictlady", slot_troop_morality_type, tmt_egalitarian),  #deshavi
        (troop_set_slot, "trp_npcpictlady", slot_troop_morality_value, 3),  #beheshtur
        (troop_set_slot, "trp_npcpictlady", slot_troop_2ary_morality_type, -1),
        (troop_set_slot, "trp_npcpictlady", slot_troop_2ary_morality_value, 0),
        (troop_set_slot, "trp_npcpictlady", slot_troop_personalityclash_object, "trp_npc1"),  #deshavi
        (troop_set_slot, "trp_npcpictlady", slot_troop_personalityclash2_object, "trp_npc_noblebriton"),  #deshavi - rolf
        (troop_set_slot, "trp_npcpictlady", slot_troop_personalitymatch_object, "trp_npc16cleric"),  #deshavi - klethi
        (troop_set_slot, "trp_npcpictlady", slot_troop_home, "p_town_39"), #Kulum
        (troop_set_slot, "trp_npcpictlady", slot_troop_payment_request, 300),
        (troop_set_slot, "trp_npcpictlady", slot_troop_kingsupport_argument, argument_victory),
        (troop_set_slot, "trp_npcpictlady", slot_troop_kingsupport_opponent, "trp_npclady1"), #ymira
        (troop_set_slot, "trp_npcpictlady", slot_troop_town_with_contacts, "p_town_37"), #tihr
        (troop_set_slot, "trp_npcpictlady", slot_troop_original_faction, 0), #swadia
        (troop_set_slot, "trp_npcpictlady", slot_lord_reputation_type, lrep_custodian), #

        #siwi
        (troop_set_slot, "trp_npc8", slot_troop_morality_type, tmt_aristocratic), #matheld
        (troop_set_slot, "trp_npc8", slot_troop_morality_value, 3),  #beheshtur
        (troop_set_slot, "trp_npc8", slot_troop_2ary_morality_type, -1),
        (troop_set_slot, "trp_npc8", slot_troop_2ary_morality_value, 0),
        (troop_set_slot, "trp_npc8", slot_troop_personalityclash_object, "trp_npc12"), #matheld
        (troop_set_slot, "trp_npc8", slot_troop_personalityclash2_object, "trp_npclady1"), #matheld - ymira
        (troop_set_slot, "trp_npc8", slot_troop_personalitymatch_object, "trp_npc13"),  #matheld - nizar
        (troop_set_slot, "trp_npc8", slot_troop_home, "p_town_18"), #Gundig's Point
        (troop_set_slot, "trp_npc8", slot_troop_payment_request, 500),
        (troop_set_slot, "trp_npc8", slot_troop_kingsupport_argument, argument_lords),
        (troop_set_slot, "trp_npc8", slot_troop_kingsupport_opponent, "trp_npc_tradecompanion"), #marnid
        (troop_set_slot, "trp_npc8", slot_troop_town_with_contacts, "p_town_16"), #wercheg
        (troop_set_slot, "trp_npc8", slot_troop_original_faction, "fac_kingdom_5"), #nords
        (troop_set_slot, "trp_npc8", slot_lord_reputation_type, lrep_martial), #

        #lothar
        (troop_set_slot, "trp_npc9", slot_troop_morality_type, tmt_aristocratic), #alayen
        (troop_set_slot, "trp_npc9", slot_troop_morality_value, 2),  #beheshtur
        (troop_set_slot, "trp_npc9", slot_troop_2ary_morality_type, tmt_honest),
        (troop_set_slot, "trp_npc9", slot_troop_2ary_morality_value, 1),
        (troop_set_slot, "trp_npc9", slot_troop_personalityclash_object, "trp_npc13"), #alayen vs nizar
        (troop_set_slot, "trp_npc9", slot_troop_personalityclash2_object, "trp_npc_tradecompanion"), #alayen vs marnid
        (troop_set_slot, "trp_npc9", slot_troop_personalitymatch_object, "trp_npclady1"),  #alayen - ymira
        (troop_set_slot, "trp_npc9", slot_troop_home, "p_town_14"), #Rivacheg
        (troop_set_slot, "trp_npc9", slot_troop_payment_request, 300),
        (troop_set_slot, "trp_npc9", slot_troop_kingsupport_argument, argument_lords),
        (troop_set_slot, "trp_npc9", slot_troop_kingsupport_opponent, "trp_npc1"), #borcha
        (troop_set_slot, "trp_npc9", slot_troop_town_with_contacts, "p_town_14"), #reyvadin
        (troop_set_slot, "trp_npc9", slot_troop_original_faction, "fac_kingdom_4"), #vaegirs
        (troop_set_slot, "trp_npc9", slot_lord_reputation_type, lrep_martial), #

        #ceawlin
        (troop_set_slot, "trp_npc10", slot_troop_morality_type, tmt_humanitarian), #bunduk
        (troop_set_slot, "trp_npc10", slot_troop_morality_value, 2),
        (troop_set_slot, "trp_npc10", slot_troop_2ary_morality_type, tmt_egalitarian),
        (troop_set_slot, "trp_npc10", slot_troop_2ary_morality_value, 1),
        (troop_set_slot, "trp_npc10", slot_troop_personalityclash_object, "trp_npc_noblebriton"), #bunduk vs rolf
        (troop_set_slot, "trp_npc10", slot_troop_personalityclash2_object, "trp_npc14"), #bunduk vs lazalet
        (troop_set_slot, "trp_npc10", slot_troop_personalitymatch_object, "trp_npclady2"),  #bunduk likes katrin
        (troop_set_slot, "trp_npc10", slot_troop_home, "p_town_12"), #Grunwalder Castle
        (troop_set_slot, "trp_npc10", slot_troop_payment_request, 200),
        (troop_set_slot, "trp_npc10", slot_troop_kingsupport_argument, argument_ruler),
        (troop_set_slot, "trp_npc10", slot_troop_kingsupport_opponent, "trp_npcpictlady"), #nizar
        (troop_set_slot, "trp_npc10", slot_troop_town_with_contacts, "p_town_12"), #jelkala
        (troop_set_slot, "trp_npc10", slot_troop_original_faction, "fac_kingdom_3"), #rhodoks
        (troop_set_slot, "trp_npc10", slot_lord_reputation_type, lrep_benefactor), #

        
        #gwenallian
        (troop_set_slot, "trp_npclady2", slot_troop_morality_type, tmt_egalitarian),  #katrin
        (troop_set_slot, "trp_npclady2", slot_troop_morality_value, 3),
        (troop_set_slot, "trp_npclady2", slot_troop_2ary_morality_type, -1),
        (troop_set_slot, "trp_npclady2", slot_troop_2ary_morality_value, 0),
        (troop_set_slot, "trp_npclady2", slot_troop_personalityclash_object, "trp_npc6"),  #katrin vs firenz
        (troop_set_slot, "trp_npclady2", slot_troop_personalityclash2_object, "trp_npc5"),  #katrin - beheshtur
        (troop_set_slot, "trp_npclady2", slot_troop_personalitymatch_object, "trp_npc10"),  #katrin likes bunduk
        (troop_set_slot, "trp_npclady2", slot_troop_home, "p_town_13"), #Praven
        (troop_set_slot, "trp_npclady2", slot_troop_payment_request, 100),
        (troop_set_slot, "trp_npclady2", slot_troop_kingsupport_argument, argument_claim),
        (troop_set_slot, "trp_npclady2", slot_troop_kingsupport_opponent, "trp_npcengineer"), #borcha
        (troop_set_slot, "trp_npclady2", slot_troop_town_with_contacts, "p_town_13"), #praven
        (troop_set_slot, "trp_npclady2", slot_troop_original_faction, 0), #    
        (troop_set_slot, "trp_npclady2", slot_lord_reputation_type, lrep_custodian), #
        
        #orosio
        (troop_set_slot, "trp_npc12", slot_troop_morality_type, tmt_humanitarian), #jeremus
        (troop_set_slot, "trp_npc12", slot_troop_morality_value, 3),
        (troop_set_slot, "trp_npc12", slot_troop_2ary_morality_type, -1),
        (troop_set_slot, "trp_npc12", slot_troop_2ary_morality_value, 0),
        (troop_set_slot, "trp_npc12", slot_troop_personalityclash_object, "trp_npc8"), #jerem
        (troop_set_slot, "trp_npc12", slot_troop_personalityclash2_object, "trp_npcengineer"), #jeremus - artimenner
        (troop_set_slot, "trp_npc12", slot_troop_personalitymatch_object, "trp_npc6"),  #jeremus - firenz
        (troop_set_slot, "trp_npc12", slot_troop_home, "p_town_7"), #undetermined #University
        (troop_set_slot, "trp_npc12", slot_troop_payment_request, 0),
        (troop_set_slot, "trp_npc12", slot_troop_kingsupport_argument, argument_claim),
        (troop_set_slot, "trp_npc12", slot_troop_kingsupport_opponent, "trp_npc13"), #nizar
        (troop_set_slot, "trp_npc12", slot_troop_town_with_contacts, "p_town_7"), #halmar
        (troop_set_slot, "trp_npc12", slot_troop_original_faction, 0), #    
        (troop_set_slot, "trp_npc12", slot_lord_reputation_type, lrep_benefactor), #

        
        #liuva
        (troop_set_slot, "trp_npc13", slot_troop_morality_type, tmt_aristocratic), #nizar
        (troop_set_slot, "trp_npc13", slot_troop_morality_value, 3),
        (troop_set_slot, "trp_npc13", slot_troop_2ary_morality_type, -1),
        (troop_set_slot, "trp_npc13", slot_troop_2ary_morality_value, 0),
        (troop_set_slot, "trp_npc13", slot_troop_personalityclash_object, "trp_npc9"), #nizar
        (troop_set_slot, "trp_npc13", slot_troop_personalityclash2_object, "trp_npc6"), #nizar - firenz
        (troop_set_slot, "trp_npc13", slot_troop_personalitymatch_object, "trp_npc8"), #nizar - matheld
        (troop_set_slot, "trp_npc13", slot_troop_home, "p_town_33"), #Ergellon Castle
        (troop_set_slot, "trp_npc13", slot_troop_payment_request, 300),
        (troop_set_slot, "trp_npc13", slot_troop_kingsupport_argument, argument_claim),
        (troop_set_slot, "trp_npc13", slot_troop_kingsupport_opponent, "trp_npc10"), #nizar
        (troop_set_slot, "trp_npc13", slot_troop_town_with_contacts, "p_town_33"), #suno
        (troop_set_slot, "trp_npc13", slot_troop_original_faction, 0), #    
        (troop_set_slot, "trp_npc13", slot_lord_reputation_type, lrep_roguish), #

        
        #brian
        (troop_set_slot, "trp_npc14", slot_troop_morality_type, tmt_aristocratic), #lezalit
        (troop_set_slot, "trp_npc14", slot_troop_morality_value, 4),
        (troop_set_slot, "trp_npc14", slot_troop_2ary_morality_type, tmt_egalitarian),
        (troop_set_slot, "trp_npc14", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc14", slot_troop_personalityclash_object, "trp_npclady1"), #lezalit
        (troop_set_slot, "trp_npc14", slot_troop_personalityclash2_object, "trp_npc10"), #lezalit - bunduk
        (troop_set_slot, "trp_npc14", slot_troop_personalitymatch_object, "trp_npc_paintrain"), #lezalit - artimenner
        (troop_set_slot, "trp_npc14", slot_troop_home, "p_town_35"), #Ismirala Castle
        (troop_set_slot, "trp_npc14", slot_troop_payment_request, 400),
        (troop_set_slot, "trp_npc14", slot_troop_kingsupport_argument, argument_victory),
        (troop_set_slot, "trp_npc14", slot_troop_kingsupport_opponent, "trp_npclady2"), #nizar
        (troop_set_slot, "trp_npc14", slot_troop_town_with_contacts, "p_town_35"), #dhirim
        (troop_set_slot, "trp_npc14", slot_troop_original_faction, 0), #    
        (troop_set_slot, "trp_npc14", slot_lord_reputation_type, lrep_selfrighteous), #

        #agasicles 
        (troop_set_slot, "trp_npcengineer", slot_troop_morality_type, tmt_egalitarian),  #artimenner
        (troop_set_slot, "trp_npcengineer", slot_troop_morality_value, 2),
        (troop_set_slot, "trp_npcengineer", slot_troop_2ary_morality_type, tmt_honest),
        (troop_set_slot, "trp_npcengineer", slot_troop_2ary_morality_value, 1),
        (troop_set_slot, "trp_npcengineer", slot_troop_personalityclash_object, "trp_npc16cleric"), #artimenner - klethi
        (troop_set_slot, "trp_npcengineer", slot_troop_personalityclash2_object, "trp_npc12"), #artimenner - jeremus
        (troop_set_slot, "trp_npcengineer", slot_troop_personalitymatch_object, "trp_npc_grim"), ##lazalit - artimenner
        (troop_set_slot, "trp_npcengineer", slot_troop_home, "p_town_4"), #Culmarr Castle
        (troop_set_slot, "trp_npcengineer", slot_troop_payment_request, 300),
        (troop_set_slot, "trp_npcengineer", slot_troop_kingsupport_argument, argument_ruler),
        (troop_set_slot, "trp_npcengineer", slot_troop_kingsupport_opponent, "trp_npc_noblebriton"), #nizar
        (troop_set_slot, "trp_npcengineer", slot_troop_town_with_contacts, "p_town_4"), #narra
        (troop_set_slot, "trp_npcengineer", slot_lord_reputation_type, lrep_custodian), #

        #aedh
        (troop_set_slot, "trp_npc16cleric", slot_troop_morality_type, tmt_aristocratic), #klethi
        (troop_set_slot, "trp_npc16cleric", slot_troop_morality_value, 4),
        (troop_set_slot, "trp_npc16cleric", slot_troop_2ary_morality_type, tmt_humanitarian),
        (troop_set_slot, "trp_npc16cleric", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc16cleric", slot_troop_personalityclash_object, "trp_npcengineer"), #klethi
        (troop_set_slot, "trp_npc16cleric", slot_troop_personalityclash2_object, "trp_npc1"), #klethi - borcha
        (troop_set_slot, "trp_npc16cleric", slot_troop_personalitymatch_object, "trp_npcpictlady"),  #deshavi - klethi
        (troop_set_slot, "trp_npc16cleric", slot_troop_home, "p_town_30"), #Uslum
        (troop_set_slot, "trp_npc16cleric", slot_troop_payment_request, 200),
        (troop_set_slot, "trp_npc16cleric", slot_troop_kingsupport_argument, argument_lords),
        (troop_set_slot, "trp_npc16cleric", slot_troop_kingsupport_opponent, "trp_npc12"), #nizar
        (troop_set_slot, "trp_npc16cleric", slot_troop_town_with_contacts, "p_town_30"), #khudan
        (troop_set_slot, "trp_npc16cleric", slot_lord_reputation_type, lrep_roguish), #

        #ciniod
        (troop_set_slot, "trp_npc_pict1", slot_troop_morality_type, tmt_aristocratic), #Ciniod
        (troop_set_slot, "trp_npc_pict1", slot_troop_morality_value, 2),
        (troop_set_slot, "trp_npc_pict1", slot_troop_2ary_morality_type, tmt_humanitarian),
        (troop_set_slot, "trp_npc_pict1", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc_pict1", slot_troop_personalityclash_object, "trp_npclady2"), #klethi
        (troop_set_slot, "trp_npc_pict1", slot_troop_personalityclash2_object, "trp_npcengineer"), #klethi - borcha
        (troop_set_slot, "trp_npc_pict1", slot_troop_personalitymatch_object, "trp_npc_pict2"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_pict1", slot_troop_home, "p_town_39"), #Uslum
        (troop_set_slot, "trp_npc_pict1", slot_troop_payment_request, 400),
        (troop_set_slot, "trp_npc_pict1", slot_troop_kingsupport_argument, argument_lords),
        (troop_set_slot, "trp_npc_pict1", slot_troop_kingsupport_opponent, "trp_npc5"), #nizar
        (troop_set_slot, "trp_npc_pict1", slot_troop_town_with_contacts, "p_town_39"), #khudan
        (troop_set_slot, "trp_npc_pict1", slot_lord_reputation_type, lrep_martial), #

        #onuist
        (troop_set_slot, "trp_npc_pict2", slot_troop_morality_type, tmt_aristocratic), #Onuist
        (troop_set_slot, "trp_npc_pict2", slot_troop_morality_value, 2),
        (troop_set_slot, "trp_npc_pict2", slot_troop_2ary_morality_type, tmt_humanitarian),
        (troop_set_slot, "trp_npc_pict2", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc_pict2", slot_troop_personalityclash_object, "trp_npc12"), #klethi
        (troop_set_slot, "trp_npc_pict2", slot_troop_personalityclash2_object, "trp_npcpictlady"), #klethi - borcha
        (troop_set_slot, "trp_npc_pict2", slot_troop_personalitymatch_object, "trp_npc_pict1"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_pict2", slot_troop_home, "p_town_39"), #Uslum
        (troop_set_slot, "trp_npc_pict2", slot_troop_payment_request, 350),
        (troop_set_slot, "trp_npc_pict2", slot_troop_kingsupport_argument, argument_lords),
        (troop_set_slot, "trp_npc_pict2", slot_troop_kingsupport_opponent, "trp_npc_noblebriton"), #nizar
        (troop_set_slot, "trp_npc_pict2", slot_troop_town_with_contacts, "p_town_37"), #khudan
        (troop_set_slot, "trp_npc_pict2", slot_lord_reputation_type, lrep_martial), #

        #eadwin
        (troop_set_slot, "trp_npc_paintrain", slot_troop_morality_type, tmt_honest), #edwin
        (troop_set_slot, "trp_npc_paintrain", slot_troop_morality_value, 4),
        (troop_set_slot, "trp_npc_paintrain", slot_troop_2ary_morality_type, tmt_egalitarian),
        (troop_set_slot, "trp_npc_paintrain", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc_paintrain", slot_troop_personalityclash_object, "trp_npc_hammertime"), #klethi
        (troop_set_slot, "trp_npc_paintrain", slot_troop_personalityclash2_object, "trp_npc_deadeye"), #klethi - borcha
        (troop_set_slot, "trp_npc_paintrain", slot_troop_personalitymatch_object, "trp_npclady3"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_paintrain", slot_troop_home, "p_town_8"), #Uslum
        (troop_set_slot, "trp_npc_paintrain", slot_troop_payment_request, 200),
        (troop_set_slot, "trp_npc_paintrain", slot_troop_kingsupport_argument, argument_victory),
        (troop_set_slot, "trp_npc_paintrain", slot_troop_kingsupport_opponent, "trp_npc_hammertime"), #nizar
        (troop_set_slot, "trp_npc_paintrain", slot_troop_town_with_contacts, "p_town_8"), #khudan
        (troop_set_slot, "trp_npc_paintrain", slot_lord_reputation_type, lrep_martial), #

        #Mihael ap cad
        (troop_set_slot, "trp_npc_hammertime", slot_troop_morality_type, tmt_aristocratic), #mihael
        (troop_set_slot, "trp_npc_hammertime", slot_troop_morality_value, 4),
        (troop_set_slot, "trp_npc_hammertime", slot_troop_2ary_morality_type, tmt_egalitarian),
        (troop_set_slot, "trp_npc_hammertime", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc_hammertime", slot_troop_personalityclash_object, "trp_npc_paintrain"), #klethi
        (troop_set_slot, "trp_npc_hammertime", slot_troop_personalityclash2_object, "trp_npc_deadeye"), #klethi - borcha
        (troop_set_slot, "trp_npc_hammertime", slot_troop_personalitymatch_object, "trp_npclady3"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_hammertime", slot_troop_home, "p_town_23"), #licidfelh
        (troop_set_slot, "trp_npc_hammertime", slot_troop_payment_request, 150),
        (troop_set_slot, "trp_npc_hammertime", slot_troop_kingsupport_argument, argument_victory),
        (troop_set_slot, "trp_npc_hammertime", slot_troop_kingsupport_opponent, "trp_npc_paintrain"), #nizar
        (troop_set_slot, "trp_npc_hammertime", slot_troop_town_with_contacts, "p_town_15"), #khudan
        (troop_set_slot, "trp_npc_hammertime", slot_lord_reputation_type, lrep_cunning), #gdw lrep_selfrighteous

        #Inka
        (troop_set_slot, "trp_npclady3", slot_troop_morality_type, tmt_aristocratic), #Inka
        (troop_set_slot, "trp_npclady3", slot_troop_morality_value, 4),
        (troop_set_slot, "trp_npclady3", slot_troop_2ary_morality_type, tmt_humanitarian),
        (troop_set_slot, "trp_npclady3", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npclady3", slot_troop_personalityclash_object, "trp_npc_pict1"), #klethi
        (troop_set_slot, "trp_npclady3", slot_troop_personalityclash2_object, "trp_npc_pict1"), #klethi - borcha
        (troop_set_slot, "trp_npclady3", slot_troop_personalitymatch_object, "trp_npc_deadeye"),  #deshavi - klethi
        (troop_set_slot, "trp_npclady3", slot_troop_home, "p_town_2"), #Uslum
        (troop_set_slot, "trp_npclady3", slot_troop_payment_request, 150),
        (troop_set_slot, "trp_npclady3", slot_troop_kingsupport_argument, argument_victory),
        (troop_set_slot, "trp_npclady3", slot_troop_kingsupport_opponent, "trp_npc_pict1"), #nizar
        (troop_set_slot, "trp_npclady3", slot_troop_town_with_contacts, "p_town_2"), #khudan
        (troop_set_slot, "trp_npclady3", slot_lord_reputation_type, lrep_goodnatured), #gdw selfrighteous

        #Ultan
        (troop_set_slot, "trp_npc_surgeon", slot_troop_morality_type, tmt_humanitarian), 
        (troop_set_slot, "trp_npc_surgeon", slot_troop_morality_value, 4),
        (troop_set_slot, "trp_npc_surgeon", slot_troop_2ary_morality_type, tmt_honest),
        (troop_set_slot, "trp_npc_surgeon", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc_surgeon", slot_troop_personalityclash_object, "trp_npc_pict1"), #klethi
        (troop_set_slot, "trp_npc_surgeon", slot_troop_personalityclash2_object, "trp_npc_deadeye"), #klethi - borcha
        (troop_set_slot, "trp_npc_surgeon", slot_troop_personalitymatch_object, "trp_npclady3"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_surgeon", slot_troop_home, "p_town_3"), #Uslum
        (troop_set_slot, "trp_npc_surgeon", slot_troop_payment_request, 150),
        (troop_set_slot, "trp_npc_surgeon", slot_troop_kingsupport_argument, argument_victory),
        (troop_set_slot, "trp_npc_surgeon", slot_troop_kingsupport_opponent, "trp_npc_deadeye"), #nizar
        (troop_set_slot, "trp_npc_surgeon", slot_troop_town_with_contacts, "p_town_3"), #khudan
        (troop_set_slot, "trp_npc_surgeon", slot_lord_reputation_type, lrep_goodnatured), #gdw cunning

        #eadfrith
        (troop_set_slot, "trp_npc_deadeye", slot_troop_morality_type, tmt_aristocratic), #Eadfrith Cearling
        (troop_set_slot, "trp_npc_deadeye", slot_troop_morality_value, 4),
        (troop_set_slot, "trp_npc_deadeye", slot_troop_2ary_morality_type, tmt_humanitarian),
        (troop_set_slot, "trp_npc_deadeye", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc_deadeye", slot_troop_personalityclash_object, "trp_npc_surgeon"), #klethi
        (troop_set_slot, "trp_npc_deadeye", slot_troop_personalityclash2_object, "trp_npc_probulator"), #klethi - borcha
        (troop_set_slot, "trp_npc_deadeye", slot_troop_personalitymatch_object, "trp_npclady3"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_deadeye", slot_troop_home, "p_town_4"), #Uslum
        (troop_set_slot, "trp_npc_deadeye", slot_troop_payment_request, 150),
        (troop_set_slot, "trp_npc_deadeye", slot_troop_kingsupport_argument, argument_victory),
        (troop_set_slot, "trp_npc_deadeye", slot_troop_kingsupport_opponent, "trp_npc_surgeon"), #nizar
        (troop_set_slot, "trp_npc_deadeye", slot_troop_town_with_contacts, "p_town_4"), #khudan
        (troop_set_slot, "trp_npc_deadeye", slot_lord_reputation_type, lrep_cunning), #

        #matui
        (troop_set_slot, "trp_npc_probulator", slot_troop_morality_type, tmt_aristocratic), #Domnaill
        (troop_set_slot, "trp_npc_probulator", slot_troop_morality_value, 4),
        (troop_set_slot, "trp_npc_probulator", slot_troop_2ary_morality_type, tmt_egalitarian),
        (troop_set_slot, "trp_npc_probulator", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc_probulator", slot_troop_personalityclash_object, "trp_npc_grim"), #klethi
        (troop_set_slot, "trp_npc_probulator", slot_troop_personalityclash2_object, "trp_npc_irish1"), #klethi - borcha
        (troop_set_slot, "trp_npc_probulator", slot_troop_personalitymatch_object, "trp_npc_deadeye"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_probulator", slot_troop_home, "p_town_31"), #Uslum
        (troop_set_slot, "trp_npc_probulator", slot_troop_payment_request, 150),
        (troop_set_slot, "trp_npc_probulator", slot_troop_kingsupport_argument, argument_victory),
        (troop_set_slot, "trp_npc_probulator", slot_troop_kingsupport_opponent, "trp_npc_grim"), #nizar
        (troop_set_slot, "trp_npc_probulator", slot_troop_town_with_contacts, "p_town_31"), #khudan
        (troop_set_slot, "trp_npc_probulator", slot_lord_reputation_type, lrep_cunning), #gdw self-ri

        #clovis
        (troop_set_slot, "trp_npc_grim", slot_troop_morality_type, tmt_honest), #domnaill
        (troop_set_slot, "trp_npc_grim", slot_troop_morality_value, 2),
        (troop_set_slot, "trp_npc_grim", slot_troop_2ary_morality_type, tmt_egalitarian),
        (troop_set_slot, "trp_npc_grim", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc_grim", slot_troop_personalityclash_object, "trp_npc_probulator"), #klethi
        (troop_set_slot, "trp_npc_grim", slot_troop_personalityclash2_object, "trp_npc_deadeye"), #klethi - borcha
        (troop_set_slot, "trp_npc_grim", slot_troop_personalitymatch_object, "trp_npc_irish1"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_grim", slot_troop_home, "p_town_6"), #Uslum
        (troop_set_slot, "trp_npc_grim", slot_troop_payment_request, 100),
        (troop_set_slot, "trp_npc_grim", slot_troop_kingsupport_argument, argument_victory),
        (troop_set_slot, "trp_npc_grim", slot_troop_kingsupport_opponent, "trp_npc_probulator"), #nizar
        (troop_set_slot, "trp_npc_grim", slot_troop_town_with_contacts, "p_town_6"), #khudan
        (troop_set_slot, "trp_npc_grim", slot_lord_reputation_type, lrep_martial), #

        #connor
        (troop_set_slot, "trp_npc_irish1", slot_troop_morality_type, tmt_aristocratic), #Connor
        (troop_set_slot, "trp_npc_irish1", slot_troop_morality_value, 2),
        (troop_set_slot, "trp_npc_irish1", slot_troop_2ary_morality_type, tmt_honest),
        (troop_set_slot, "trp_npc_irish1", slot_troop_2ary_morality_value, -1),
        (troop_set_slot, "trp_npc_irish1", slot_troop_personalityclash_object, "trp_npc_grim"), #klethi
        (troop_set_slot, "trp_npc_irish1", slot_troop_personalityclash2_object, "trp_npc_surgeon"), #klethi - borcha
        (troop_set_slot, "trp_npc_irish1", slot_troop_personalitymatch_object, "trp_npc_probulator"),  #deshavi - klethi
        (troop_set_slot, "trp_npc_irish1", slot_troop_home, "p_castle_6"), #Rath Cormac
        (troop_set_slot, "trp_npc_irish1", slot_troop_payment_request, 100),
        (troop_set_slot, "trp_npc_irish1", slot_troop_kingsupport_argument, argument_victory),
        (troop_set_slot, "trp_npc_irish1", slot_troop_kingsupport_opponent, "trp_npc_surgeon"), #nizar
        (troop_set_slot, "trp_npc_irish1", slot_troop_town_with_contacts, "p_town_33"), #Aileach
        (troop_set_slot, "trp_npc_irish1", slot_lord_reputation_type, lrep_cunning), #

        (troop_set_slot, "trp_npc17", slot_troop_morality_type, tmt_honest),
        (troop_set_slot, "trp_npc17", slot_troop_morality_value, 1),
        (troop_set_slot, "trp_npc17", slot_troop_2ary_morality_type, -1),
        (troop_set_slot, "trp_npc17", slot_troop_2ary_morality_value, 0),
        (troop_set_slot, "trp_npc17", slot_troop_personalityclash_object, "trp_npc12"),
        (troop_set_slot, "trp_npc17", slot_troop_personalityclash2_object, "trp_npc18"),
        (troop_set_slot, "trp_npc17", slot_troop_personalitymatch_object, "trp_npc_deadeye"),
        (troop_set_slot, "trp_npc17", slot_troop_home, 0),
        (troop_set_slot, "trp_npc17", slot_troop_payment_request, 1450),
        (troop_set_slot, "trp_npc17", slot_troop_kingsupport_argument, argument_claim),
        (troop_set_slot, "trp_npc17", slot_troop_kingsupport_opponent, "trp_npc_grim"),
        (troop_set_slot, "trp_npc17", slot_troop_town_with_contacts, "p_town_22"),
        (troop_set_slot, "trp_npc17", slot_troop_original_faction, 0),
        (troop_set_slot, "trp_npc17", slot_lord_reputation_type, lrep_custodian),

        # Bronn
        (troop_set_slot, "trp_npc18", slot_troop_morality_type, tmt_humanitarian),
        (troop_set_slot, "trp_npc18", slot_troop_morality_value, 3),
        (troop_set_slot, "trp_npc18", slot_troop_2ary_morality_type, -1),
        (troop_set_slot, "trp_npc18", slot_troop_2ary_morality_value, 0),
        (troop_set_slot, "trp_npc18", slot_troop_personalityclash_object, "trp_npclady1"),
        (troop_set_slot, "trp_npc18", slot_troop_personalityclash2_object, "trp_npc17"),
        (troop_set_slot, "trp_npc18", slot_troop_personalitymatch_object, "trp_npc10"),
        (troop_set_slot, "trp_npc18", slot_troop_home, 0),
        (troop_set_slot, "trp_npc18", slot_troop_payment_request, 1450),
        (troop_set_slot, "trp_npc18", slot_troop_kingsupport_argument, argument_claim),
        (troop_set_slot, "trp_npc18", slot_troop_kingsupport_opponent, "trp_npc_grim"),
        (troop_set_slot, "trp_npc18", slot_troop_town_with_contacts, "p_town_6"),
        (troop_set_slot, "trp_npc18", slot_troop_original_faction, 0),
        (troop_set_slot, "trp_npc18", slot_lord_reputation_type, lrep_roguish),

        # Placeholder - don't hire (indicates last npc)
        # todo: why is it necessary to set attributes to him?
        (troop_set_slot, "trp_npc19", slot_troop_morality_type, tmt_egalitarian),
        (troop_set_slot, "trp_npc19", slot_troop_morality_value, 3),
        (troop_set_slot, "trp_npc19", slot_troop_2ary_morality_type, -1),
        (troop_set_slot, "trp_npc19", slot_troop_2ary_morality_value, 0),
        (troop_set_slot, "trp_npc19", slot_troop_personalityclash_object, "trp_npc16cleric"),
        (troop_set_slot, "trp_npc19", slot_troop_personalityclash2_object, "trp_npclady1"),
        (troop_set_slot, "trp_npc19", slot_troop_personalitymatch_object, "trp_npc_surgeon"),
        (troop_set_slot, "trp_npc19", slot_troop_home, 0),
        (troop_set_slot, "trp_npc19", slot_troop_payment_request, 850),
        (troop_set_slot, "trp_npc19", slot_troop_kingsupport_argument, argument_claim),
        (troop_set_slot, "trp_npc19", slot_troop_kingsupport_opponent, "trp_npc_grim"),
        (troop_set_slot, "trp_npc19", slot_troop_town_with_contacts, "p_town_5"),
        (troop_set_slot, "trp_npc19", slot_troop_original_faction, 0),
        (troop_set_slot, "trp_npc19", slot_lord_reputation_type, lrep_roguish),

        (store_sub, ":number_of_npc_slots", slot_troop_strings_end, slot_troop_intro),

        (try_for_range, ":npc", companions_begin, companions_end),
            (try_for_range, ":slot_addition", 0, ":number_of_npc_slots"),
                (store_add, ":slot", ":slot_addition", slot_troop_intro),

                (store_mul, ":string_addition", ":slot_addition", 29), #chief cambiado
                (store_add, ":string", "str_npc1_intro", ":string_addition"), 
                (val_add, ":string", ":npc"),
                (val_sub, ":string", companions_begin),

                (troop_set_slot, ":npc", ":slot", ":string"),
            (try_end),
        (try_end),

        # set personality clashes
        (try_for_range, ":companion", companions_begin, companions_end),
            (try_for_range, ":other_companion", companions_begin, companions_end),
                (neq, ":other_companion", ":companion"),
                (neg|troop_slot_eq, ":companion", slot_troop_personalityclash_object, ":other_companion"),
                (neg|troop_slot_eq, ":companion", slot_troop_personalityclash2_object, ":other_companion"),

                # todo: how come that the initial relation is set when they do not clash?
                (call_script, "script_troop_change_relation_with_troop", ":companion", ":other_companion", 7),
            (try_end),
        (try_end),

        (call_script, "script_update_companion_candidates_in_taverns"),
    ]),

    #script_update_companion_candidates_in_taverns
    # INPUT: none
    # OUTPUT: none
    ("update_companion_candidates_in_taverns", [
        (try_begin),
            (eq, "$cheat_mode", 1),
            (display_message, "str_shuffling_companion_locations"),
        (try_end),

        (try_for_range, ":troop_no", companions_begin, companions_end),
            (troop_set_slot, ":troop_no", slot_troop_cur_center, -1),
            (troop_slot_eq, ":troop_no", slot_troop_days_on_mission, 0),
            (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_inactive),

            (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),

            (store_random_in_range, ":town_no", towns_begin, towns_end),
            (try_begin),
                (neg|troop_slot_eq, ":troop_no", slot_troop_home, ":town_no"),
                (neg|troop_slot_eq, ":troop_no", slot_troop_first_encountered, ":town_no"),
                (troop_set_slot, ":troop_no", slot_troop_cur_center, ":town_no"),
                (try_begin),
                    (eq, "$cheat_mode", 1),
                    (str_store_troop_name, 4, ":troop_no"),
                    (str_store_party_name, 5, ":town_no"),
                    (display_message, "@{!}{s4} is in {s5}"),
                (try_end),
            (try_end),
        (try_end),
    ]),

    # script_recruit_troop_as_companion
    # Input: arg1 = troop_no,
    # Output: none
    ("recruit_troop_as_companion", [

        (store_script_param_1, ":troop_no"),
        (troop_set_slot, ":troop_no", slot_troop_occupation, slto_player_companion),
        (troop_set_slot, ":troop_no", slot_troop_cur_center, -1),
        (troop_set_auto_equip, ":troop_no", 0),

        (party_add_members, "p_main_party", ":troop_no", 1),
        (str_store_troop_name, s6, ":troop_no"),
        (display_message, "@{s6} has joined your party.", color_hero_news),

        (troop_set_note_available, ":troop_no", 1),

        # ACHIEVEMENT_KNIGHTS_OF_THE_ROUND
        (try_begin),
            (is_between, ":troop_no", companions_begin, companions_end),
            (store_sub, ":companion_number", ":troop_no", companions_begin),

            (set_achievement_stat, ACHIEVEMENT_KNIGHTS_OF_THE_ROUND, ":companion_number", 1),

            (assign, ":number_of_companions_hired", 0),
            (try_for_range, ":cur_companion", 0, 18),
                (get_achievement_stat, ":is_hired", ACHIEVEMENT_KNIGHTS_OF_THE_ROUND, ":cur_companion"),
                (eq, ":is_hired", 1),
                (val_add, ":number_of_companions_hired", 1),
            (try_end),

            (try_begin),
                (ge, ":number_of_companions_hired", 10),
                (unlock_achievement, ACHIEVEMENT_KNIGHTS_OF_THE_ROUND),
            (try_end),
        (try_end),
    ]),

    # Updates grievance of companions by actions that it does not like.
    ("objectionable_action", [
        (store_script_param_1, ":action_type"),
        (store_script_param_2, ":action_string"),

        (assign, ":grievance_minimum", -2),
        (try_for_range, ":npc", companions_begin, companions_end),
            (main_party_has_troop, ":npc"),

            # Primary morality check
            (try_begin),
                _affect_morality_by_action(slot_troop_morality_type,
                                           slot_troop_morality_state,
                                           slot_troop_morality_value),

            # Secondary morality check
            (else_try),
                _affect_morality_by_action(slot_troop_2ary_morality_type,
                                           slot_troop_2ary_morality_state,
                                           slot_troop_2ary_morality_value),
            (try_end),

            (try_begin),
                (gt, "$npc_with_grievance", 0),
                (eq, "$npc_praise_not_complaint", 0),
                (str_store_troop_name, 4, "$npc_with_grievance"),
                (display_message, "@{s4} looks upset."),
            (try_end),
        (try_end),
     ]),

    # todo: add comments to this script with more details
    ("post_battle_personality_clash_check", [
        (try_for_range, ":npc", companions_begin, companions_end),
            (troop_slot_eq, ":npc", slot_troop_personalityclash2_state, 0),
            (eq, "$disable_npc_complaints", 0),

            (main_party_has_troop, ":npc"),
            (neg|troop_is_wounded, ":npc"),

            (troop_get_slot, ":other_npc", ":npc", slot_troop_personalityclash2_object),
            (main_party_has_troop, ":other_npc"),
            (neg|troop_is_wounded, ":other_npc"),

            (assign, "$npc_with_personality_clash_2", ":npc"),
        (try_end),

        (try_for_range, ":npc", companions_begin, companions_end),
            (troop_slot_eq, ":npc", slot_troop_personalitymatch_state, 0),
            (eq, "$disable_npc_complaints", 0),

            (main_party_has_troop, ":npc"),
            (neg|troop_is_wounded, ":npc"),

            (troop_get_slot, ":other_npc", ":npc", slot_troop_personalitymatch_object),
            (main_party_has_troop, ":other_npc"),
            (neg|troop_is_wounded, ":other_npc"),
            (assign, "$npc_with_personality_match", ":npc"),
        (try_end),

        (try_begin),
            (gt, "$npc_with_personality_clash_2", 0),
            (try_begin),
                (eq, "$cheat_mode", 1),
                (display_message, "str_personality_clash_conversation_begins"),
            (try_end),

            (try_begin),
                (main_party_has_troop, "$npc_with_personality_clash_2"),
                (assign, "$npc_map_talk_context", slot_troop_personalityclash2_state),
                (start_map_conversation, "$npc_with_personality_clash_2"),
            (else_try),
                (assign, "$npc_with_personality_clash_2", 0),
            (try_end),
        (else_try),
            (gt, "$npc_with_personality_match", 0),
            (try_begin),
                (eq, "$cheat_mode", 1),
                (display_message, "str_personality_match_conversation_begins"),
            (try_end),

            (try_begin),
                (main_party_has_troop, "$npc_with_personality_match"),
                (assign, "$npc_map_talk_context", slot_troop_personalitymatch_state),
                (start_map_conversation, "$npc_with_personality_match"),
            (else_try),
                (assign, "$npc_with_personality_match", 0),
            (try_end),
        (try_end),
     ]),

    ("retire_companion", [
        (store_script_param_1, ":npc"),
        (store_script_param_2, ":length"),

        (remove_member_from_party, ":npc", "p_main_party"),
        (troop_set_slot, ":npc", slot_troop_personalityclash_penalties, 0),
        (troop_set_slot, ":npc", slot_troop_morality_penalties, 0),
        (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
        (store_add, ":return_renown", ":renown", ":length"),
        (troop_set_slot, ":npc", slot_troop_occupation, slto_retirement),
        (troop_set_slot, ":npc", slot_troop_return_renown, ":return_renown"),
    ]),

    # INPUT: arg1 = troop_no for companion1 arg2 = troop_no for companion2 arg3 = slot_for_clash_state
    # slot_for_clash_state means: 1=give full penalty to companion1; 2=give full penalty to companion2; 3=give penalty equally
    ("reduce_companion_morale_for_clash", [
        (store_script_param, ":companion_1", 1),
        (store_script_param, ":companion_2", 2),
        (store_script_param, ":slot_for_clash_state", 3),

        (troop_get_slot, ":clash_state", ":companion_1", ":slot_for_clash_state"),
        (troop_get_slot, ":grievance_1", ":companion_1", slot_troop_personalityclash_penalties),
        (troop_get_slot, ":grievance_2", ":companion_2", slot_troop_personalityclash_penalties),
        (try_begin),
          (eq, ":clash_state", pclash_penalty_to_self),
          (val_add, ":grievance_1", 5),
        (else_try),
          (eq, ":clash_state", pclash_penalty_to_other),
          (val_add, ":grievance_2", 5),
        (else_try),
          (eq, ":clash_state", pclash_penalty_to_both),
          (val_add, ":grievance_1", 3),
          (val_add, ":grievance_2", 3),
        (try_end),
        (troop_set_slot, ":companion_1", slot_troop_personalityclash_penalties, ":grievance_1"),
        (troop_set_slot, ":companion_2", slot_troop_personalityclash_penalties, ":grievance_2"),
    ]),
]


def _loop_quest_available_companions(*args):
    return StatementBlock(
        (try_for_range, ":i_stack", 0, ":num_stacks"),
            (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":i_stack"),
            (troop_is_hero, ":stack_troop"),
            (is_between, ":stack_troop", companions_begin, companions_end),

            (store_character_level, ":stack_level", ":stack_troop"),
            # todo: what this 15 represent? that only +15 lvl heros can be used?
            (ge, ":stack_level", 15),

            # check that hero is not being used in another quest.
            (assign, ":is_quest_hero", 0),
            (try_for_range, ":i_quest", all_quests_begin, all_quests_end),
                (check_quest_active, ":i_quest"),
                (this_or_next|quest_slot_eq, ":i_quest", slot_quest_target_troop, ":stack_troop"),
                (quest_slot_eq, ":i_quest", slot_quest_object_troop, ":stack_troop"),
                (assign, ":is_quest_hero", 1),
                # todo: it was found: break the loop.
            (try_end),
            (eq, ":is_quest_hero", 0),

            StatementBlock(*args),
        (try_end),
    )


quest = StatementBlock(
    (eq, ":quest_no", "qst_lend_companion"),
    (try_begin),
        (ge, "$g_talk_troop_faction_relation", 0),
        (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),

        # count the number of available companions for the quest
        (assign, ":total_heroes", 0),
        _loop_quest_available_companions((val_add, ":total_heroes", 1),),

        # Skip if party has no eligible heroes
        (gt, ":total_heroes", 0),

        # select a random hero (:target_hero)
        (store_random_in_range, ":random_hero", 0, ":total_heroes"),
        (assign, ":target_hero", -1),
        (assign, ":total_heroes", 0),
        _loop_quest_available_companions(
            (val_add, ":total_heroes", 1),
            (gt, ":total_heroes", ":random_hero"),
            (assign, ":target_hero", ":stack_troop")
            # todo: break the loop or the last hero is always chosen
        ),

        # I'm almost certain that by construction it always finds, but well.
        (try_begin),
            (eq, ':target_hero', -1),
            (display_debug_message, "@qst_lend_companion quest failed to find "
                                    "a hero when it should."),
        (try_end),
        (neq, ':target_hero', -1),

        # build the quest
        (assign, ":quest_target_troop", ":target_hero"),
        (store_current_day, ":quest_target_amount"),
        (val_add, ":quest_target_amount", 8),

        (assign, ":quest_importance", 1),
        (assign, ":quest_xp_reward", 500),
        (assign, ":quest_gold_reward", 400),
        (assign, ":result", ":quest_no"),
        (assign, ":quest_dont_give_again_period", 25),
    (try_end),
)
