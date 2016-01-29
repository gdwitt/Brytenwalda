from source.header_operations import *
from source.header_common import reg0, reg3

from ..module_constants import *


scripts = [
    ("initialize_aristocracy", [
        # Lord occupations, blood relationships, renown, Age and reputation

        (try_for_range, ":cur_troop", kings_begin, kings_end),
            (troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),
        (try_end),

        # king ages
        (troop_set_slot, "trp_kingdom_1_lord", slot_troop_age, 37),
        (troop_set_slot, "trp_kingdom_2_lord", slot_troop_age, 44),
        (troop_set_slot, "trp_kingdom_3_lord", slot_troop_age, 30),
        (troop_set_slot, "trp_kingdom_4_lord", slot_troop_age, 37),
        (troop_set_slot, "trp_kingdom_5_lord", slot_troop_age, 40),
        (troop_set_slot, "trp_kingdom_6_lord", slot_troop_age, 29),
        (troop_set_slot, "trp_kingdom_7_lord", slot_troop_age, 46),
        (troop_set_slot, "trp_kingdom_8_lord", slot_troop_age, 36),
        (troop_set_slot, "trp_kingdom_9_lord", slot_troop_age, 43),
        (troop_set_slot, "trp_kingdom_10_lord", slot_troop_age, 47),
        (troop_set_slot, "trp_kingdom_11_lord", slot_troop_age, 33),
        (troop_set_slot, "trp_kingdom_12_lord", slot_troop_age, 70),
        (troop_set_slot, "trp_kingdom_13_lord", slot_troop_age, 32),
        (troop_set_slot, "trp_kingdom_14_lord", slot_troop_age, 44),
        (troop_set_slot, "trp_kingdom_15_lord", slot_troop_age, 42),
        (troop_set_slot, "trp_kingdom_16_lord", slot_troop_age, 41),
        (troop_set_slot, "trp_kingdom_17_lord", slot_troop_age, 46),
        (troop_set_slot, "trp_kingdom_18_lord", slot_troop_age, 46),
        (troop_set_slot, "trp_kingdom_19_lord", slot_troop_age, 41),
        (troop_set_slot, "trp_kingdom_20_lord", slot_troop_age, 45),
        (troop_set_slot, "trp_kingdom_21_lord", slot_troop_age, 31),
        (troop_set_slot, "trp_kingdom_22_lord", slot_troop_age, 32),
        (troop_set_slot, "trp_kingdom_23_lord", slot_troop_age, 31),
        (troop_set_slot, "trp_kingdom_24_lord", slot_troop_age, 31),
        (troop_set_slot, "trp_kingdom_25_lord", slot_troop_age, 36),
        (troop_set_slot, "trp_kingdom_26_lord", slot_troop_age, 40),
        (troop_set_slot, "trp_kingdom_27_lord", slot_troop_age, 61),
        (troop_set_slot, "trp_kingdom_28_lord", slot_troop_age, 46),
        (troop_set_slot, "trp_kingdom_29_lord", slot_troop_age, 35),
        (troop_set_slot, "trp_kingdom_30_lord", slot_troop_age, 56),
        (troop_set_slot, "trp_kingdom_31_lord", slot_troop_age, 39),

        # Ladies age
        (troop_set_slot, "trp_kingdom_1_lady_1", slot_troop_age, 44),
        (troop_set_slot, "trp_kingdom_1_lady_2", slot_troop_age, 22),
        (troop_set_slot, "trp_kingdom_1_lady_3", slot_troop_age, 10),

        (troop_set_slot, "trp_kingdom_2_lady_1", slot_troop_age, 42),
        (troop_set_slot, "trp_kingdom_2_lady_2", slot_troop_age, 16),
        (troop_set_slot, "trp_kingdom_2_lady_3", slot_troop_age, 38),

        (troop_set_slot, "trp_kingdom_3_lady_1", slot_troop_age, 49),
        (troop_set_slot, "trp_kingdom_3_lady_2", slot_troop_age, 17),
        (troop_set_slot, "trp_kingdom_3_lady_3", slot_troop_age, 15),

        (troop_set_slot, "trp_kingdom_4_lady_1", slot_troop_age, 37),
        (troop_set_slot, "trp_kingdom_4_lady_4", slot_troop_age, 34),
        (troop_set_slot, "trp_kingdom_4_lady_2", slot_troop_age, 26),
        (troop_set_slot, "trp_kingdom_4_lady_3", slot_troop_age, 23),
        (troop_set_slot, "trp_kingdom_4_lady_5", slot_troop_age, 21),
        (troop_set_slot, "trp_kingdom_4_lady_6", slot_troop_age, 15),

        (troop_set_slot, "trp_kingdom_5_lady_1", slot_troop_age, 44),
        (troop_set_slot, "trp_kingdom_5_lady_2", slot_troop_age, 49),
        (troop_set_slot, "trp_kingdom_5_lady_6", slot_troop_age, 36),
        (troop_set_slot, "trp_kingdom_5_lady_7", slot_troop_age, 32),
        (troop_set_slot, "trp_kingdom_5_lady_3", slot_troop_age, 16),
        (troop_set_slot, "trp_kingdom_5_lady_4", slot_troop_age, 16),
        (troop_set_slot, "trp_kingdom_5_lady_5", slot_troop_age, 14),

        (troop_set_slot, "trp_kingdom_6_lady_1", slot_troop_age, 41),
        (troop_set_slot, "trp_kingdom_6_lady_2", slot_troop_age, 14),

        (troop_set_slot, "trp_kingdom_7_lady_1", slot_troop_age, 16),

        (troop_set_slot, "trp_kingdom_8_lady_1", slot_troop_age, 37),
        (troop_set_slot, "trp_kingdom_8_lady_2", slot_troop_age, 35),
        (troop_set_slot, "trp_kingdom_8_lady_4", slot_troop_age, 39),
        (troop_set_slot, "trp_kingdom_8_lady_3", slot_troop_age, 16),
        (troop_set_slot, "trp_kingdom_8_lady_5", slot_troop_age, 20),
        (troop_set_slot, "trp_kingdom_8_lady_6", slot_troop_age, 22),

        (troop_set_slot, "trp_kingdom_9_lady_1", slot_troop_age, 48),
        (troop_set_slot, "trp_kingdom_9_lady_6", slot_troop_age, 47),
        (troop_set_slot, "trp_kingdom_9_lady_2", slot_troop_age, 10),
        (troop_set_slot, "trp_kingdom_9_lady_7", slot_troop_age, 36),
        (troop_set_slot, "trp_kingdom_9_lady_5", slot_troop_age, 21),
        (troop_set_slot, "trp_kingdom_9_lady_3", slot_troop_age, 15),
        (troop_set_slot, "trp_kingdom_9_lady_4", slot_troop_age, 17),
        (troop_set_slot, "trp_kingdom_9_lady_8", slot_troop_age, 18),
        (troop_set_slot, "trp_kingdom_9_lady_9", slot_troop_age, 19),

        (troop_set_slot, "trp_kingdom_10_lady_1", slot_troop_age, 30),

        (troop_set_slot, "trp_kingdom_11_lady_5", slot_troop_age, 27),
        (troop_set_slot, "trp_kingdom_11_lady_1", slot_troop_age, 27),
        (troop_set_slot, "trp_kingdom_11_lady_2", slot_troop_age, 26),
        (troop_set_slot, "trp_kingdom_11_lady_3", slot_troop_age, 21),
        (troop_set_slot, "trp_kingdom_11_lady_4", slot_troop_age, 21),
        (troop_set_slot, "trp_kingdom_11_lady_6", slot_troop_age, 16),
        (troop_set_slot, "trp_kingdom_11_lady_7", slot_troop_age, 18),

        (troop_set_slot, "trp_kingdom_12_lady_1", slot_troop_age, 42),
        (troop_set_slot, "trp_kingdom_12_lady_4", slot_troop_age, 47),
        (troop_set_slot, "trp_kingdom_12_lady_2", slot_troop_age, 23),
        (troop_set_slot, "trp_kingdom_12_lady_3", slot_troop_age, 16),

        (troop_set_slot, "trp_kingdom_13_lady_1", slot_troop_age, 43),
        (troop_set_slot, "trp_kingdom_13_lady_2", slot_troop_age, 32),
        (troop_set_slot, "trp_kingdom_13_lady_5", slot_troop_age, 34),
        (troop_set_slot, "trp_kingdom_13_lady_3", slot_troop_age, 21),
        (troop_set_slot, "trp_kingdom_13_lady_4", slot_troop_age, 16),

        (troop_set_slot, "trp_kingdom_13_lady_6", slot_troop_age, 17),
        (troop_set_slot, "trp_kingdom_13_lady_7", slot_troop_age, 17),
        (troop_set_slot, "trp_kingdom_13_lady_8", slot_troop_age, 15),

        (troop_set_slot, "trp_kingdom_14_lady_1", slot_troop_age, 45),
        (troop_set_slot, "trp_kingdom_14_lady_2", slot_troop_age, 16),

        (troop_set_slot, "trp_kingdom_15_lady_4", slot_troop_age, 46),
        (troop_set_slot, "trp_kingdom_15_lady_3", slot_troop_age, 38),
        (troop_set_slot, "trp_kingdom_15_lady_1", slot_troop_age, 16),
        (troop_set_slot, "trp_kingdom_15_lady_2", slot_troop_age, 18),

        (troop_set_slot, "trp_kingdom_16_lady_1", slot_troop_age, 16),
        (troop_set_slot, "trp_kingdom_16_lady_2", slot_troop_age, 17),

        (troop_set_slot, "trp_kingdom_17_lady_1", slot_troop_age, 47),
        (troop_set_slot, "trp_kingdom_17_lady_4", slot_troop_age, 21),
        (troop_set_slot, "trp_kingdom_17_lady_3", slot_troop_age, 35),
        (troop_set_slot, "trp_kingdom_17_lady_2", slot_troop_age, 21),
        (troop_set_slot, "trp_kingdom_17_lady_5", slot_troop_age, 23),
        (troop_set_slot, "trp_kingdom_17_lady_6", slot_troop_age, 16),

        (troop_set_slot, "trp_kingdom_18_lady_2", slot_troop_age, 41),
        (troop_set_slot, "trp_kingdom_18_lady_3", slot_troop_age, 36),
        (troop_set_slot, "trp_kingdom_18_lady_1", slot_troop_age, 16),
        (troop_set_slot, "trp_kingdom_18_lady_4", slot_troop_age, 18),
        (troop_set_slot, "trp_kingdom_18_lady_5", slot_troop_age, 15),
        (troop_set_slot, "trp_kingdom_18_lady_6", slot_troop_age, 16),

        (troop_set_slot, "trp_kingdom_19_lady_1", slot_troop_age, 40),
        (troop_set_slot, "trp_kingdom_19_lady_2", slot_troop_age, 17),
        (troop_set_slot, "trp_kingdom_19_lady_3", slot_troop_age, 18),

        (troop_set_slot, "trp_kingdom_20_lady_3", slot_troop_age, 38),
        (troop_set_slot, "trp_kingdom_20_lady_7", slot_troop_age, 41),
        (troop_set_slot, "trp_kingdom_20_lady_1", slot_troop_age, 36),
        (troop_set_slot, "trp_kingdom_20_lady_2", slot_troop_age, 16),

        (troop_set_slot, "trp_kingdom_20_lady_6", slot_troop_age, 20),
        (troop_set_slot, "trp_kingdom_20_lady_4", slot_troop_age, 22),
        (troop_set_slot, "trp_kingdom_20_lady_5", slot_troop_age, 23),

        (troop_set_slot, "trp_kingdom_21_lady_1", slot_troop_age, 21),

        (troop_set_slot, "trp_kingdom_22_lady_1", slot_troop_age, 41),
        (troop_set_slot, "trp_kingdom_22_lady_2", slot_troop_age, 16),
        (troop_set_slot, "trp_kingdom_22_lady_3", slot_troop_age, 20),

        (troop_set_slot, "trp_kingdom_23_lady_1", slot_troop_age, 43),
        (troop_set_slot, "trp_kingdom_23_lady_2", slot_troop_age, 34),
        (troop_set_slot, "trp_kingdom_23_lady_3", slot_troop_age, 16),
        (troop_set_slot, "trp_kingdom_23_lady_4", slot_troop_age, 16),

        (troop_set_slot, "trp_kingdom_24_lady_1", slot_troop_age, 12),
        (troop_set_slot, "trp_kingdom_24_lady_2", slot_troop_age, 20),

        (troop_set_slot, "trp_kingdom_25_lady_1", slot_troop_age, 37),
        (troop_set_slot, "trp_kingdom_25_lady_2", slot_troop_age, 16),

        (troop_set_slot, "trp_kingdom_26_lady_1", slot_troop_age, 16),
        (troop_set_slot, "trp_kingdom_26_lady_2", slot_troop_age, 17),
        (troop_set_slot, "trp_kingdom_26_lady_3", slot_troop_age, 19),
        (troop_set_slot, "trp_kingdom_26_lady_4", slot_troop_age, 32),
        (troop_set_slot, "trp_kingdom_26_lady_5", slot_troop_age, 16),

        (troop_set_slot, "trp_kingdom_27_lady_1", slot_troop_age, 40),
        (troop_set_slot, "trp_kingdom_27_lady_2", slot_troop_age, 43),
        (troop_set_slot, "trp_kingdom_27_lady_3", slot_troop_age, 20),

        (troop_set_slot, "trp_kingdom_28_lady_1", slot_troop_age, 45),
        (troop_set_slot, "trp_kingdom_28_lady_2", slot_troop_age, 50),
        (troop_set_slot, "trp_kingdom_28_lady_3", slot_troop_age, 21),
        (troop_set_slot, "trp_kingdom_28_lady_5", slot_troop_age, 16),
        (troop_set_slot, "trp_kingdom_28_lady_6", slot_troop_age, 16),
        (troop_set_slot, "trp_kingdom_28_lady_4", slot_troop_age, 38),

        (troop_set_slot, "trp_kingdom_29_lady_1", slot_troop_age, 39),
        (troop_set_slot, "trp_kingdom_29_lady_2", slot_troop_age, 20),
        (troop_set_slot, "trp_kingdom_29_lady_3", slot_troop_age, 21),

        (troop_set_slot, "trp_kingdom_30_lady_5", slot_troop_age, 39),
        (troop_set_slot, "trp_kingdom_30_lady_6", slot_troop_age, 40),
        (troop_set_slot, "trp_kingdom_30_lady_1", slot_troop_age, 24),
        (troop_set_slot, "trp_kingdom_30_lady_2", slot_troop_age, 16),
        (troop_set_slot, "trp_kingdom_30_lady_3", slot_troop_age, 17),
        (troop_set_slot, "trp_kingdom_30_lady_4", slot_troop_age, 16),

        (troop_set_slot, "trp_kingdom_31_lady_2", slot_troop_age, 41),
        (troop_set_slot, "trp_kingdom_31_lady_3", slot_troop_age, 38),
        (troop_set_slot, "trp_kingdom_31_lady_1", slot_troop_age, 20),

        # Ladies reputation
        (try_for_range, ":cur_lady", kingdom_ladies_begin, kingdom_ladies_end),
            (troop_set_slot, ":cur_lady", slot_troop_occupation, slto_kingdom_lady),

            (store_random_in_range, ":lady_reputation", 20, 26),
            (try_begin),
                (eq, ":lady_reputation", 20),
                (assign, ":lady_reputation", lrep_moralist),
            (else_try),
                (eq, ":lady_reputation", 21),
                (assign, ":lady_reputation", lrep_ambitious),
            (else_try),
                (eq, ":lady_reputation", 22),
                (assign, ":lady_reputation", lrep_adventurous),
            (else_try),
                (eq, ":lady_reputation", 23),
                (assign, ":lady_reputation", lrep_otherworldly),
            (else_try),
                (eq, ":lady_reputation", 24),
                (assign, ":lady_reputation", lrep_ambitious),
            (else_try),
                (assign, ":lady_reputation", lrep_conventional),
            (try_end),
            (troop_set_slot, ":cur_lady", slot_lord_reputation_type, ":lady_reputation"),
            (call_script, "script_add_lady_items", ":cur_lady"),
        (try_end),

        # Others lords age
        (troop_set_slot, "trp_knight_1_1", slot_troop_age, 42),
        (troop_set_slot, "trp_knight_2_2", slot_troop_age, 46),
        (troop_set_slot, "trp_knight_2_3", slot_troop_age, 41),
        (troop_set_slot, "trp_knight_3_1", slot_troop_age, 40),
        (troop_set_slot, "trp_knight_4_2", slot_troop_age, 40),
        (troop_set_slot, "trp_knight_4_3", slot_troop_age, 39),
        (troop_set_slot, "trp_knight_5_1", slot_troop_age, 38),
        (troop_set_slot, "trp_knight_5_2", slot_troop_age, 22),
        (troop_set_slot, "trp_knight_5_4", slot_troop_age, 18),
        (troop_set_slot, "trp_knight_5_5", slot_troop_age, 35),
        (troop_set_slot, "trp_knight_6_1", slot_troop_age, 35),
        (troop_set_slot, "trp_knight_8_2", slot_troop_age, 65),
        (troop_set_slot, "trp_knight_8_4", slot_troop_age, 41),
        (troop_set_slot, "trp_knight_8_5", slot_troop_age, 41),
        (troop_set_slot, "trp_knight_9_2", slot_troop_age, 39),
        (troop_set_slot, "trp_knight_9_3", slot_troop_age, 38),
        (troop_set_slot, "trp_knight_9_5", slot_troop_age, 30),
        (troop_set_slot, "trp_knight_9_6", slot_troop_age, 44),
        (troop_set_slot, "trp_knight_10_1", slot_troop_age, 26),
        (troop_set_slot, "trp_knight_11_8", slot_troop_age, 34),
        (troop_set_slot, "trp_knight_12_2", slot_troop_age, 56),
        (troop_set_slot, "trp_knight_12_3", slot_troop_age, 48),
        (troop_set_slot, "trp_knight_13_1", slot_troop_age, 23),
        (troop_set_slot, "trp_knight_13_7", slot_troop_age, 41),
        (troop_set_slot, "trp_knight_13_9", slot_troop_age, 46),
        (troop_set_slot, "trp_knight_14_3", slot_troop_age, 51),
        (troop_set_slot, "trp_knight_15_2", slot_troop_age, 44),
        (troop_set_slot, "trp_knight_15_4", slot_troop_age, 36),
        (troop_set_slot, "trp_knight_17_2", slot_troop_age, 38),
        (troop_set_slot, "trp_knight_17_4", slot_troop_age, 46),
        (troop_set_slot, "trp_knight_17_6", slot_troop_age, 36),
        (troop_set_slot, "trp_knight_18_5", slot_troop_age, 46),
        (troop_set_slot, "trp_knight_18_6", slot_troop_age, 68),
        (troop_set_slot, "trp_knight_19_5", slot_troop_age, 36),
        (troop_set_slot, "trp_knight_20_6", slot_troop_age, 66),
        (troop_set_slot, "trp_knight_20_9", slot_troop_age, 46),
        (troop_set_slot, "trp_knight_22_2", slot_troop_age, 58),
        (troop_set_slot, "trp_knight_23_1", slot_troop_age, 46),
        (troop_set_slot, "trp_knight_23_3", slot_troop_age, 45),
        (troop_set_slot, "trp_knight_25_1", slot_troop_age, 66),
        (troop_set_slot, "trp_knight_26_3", slot_troop_age, 20),
        (troop_set_slot, "trp_knight_27_1", slot_troop_age, 18),
        (troop_set_slot, "trp_knight_27_2", slot_troop_age, 37),
        (troop_set_slot, "trp_knight_28_2", slot_troop_age, 37),
        (troop_set_slot, "trp_knight_28_4", slot_troop_age, 41),
        (troop_set_slot, "trp_knight_28_5", slot_troop_age, 44),
        (troop_set_slot, "trp_knight_29_1", slot_troop_age, 36),
        (troop_set_slot, "trp_knight_30_2", slot_troop_age, 38),
        (troop_set_slot, "trp_knight_30_6", slot_troop_age, 28),
        (troop_set_slot, "trp_knight_31_2", slot_troop_age, 48),
        (troop_set_slot, "trp_knight_31_3", slot_troop_age, 36),

        #viudos con hijas
        (troop_set_slot, "trp_knight_4_5", slot_troop_age, 44),
        (troop_set_slot, "trp_knight_7_1", slot_troop_age, 34),
        (troop_set_slot, "trp_knight_11_2", slot_troop_age, 32),
        (troop_set_slot, "trp_knight_15_1", slot_troop_age, 42),
        (troop_set_slot, "trp_knight_16_1", slot_troop_age, 31),
        (troop_set_slot, "trp_knight_17_3", slot_troop_age, 36),
        (troop_set_slot, "trp_knight_18_3", slot_troop_age, 42),
        (troop_set_slot, "trp_knight_20_1", slot_troop_age, 43),
        (troop_set_slot, "trp_knight_20_2", slot_troop_age, 41),
        (troop_set_slot, "trp_knight_21_1", slot_troop_age, 53),
        (troop_set_slot, "trp_knight_22_1", slot_troop_age, 44),
        (troop_set_slot, "trp_knight_24_2", slot_troop_age, 38),
        (troop_set_slot, "trp_knight_26_1", slot_troop_age, 26),
        (troop_set_slot, "trp_knight_26_2", slot_troop_age, 50),
        (troop_set_slot, "trp_knight_28_1", slot_troop_age, 51),
        (troop_set_slot, "trp_knight_29_2", slot_troop_age, 26),
        (troop_set_slot, "trp_knight_30_5", slot_troop_age, 42),
        (troop_set_slot, "trp_knight_31_1", slot_troop_age, 56),

        #caballeros solterones
        (troop_set_slot, "trp_knight_1_2", slot_troop_age, 16),
        (troop_set_slot, "trp_knight_1_3", slot_troop_age, 42),
        (troop_set_slot, "trp_knight_2_1", slot_troop_age, 20),
        (troop_set_slot, "trp_knight_3_2", slot_troop_age, 30),
        (troop_set_slot, "trp_knight_3_3", slot_troop_age, 30),
        (troop_set_slot, "trp_knight_4_1", slot_troop_age, 16),
        (troop_set_slot, "trp_knight_4_4", slot_troop_age, 30),
        (troop_set_slot, "trp_knight_4_6", slot_troop_age, 16),
        (troop_set_slot, "trp_knight_5_3", slot_troop_age, 20),
        (troop_set_slot, "trp_knight_6_2", slot_troop_age, 27),
        (troop_set_slot, "trp_knight_8_1", slot_troop_age, 17),
        (troop_set_slot, "trp_knight_8_3", slot_troop_age, 16),
        (troop_set_slot, "trp_knight_8_6", slot_troop_age, 62),
        (troop_set_slot, "trp_knight_9_1", slot_troop_age, 21),
        (troop_set_slot, "trp_knight_9_4", slot_troop_age, 20),
        (troop_set_slot, "trp_knight_11_1", slot_troop_age, 18),
        (troop_set_slot, "trp_knight_11_3", slot_troop_age, 30),
        (troop_set_slot, "trp_knight_11_4", slot_troop_age, 28),
        (troop_set_slot, "trp_knight_11_5", slot_troop_age, 24),
        (troop_set_slot, "trp_knight_11_6", slot_troop_age, 23),
        (troop_set_slot, "trp_knight_11_7", slot_troop_age, 21),
        (troop_set_slot, "trp_knight_12_1", slot_troop_age, 50),
        (troop_set_slot, "trp_knight_13_2", slot_troop_age, 21),
        (troop_set_slot, "trp_knight_13_3", slot_troop_age, 21),
        (troop_set_slot, "trp_knight_13_4", slot_troop_age, 20),
        (troop_set_slot, "trp_knight_13_5", slot_troop_age, 19),
        (troop_set_slot, "trp_knight_13_6", slot_troop_age, 18),
        (troop_set_slot, "trp_knight_13_8", slot_troop_age, 32),
        (troop_set_slot, "trp_knight_14_1", slot_troop_age, 29),
        (troop_set_slot, "trp_knight_14_2", slot_troop_age, 28),
        (troop_set_slot, "trp_knight_15_3", slot_troop_age, 48),
        (troop_set_slot, "trp_knight_16_2", slot_troop_age, 26),
        (troop_set_slot, "trp_knight_16_3", slot_troop_age, 32),
        (troop_set_slot, "trp_knight_17_1", slot_troop_age, 21),
        (troop_set_slot, "trp_knight_17_5", slot_troop_age, 26),
        (troop_set_slot, "trp_knight_18_1", slot_troop_age, 24),
        (troop_set_slot, "trp_knight_18_2", slot_troop_age, 21),
        (troop_set_slot, "trp_knight_18_4", slot_troop_age, 76),
        (troop_set_slot, "trp_knight_18_7", slot_troop_age, 36),
        (troop_set_slot, "trp_knight_19_1", slot_troop_age, 29),
        (troop_set_slot, "trp_knight_19_2", slot_troop_age, 21),
        (troop_set_slot, "trp_knight_19_3", slot_troop_age, 20),
        (troop_set_slot, "trp_knight_19_4", slot_troop_age, 19),
        (troop_set_slot, "trp_knight_20_3", slot_troop_age, 20),
        (troop_set_slot, "trp_knight_20_4", slot_troop_age, 56),
        (troop_set_slot, "trp_knight_20_5", slot_troop_age, 16),
        (troop_set_slot, "trp_knight_20_7", slot_troop_age, 18),
        (troop_set_slot, "trp_knight_20_8", slot_troop_age, 36),
        (troop_set_slot, "trp_knight_22_3", slot_troop_age, 26),
        (troop_set_slot, "trp_knight_23_2", slot_troop_age, 48),
        (troop_set_slot, "trp_knight_23_4", slot_troop_age, 39),
        (troop_set_slot, "trp_knight_24_1", slot_troop_age, 16),
        (troop_set_slot, "trp_knight_24_3", slot_troop_age, 36),
        (troop_set_slot, "trp_knight_27_3", slot_troop_age, 46),
        (troop_set_slot, "trp_knight_28_3", slot_troop_age, 36),
        (troop_set_slot, "trp_knight_30_1", slot_troop_age, 23),
        (troop_set_slot, "trp_knight_30_3", slot_troop_age, 36),
        (troop_set_slot, "trp_knight_30_4", slot_troop_age, 33),
        (troop_set_slot, "trp_knight_30_7", slot_troop_age, 19),

        #edades hijos chief
        (troop_set_slot, "trp_knight_4_6", slot_troop_age, 16),
        (troop_set_slot, "trp_knight_5_6", slot_troop_age, 21),
        (troop_set_slot, "trp_knight_5_7", slot_troop_age, 17),
        (troop_set_slot, "trp_knight_9_7", slot_troop_age, 20),
        (troop_set_slot, "trp_knight_9_8", slot_troop_age, 17),
        (troop_set_slot, "trp_knight_9_9", slot_troop_age, 16),
        (troop_set_slot, "trp_knight_17_7", slot_troop_age, 16),
        (troop_set_slot, "trp_knight_28_6", slot_troop_age, 27),
        (troop_set_slot, "trp_knight_28_7", slot_troop_age, 16),
        (troop_set_slot, "trp_knight_29_3", slot_troop_age, 26),

        # Reputation of the Lords
        (try_for_range, ":cur_troop", lords_begin, lords_end),
            (troop_set_slot, ":cur_troop", slot_troop_occupation, slto_kingdom_hero),

           (store_random_in_range, ":lord_reputation", 20, 26),
            (try_begin),
                (eq, ":lord_reputation", 20),
                (assign, ":lord_reputation", lrep_martial),
            (else_try),
                (eq, ":lord_reputation", 21),
                (assign, ":lord_reputation", lrep_quarrelsome),
            (else_try),
                (eq, ":lord_reputation", 22),
                (assign, ":lord_reputation", lrep_selfrighteous),
            (else_try),
                (eq, ":lord_reputation", 23),
                (assign, ":lord_reputation", lrep_cunning),
            (else_try),
                (eq, ":lord_reputation", 24),
                (assign, ":lord_reputation", lrep_upstanding),
            (else_try),
                (assign, ":lord_reputation", lrep_debauched),
            (try_end),

            (troop_set_slot, ":cur_troop", slot_lord_reputation_type, ":lord_reputation"),
        (try_end),

        # blood relationships
        (troop_set_slot, "trp_knight_1_1", slot_troop_spouse, "trp_kingdom_1_lady_1"),
        (troop_set_slot, "trp_kingdom_1_lady_1", slot_troop_spouse, "trp_knight_1_1"),
        (troop_set_slot, "trp_kingdom_1_lady_2", slot_troop_father, "trp_knight_1_1"),
        (troop_set_slot, "trp_kingdom_1_lady_2", slot_troop_mother, "trp_kingdom_1_lady_1"),
        (troop_set_slot, "trp_kingdom_1_lady_3", slot_troop_guardian, "trp_knight_1_2"),

        (troop_set_slot, "trp_knight_2_2", slot_troop_spouse, "trp_kingdom_2_lady_1"),
        (troop_set_slot, "trp_kingdom_2_lady_1", slot_troop_spouse, "trp_knight_2_2"),
        (troop_set_slot, "trp_kingdom_2_lady_2", slot_troop_mother, "trp_kingdom_2_lady_1"),
        (troop_set_slot, "trp_kingdom_2_lady_2", slot_troop_father, "trp_knight_2_2"),

        (troop_set_slot, "trp_knight_2_3", slot_troop_spouse, "trp_kingdom_2_lady_3"),
        (troop_set_slot, "trp_kingdom_2_lady_3", slot_troop_spouse, "trp_knight_2_3"),

        (troop_set_slot, "trp_knight_3_1", slot_troop_spouse, "trp_kingdom_3_lady_1"),
        (troop_set_slot, "trp_kingdom_3_lady_1", slot_troop_spouse, "trp_knight_3_1"),
        (troop_set_slot, "trp_kingdom_3_lady_2", slot_troop_mother, "trp_kingdom_3_lady_1"),
        (troop_set_slot, "trp_kingdom_3_lady_2", slot_troop_father, "trp_knight_3_1"),
        (troop_set_slot, "trp_kingdom_3_lady_3", slot_troop_guardian, "trp_knight_3_2"),

        (troop_set_slot, "trp_knight_4_2", slot_troop_spouse, "trp_kingdom_4_lady_1"),
        (troop_set_slot, "trp_kingdom_4_lady_1", slot_troop_spouse, "trp_knight_4_2"),
        (troop_set_slot, "trp_kingdom_4_lady_2", slot_troop_mother, "trp_kingdom_4_lady_1"),
        (troop_set_slot, "trp_kingdom_4_lady_3", slot_troop_mother, "trp_kingdom_4_lady_1"),
        (troop_set_slot, "trp_kingdom_4_lady_2", slot_troop_father, "trp_knight_4_2"),
        (troop_set_slot, "trp_kingdom_4_lady_3", slot_troop_father, "trp_knight_4_2"),

        (troop_set_slot, "trp_knight_4_3", slot_troop_spouse, "trp_kingdom_4_lady_4"),
        (troop_set_slot, "trp_kingdom_4_lady_4", slot_troop_spouse, "trp_knight_4_3"),
        (troop_set_slot, "trp_kingdom_4_lady_5", slot_troop_father, "trp_knight_4_3"),
        (troop_set_slot, "trp_kingdom_4_lady_5", slot_troop_mother, "trp_kingdom_4_lady_4"),
        (troop_set_slot, "trp_knight_4_6", slot_troop_father, "trp_knight_4_3"),
        (troop_set_slot, "trp_knight_4_6", slot_troop_mother, "trp_kingdom_4_lady_4"),

        (troop_set_slot, "trp_kingdom_4_lady_6", slot_troop_guardian, "trp_knight_4_5"),

        (troop_set_slot, "trp_knight_5_1", slot_troop_spouse, "trp_kingdom_5_lady_1"),
        (troop_set_slot, "trp_kingdom_5_lady_1", slot_troop_spouse, "trp_knight_5_1"),
        (troop_set_slot, "trp_kingdom_5_lady_3", slot_troop_mother, "trp_kingdom_5_lady_1"),
        (troop_set_slot, "trp_kingdom_5_lady_4", slot_troop_mother, "trp_kingdom_5_lady_1"),
        (troop_set_slot, "trp_kingdom_5_lady_3", slot_troop_father, "trp_knight_5_1"),
        (troop_set_slot, "trp_kingdom_5_lady_4", slot_troop_father, "trp_knight_5_1"),
        (troop_set_slot, "trp_knight_5_6", slot_troop_father, "trp_knight_5_1"),
        (troop_set_slot, "trp_knight_5_6", slot_troop_mother, "trp_kingdom_5_lady_1"),

        (troop_set_slot, "trp_knight_5_2", slot_troop_spouse, "trp_kingdom_5_lady_2"),
        (troop_set_slot, "trp_kingdom_5_lady_2", slot_troop_spouse, "trp_knight_5_2"),

        (troop_set_slot, "trp_knight_5_4", slot_troop_spouse, "trp_kingdom_5_lady_6"),
        (troop_set_slot, "trp_kingdom_5_lady_6", slot_troop_spouse, "trp_knight_5_4"),

        (troop_set_slot, "trp_knight_5_5", slot_troop_spouse, "trp_kingdom_5_lady_7"),
        (troop_set_slot, "trp_kingdom_5_lady_7", slot_troop_spouse, "trp_knight_5_5"),
        (troop_set_slot, "trp_kingdom_5_lady_5", slot_troop_father, "trp_knight_5_5"),
        (troop_set_slot, "trp_kingdom_5_lady_5", slot_troop_mother, "trp_kingdom_5_lady_7"),
        (troop_set_slot, "trp_knight_5_7", slot_troop_mother, "trp_kingdom_5_lady_7"),
        (troop_set_slot, "trp_knight_5_7", slot_troop_father, "trp_knight_5_5"),

        (troop_set_slot, "trp_knight_6_1", slot_troop_spouse, "trp_kingdom_6_lady_1"),
        (troop_set_slot, "trp_kingdom_6_lady_1", slot_troop_spouse, "trp_knight_6_1"),
        (troop_set_slot, "trp_kingdom_6_lady_2", slot_troop_mother, "trp_kingdom_6_lady_1"),
        (troop_set_slot, "trp_kingdom_6_lady_2", slot_troop_father, "trp_knight_6_1"),

        (troop_set_slot, "trp_kingdom_7_lady_1", slot_troop_father, "trp_knight_7_1"),

        (troop_set_slot, "trp_knight_8_2", slot_troop_spouse, "trp_kingdom_8_lady_1"),
        (troop_set_slot, "trp_kingdom_8_lady_1", slot_troop_spouse, "trp_knight_8_2"),

        (troop_set_slot, "trp_knight_8_4", slot_troop_spouse, "trp_kingdom_8_lady_2"),
        (troop_set_slot, "trp_kingdom_8_lady_2", slot_troop_spouse, "trp_knight_8_4"),
        (troop_set_slot, "trp_knight_8_5", slot_troop_spouse, "trp_kingdom_8_lady_4"),
        (troop_set_slot, "trp_kingdom_8_lady_4", slot_troop_spouse, "trp_knight_8_5"),
        (troop_set_slot, "trp_kingdom_8_lady_3", slot_troop_father, "trp_knight_8_4"),

        (troop_set_slot, "trp_kingdom_8_lady_5", slot_troop_father, "trp_knight_8_5"),
        (troop_set_slot, "trp_kingdom_8_lady_6", slot_troop_father, "trp_knight_8_5"),
        (troop_set_slot, "trp_kingdom_8_lady_3", slot_troop_mother, "trp_kingdom_8_lady_2"),

        (troop_set_slot, "trp_kingdom_8_lady_5", slot_troop_mother, "trp_kingdom_8_lady_4"),
        (troop_set_slot, "trp_kingdom_8_lady_6", slot_troop_mother, "trp_kingdom_8_lady_4"),

        (troop_set_slot, "trp_knight_9_2", slot_troop_spouse, "trp_kingdom_9_lady_1"),
        (troop_set_slot, "trp_kingdom_9_lady_1", slot_troop_spouse, "trp_knight_9_2"),

        (troop_set_slot, "trp_knight_9_3", slot_troop_spouse, "trp_kingdom_9_lady_6"),
        (troop_set_slot, "trp_kingdom_9_lady_6", slot_troop_spouse, "trp_knight_9_3"),

        (troop_set_slot, "trp_knight_9_5", slot_troop_spouse, "trp_kingdom_9_lady_2"),
        (troop_set_slot, "trp_kingdom_9_lady_2", slot_troop_spouse, "trp_knight_9_5"),

        (troop_set_slot, "trp_knight_9_6", slot_troop_spouse, "trp_kingdom_9_lady_7"),
        (troop_set_slot, "trp_kingdom_9_lady_7", slot_troop_spouse, "trp_knight_9_6"),

        (troop_set_slot, "trp_kingdom_9_lady_5", slot_troop_father, "trp_knight_9_2"),

        (troop_set_slot, "trp_kingdom_9_lady_3", slot_troop_father, "trp_knight_9_3"),
        (troop_set_slot, "trp_kingdom_9_lady_4", slot_troop_father, "trp_knight_9_3"),

        (troop_set_slot, "trp_kingdom_9_lady_8", slot_troop_father, "trp_knight_9_6"),
        (troop_set_slot, "trp_kingdom_9_lady_9", slot_troop_father, "trp_knight_9_6"),
        (troop_set_slot, "trp_kingdom_9_lady_5", slot_troop_mother, "trp_kingdom_9_lady_1"),

        (troop_set_slot, "trp_kingdom_9_lady_3", slot_troop_mother, "trp_kingdom_9_lady_6"),
        (troop_set_slot, "trp_kingdom_9_lady_4", slot_troop_mother, "trp_kingdom_9_lady_6"),

        (troop_set_slot, "trp_kingdom_9_lady_8", slot_troop_mother, "trp_kingdom_9_lady_7"),
        (troop_set_slot, "trp_kingdom_9_lady_9", slot_troop_mother, "trp_kingdom_9_lady_7"),
        (troop_set_slot, "trp_knight_9_7", slot_troop_father, "trp_knight_9_2"),
        (troop_set_slot, "trp_knight_9_8", slot_troop_father, "trp_knight_9_2"),
        (troop_set_slot, "trp_knight_9_9", slot_troop_father, "trp_knight_9_3"),
        (troop_set_slot, "trp_knight_9_7", slot_troop_mother, "trp_kingdom_9_lady_1"),
        (troop_set_slot, "trp_knight_9_8", slot_troop_mother, "trp_kingdom_9_lady_1"),
        (troop_set_slot, "trp_knight_9_9", slot_troop_mother, "trp_kingdom_9_lady_6"),

        (troop_set_slot, "trp_knight_10_1", slot_troop_spouse, "trp_kingdom_10_lady_1"),
        (troop_set_slot, "trp_kingdom_10_lady_1", slot_troop_spouse, "trp_knight_10_1"),

        (troop_set_slot, "trp_knight_11_8", slot_troop_spouse, "trp_kingdom_11_lady_5"),
        (troop_set_slot, "trp_kingdom_11_lady_5", slot_troop_spouse, "trp_knight_11_8"),
        (troop_set_slot, "trp_kingdom_11_lady_1", slot_troop_father, "trp_knight_11_2"),
        (troop_set_slot, "trp_kingdom_11_lady_2", slot_troop_father, "trp_knight_11_2"),
        (troop_set_slot, "trp_kingdom_11_lady_3", slot_troop_father, "trp_knight_11_2"),
        (troop_set_slot, "trp_kingdom_11_lady_4", slot_troop_father, "trp_knight_11_2"),
        (troop_set_slot, "trp_kingdom_11_lady_1", slot_troop_mother, "trp_kingdom_11_lady_7"),
        (troop_set_slot, "trp_kingdom_11_lady_2", slot_troop_mother, "trp_kingdom_11_lady_7"),
        (troop_set_slot, "trp_kingdom_11_lady_3", slot_troop_mother, "trp_kingdom_11_lady_7"),
        (troop_set_slot, "trp_kingdom_11_lady_4", slot_troop_mother, "trp_kingdom_11_lady_7"),

        (troop_set_slot, "trp_kingdom_11_lady_6", slot_troop_father, "trp_knight_11_8"),
        (troop_set_slot, "trp_kingdom_11_lady_6", slot_troop_mother, "trp_kingdom_11_lady_5"),
        (troop_set_slot, "trp_kingdom_11_lady_7", slot_troop_spouse, "trp_knight_11_2"),
        (troop_set_slot, "trp_knight_11_2", slot_troop_spouse, "trp_kingdom_11_lady_7"),

        (troop_set_slot, "trp_knight_12_2", slot_troop_spouse, "trp_kingdom_12_lady_1"),
        (troop_set_slot, "trp_kingdom_12_lady_1", slot_troop_spouse, "trp_knight_12_2"),

        (troop_set_slot, "trp_knight_12_3", slot_troop_spouse, "trp_kingdom_12_lady_4"),
        (troop_set_slot, "trp_kingdom_12_lady_4", slot_troop_spouse, "trp_knight_12_3"),
        (troop_set_slot, "trp_kingdom_12_lady_2", slot_troop_father, "trp_knight_12_2"),
        (troop_set_slot, "trp_kingdom_12_lady_3", slot_troop_father, "trp_knight_12_2"),
        (troop_set_slot, "trp_kingdom_12_lady_2", slot_troop_mother, "trp_kingdom_12_lady_1"),
        (troop_set_slot, "trp_kingdom_12_lady_3", slot_troop_mother, "trp_kingdom_12_lady_1"),

        (troop_set_slot, "trp_knight_13_1", slot_troop_spouse, "trp_kingdom_13_lady_1"),
        (troop_set_slot, "trp_kingdom_13_lady_1", slot_troop_spouse, "trp_knight_13_1"),


        (troop_set_slot, "trp_knight_13_7", slot_troop_spouse, "trp_kingdom_13_lady_2"),
        (troop_set_slot, "trp_kingdom_13_lady_2", slot_troop_spouse, "trp_knight_13_7"),

        (troop_set_slot, "trp_knight_13_9", slot_troop_spouse, "trp_kingdom_13_lady_5"),
        (troop_set_slot, "trp_kingdom_13_lady_5", slot_troop_spouse, "trp_knight_13_9"),
        (troop_set_slot, "trp_knight_13_8", slot_troop_spouse, "trp_kingdom_13_lady_8"),
        (troop_set_slot, "trp_kingdom_13_lady_8", slot_troop_spouse, "trp_knight_13_8"),

        (troop_set_slot, "trp_kingdom_13_lady_3", slot_troop_father, "trp_knight_13_7"),
        (troop_set_slot, "trp_kingdom_13_lady_4", slot_troop_father, "trp_knight_13_7"),

        (troop_set_slot, "trp_kingdom_13_lady_6", slot_troop_father, "trp_knight_13_9"),
        (troop_set_slot, "trp_kingdom_13_lady_7", slot_troop_father, "trp_knight_13_9"),
        (troop_set_slot, "trp_kingdom_13_lady_3", slot_troop_mother, "trp_kingdom_13_lady_2"),
        (troop_set_slot, "trp_kingdom_13_lady_4", slot_troop_mother, "trp_kingdom_13_lady_2"),

        (troop_set_slot, "trp_kingdom_13_lady_6", slot_troop_mother, "trp_kingdom_13_lady_5"),
        (troop_set_slot, "trp_kingdom_13_lady_7", slot_troop_mother, "trp_kingdom_13_lady_5"),

        (troop_set_slot, "trp_knight_14_3", slot_troop_spouse, "trp_kingdom_14_lady_1"),
        (troop_set_slot, "trp_kingdom_14_lady_1", slot_troop_spouse, "trp_knight_14_3"),
        (troop_set_slot, "trp_kingdom_14_lady_2", slot_troop_father, "trp_knight_14_3"),
        (troop_set_slot, "trp_kingdom_14_lady_2", slot_troop_mother, "trp_kingdom_14_lady_1"),

        (troop_set_slot, "trp_knight_15_2", slot_troop_spouse, "trp_kingdom_15_lady_4"),
        (troop_set_slot, "trp_kingdom_15_lady_4", slot_troop_spouse, "trp_knight_15_2"),

        (troop_set_slot, "trp_knight_15_4", slot_troop_spouse, "trp_kingdom_15_lady_3"),
        (troop_set_slot, "trp_kingdom_15_lady_3", slot_troop_spouse, "trp_knight_15_4"),
        (troop_set_slot, "trp_kingdom_15_lady_1", slot_troop_father, "trp_knight_15_1"),
        (troop_set_slot, "trp_kingdom_15_lady_2", slot_troop_father, "trp_knight_15_1"),

        (troop_set_slot, "trp_kingdom_16_lady_1", slot_troop_father, "trp_knight_16_1"),
        (troop_set_slot, "trp_kingdom_16_lady_2", slot_troop_guardian, "trp_knight_16_2"),

        (troop_set_slot, "trp_knight_17_2", slot_troop_spouse, "trp_kingdom_17_lady_1"),
        (troop_set_slot, "trp_kingdom_17_lady_1", slot_troop_spouse, "trp_knight_17_2"),

        (troop_set_slot, "trp_knight_17_4", slot_troop_spouse, "trp_kingdom_17_lady_4"),
        (troop_set_slot, "trp_kingdom_17_lady_4", slot_troop_spouse, "trp_knight_17_4"),

        (troop_set_slot, "trp_knight_17_6", slot_troop_spouse, "trp_kingdom_17_lady_3"),
        (troop_set_slot, "trp_kingdom_17_lady_3", slot_troop_spouse, "trp_knight_17_6"),
        (troop_set_slot, "trp_kingdom_17_lady_2", slot_troop_father, "trp_knight_17_2"),

        (troop_set_slot, "trp_kingdom_17_lady_5", slot_troop_father, "trp_knight_17_6"),
        (troop_set_slot, "trp_kingdom_17_lady_6", slot_troop_father, "trp_knight_17_6"),
        (troop_set_slot, "trp_kingdom_17_lady_2", slot_troop_mother, "trp_kingdom_17_lady_1"),

        (troop_set_slot, "trp_kingdom_17_lady_5", slot_troop_mother, "trp_kingdom_17_lady_3"),
        (troop_set_slot, "trp_kingdom_17_lady_6", slot_troop_mother, "trp_kingdom_17_lady_3"),
        (troop_set_slot, "trp_knight_17_7", slot_troop_father, "trp_knight_17_3"),

        (troop_set_slot, "trp_knight_18_5", slot_troop_spouse, "trp_kingdom_18_lady_2"),
        (troop_set_slot, "trp_kingdom_18_lady_2", slot_troop_spouse, "trp_knight_18_5"),

        (troop_set_slot, "trp_knight_18_6", slot_troop_spouse, "trp_kingdom_18_lady_3"),
        (troop_set_slot, "trp_kingdom_18_lady_3", slot_troop_spouse, "trp_knight_18_6"),
        (troop_set_slot, "trp_kingdom_18_lady_1", slot_troop_father, "trp_knight_18_3"),

        (troop_set_slot, "trp_kingdom_18_lady_4", slot_troop_father, "trp_knight_18_5"),
        (troop_set_slot, "trp_kingdom_18_lady_5", slot_troop_father, "trp_knight_18_5"),

        (troop_set_slot, "trp_knight_18_1", slot_troop_spouse, "trp_kingdom_18_lady_6"),
        (troop_set_slot, "trp_kingdom_18_lady_6", slot_troop_spouse, "trp_knight_18_1"),
        (troop_set_slot, "trp_kingdom_18_lady_4", slot_troop_mother, "trp_kingdom_18_lady_2"),
        (troop_set_slot, "trp_kingdom_18_lady_5", slot_troop_mother, "trp_kingdom_18_lady_2"),

        (troop_set_slot, "trp_knight_19_5", slot_troop_spouse, "trp_kingdom_19_lady_1"),
        (troop_set_slot, "trp_kingdom_19_lady_1", slot_troop_spouse, "trp_knight_19_5"),
        (troop_set_slot, "trp_kingdom_19_lady_2", slot_troop_father, "trp_knight_19_5"),
        (troop_set_slot, "trp_kingdom_19_lady_3", slot_troop_father, "trp_knight_19_5"),
        (troop_set_slot, "trp_kingdom_19_lady_2", slot_troop_mother, "trp_kingdom_19_lady_1"),
        (troop_set_slot, "trp_kingdom_19_lady_3", slot_troop_mother, "trp_kingdom_19_lady_1"),

        (troop_set_slot, "trp_knight_20_6", slot_troop_spouse, "trp_kingdom_20_lady_3"),
        (troop_set_slot, "trp_kingdom_20_lady_3", slot_troop_spouse, "trp_knight_20_6"),

        (troop_set_slot, "trp_knight_20_9", slot_troop_spouse, "trp_kingdom_20_lady_7"),
        (troop_set_slot, "trp_kingdom_20_lady_7", slot_troop_spouse, "trp_knight_20_9"),
        (troop_set_slot, "trp_kingdom_20_lady_1", slot_troop_father, "trp_knight_20_1"),
        (troop_set_slot, "trp_kingdom_20_lady_2", slot_troop_father, "trp_knight_20_1"),
        (troop_set_slot, "trp_knight_20_2", slot_troop_spouse, "trp_kingdom_20_lady_6"),
        (troop_set_slot, "trp_kingdom_20_lady_6",slot_troop_spouse, "trp_knight_20_2"),

        (troop_set_slot, "trp_kingdom_20_lady_4", slot_troop_father, "trp_knight_20_6"),
        (troop_set_slot, "trp_kingdom_20_lady_5", slot_troop_father, "trp_knight_20_6"),
        (troop_set_slot, "trp_kingdom_20_lady_4", slot_troop_mother, "trp_kingdom_20_lady_3"),
        (troop_set_slot, "trp_kingdom_20_lady_5", slot_troop_mother, "trp_kingdom_20_lady_3"),

        (troop_set_slot, "trp_kingdom_21_lady_1", slot_troop_father, "trp_knight_21_1"),

        (troop_set_slot, "trp_knight_22_2", slot_troop_spouse, "trp_kingdom_22_lady_1"),
        (troop_set_slot, "trp_kingdom_22_lady_1", slot_troop_spouse, "trp_knight_22_2"),
        (troop_set_slot, "trp_kingdom_22_lady_2", slot_troop_father, "trp_knight_22_2"),
        (troop_set_slot, "trp_kingdom_22_lady_3", slot_troop_father, "trp_knight_22_2"),
        (troop_set_slot, "trp_kingdom_20_lady_2", slot_troop_mother, "trp_kingdom_20_lady_1"),
        (troop_set_slot, "trp_kingdom_20_lady_3", slot_troop_mother, "trp_kingdom_20_lady_1"),

        (troop_set_slot, "trp_knight_23_1", slot_troop_spouse, "trp_kingdom_23_lady_1"),
        (troop_set_slot, "trp_kingdom_23_lady_1", slot_troop_spouse, "trp_knight_23_2"),

        (troop_set_slot, "trp_knight_23_3", slot_troop_spouse, "trp_kingdom_23_lady_2"),
        (troop_set_slot, "trp_kingdom_23_lady_2", slot_troop_spouse, "trp_knight_23_3"),
        (troop_set_slot, "trp_kingdom_23_lady_3", slot_troop_father, "trp_knight_23_2"),

        (troop_set_slot, "trp_kingdom_23_lady_4", slot_troop_father, "trp_knight_23_3"),
        (troop_set_slot, "trp_kingdom_23_lady_3", slot_troop_mother, "trp_kingdom_23_lady_1"),

        (troop_set_slot, "trp_kingdom_23_lady_4", slot_troop_mother, "trp_kingdom_23_lady_2"),

        (troop_set_slot, "trp_knight_24_1", slot_troop_spouse, "trp_kingdom_24_lady_1"),
        (troop_set_slot, "trp_kingdom_24_lady_1", slot_troop_spouse, "trp_knight_24_1"),
        (troop_set_slot, "trp_kingdom_24_lady_2", slot_troop_guardian, "trp_knight_24_2"),

        (troop_set_slot, "trp_knight_25_1", slot_troop_spouse, "trp_kingdom_25_lady_1"),
        (troop_set_slot, "trp_kingdom_25_lady_1", slot_troop_spouse, "trp_knight_25_1"),
        (troop_set_slot, "trp_kingdom_25_lady_2", slot_troop_father, "trp_knight_25_1"),
        (troop_set_slot, "trp_kingdom_25_lady_2", slot_troop_mother, "trp_kingdom_23_lady_1"),

        (troop_set_slot, "trp_knight_26_3", slot_troop_spouse, "trp_kingdom_26_lady_5"),
        (troop_set_slot, "trp_kingdom_26_lady_5", slot_troop_spouse, "trp_knight_26_3"),
        (troop_set_slot, "trp_kingdom_26_lady_1", slot_troop_father, "trp_knight_26_3"),
        (troop_set_slot, "trp_kingdom_26_lady_1", slot_troop_mother, "trp_kingdom_26_lady_5"),

        (troop_set_slot, "trp_kingdom_26_lady_2", slot_troop_father, "trp_knight_26_2"),
        (troop_set_slot, "trp_kingdom_26_lady_2", slot_troop_mother, "trp_kingdom_26_lady_4"),
        (troop_set_slot, "trp_kingdom_26_lady_3", slot_troop_mother, "trp_kingdom_26_lady_4"),
        (troop_set_slot, "trp_kingdom_26_lady_3", slot_troop_father, "trp_knight_26_2"),
        (troop_set_slot, "trp_knight_26_2", slot_troop_spouse, "trp_kingdom_26_lady_4"),
        (troop_set_slot, "trp_kingdom_26_lady_4", slot_troop_spouse, "trp_knight_26_2"),

        (troop_set_slot, "trp_knight_27_1", slot_troop_spouse, "trp_kingdom_27_lady_1"),
        (troop_set_slot, "trp_kingdom_27_lady_1", slot_troop_spouse, "trp_knight_27_1"),

        (troop_set_slot, "trp_knight_27_2", slot_troop_spouse, "trp_kingdom_27_lady_2"),
        (troop_set_slot, "trp_kingdom_27_lady_2", slot_troop_spouse, "trp_knight_27_2"),
        (troop_set_slot, "trp_kingdom_27_lady_3", slot_troop_father, "trp_knight_27_2"),
        (troop_set_slot, "trp_kingdom_27_lady_3", slot_troop_mother, "trp_kingdom_27_lady_2"),

        (troop_set_slot, "trp_knight_28_2", slot_troop_spouse, "trp_kingdom_28_lady_1"),
        (troop_set_slot, "trp_kingdom_28_lady_1", slot_troop_spouse, "trp_knight_28_2"),

        (troop_set_slot, "trp_knight_28_4", slot_troop_spouse, "trp_kingdom_28_lady_2"),
        (troop_set_slot, "trp_kingdom_28_lady_2", slot_troop_spouse, "trp_knight_28_4"),

        (troop_set_slot, "trp_knight_28_5", slot_troop_spouse, "trp_kingdom_28_lady_4"),
        (troop_set_slot, "trp_kingdom_28_lady_4", slot_troop_spouse, "trp_knight_28_5"),
        (troop_set_slot, "trp_kingdom_28_lady_3", slot_troop_father, "trp_knight_28_4"),

        (troop_set_slot, "trp_kingdom_28_lady_5", slot_troop_father, "trp_knight_28_5"),
        (troop_set_slot, "trp_kingdom_28_lady_6", slot_troop_father, "trp_knight_28_5"),
        (troop_set_slot, "trp_kingdom_28_lady_3", slot_troop_mother, "trp_kingdom_28_lady_2"),

        (troop_set_slot, "trp_kingdom_28_lady_5", slot_troop_mother, "trp_kingdom_28_lady_4"),
        (troop_set_slot, "trp_kingdom_28_lady_6", slot_troop_mother, "trp_kingdom_28_lady_4"),
        (troop_set_slot, "trp_knight_28_6", slot_troop_father, "trp_knight_28_1"),
        (troop_set_slot, "trp_knight_28_7", slot_troop_father, "trp_knight_28_4"),
        (troop_set_slot, "trp_knight_28_7", slot_troop_mother, "trp_kingdom_28_lady_2"),

        (troop_set_slot, "trp_knight_29_1", slot_troop_spouse, "trp_kingdom_29_lady_1"),
        (troop_set_slot, "trp_kingdom_29_lady_1", slot_troop_spouse, "trp_knight_29_1"),
        (troop_set_slot, "trp_kingdom_29_lady_2", slot_troop_father, "trp_knight_29_1"),

        (troop_set_slot, "trp_kingdom_29_lady_3", slot_troop_guardian, "trp_knight_29_2"),
        (troop_set_slot, "trp_kingdom_29_lady_2", slot_troop_mother, "trp_kingdom_29_lady_1"),
        (troop_set_slot, "trp_knight_29_3", slot_troop_father, "trp_knight_29_2"),

        (troop_set_slot, "trp_knight_30_2", slot_troop_spouse, "trp_kingdom_30_lady_5"),
        (troop_set_slot, "trp_kingdom_30_lady_5", slot_troop_spouse, "trp_knight_30_2"),

        (troop_set_slot, "trp_knight_30_6", slot_troop_spouse, "trp_kingdom_30_lady_6"),
        (troop_set_slot, "trp_kingdom_30_lady_6", slot_troop_spouse, "trp_knight_30_6"),
        (troop_set_slot, "trp_kingdom_30_lady_1", slot_troop_father, "trp_knight_30_2"),
        (troop_set_slot, "trp_kingdom_30_lady_2", slot_troop_father, "trp_knight_30_2"),

        (troop_set_slot, "trp_kingdom_30_lady_3", slot_troop_father, "trp_knight_30_5"),
        (troop_set_slot, "trp_kingdom_30_lady_4", slot_troop_father, "trp_knight_30_5"),
        (troop_set_slot, "trp_kingdom_30_lady_1", slot_troop_mother, "trp_kingdom_30_lady_5"),
        (troop_set_slot, "trp_kingdom_30_lady_2", slot_troop_mother, "trp_kingdom_30_lady_5"),

        (troop_set_slot, "trp_knight_31_2", slot_troop_spouse, "trp_kingdom_31_lady_2"),
        (troop_set_slot, "trp_kingdom_31_lady_2", slot_troop_spouse, "trp_knight_31_2"),

        (troop_set_slot, "trp_knight_31_3", slot_troop_spouse, "trp_kingdom_31_lady_3"),
        (troop_set_slot, "trp_kingdom_31_lady_3", slot_troop_spouse, "trp_knight_31_3"),
        (troop_set_slot, "trp_kingdom_31_lady_1", slot_troop_father, "trp_knight_31_1"),

        (try_begin),
            (eq, "$cheat_mode", 1),
            (assign, reg3, "$cheat_mode"),
            (display_message, "@{!}DEBUG -- Assigned lord reputation and relations"),
        (try_end),

        (try_for_range, ":cur_troop", pretenders_begin, pretenders_end),
            (troop_set_slot, ":cur_troop", slot_troop_occupation, slto_inactive_pretender),
            (store_random_in_range, ":age", 15, 40),
            (troop_set_slot, ":cur_troop", slot_troop_age, ":age"),

            (eq, ":cur_troop", "trp_kingdom_5_pretender"),
            (troop_set_slot, ":cur_troop", slot_troop_age, 45),
        (try_end),
    ]),

    ("initialize_religion", [
        (assign, "$g_sod_faith", 0),
        (assign, "$g_pueblos_religion", 0),
        (assign, "$g_sod_global_faith", 0),
        (party_set_slot, "p_town_8", center_religion_pagana, 1),  # grantebrydge
        (party_set_slot, "p_town_11", center_religion_pagana, 1),  # Aegelesburh
        (party_set_slot, "p_town_18", center_religion_pagana, 1),  # Searoburh
        (party_set_slot, "p_town_23", center_religion_pagana, 1),  # Licidfelth
        (party_set_slot, "p_town_24", center_religion_pagana, 1),  # Linnuis

        (party_set_slot, "p_village_1", center_religion_pagana, 1),
        (party_set_slot, "p_village_2", center_religion_pagana, 1),
        (party_set_slot, "p_village_4", center_religion_pagana, 1),
        (party_set_slot, "p_village_8", center_religion_pagana, 1),
        (party_set_slot, "p_village_10", center_religion_pagana, 1),
        (party_set_slot, "p_village_14", center_religion_pagana, 1),
        (party_set_slot, "p_village_74", center_religion_pagana, 1),
        (party_set_slot, "p_village_51", center_religion_pagana, 1),
        (party_set_slot, "p_village_16", center_religion_pagana, 1),
        (party_set_slot, "p_village_41", center_religion_pagana, 1),
        (party_set_slot, "p_village_49", center_religion_pagana, 1),
        (party_set_slot, "p_village_12", center_religion_pagana, 1),
        (party_set_slot, "p_village_21", center_religion_pagana, 1),
        (party_set_slot, "p_village_76", center_religion_pagana, 1),
        (party_set_slot, "p_village_87", center_religion_pagana, 1),
        (party_set_slot, "p_village_75", center_religion_pagana, 1),
        (party_set_slot, "p_village_38", center_religion_pagana, 1),
        (party_set_slot, "p_village_88", center_religion_pagana, 1),
        (party_set_slot, "p_village_89", center_religion_pagana, 1),
        (party_set_slot, "p_village_44", center_religion_pagana, 1),
        (party_set_slot, "p_village_93", center_religion_pagana, 1),
        (party_set_slot, "p_village_52", center_religion_pagana, 1),
        (party_set_slot, "p_village_98", center_religion_pagana, 1),
        (party_set_slot, "p_village_17", center_religion_pagana, 1),
        (party_set_slot, "p_village_48", center_religion_pagana, 1),
        (party_set_slot, "p_village_36", center_religion_pagana, 1),
        (party_set_slot, "p_village_67", center_religion_pagana, 1),
        (party_set_slot, "p_village_103", center_religion_pagana, 1),
        (party_set_slot, "p_village_129", center_religion_pagana, 1),
        (party_set_slot, "p_village_122", center_religion_pagana, 1),
        (party_set_slot, "p_village_55", center_religion_pagana, 1),
        (party_set_slot, "p_village_54", center_religion_pagana, 1),
        (party_set_slot, "p_village_124", center_religion_pagana, 1),
        (party_set_slot, "p_village_42", center_religion_pagana, 1),
        (party_set_slot, "p_village_90", center_religion_pagana, 1),
        (party_set_slot, "p_village_91", center_religion_pagana, 1),
        (party_set_slot, "p_village_151", center_religion_pagana, 1),
        (party_set_slot, "p_village_95", center_religion_pagana, 1),
        (party_set_slot, "p_village_99", center_religion_pagana, 1),
        (party_set_slot, "p_village_20", center_religion_pagana, 1),
        (party_set_slot, "p_village_3", center_religion_pagana, 1),
        (party_set_slot, "p_village_28", center_religion_pagana, 1),
        (party_set_slot, "p_village_47", center_religion_pagana, 1),
        (party_set_slot, "p_village_46", center_religion_pagana, 1),

        (party_set_slot, "p_village_170", center_religion_pagana, 1),
        (party_set_slot, "p_village_71", center_religion_pagana, 1),
        (party_set_slot, "p_village_116", center_religion_pagana, 1),
        (party_set_slot, "p_village_57", center_religion_pagana, 1),
        (party_set_slot, "p_village_20", center_religion_pagana, 1),
        (party_set_slot, "p_village_99", center_religion_pagana, 1),
        (party_set_slot, "p_village_43", center_religion_pagana, 1),
        (party_set_slot, "p_village_21", center_religion_pagana, 1),
        (party_set_slot, "p_village_16", center_religion_pagana, 1),
        (party_set_slot, "p_village_38", center_religion_pagana, 1),
        (party_set_slot, "p_village_65", center_religion_pagana, 1),
        (party_set_slot, "p_village_35", center_religion_pagana, 1),

        #gente cristiana
        (try_for_range, ":center_no", centers_begin, centers_end),
            (neg|party_slot_ge, ":center_no", center_religion_pagana, 1),  #skip villages which are pagan.
            (neg|party_slot_eq, ":center_no", slot_party_type, spt_castle),
            (assign, "$g_pueblos_religion", 4),
            (store_random_in_range, ":rand", 30, 90),
            (party_set_slot, ":center_no", slot_center_sod_local_faith, ":rand"),
        (try_end),
            (try_for_range, ":center_no", centers_begin, centers_end),
            (neg|party_slot_eq, ":center_no", slot_party_type, spt_castle),
            (party_slot_eq, ":center_no", center_religion_pagana, 1),  #anade fe a las villas paganas
            (store_random_in_range, ":rand", -90, -30),
            (party_set_slot, ":center_no", slot_center_sod_local_faith, ":rand"),
        (try_end),
    ]),

    ("initialize_cultures",[
        # player culture
        (assign, ":player_faction_culture", "fac_culture_1"),
        (faction_set_slot, "fac_player_supporters_faction", slot_faction_culture, ":player_faction_culture"),
        (faction_set_slot, "fac_player_faction", slot_faction_culture, ":player_faction_culture"),

        # others culture
        (faction_set_slot, "fac_culture_1", slot_faction_tier_1_troop, "trp_jute_recruit"),
        (faction_set_slot, "fac_culture_1", slot_faction_tier_2_troop, "trp_jute_footmant2"),
        (faction_set_slot, "fac_culture_1", slot_faction_tier_3_troop, "trp_jute_skirmishert3"),
        (faction_set_slot, "fac_culture_1", slot_faction_tier_4_troop, "trp_jute_infantryt3"),
        (faction_set_slot, "fac_culture_1", slot_faction_tier_5_troop, "trp_jute_horsemant4"),

        (faction_set_slot, "fac_culture_2", slot_faction_tier_1_troop, "trp_saxon_recruit"),
        (faction_set_slot, "fac_culture_2", slot_faction_tier_2_troop, "trp_saxon_footmant2"),
        (faction_set_slot, "fac_culture_2", slot_faction_tier_3_troop, "trp_saxon_skirmishert3"),
        (faction_set_slot, "fac_culture_2", slot_faction_tier_4_troop, "trp_saxon_infantryt3"),
        (faction_set_slot, "fac_culture_2", slot_faction_tier_5_troop, "trp_saxon_horseman1"),

        (faction_set_slot, "fac_culture_3", slot_faction_tier_1_troop, "trp_saxon_recruit"),
        (faction_set_slot, "fac_culture_3", slot_faction_tier_2_troop, "trp_saxon_footmant2"),
        (faction_set_slot, "fac_culture_3", slot_faction_tier_3_troop, "trp_saxon_skirmishert3"),
        (faction_set_slot, "fac_culture_3", slot_faction_tier_4_troop, "trp_saxon_infantryt3"),
        (faction_set_slot, "fac_culture_3", slot_faction_tier_5_troop, "trp_saxon_horseman1"),

        (faction_set_slot, "fac_culture_4", slot_faction_tier_1_troop, "trp_engle_recruit"),
        (faction_set_slot, "fac_culture_4", slot_faction_tier_2_troop, "trp_engle_footmant2"),
        (faction_set_slot, "fac_culture_4", slot_faction_tier_3_troop, "trp_engle_skirmishert3"),
        (faction_set_slot, "fac_culture_4", slot_faction_tier_4_troop, "trp_engle_infantryt3"),
        (faction_set_slot, "fac_culture_4", slot_faction_tier_5_troop, "trp_engle_horseman"),

        (faction_set_slot, "fac_culture_5", slot_faction_tier_1_troop, "trp_saxon_recruit"),
        (faction_set_slot, "fac_culture_5", slot_faction_tier_2_troop, "trp_saxon_footmant2"),
        (faction_set_slot, "fac_culture_5", slot_faction_tier_3_troop, "trp_saxon_skirmishert3"),
        (faction_set_slot, "fac_culture_5", slot_faction_tier_4_troop, "trp_saxon_infantryt3"),
        (faction_set_slot, "fac_culture_5", slot_faction_tier_5_troop, "trp_saxon_horseman1"),

        (faction_set_slot, "fac_culture_6", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_6", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_6", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_6", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_6", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_7", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_7", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_7", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_7", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_7", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_8", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_8", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_8", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_8", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_8", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_9", slot_faction_tier_1_troop, "trp_engle_recruit"),
        (faction_set_slot, "fac_culture_9", slot_faction_tier_2_troop, "trp_engle_footmant2"),
        (faction_set_slot, "fac_culture_9", slot_faction_tier_3_troop, "trp_engle_skirmishert3"),
        (faction_set_slot, "fac_culture_9", slot_faction_tier_4_troop, "trp_engle_infantryt3"),
        (faction_set_slot, "fac_culture_9", slot_faction_tier_5_troop, "trp_engle_horseman"),

        (faction_set_slot, "fac_culture_10", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_10", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_10", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_10", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_10", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_11", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_11", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_11", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_11", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_11", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_12", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_12", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_12", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_12", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_12", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_13", slot_faction_tier_1_troop, "trp_engle_recruit"),
        (faction_set_slot, "fac_culture_13", slot_faction_tier_2_troop, "trp_engle_footmant2"),
        (faction_set_slot, "fac_culture_13", slot_faction_tier_3_troop, "trp_engle_skirmishert3"),
        (faction_set_slot, "fac_culture_13", slot_faction_tier_4_troop, "trp_engle_infantryt3"),
        (faction_set_slot, "fac_culture_13", slot_faction_tier_5_troop, "trp_engle_horseman"),

        (faction_set_slot, "fac_culture_14", slot_faction_tier_1_troop, "trp_engle_recruit"),
        (faction_set_slot, "fac_culture_14", slot_faction_tier_2_troop, "trp_engle_footmant2"),
        (faction_set_slot, "fac_culture_14", slot_faction_tier_3_troop, "trp_engle_skirmishert3"),
        (faction_set_slot, "fac_culture_14", slot_faction_tier_4_troop, "trp_engle_infantryt3"),
        (faction_set_slot, "fac_culture_14", slot_faction_tier_5_troop, "trp_engle_horseman"),

        (faction_set_slot, "fac_culture_15", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_15", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_15", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_15", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_15", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_16", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_16", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_16", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_16", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_16", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_17", slot_faction_tier_1_troop, "trp_irish_recruit"),
        (faction_set_slot, "fac_culture_17", slot_faction_tier_2_troop, "trp_irish_footmant2"),
        (faction_set_slot, "fac_culture_17", slot_faction_tier_3_troop, "trp_irish_infantryt3"),
        (faction_set_slot, "fac_culture_17", slot_faction_tier_4_troop, "trp_irish_skirmishert3"),
        (faction_set_slot, "fac_culture_17", slot_faction_tier_5_troop, "trp_irish_infantryt5"),

        (faction_set_slot, "fac_culture_18", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_18", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_18", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_18", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_18", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_19", slot_faction_tier_1_troop, "trp_irish_recruit"),
        (faction_set_slot, "fac_culture_19", slot_faction_tier_2_troop, "trp_irish_footmant2"),
        (faction_set_slot, "fac_culture_19", slot_faction_tier_3_troop, "trp_irish_infantryt3"),
        (faction_set_slot, "fac_culture_19", slot_faction_tier_4_troop, "trp_irish_skirmishert3"),
        (faction_set_slot, "fac_culture_19", slot_faction_tier_5_troop, "trp_irish_infantryt5"),

        (faction_set_slot, "fac_culture_20", slot_faction_tier_1_troop, "trp_pict_recruit"),
        (faction_set_slot, "fac_culture_20", slot_faction_tier_2_troop, "trp_pict_footmant2"),
        (faction_set_slot, "fac_culture_20", slot_faction_tier_3_troop, "trp_pict_skirmishert3"),
        (faction_set_slot, "fac_culture_20", slot_faction_tier_4_troop, "trp_pict_horsesquiret3"),
        (faction_set_slot, "fac_culture_20", slot_faction_tier_5_troop, "trp_pict_skirmishert4"),

        (faction_set_slot, "fac_culture_21", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_21", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_21", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_21", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_21", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_22", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_22", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_22", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_22", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_22", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_23", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_23", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_23", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_23", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_23", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_24", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_24", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_24", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_24", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_24", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_25", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_25", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_25", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_25", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_25", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_26", slot_faction_tier_1_troop, "trp_briton_recruit"),
        (faction_set_slot, "fac_culture_26", slot_faction_tier_2_troop, "trp_briton_footmant2"),
        (faction_set_slot, "fac_culture_26", slot_faction_tier_3_troop, "trp_briton_infantryt3"),
        (faction_set_slot, "fac_culture_26", slot_faction_tier_4_troop, "trp_briton_skirmt3"),
        (faction_set_slot, "fac_culture_26", slot_faction_tier_5_troop, "trp_briton_horseman"),

        (faction_set_slot, "fac_culture_27", slot_faction_tier_1_troop, "trp_irish_recruit"),
        (faction_set_slot, "fac_culture_27", slot_faction_tier_2_troop, "trp_irish_footmant2"),
        (faction_set_slot, "fac_culture_27", slot_faction_tier_3_troop, "trp_irish_infantryt3"),
        (faction_set_slot, "fac_culture_27", slot_faction_tier_4_troop, "trp_irish_skirmishert3"),
        (faction_set_slot, "fac_culture_27", slot_faction_tier_5_troop, "trp_irish_infantryt5"),

        (faction_set_slot, "fac_culture_28", slot_faction_tier_1_troop, "trp_irish_recruit"),
        (faction_set_slot, "fac_culture_28", slot_faction_tier_2_troop, "trp_irish_footmant2"),
        (faction_set_slot, "fac_culture_28", slot_faction_tier_3_troop, "trp_irish_infantryt3"),
        (faction_set_slot, "fac_culture_28", slot_faction_tier_4_troop, "trp_irish_skirmishert3"),
        (faction_set_slot, "fac_culture_28", slot_faction_tier_5_troop, "trp_irish_infantryt5"),

        (faction_set_slot, "fac_culture_29", slot_faction_tier_1_troop, "trp_irish_recruit"),
        (faction_set_slot, "fac_culture_29", slot_faction_tier_2_troop, "trp_irish_footmant2"),
        (faction_set_slot, "fac_culture_29", slot_faction_tier_3_troop, "trp_irish_infantryt3"),
        (faction_set_slot, "fac_culture_29", slot_faction_tier_4_troop, "trp_irish_skirmishert3"),
        (faction_set_slot, "fac_culture_29", slot_faction_tier_5_troop, "trp_irish_infantryt5"),

        (faction_set_slot, "fac_culture_30", slot_faction_tier_1_troop, "trp_irish_recruit"),
        (faction_set_slot, "fac_culture_30", slot_faction_tier_2_troop, "trp_irish_footmant2"),
        (faction_set_slot, "fac_culture_30", slot_faction_tier_3_troop, "trp_irish_infantryt3"),
        (faction_set_slot, "fac_culture_30", slot_faction_tier_4_troop, "trp_irish_skirmishert3"),
        (faction_set_slot, "fac_culture_30", slot_faction_tier_5_troop, "trp_irish_infantryt5"),

        (faction_set_slot, "fac_culture_31", slot_faction_tier_1_troop, "trp_irish_recruit"),
        (faction_set_slot, "fac_culture_31", slot_faction_tier_2_troop, "trp_irish_footmant2"),
        (faction_set_slot, "fac_culture_31", slot_faction_tier_3_troop, "trp_irish_infantryt3"),
        (faction_set_slot, "fac_culture_31", slot_faction_tier_4_troop, "trp_irish_skirmishert3"),
        (faction_set_slot, "fac_culture_31", slot_faction_tier_5_troop, "trp_irish_infantryt5"),

        (faction_set_slot, "fac_culture_1", slot_faction_town_walker_male_troop, "trp_town_walker_5"),
        (faction_set_slot, "fac_culture_1", slot_faction_town_walker_female_troop, "trp_town_walker_6"),
        (faction_set_slot, "fac_culture_1", slot_faction_village_walker_male_troop, "trp_village_walker_5"),
        (faction_set_slot, "fac_culture_1", slot_faction_village_walker_female_troop, "trp_village_walker_6"),
        (faction_set_slot, "fac_culture_1", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_1", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_2", slot_faction_town_walker_male_troop, "trp_town_walker_5"),
        (faction_set_slot, "fac_culture_2", slot_faction_town_walker_female_troop, "trp_town_walker_6"),
        (faction_set_slot, "fac_culture_2", slot_faction_village_walker_male_troop, "trp_village_walker_5"),
        (faction_set_slot, "fac_culture_2", slot_faction_village_walker_female_troop, "trp_village_walker_6"),
        (faction_set_slot, "fac_culture_2", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_2", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_3", slot_faction_town_walker_male_troop, "trp_town_walker_5"),
        (faction_set_slot, "fac_culture_3", slot_faction_town_walker_female_troop, "trp_town_walker_6"),
        (faction_set_slot, "fac_culture_3", slot_faction_village_walker_male_troop, "trp_village_walker_5"),
        (faction_set_slot, "fac_culture_3", slot_faction_village_walker_female_troop, "trp_village_walker_6"),
        (faction_set_slot, "fac_culture_3", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_3", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_4", slot_faction_town_walker_male_troop, "trp_town_walker_5"),
        (faction_set_slot, "fac_culture_4", slot_faction_town_walker_female_troop, "trp_town_walker_6"),
        (faction_set_slot, "fac_culture_4", slot_faction_village_walker_male_troop, "trp_village_walker_5"),
        (faction_set_slot, "fac_culture_4", slot_faction_village_walker_female_troop, "trp_village_walker_6"),
        (faction_set_slot, "fac_culture_4", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_4", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_5", slot_faction_town_walker_male_troop, "trp_town_walker_5"),
        (faction_set_slot, "fac_culture_5", slot_faction_town_walker_female_troop, "trp_town_walker_6"),
        (faction_set_slot, "fac_culture_5", slot_faction_village_walker_male_troop, "trp_village_walker_5"),
        (faction_set_slot, "fac_culture_5", slot_faction_village_walker_female_troop, "trp_village_walker_6"),
        (faction_set_slot, "fac_culture_5", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_5", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_6", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_6", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_6", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_6", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_6", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_6", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_7", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_7", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_7", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_7", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_7", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_7", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_8", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_8", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_8", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_8", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_8", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_8", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_9", slot_faction_town_walker_male_troop, "trp_town_walker_5"),
        (faction_set_slot, "fac_culture_9", slot_faction_town_walker_female_troop, "trp_town_walker_6"),
        (faction_set_slot, "fac_culture_9", slot_faction_village_walker_male_troop, "trp_village_walker_5"),
        (faction_set_slot, "fac_culture_9", slot_faction_village_walker_female_troop, "trp_village_walker_6"),
        (faction_set_slot, "fac_culture_9", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_9", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_10", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_10", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_10", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_10", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_10", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_10", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_11", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_11", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_11", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_11", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_11", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_11", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_12", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_12", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_12", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_12", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_12", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_12", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_13", slot_faction_town_walker_male_troop, "trp_town_walker_5"),
        (faction_set_slot, "fac_culture_13", slot_faction_town_walker_female_troop, "trp_town_walker_6"),
        (faction_set_slot, "fac_culture_13", slot_faction_village_walker_male_troop, "trp_village_walker_5"),
        (faction_set_slot, "fac_culture_13", slot_faction_village_walker_female_troop, "trp_village_walker_6"),
        (faction_set_slot, "fac_culture_13", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_13", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_14", slot_faction_town_walker_male_troop, "trp_town_walker_5"),
        (faction_set_slot, "fac_culture_14", slot_faction_town_walker_female_troop, "trp_town_walker_6"),
        (faction_set_slot, "fac_culture_14", slot_faction_village_walker_male_troop, "trp_village_walker_5"),
        (faction_set_slot, "fac_culture_14", slot_faction_village_walker_female_troop, "trp_village_walker_6"),
        (faction_set_slot, "fac_culture_14", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_14", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_15", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_15", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_15", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_15", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_15", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_15", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_16", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_16", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_16", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_16", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_16", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_16", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_17", slot_faction_town_walker_male_troop, "trp_town_walker_3"),
        (faction_set_slot, "fac_culture_17", slot_faction_town_walker_female_troop, "trp_town_walker_4"),
        (faction_set_slot, "fac_culture_17", slot_faction_village_walker_male_troop, "trp_village_walker_3"),
        (faction_set_slot, "fac_culture_17", slot_faction_village_walker_female_troop, "trp_village_walker_4"),
        (faction_set_slot, "fac_culture_17", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_17", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_18", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_18", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_18", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_18", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_18", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_18", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_19", slot_faction_town_walker_male_troop, "trp_town_walker_3"),
        (faction_set_slot, "fac_culture_19", slot_faction_town_walker_female_troop, "trp_town_walker_4"),
        (faction_set_slot, "fac_culture_19", slot_faction_village_walker_male_troop, "trp_village_walker_3"),
        (faction_set_slot, "fac_culture_19", slot_faction_village_walker_female_troop, "trp_village_walker_4"),
        (faction_set_slot, "fac_culture_19", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_19", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_20", slot_faction_town_walker_male_troop, "trp_town_walker_3"),
        (faction_set_slot, "fac_culture_20", slot_faction_town_walker_female_troop, "trp_town_walker_4"),
        (faction_set_slot, "fac_culture_20", slot_faction_village_walker_male_troop, "trp_village_walker_3"),
        (faction_set_slot, "fac_culture_20", slot_faction_village_walker_female_troop, "trp_village_walker_4"),
        (faction_set_slot, "fac_culture_20", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_20", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_21", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_21", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_21", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_21", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_21", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_21", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_22", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_22", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_22", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_22", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_22", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_22", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_23", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_23", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_23", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_23", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_23", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_23", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_24", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_24", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_24", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_24", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_24", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_24", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_25", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_25", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_25", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_25", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_25", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_25", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_26", slot_faction_town_walker_male_troop, "trp_town_walker_1"),
        (faction_set_slot, "fac_culture_26", slot_faction_town_walker_female_troop, "trp_town_walker_2"),
        (faction_set_slot, "fac_culture_26", slot_faction_village_walker_male_troop, "trp_village_walker_1"),
        (faction_set_slot, "fac_culture_26", slot_faction_village_walker_female_troop, "trp_village_walker_2"),
        (faction_set_slot, "fac_culture_26", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_26", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_27", slot_faction_town_walker_male_troop, "trp_town_walker_3"),
        (faction_set_slot, "fac_culture_27", slot_faction_town_walker_female_troop, "trp_town_walker_4"),
        (faction_set_slot, "fac_culture_27", slot_faction_village_walker_male_troop, "trp_village_walker_3"),
        (faction_set_slot, "fac_culture_27", slot_faction_village_walker_female_troop, "trp_village_walker_4"),
        (faction_set_slot, "fac_culture_27", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_27", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_28", slot_faction_town_walker_male_troop, "trp_town_walker_3"),
        (faction_set_slot, "fac_culture_28", slot_faction_town_walker_female_troop, "trp_town_walker_4"),
        (faction_set_slot, "fac_culture_28", slot_faction_village_walker_male_troop, "trp_village_walker_3"),
        (faction_set_slot, "fac_culture_28", slot_faction_village_walker_female_troop, "trp_village_walker_4"),
        (faction_set_slot, "fac_culture_28", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_28", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_29", slot_faction_town_walker_male_troop, "trp_town_walker_3"),
        (faction_set_slot, "fac_culture_29", slot_faction_town_walker_female_troop, "trp_town_walker_4"),
        (faction_set_slot, "fac_culture_29", slot_faction_village_walker_male_troop, "trp_village_walker_3"),
        (faction_set_slot, "fac_culture_29", slot_faction_village_walker_female_troop, "trp_village_walker_4"),
        (faction_set_slot, "fac_culture_29", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_29", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_30", slot_faction_town_walker_male_troop, "trp_town_walker_3"),
        (faction_set_slot, "fac_culture_30", slot_faction_town_walker_female_troop, "trp_town_walker_4"),
        (faction_set_slot, "fac_culture_30", slot_faction_village_walker_male_troop, "trp_village_walker_3"),
        (faction_set_slot, "fac_culture_30", slot_faction_village_walker_female_troop, "trp_village_walker_4"),
        (faction_set_slot, "fac_culture_30", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_30", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        (faction_set_slot, "fac_culture_31", slot_faction_town_walker_male_troop, "trp_town_walker_3"),
        (faction_set_slot, "fac_culture_31", slot_faction_town_walker_female_troop, "trp_town_walker_4"),
        (faction_set_slot, "fac_culture_31", slot_faction_village_walker_male_troop, "trp_village_walker_3"),
        (faction_set_slot, "fac_culture_31", slot_faction_village_walker_female_troop, "trp_village_walker_4"),
        (faction_set_slot, "fac_culture_31", slot_faction_town_spy_male_troop, "trp_spy_walker_1"),
        (faction_set_slot, "fac_culture_31", slot_faction_town_spy_female_troop, "trp_spy_walker_2"),

        # Factions:
        (faction_set_slot, "fac_kingdom_1", slot_faction_culture, "fac_culture_1"),
        (faction_set_slot, "fac_kingdom_1", slot_faction_leader, "trp_kingdom_1_lord"),
        (troop_set_slot, "trp_kingdom_1_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_2", slot_faction_culture, "fac_culture_2"),
        (faction_set_slot, "fac_kingdom_2", slot_faction_leader, "trp_kingdom_2_lord"),
        (troop_set_slot, "trp_kingdom_2_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_3", slot_faction_culture, "fac_culture_3"),
        (faction_set_slot, "fac_kingdom_3", slot_faction_leader, "trp_kingdom_3_lord"),
        (troop_set_slot, "trp_kingdom_3_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_4", slot_faction_culture, "fac_culture_4"),
        (faction_set_slot, "fac_kingdom_4", slot_faction_leader, "trp_kingdom_4_lord"),
        (troop_set_slot, "trp_kingdom_4_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_5", slot_faction_culture, "fac_culture_5"),
        (faction_set_slot, "fac_kingdom_5", slot_faction_leader, "trp_kingdom_5_lord"),
        (troop_set_slot, "trp_kingdom_5_lord", slot_troop_renown, 1600),

        (faction_set_slot, "fac_kingdom_6", slot_faction_culture, "fac_culture_6"),
        (faction_set_slot, "fac_kingdom_6", slot_faction_leader, "trp_kingdom_6_lord"),
        (troop_set_slot, "trp_kingdom_6_lord", slot_troop_renown, 1000),

        (faction_set_slot, "fac_kingdom_7", slot_faction_culture, "fac_culture_7"),
        (faction_set_slot, "fac_kingdom_7", slot_faction_leader, "trp_kingdom_7_lord"),
        (troop_set_slot, "trp_kingdom_7_lord", slot_troop_renown, 900),

        (faction_set_slot, "fac_kingdom_8", slot_faction_culture, "fac_culture_8"),
        (faction_set_slot, "fac_kingdom_8", slot_faction_leader, "trp_kingdom_8_lord"),
        (troop_set_slot, "trp_kingdom_8_lord", slot_troop_renown, 1400),

        (faction_set_slot, "fac_kingdom_9", slot_faction_culture, "fac_culture_9"),
        (faction_set_slot, "fac_kingdom_9", slot_faction_leader, "trp_kingdom_9_lord"),
        (troop_set_slot, "trp_kingdom_9_lord", slot_troop_renown, 2000),

        (faction_set_slot, "fac_kingdom_10", slot_faction_culture, "fac_culture_10"),
        (faction_set_slot, "fac_kingdom_10", slot_faction_leader, "trp_kingdom_10_lord"),
        (troop_set_slot, "trp_kingdom_10_lord", slot_troop_renown, 800),

        (faction_set_slot, "fac_kingdom_11", slot_faction_culture, "fac_culture_11"),
        (faction_set_slot, "fac_kingdom_11", slot_faction_leader, "trp_kingdom_11_lord"),
        (troop_set_slot, "trp_kingdom_11_lord", slot_troop_renown, 1600),

        (faction_set_slot, "fac_kingdom_12", slot_faction_culture, "fac_culture_12"),
        (faction_set_slot, "fac_kingdom_12", slot_faction_leader, "trp_kingdom_12_lord"),
        (troop_set_slot, "trp_kingdom_12_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_13", slot_faction_culture, "fac_culture_13"),
        (faction_set_slot, "fac_kingdom_13", slot_faction_leader, "trp_kingdom_13_lord"),
        (troop_set_slot, "trp_kingdom_13_lord", slot_troop_renown, 2200),

        (faction_set_slot, "fac_kingdom_14", slot_faction_culture, "fac_culture_14"),
        (faction_set_slot, "fac_kingdom_14", slot_faction_leader, "trp_kingdom_14_lord"),
        (troop_set_slot, "trp_kingdom_14_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_15", slot_faction_culture, "fac_culture_15"),
        (faction_set_slot, "fac_kingdom_15", slot_faction_leader, "trp_kingdom_15_lord"),
        (troop_set_slot, "trp_kingdom_15_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_16", slot_faction_culture, "fac_culture_16"),
        (faction_set_slot, "fac_kingdom_16", slot_faction_leader, "trp_kingdom_16_lord"),
        (troop_set_slot, "trp_kingdom_16_lord", slot_troop_renown, 1000),

        (faction_set_slot, "fac_kingdom_17", slot_faction_culture, "fac_culture_17"),
        (faction_set_slot, "fac_kingdom_17", slot_faction_leader, "trp_kingdom_17_lord"),
        (troop_set_slot, "trp_kingdom_17_lord", slot_troop_renown, 1600),

        (faction_set_slot, "fac_kingdom_18", slot_faction_culture, "fac_culture_18"),
        (faction_set_slot, "fac_kingdom_18", slot_faction_leader, "trp_kingdom_18_lord"),
        (troop_set_slot, "trp_kingdom_18_lord", slot_troop_renown, 1600),

        (faction_set_slot, "fac_kingdom_19", slot_faction_culture, "fac_culture_19"),
        (faction_set_slot, "fac_kingdom_19", slot_faction_leader, "trp_kingdom_19_lord"),
        (troop_set_slot, "trp_kingdom_19_lord", slot_troop_renown, 1600),

        (faction_set_slot, "fac_kingdom_20", slot_faction_culture, "fac_culture_20"),
        (faction_set_slot, "fac_kingdom_20", slot_faction_leader, "trp_kingdom_20_lord"),
        (troop_set_slot, "trp_kingdom_20_lord", slot_troop_renown, 1800),

        (faction_set_slot, "fac_kingdom_21", slot_faction_culture, "fac_culture_21"),
        (faction_set_slot, "fac_kingdom_21", slot_faction_leader, "trp_kingdom_21_lord"),
        (troop_set_slot, "trp_kingdom_21_lord", slot_troop_renown, 900),

        (faction_set_slot, "fac_kingdom_22", slot_faction_culture, "fac_culture_22"),
        (faction_set_slot, "fac_kingdom_22", slot_faction_leader, "trp_kingdom_22_lord"),
        (troop_set_slot, "trp_kingdom_22_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_23", slot_faction_culture, "fac_culture_23"),
        (faction_set_slot, "fac_kingdom_23", slot_faction_leader, "trp_kingdom_23_lord"),
        (troop_set_slot, "trp_kingdom_23_lord", slot_troop_renown, 1400),

        (faction_set_slot, "fac_kingdom_24", slot_faction_culture, "fac_culture_24"),
        (faction_set_slot, "fac_kingdom_24", slot_faction_leader, "trp_kingdom_24_lord"),
        (troop_set_slot, "trp_kingdom_24_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_25", slot_faction_culture, "fac_culture_25"),
        (faction_set_slot, "fac_kingdom_25", slot_faction_leader, "trp_kingdom_25_lord"),
        (troop_set_slot, "trp_kingdom_25_lord", slot_troop_renown, 900),

        (faction_set_slot, "fac_kingdom_26", slot_faction_culture, "fac_culture_26"),
        (faction_set_slot, "fac_kingdom_26", slot_faction_leader, "trp_kingdom_26_lord"),
        (troop_set_slot, "trp_kingdom_26_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_27", slot_faction_culture, "fac_culture_27"),
        (faction_set_slot, "fac_kingdom_27", slot_faction_leader, "trp_kingdom_27_lord"),
        (troop_set_slot, "trp_kingdom_27_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_28", slot_faction_culture, "fac_culture_28"),
        (faction_set_slot, "fac_kingdom_28", slot_faction_leader, "trp_kingdom_28_lord"),
        (troop_set_slot, "trp_kingdom_28_lord", slot_troop_renown, 1600),

        (faction_set_slot, "fac_kingdom_29", slot_faction_culture, "fac_culture_29"),
        (faction_set_slot, "fac_kingdom_29", slot_faction_leader, "trp_kingdom_29_lord"),
        (troop_set_slot, "trp_kingdom_29_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_30", slot_faction_culture, "fac_culture_30"),
        (faction_set_slot, "fac_kingdom_30", slot_faction_leader, "trp_kingdom_30_lord"),
        (troop_set_slot, "trp_kingdom_30_lord", slot_troop_renown, 1800),

        (faction_set_slot, "fac_kingdom_31", slot_faction_culture, "fac_culture_31"),
        (faction_set_slot, "fac_kingdom_31", slot_faction_leader, "trp_kingdom_31_lord"),
        (troop_set_slot, "trp_kingdom_31_lord", slot_troop_renown, 1200),

        (faction_set_slot, "fac_kingdom_1", slot_faction_adjective, "str_kingdom_1_adjective"),
        (faction_set_slot, "fac_kingdom_2", slot_faction_adjective, "str_kingdom_2_adjective"),
        (faction_set_slot, "fac_kingdom_3", slot_faction_adjective, "str_kingdom_3_adjective"),
        (faction_set_slot, "fac_kingdom_4", slot_faction_adjective, "str_kingdom_4_adjective"),
        (faction_set_slot, "fac_kingdom_5", slot_faction_adjective, "str_kingdom_5_adjective"),
        (faction_set_slot, "fac_kingdom_6", slot_faction_adjective, "str_kingdom_6_adjective"),
        (faction_set_slot, "fac_kingdom_7", slot_faction_adjective, "str_kingdom_7_adjective"),
        (faction_set_slot, "fac_kingdom_8", slot_faction_adjective, "str_kingdom_8_adjective"),
        (faction_set_slot, "fac_kingdom_9", slot_faction_adjective, "str_kingdom_9_adjective"),
        (faction_set_slot, "fac_kingdom_10", slot_faction_adjective, "str_kingdom_10_adjective"),
        (faction_set_slot, "fac_kingdom_11", slot_faction_adjective, "str_kingdom_11_adjective"),
        (faction_set_slot, "fac_kingdom_12", slot_faction_adjective, "str_kingdom_12_adjective"),
        (faction_set_slot, "fac_kingdom_13", slot_faction_adjective, "str_kingdom_13_adjective"),
        (faction_set_slot, "fac_kingdom_14", slot_faction_adjective, "str_kingdom_14_adjective"),
        (faction_set_slot, "fac_kingdom_15", slot_faction_adjective, "str_kingdom_15_adjective"),
        (faction_set_slot, "fac_kingdom_16", slot_faction_adjective, "str_kingdom_16_adjective"),
        (faction_set_slot, "fac_kingdom_17", slot_faction_adjective, "str_kingdom_17_adjective"),
        (faction_set_slot, "fac_kingdom_18", slot_faction_adjective, "str_kingdom_18_adjective"),
        (faction_set_slot, "fac_kingdom_19", slot_faction_adjective, "str_kingdom_19_adjective"),
        (faction_set_slot, "fac_kingdom_20", slot_faction_adjective, "str_kingdom_20_adjective"),
        (faction_set_slot, "fac_kingdom_21", slot_faction_adjective, "str_kingdom_21_adjective"),
        (faction_set_slot, "fac_kingdom_22", slot_faction_adjective, "str_kingdom_22_adjective"),
        (faction_set_slot, "fac_kingdom_23", slot_faction_adjective, "str_kingdom_23_adjective"),
        (faction_set_slot, "fac_kingdom_24", slot_faction_adjective, "str_kingdom_24_adjective"),
        (faction_set_slot, "fac_kingdom_25", slot_faction_adjective, "str_kingdom_25_adjective"),
        (faction_set_slot, "fac_kingdom_26", slot_faction_adjective, "str_kingdom_26_adjective"),
        (faction_set_slot, "fac_kingdom_27", slot_faction_adjective, "str_kingdom_27_adjective"),
        (faction_set_slot, "fac_kingdom_28", slot_faction_adjective, "str_kingdom_28_adjective"),
        (faction_set_slot, "fac_kingdom_29", slot_faction_adjective, "str_kingdom_29_adjective"),
        (faction_set_slot, "fac_kingdom_30", slot_faction_adjective, "str_kingdom_30_adjective"),
        (faction_set_slot, "fac_kingdom_31", slot_faction_adjective, "str_kingdom_31_adjective"),
    ]),

    ("initialize_banners", [
        (faction_set_slot, "fac_kingdom_1", slot_faction_banner, "mesh_banner_kingdom_a"),
        (faction_set_slot, "fac_kingdom_2", slot_faction_banner, "mesh_banner_kingdom_b"),
        (faction_set_slot, "fac_kingdom_3", slot_faction_banner, "mesh_banner_kingdom_c"),
        (faction_set_slot, "fac_kingdom_4", slot_faction_banner, "mesh_banner_kingdom_d"),
        (faction_set_slot, "fac_kingdom_5", slot_faction_banner, "mesh_banner_kingdom_e"),
        (faction_set_slot, "fac_kingdom_6", slot_faction_banner, "mesh_banner_kingdom_f"),
        (faction_set_slot, "fac_kingdom_7", slot_faction_banner, "mesh_banner_kingdom_g"),
        (faction_set_slot, "fac_kingdom_8", slot_faction_banner, "mesh_banner_kingdom_h"),
        (faction_set_slot, "fac_kingdom_9", slot_faction_banner, "mesh_banner_kingdom_i"),
        (faction_set_slot, "fac_kingdom_10", slot_faction_banner, "mesh_banner_kingdom_j"),
        (faction_set_slot, "fac_kingdom_11", slot_faction_banner, "mesh_banner_kingdom_k"),
        (faction_set_slot, "fac_kingdom_12", slot_faction_banner, "mesh_banner_kingdom_l"),
        (faction_set_slot, "fac_kingdom_13", slot_faction_banner, "mesh_banner_kingdom_ll"),
        (faction_set_slot, "fac_kingdom_14", slot_faction_banner, "mesh_banner_kingdom_m"),
        (faction_set_slot, "fac_kingdom_15", slot_faction_banner, "mesh_banner_kingdom_n"),
        (faction_set_slot, "fac_kingdom_16", slot_faction_banner, "mesh_banner_kingdom_o"),
        (faction_set_slot, "fac_kingdom_17", slot_faction_banner, "mesh_banner_kingdom_p"),
        (faction_set_slot, "fac_kingdom_18", slot_faction_banner, "mesh_banner_kingdom_q"),
        (faction_set_slot, "fac_kingdom_19", slot_faction_banner, "mesh_banner_kingdom_r"),
        (faction_set_slot, "fac_kingdom_20", slot_faction_banner, "mesh_banner_kingdom_s"),
        (faction_set_slot, "fac_kingdom_21", slot_faction_banner, "mesh_banner_kingdom_t"),
        (faction_set_slot, "fac_kingdom_22", slot_faction_banner, "mesh_banner_kingdom_u"),
        (faction_set_slot, "fac_kingdom_23", slot_faction_banner, "mesh_banner_kingdom_v"),
        (faction_set_slot, "fac_kingdom_24", slot_faction_banner, "mesh_banner_kingdom_w"),
        (faction_set_slot, "fac_kingdom_25", slot_faction_banner, "mesh_banner_kingdom_x"),
        (faction_set_slot, "fac_kingdom_26", slot_faction_banner, "mesh_banner_kingdom_y"),
        (faction_set_slot, "fac_kingdom_27", slot_faction_banner, "mesh_banner_kingdom_z"),
        (faction_set_slot, "fac_kingdom_28", slot_faction_banner, "mesh_banner_kingdom_2a"),
        (faction_set_slot, "fac_kingdom_29", slot_faction_banner, "mesh_banner_kingdom_2b"),
        (faction_set_slot, "fac_kingdom_30", slot_faction_banner, "mesh_banner_kingdom_2c"),
        (faction_set_slot, "fac_kingdom_31", slot_faction_banner, "mesh_banner_kingdom_2d"),

        (try_for_range, ":cur_faction", npc_kingdoms_begin, npc_kingdoms_end),
            (faction_get_slot, ":cur_faction_king", ":cur_faction", slot_faction_leader),
            (faction_get_slot, ":cur_faction_banner", ":cur_faction", slot_faction_banner),
            (val_sub, ":cur_faction_banner", banner_meshes_begin),
            (val_add, ":cur_faction_banner", banner_scene_props_begin),
            (troop_set_slot, ":cur_faction_king", slot_troop_banner_scene_prop, ":cur_faction_banner"),
        (try_end),

        (try_for_range, ":kingdom_hero", active_npcs_begin, active_npcs_end),
            (this_or_next|troop_slot_eq, ":kingdom_hero", slot_troop_occupation, slto_kingdom_hero),
            (troop_slot_eq, ":kingdom_hero", slot_troop_occupation, slto_inactive_pretender),

            (store_troop_faction, ":kingdom_hero_faction", ":kingdom_hero"),
            (neg|faction_slot_eq, ":kingdom_hero_faction", slot_faction_leader, ":kingdom_hero"),
            (try_begin),
                (eq, ":kingdom_hero_faction", "fac_kingdom_1"),
                (troop_set_slot, "trp_knight_1_1", slot_troop_banner_scene_prop, "spr_banner_cj"),
                (troop_set_slot, "trp_knight_1_2", slot_troop_banner_scene_prop, "spr_banner_ck"),
                (troop_set_slot, "trp_knight_1_3", slot_troop_banner_scene_prop, "spr_banner_cl"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_2"),
                (troop_set_slot, "trp_knight_2_1", slot_troop_banner_scene_prop, "spr_banner_cm"),
                (troop_set_slot, "trp_knight_2_2", slot_troop_banner_scene_prop, "spr_banner_cn"),
                (troop_set_slot, "trp_knight_2_3", slot_troop_banner_scene_prop, "spr_banner_co"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_3"),
                (troop_set_slot, "trp_knight_3_1", slot_troop_banner_scene_prop, "spr_banner_cp"),
                (troop_set_slot, "trp_knight_3_2", slot_troop_banner_scene_prop, "spr_banner_cq"),
                (troop_set_slot, "trp_knight_3_3", slot_troop_banner_scene_prop, "spr_banner_cr"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_4"),
                (troop_set_slot, "trp_knight_4_1", slot_troop_banner_scene_prop, "spr_banner_cs"),
                (troop_set_slot, "trp_knight_4_2", slot_troop_banner_scene_prop, "spr_banner_ct"),
                (troop_set_slot, "trp_knight_4_3", slot_troop_banner_scene_prop, "spr_banner_cu"),
                (troop_set_slot, "trp_knight_4_4", slot_troop_banner_scene_prop, "spr_banner_da"),
                (troop_set_slot, "trp_knight_4_5", slot_troop_banner_scene_prop, "spr_banner_db"),
                (troop_set_slot, "trp_knight_4_6", slot_troop_banner_scene_prop, "spr_banner_dc"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_5"),
                (troop_set_slot, "trp_knight_5_1", slot_troop_banner_scene_prop, "spr_banner_dd"),
                (troop_set_slot, "trp_knight_5_2", slot_troop_banner_scene_prop, "spr_banner_de"),
                (troop_set_slot, "trp_knight_5_3", slot_troop_banner_scene_prop, "spr_banner_df"),
                (troop_set_slot, "trp_knight_5_4", slot_troop_banner_scene_prop, "spr_banner_dg"),
                (troop_set_slot, "trp_knight_5_5", slot_troop_banner_scene_prop, "spr_banner_dh"),
                (troop_set_slot, "trp_knight_5_6", slot_troop_banner_scene_prop, "spr_banner_di"),
                (troop_set_slot, "trp_knight_5_7", slot_troop_banner_scene_prop, "spr_banner_dj"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_6"),
                (troop_set_slot, "trp_knight_6_1", slot_troop_banner_scene_prop, "spr_banner_dk"),
                (troop_set_slot, "trp_knight_6_2", slot_troop_banner_scene_prop, "spr_banner_dl"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_7"),
                (troop_set_slot, "trp_knight_7_1", slot_troop_banner_scene_prop, "spr_banner_dm"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_8"),
                (troop_set_slot, "trp_knight_8_1", slot_troop_banner_scene_prop, "spr_banner_dn"),
                (troop_set_slot, "trp_knight_8_2", slot_troop_banner_scene_prop, "spr_banner_do"),
                (troop_set_slot, "trp_knight_8_3", slot_troop_banner_scene_prop, "spr_banner_dp"),
                (troop_set_slot, "trp_knight_8_4", slot_troop_banner_scene_prop, "spr_banner_dq"),
                (troop_set_slot, "trp_knight_8_5", slot_troop_banner_scene_prop, "spr_banner_dr"),
                (troop_set_slot, "trp_knight_8_6", slot_troop_banner_scene_prop, "spr_banner_ds"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_9"),
                (troop_set_slot, "trp_knight_9_1", slot_troop_banner_scene_prop, "spr_banner_dt"),
                (troop_set_slot, "trp_knight_9_2", slot_troop_banner_scene_prop, "spr_banner_du"),
                (troop_set_slot, "trp_knight_9_3", slot_troop_banner_scene_prop, "spr_banner_ea"),
                (troop_set_slot, "trp_knight_9_4", slot_troop_banner_scene_prop, "spr_banner_eb"),
                (troop_set_slot, "trp_knight_9_5", slot_troop_banner_scene_prop, "spr_banner_ec"),
                (troop_set_slot, "trp_knight_9_6", slot_troop_banner_scene_prop, "spr_banner_ed"),
                (troop_set_slot, "trp_knight_9_7", slot_troop_banner_scene_prop, "spr_banner_ee"),
                (troop_set_slot, "trp_knight_9_8", slot_troop_banner_scene_prop, "spr_banner_ef"),
                (troop_set_slot, "trp_knight_9_9", slot_troop_banner_scene_prop, "spr_banner_eg"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_10"),
                (troop_set_slot, "trp_knight_10_1", slot_troop_banner_scene_prop, "spr_banner_eh"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_11"),
                (troop_set_slot, "trp_knight_11_1", slot_troop_banner_scene_prop, "spr_banner_ei"),
                (troop_set_slot, "trp_knight_11_2", slot_troop_banner_scene_prop, "spr_banner_ej"),
                (troop_set_slot, "trp_knight_11_3", slot_troop_banner_scene_prop, "spr_banner_ek"),
                (troop_set_slot, "trp_knight_11_4", slot_troop_banner_scene_prop, "spr_banner_el"),
                (troop_set_slot, "trp_knight_11_5", slot_troop_banner_scene_prop, "spr_banner_em"),
                (troop_set_slot, "trp_knight_11_6", slot_troop_banner_scene_prop, "spr_banner_en"),
                (troop_set_slot, "trp_knight_11_7", slot_troop_banner_scene_prop, "spr_banner_eo"),
                (troop_set_slot, "trp_knight_11_8", slot_troop_banner_scene_prop, "spr_banner_ep"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_12"),
                (troop_set_slot, "trp_knight_12_1", slot_troop_banner_scene_prop, "spr_banner_eq"),
                (troop_set_slot, "trp_knight_12_2", slot_troop_banner_scene_prop, "spr_banner_er"),
                (troop_set_slot, "trp_knight_12_3", slot_troop_banner_scene_prop, "spr_banner_es"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_13"),
                (troop_set_slot, "trp_knight_13_1", slot_troop_banner_scene_prop, "spr_banner_et"),
                (troop_set_slot, "trp_knight_13_2", slot_troop_banner_scene_prop, "spr_banner_eu"),
                (troop_set_slot, "trp_knight_13_3", slot_troop_banner_scene_prop, "spr_banner_f01"),
                (troop_set_slot, "trp_knight_13_4", slot_troop_banner_scene_prop, "spr_banner_f02"),
                (troop_set_slot, "trp_knight_13_5", slot_troop_banner_scene_prop, "spr_banner_f03"),
                (troop_set_slot, "trp_knight_13_6", slot_troop_banner_scene_prop, "spr_banner_f04"),
                (troop_set_slot, "trp_knight_13_7", slot_troop_banner_scene_prop, "spr_banner_f05"),
                (troop_set_slot, "trp_knight_13_8", slot_troop_banner_scene_prop, "spr_banner_f06"),
                (troop_set_slot, "trp_knight_13_9", slot_troop_banner_scene_prop, "spr_banner_f07"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_14"),
                (troop_set_slot, "trp_knight_14_1", slot_troop_banner_scene_prop, "spr_banner_f08"),
                (troop_set_slot, "trp_knight_14_2", slot_troop_banner_scene_prop, "spr_banner_f09"),
                (troop_set_slot, "trp_knight_14_3", slot_troop_banner_scene_prop, "spr_banner_f10"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_15"),
                (troop_set_slot, "trp_knight_15_1", slot_troop_banner_scene_prop, "spr_banner_f11"),
                (troop_set_slot, "trp_knight_15_2", slot_troop_banner_scene_prop, "spr_banner_f12"),
                (troop_set_slot, "trp_knight_15_3", slot_troop_banner_scene_prop, "spr_banner_f13"),
                (troop_set_slot, "trp_knight_15_4", slot_troop_banner_scene_prop, "spr_banner_f14"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_16"),
                (troop_set_slot, "trp_knight_16_1", slot_troop_banner_scene_prop, "spr_banner_f15"),
                (troop_set_slot, "trp_knight_16_2", slot_troop_banner_scene_prop, "spr_banner_f16"),
                (troop_set_slot, "trp_knight_16_3", slot_troop_banner_scene_prop, "spr_banner_f17"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_17"),
                (troop_set_slot, "trp_knight_17_1", slot_troop_banner_scene_prop, "spr_banner_f18"),
                (troop_set_slot, "trp_knight_17_2", slot_troop_banner_scene_prop, "spr_banner_f19"),
                (troop_set_slot, "trp_knight_17_3", slot_troop_banner_scene_prop, "spr_banner_f20"),
                (troop_set_slot, "trp_knight_17_4", slot_troop_banner_scene_prop, "spr_banner_g01"),
                (troop_set_slot, "trp_knight_17_5", slot_troop_banner_scene_prop, "spr_banner_h01"),
                (troop_set_slot, "trp_knight_17_6", slot_troop_banner_scene_prop, "spr_banner_h02"),
                (troop_set_slot, "trp_knight_17_7", slot_troop_banner_scene_prop, "spr_banner_h03"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_18"),
                (troop_set_slot, "trp_knight_18_1", slot_troop_banner_scene_prop, "spr_banner_h04"),
                (troop_set_slot, "trp_knight_18_2", slot_troop_banner_scene_prop, "spr_banner_h05"),
                (troop_set_slot, "trp_knight_18_3", slot_troop_banner_scene_prop, "spr_banner_h06"),
                (troop_set_slot, "trp_knight_18_4", slot_troop_banner_scene_prop, "spr_banner_h07"),
                (troop_set_slot, "trp_knight_18_5", slot_troop_banner_scene_prop, "spr_banner_h08"),
                (troop_set_slot, "trp_knight_18_6", slot_troop_banner_scene_prop, "spr_banner_h09"),
                (troop_set_slot, "trp_knight_18_7", slot_troop_banner_scene_prop, "spr_banner_h10"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_19"),
                (troop_set_slot, "trp_knight_19_1", slot_troop_banner_scene_prop, "spr_banner_h11"),
                (troop_set_slot, "trp_knight_19_2", slot_troop_banner_scene_prop, "spr_banner_h12"),
                (troop_set_slot, "trp_knight_19_3", slot_troop_banner_scene_prop, "spr_banner_h13"),
                (troop_set_slot, "trp_knight_19_4", slot_troop_banner_scene_prop, "spr_banner_h14"),
                (troop_set_slot, "trp_knight_19_5", slot_troop_banner_scene_prop, "spr_banner_h15"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_20"),
                (troop_set_slot, "trp_knight_20_1", slot_troop_banner_scene_prop, "spr_banner_h16"),
                (troop_set_slot, "trp_knight_20_2", slot_troop_banner_scene_prop, "spr_banner_h17"),
                (troop_set_slot, "trp_knight_20_3", slot_troop_banner_scene_prop, "spr_banner_h18"),
                (troop_set_slot, "trp_knight_20_4", slot_troop_banner_scene_prop, "spr_banner_h19"),
                (troop_set_slot, "trp_knight_20_5", slot_troop_banner_scene_prop, "spr_banner_h20"),
                (troop_set_slot, "trp_knight_20_6", slot_troop_banner_scene_prop, "spr_banner_h21"),
                (troop_set_slot, "trp_knight_20_7", slot_troop_banner_scene_prop, "spr_banner_i01"),
                (troop_set_slot, "trp_knight_20_8", slot_troop_banner_scene_prop, "spr_banner_i02"),
                (troop_set_slot, "trp_knight_20_9", slot_troop_banner_scene_prop, "spr_banner_i03"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_21"),
                (troop_set_slot, "trp_knight_21_1", slot_troop_banner_scene_prop, "spr_banner_i04"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_22"),
                (troop_set_slot, "trp_knight_22_1", slot_troop_banner_scene_prop, "spr_banner_i05"),
                (troop_set_slot, "trp_knight_22_2", slot_troop_banner_scene_prop, "spr_banner_i06"),
                (troop_set_slot, "trp_knight_22_3", slot_troop_banner_scene_prop, "spr_banner_i07"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_23"),
                (troop_set_slot, "trp_knight_23_1", slot_troop_banner_scene_prop, "spr_banner_i08"),
                (troop_set_slot, "trp_knight_23_2", slot_troop_banner_scene_prop, "spr_banner_i09"),
                (troop_set_slot, "trp_knight_23_3", slot_troop_banner_scene_prop, "spr_banner_i10"),
                (troop_set_slot, "trp_knight_23_4", slot_troop_banner_scene_prop, "spr_banner_i11"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_24"),
                (troop_set_slot, "trp_knight_24_1", slot_troop_banner_scene_prop, "spr_banner_i12"),
                (troop_set_slot, "trp_knight_24_2", slot_troop_banner_scene_prop, "spr_banner_i13"),
                (troop_set_slot, "trp_knight_24_3", slot_troop_banner_scene_prop, "spr_banner_i14"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_25"),
                (troop_set_slot, "trp_knight_25_1", slot_troop_banner_scene_prop, "spr_banner_i15"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_26"),
                (troop_set_slot, "trp_knight_26_1", slot_troop_banner_scene_prop, "spr_banner_i16"),
                (troop_set_slot, "trp_knight_26_2", slot_troop_banner_scene_prop, "spr_banner_i17"),
                (troop_set_slot, "trp_knight_26_3", slot_troop_banner_scene_prop, "spr_banner_i18"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_27"),
                (troop_set_slot, "trp_knight_27_1", slot_troop_banner_scene_prop, "spr_banner_i19"),
                (troop_set_slot, "trp_knight_27_2", slot_troop_banner_scene_prop, "spr_banner_i20"),
                (troop_set_slot, "trp_knight_27_3", slot_troop_banner_scene_prop, "spr_banner_i21"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_28"),
                (troop_set_slot, "trp_knight_28_1", slot_troop_banner_scene_prop, "spr_banner_k01"),
                (troop_set_slot, "trp_knight_28_2", slot_troop_banner_scene_prop, "spr_banner_k02"),
                (troop_set_slot, "trp_knight_28_3", slot_troop_banner_scene_prop, "spr_banner_k03"),
                (troop_set_slot, "trp_knight_28_4", slot_troop_banner_scene_prop, "spr_banner_k04"),
                (troop_set_slot, "trp_knight_28_5", slot_troop_banner_scene_prop, "spr_banner_k05"),
                (troop_set_slot, "trp_knight_28_6", slot_troop_banner_scene_prop, "spr_banner_k06"),
                (troop_set_slot, "trp_knight_28_7", slot_troop_banner_scene_prop, "spr_banner_k07"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_29"),
                (troop_set_slot, "trp_knight_29_1", slot_troop_banner_scene_prop, "spr_banner_k08"),
                (troop_set_slot, "trp_knight_29_2", slot_troop_banner_scene_prop, "spr_banner_k09"),
                (troop_set_slot, "trp_knight_29_3", slot_troop_banner_scene_prop, "spr_banner_k10"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_30"),
                (troop_set_slot, "trp_knight_30_1", slot_troop_banner_scene_prop, "spr_banner_k11"),
                (troop_set_slot, "trp_knight_30_2", slot_troop_banner_scene_prop, "spr_banner_k12"),
                (troop_set_slot, "trp_knight_30_3", slot_troop_banner_scene_prop, "spr_banner_k13"),
                (troop_set_slot, "trp_knight_30_4", slot_troop_banner_scene_prop, "spr_banner_k14"),
                (troop_set_slot, "trp_knight_30_5", slot_troop_banner_scene_prop, "spr_banner_k15"),
                (troop_set_slot, "trp_knight_30_6", slot_troop_banner_scene_prop, "spr_banner_k16"),
                (troop_set_slot, "trp_knight_30_7", slot_troop_banner_scene_prop, "spr_banner_k17"),
            (else_try),
                (eq, ":kingdom_hero_faction", "fac_kingdom_31"),
                (troop_set_slot, "trp_knight_31_1", slot_troop_banner_scene_prop, "spr_banner_k18"),
                (troop_set_slot, "trp_knight_31_2", slot_troop_banner_scene_prop, "spr_banner_k19"),
                (troop_set_slot, "trp_knight_31_3", slot_troop_banner_scene_prop, "spr_banner_k20"),
            (else_try),
                (troop_set_slot, "trp_kingdom_1_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_y"),
                (troop_set_slot, "trp_kingdom_2_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_r"),
                (troop_set_slot, "trp_kingdom_3_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_u"),
                (troop_set_slot, "trp_kingdom_4_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_ll"),
                (troop_set_slot, "trp_kingdom_5_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_i"),
                (troop_set_slot, "trp_kingdom_6_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_f"),
                (troop_set_slot, "trp_kingdom_7_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_l"),
                (troop_set_slot, "trp_kingdom_8_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_o"),
                (troop_set_slot, "trp_kingdom_9_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_q"),
                (troop_set_slot, "trp_kingdom_10_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_s"),
                (troop_set_slot, "trp_kingdom_11_pretender", slot_troop_banner_scene_prop, "spr_banner_kingdom_v"),
            (try_end),
        (try_end),
    ]),

    ("initialize_town_factions",[
        # Give centers to factions
        (call_script, "script_give_center_to_faction_aux", "p_town_1", "fac_kingdom_1"),
        (call_script, "script_give_center_to_faction_aux", "p_town_2", "fac_kingdom_2"),
        (call_script, "script_give_center_to_faction_aux", "p_town_3", "fac_kingdom_12"),
        (call_script, "script_give_center_to_faction_aux", "p_town_4", "fac_kingdom_9"),
        (call_script, "script_give_center_to_faction_aux", "p_town_5", "fac_kingdom_16"),
        (call_script, "script_give_center_to_faction_aux", "p_town_6", "fac_kingdom_18"),
        (call_script, "script_give_center_to_faction_aux", "p_town_7", "fac_kingdom_15"),
        (call_script, "script_give_center_to_faction_aux", "p_town_8", "fac_kingdom_4"),
        (call_script, "script_give_center_to_faction_aux", "p_town_9", "fac_kingdom_26"),
        (call_script, "script_give_center_to_faction_aux", "p_town_10", "fac_kingdom_13"),
        (call_script, "script_give_center_to_faction_aux", "p_town_11", "fac_kingdom_9"),
        (call_script, "script_give_center_to_faction_aux", "p_town_12", "fac_kingdom_3"),
        (call_script, "script_give_center_to_faction_aux", "p_town_13", "fac_kingdom_23"),
        (call_script, "script_give_center_to_faction_aux", "p_town_14", "fac_kingdom_4"),
        (call_script, "script_give_center_to_faction_aux", "p_town_15", "fac_kingdom_11"),
        (call_script, "script_give_center_to_faction_aux", "p_town_16", "fac_kingdom_5"),
        (call_script, "script_give_center_to_faction_aux", "p_town_17", "fac_kingdom_8"),
        (call_script, "script_give_center_to_faction_aux", "p_town_18", "fac_kingdom_5"),
        (call_script, "script_give_center_to_faction_aux", "p_town_19", "fac_kingdom_19"),
        (call_script, "script_give_center_to_faction_aux", "p_town_20", "fac_kingdom_13"),
        (call_script, "script_give_center_to_faction_aux", "p_town_21", "fac_kingdom_27"),
        (call_script, "script_give_center_to_faction_aux", "p_town_22", "fac_kingdom_22"),

        (call_script, "script_give_center_to_faction_aux", "p_town_23", "fac_kingdom_9"),
        (call_script, "script_give_center_to_faction_aux", "p_town_24", "fac_kingdom_14"),
        (call_script, "script_give_center_to_faction_aux", "p_town_25", "fac_kingdom_21"),
        (call_script, "script_give_center_to_faction_aux", "p_town_26", "fac_kingdom_25"),
        (call_script, "script_give_center_to_faction_aux", "p_town_27", "fac_kingdom_13"),
        (call_script, "script_give_center_to_faction_aux", "p_town_28", "fac_kingdom_11"),
        (call_script, "script_give_center_to_faction_aux", "p_town_29", "fac_kingdom_24"),
        (call_script, "script_give_center_to_faction_aux", "p_town_30", "fac_kingdom_17"),
        (call_script, "script_give_center_to_faction_aux", "p_town_31", "fac_kingdom_30"),
        (call_script, "script_give_center_to_faction_aux", "p_town_32", "fac_kingdom_29"),
        (call_script, "script_give_center_to_faction_aux", "p_town_33", "fac_kingdom_30"),
        (call_script, "script_give_center_to_faction_aux", "p_town_34", "fac_kingdom_20"),
        (call_script, "script_give_center_to_faction_aux", "p_town_35", "fac_kingdom_28"),
        (call_script, "script_give_center_to_faction_aux", "p_town_36", "fac_kingdom_28"),
        (call_script, "script_give_center_to_faction_aux", "p_town_37", "fac_kingdom_20"),
        (call_script, "script_give_center_to_faction_aux", "p_town_38", "fac_kingdom_18"),
        (call_script, "script_give_center_to_faction_aux", "p_town_39", "fac_kingdom_20"),
        (call_script, "script_give_center_to_faction_aux", "p_town_40", "fac_kingdom_31"),
        (call_script, "script_give_center_to_faction_aux", "p_town_41", "fac_kingdom_6"),
        (call_script, "script_give_center_to_faction_aux", "p_town_42", "fac_kingdom_7"),


        (call_script, "script_give_center_to_faction_aux", "p_castle_1", "fac_kingdom_9"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_2", "fac_kingdom_13"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_3", "fac_kingdom_6"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_4", "fac_kingdom_2"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_5", "fac_kingdom_30"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_6", "fac_kingdom_30"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_7", "fac_kingdom_26"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_8", "fac_kingdom_4"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_9", "fac_kingdom_30"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_10", "fac_kingdom_2"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_11", "fac_kingdom_3"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_12", "fac_kingdom_1"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_13", "fac_kingdom_24"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_14", "fac_kingdom_3"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_15", "fac_kingdom_8"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_16", "fac_kingdom_8"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_17", "fac_kingdom_16"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_18", "fac_kingdom_11"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_19", "fac_kingdom_5"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_20", "fac_kingdom_1"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_21", "fac_kingdom_28"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_22", "fac_kingdom_13"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_23", "fac_kingdom_14"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_24", "fac_kingdom_27"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_25", "fac_kingdom_23"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_26", "fac_kingdom_26"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_27", "fac_kingdom_11"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_28", "fac_kingdom_28"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_29", "fac_kingdom_17"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_30", "fac_kingdom_8"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_31", "fac_kingdom_5"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_32", "fac_kingdom_4"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_33", "fac_kingdom_9"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_34", "fac_kingdom_22"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_35", "fac_kingdom_23"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_36", "fac_kingdom_11"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_37", "fac_kingdom_6"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_38", "fac_kingdom_24"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_39", "fac_kingdom_5"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_40", "fac_kingdom_4"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_41", "fac_kingdom_17"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_42", "fac_kingdom_10"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_43", "fac_kingdom_18"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_44", "fac_kingdom_12"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_45", "fac_kingdom_28"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_46", "fac_kingdom_15"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_47", "fac_kingdom_28"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_48", "fac_kingdom_15"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_49", "fac_kingdom_22"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_50", "fac_kingdom_19"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_51", "fac_kingdom_9"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_52", "fac_kingdom_9"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_53", "fac_kingdom_13"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_54", "fac_kingdom_18"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_55", "fac_kingdom_18"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_56", "fac_kingdom_18"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_57", "fac_kingdom_13"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_58", "fac_kingdom_30"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_59", "fac_kingdom_17"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_60", "fac_kingdom_31"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_61", "fac_kingdom_12"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_62", "fac_kingdom_20"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_63", "fac_kingdom_20"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_64", "fac_kingdom_20"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_65", "fac_kingdom_13"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_66", "fac_kingdom_20"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_67", "fac_kingdom_29"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_68", "fac_kingdom_19"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_69", "fac_kingdom_17"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_70", "fac_kingdom_27"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_71", "fac_kingdom_20"),

        (call_script, "script_give_center_to_faction_aux", "p_castle_72", "fac_kingdom_19"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_73", "fac_kingdom_17"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_74", "fac_kingdom_29"),
        (call_script, "script_give_center_to_faction_aux", "p_castle_75", "fac_kingdom_31"),

        # give towns to great lords
        (call_script, "script_give_center_to_lord", "p_town_1", "trp_kingdom_1_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_2", "trp_kingdom_2_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_3", "trp_kingdom_12_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_4", "trp_knight_9_1", 0),
        (call_script, "script_give_center_to_lord", "p_town_5", "trp_kingdom_16_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_6", "trp_kingdom_18_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_7", "trp_kingdom_15_lord", 0),

        (call_script, "script_give_center_to_lord", "p_town_8", "trp_knight_4_1", 0),
        (call_script, "script_give_center_to_lord", "p_town_9", "trp_kingdom_26_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_10", "trp_knight_13_1", 0),
        (call_script, "script_give_center_to_lord", "p_town_11", "trp_knight_9_2", 0),
        (call_script, "script_give_center_to_lord", "p_town_12", "trp_kingdom_3_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_13", "trp_kingdom_23_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_14", "trp_kingdom_4_lord", 0),

        (call_script, "script_give_center_to_lord", "p_town_15", "trp_knight_11_1", 0),
        (call_script, "script_give_center_to_lord", "p_town_16", "trp_knight_5_1", 0),
        (call_script, "script_give_center_to_lord", "p_town_17", "trp_kingdom_8_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_18", "trp_kingdom_5_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_19", "trp_kingdom_19_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_20", "trp_knight_13_2", 0),
        (call_script, "script_give_center_to_lord", "p_town_21", "trp_kingdom_27_lord", 0),

        (call_script, "script_give_center_to_lord", "p_town_22", "trp_kingdom_22_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_23", "trp_kingdom_9_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_24", "trp_kingdom_14_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_25", "trp_kingdom_21_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_26", "trp_kingdom_25_lord", 0),

        (call_script, "script_give_center_to_lord", "p_town_27", "trp_kingdom_13_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_28", "trp_kingdom_11_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_29", "trp_kingdom_24_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_30", "trp_kingdom_17_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_31", "trp_kingdom_30_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_32", "trp_kingdom_29_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_33", "trp_knight_30_1", 0),

        (call_script, "script_give_center_to_lord", "p_town_34", "trp_kingdom_20_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_35", "trp_knight_28_1", 0),
        (call_script, "script_give_center_to_lord", "p_town_36", "trp_kingdom_28_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_37", "trp_knight_20_2", 0),
        (call_script, "script_give_center_to_lord", "p_town_38", "trp_knight_18_1", 0),
        (call_script, "script_give_center_to_lord", "p_town_39", "trp_knight_20_1", 0),
        (call_script, "script_give_center_to_lord", "p_town_40", "trp_kingdom_31_lord", 0),

        (call_script, "script_give_center_to_lord", "p_town_41", "trp_kingdom_6_lord", 0),
        (call_script, "script_give_center_to_lord", "p_town_42", "trp_kingdom_7_lord", 0),

        (call_script, "script_assign_lords_to_empty_centers"),

        # set original factions
        (try_for_range, ":center_no", centers_begin, centers_end),
            (store_faction_of_party, ":original_faction", ":center_no"),
            (faction_get_slot, ":culture", ":original_faction", slot_faction_culture),
            (party_set_slot, ":center_no", slot_center_culture, ":culture"),
            (party_set_slot, ":center_no", slot_center_original_faction, ":original_faction"),
            (party_set_slot, ":center_no", slot_center_ex_faction, ":original_faction"),
        (try_end),

        # set territorial disputes
        (party_set_slot, "p_castle_10", slot_center_ex_faction, "fac_kingdom_5"),  # gewissae quiere Hlew ceaster de suth seaxna
        (party_set_slot, "p_castle_37", slot_center_ex_faction, "fac_kingdom_5"),  # gewissae quiere caer baddan de Hwice
        (party_set_slot, "p_castle_30", slot_center_ex_faction, "fac_kingdom_5"),  # gewissae quiere caer durnac de Dumnonia
        (party_set_slot, "p_town_16", slot_center_ex_faction, "fac_kingdom_9"),  # Mierce quiere Dorce Ceaster de gewissae
        (party_set_slot, "p_town_10", slot_center_ex_faction, "fac_kingdom_9"),  #Mierce quiere Eorfewic de Bernaccia
        (party_set_slot, "p_town_23", slot_center_ex_faction, "fac_kingdom_13"),  #Bernacia quiere Licidfeld de Mierce
        (party_set_slot, "p_town_24", slot_center_ex_faction, "fac_kingdom_13"),  #Bernaccia quiere Linnuis de Lindisware
        (party_set_slot, "p_castle_61", slot_center_ex_faction, "fac_kingdom_13"),  #Bernaccia quiere Din Baer de Goddodin
        (party_set_slot, "p_castle_48",  slot_center_ex_faction, "fac_kingdom_18"),  #Alt Clut atacara reghed
        (party_set_slot, "p_town_34",  slot_center_ex_faction, "fac_kingdom_19"),  #Dal Riata quiere Dun Duirn de los pictos
        (party_set_slot, "p_castle_50",  slot_center_ex_faction, "fac_kingdom_20"),  #pictos atacaran a dal riata
        (party_set_slot, "p_castle_43",  slot_center_ex_faction, "fac_kingdom_20"),  #pictos atacaran a alt cult
        (party_set_slot, "p_castle_24",  slot_center_ex_faction, "fac_kingdom_28"),  #Desmumu quiere Ard de Laigin
        (party_set_slot, "p_town_40",  slot_center_ex_faction, "fac_kingdom_29"),  #Ulaid quiere Emain Mancha de Airgialla
        (party_set_slot, "p_castle_72",  slot_center_ex_faction, "fac_kingdom_30"),  #Ui Neill quiere Sebuirge de Dal Riata
        (party_set_slot, "p_castle_74",  slot_center_ex_faction, "fac_kingdom_30"),  #Ui Neill quiere Magh rath de Ulaid
        (party_set_slot, "p_castle_17",  slot_center_ex_faction, "fac_kingdom_11"),  #Pengwern quiere Caer Legionis de Crafu
        (party_set_slot, "p_castle_33",  slot_center_ex_faction, "fac_kingdom_4"),  #Anglia quiere Ligor Ceaster de Mercia

        # todo: what this does?
        # they seem to depend on which faction has which town
        (call_script, "script_update_village_market_towns"),
        # todo: what this does?
        (call_script, "script_find_neighbors"),
    ]),

    # sets the default availability of notes
    ("initialize_notes", [
        # tableaus
        (try_for_range, ":troop_no", "trp_player", "trp_merchants_end"),
            (add_troop_note_tableau_mesh, ":troop_no", "tableau_troop_note_mesh"),
        (try_end),

        (try_for_range, ":center_no", centers_begin, centers_end),
            (add_party_note_tableau_mesh, ":center_no", "tableau_center_note_mesh"),
        (try_end),

        (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
            (is_between, ":faction_no", "fac_kingdom_1", kingdoms_end),  #Exclude player kingdom
            (add_faction_note_tableau_mesh, ":faction_no", "tableau_faction_note_mesh"),
        (else_try),
            (add_faction_note_tableau_mesh, ":faction_no", "tableau_faction_note_mesh_banner"),
        (try_end),

        # notes
        (troop_set_note_available, "trp_player", 1),
        (troop_set_note_available, "trp_especiales_3", 1),
        (troop_set_note_available, "trp_npcneko", 1),
        (troop_set_note_available, "trp_iniau", 1),
        (troop_set_note_available, "trp_thyr", 1),
        (troop_set_note_available, "trp_npc_tradecompanion", 1),

        (try_for_range, ":troop_no", kings_begin, kings_end),
            (troop_set_note_available, ":troop_no", 1),
        (try_end),

        (try_for_range, ":troop_no", lords_begin, lords_end),
            (troop_set_note_available, ":troop_no", 1),
        (try_end),

        (try_for_range, ":troop_no", kingdom_ladies_begin, kingdom_ladies_end),
            (troop_set_note_available, ":troop_no", 1),
        (try_end),
        (troop_set_note_available, "trp_knight_1_1_wife", 0),

        (try_for_range, ":troop_no", pretenders_begin, pretenders_end),
            (troop_set_note_available, ":troop_no", 1),
        (try_end),

        #Lady and companion notes become available as you meet/recruit them

        (try_for_range, ":faction_no", npc_kingdoms_begin, npc_kingdoms_end),
            (faction_set_note_available, ":faction_no", 1),
        (try_end),
        (faction_set_note_available, "fac_neutral", 0),

        (try_for_range, ":party_no", centers_begin, centers_end),
            (party_set_note_available, ":party_no", 1),
        (try_end),
    ]),

    ("initialize_pretenders", [
        (troop_set_slot, "trp_kingdom_1_pretender", slot_troop_original_faction2, "fac_kingdom_1"),
        (troop_set_slot, "trp_kingdom_2_pretender", slot_troop_original_faction2, "fac_kingdom_2"),
        (troop_set_slot, "trp_kingdom_3_pretender", slot_troop_original_faction2, "fac_kingdom_3"),
        (troop_set_slot, "trp_kingdom_4_pretender", slot_troop_original_faction2, "fac_kingdom_4"),
        (troop_set_slot, "trp_kingdom_5_pretender", slot_troop_original_faction2, "fac_kingdom_5"),
        (troop_set_slot, "trp_kingdom_6_pretender", slot_troop_original_faction2, "fac_kingdom_6"),
        (troop_set_slot, "trp_kingdom_7_pretender", slot_troop_original_faction2, "fac_kingdom_7"),
        (troop_set_slot, "trp_kingdom_8_pretender", slot_troop_original_faction2, "fac_kingdom_8"),
        (troop_set_slot, "trp_kingdom_9_pretender", slot_troop_original_faction2, "fac_kingdom_9"),
        (troop_set_slot, "trp_kingdom_10_pretender", slot_troop_original_faction2, "fac_kingdom_10"),
        (troop_set_slot, "trp_kingdom_11_pretender", slot_troop_original_faction2, "fac_kingdom_11"),

        (troop_set_slot, "trp_kingdom_1_pretender", slot_troop_original_faction, "fac_kingdom_26"),
        (troop_set_slot, "trp_kingdom_2_pretender", slot_troop_original_faction, "fac_kingdom_19"),
        (troop_set_slot, "trp_kingdom_3_pretender", slot_troop_original_faction, "fac_kingdom_22"),
        (troop_set_slot, "trp_kingdom_4_pretender", slot_troop_original_faction, "fac_kingdom_13"),
        (troop_set_slot, "trp_kingdom_5_pretender", slot_troop_original_faction, "fac_kingdom_9"),
        (troop_set_slot, "trp_kingdom_6_pretender", slot_troop_original_faction, "fac_kingdom_6"),
        (troop_set_slot, "trp_kingdom_7_pretender", slot_troop_original_faction, "fac_kingdom_12"),
        (troop_set_slot, "trp_kingdom_8_pretender", slot_troop_original_faction, "fac_kingdom_16"),
        (troop_set_slot, "trp_kingdom_9_pretender", slot_troop_original_faction, "fac_kingdom_18"),
        (troop_set_slot, "trp_kingdom_10_pretender", slot_troop_original_faction, "fac_kingdom_20"),
        (troop_set_slot, "trp_kingdom_11_pretender", slot_troop_original_faction, "fac_kingdom_23"),

        (try_for_range, ":pretender", pretenders_begin, pretenders_end),
            (troop_set_slot, ":pretender", slot_lord_reputation_type, lrep_none),
        (try_end),
    ]),

    ("initialize_faction_troop_types", [

        (try_for_range, ":faction_no", kingdoms_begin, kingdoms_end),
            (faction_get_slot, ":culture", ":faction_no", slot_faction_culture),

            (faction_get_slot, ":troop", ":culture", slot_faction_tier_1_troop),
            (faction_set_slot, ":faction_no", slot_faction_tier_1_troop, ":troop"),
            (faction_get_slot, ":troop", ":culture", slot_faction_tier_2_troop),
            (faction_set_slot, ":faction_no", slot_faction_tier_2_troop, ":troop"),
            (faction_get_slot, ":troop", ":culture", slot_faction_tier_3_troop),
            (faction_set_slot, ":faction_no", slot_faction_tier_3_troop, ":troop"),
            (faction_get_slot, ":troop", ":culture", slot_faction_tier_4_troop),
            (faction_set_slot, ":faction_no", slot_faction_tier_4_troop, ":troop"),
            (faction_get_slot, ":troop", ":culture", slot_faction_tier_5_troop),
            (faction_set_slot, ":faction_no", slot_faction_tier_5_troop, ":troop"),

            (try_begin),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_1"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_jute_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_jute_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_jute_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_jute_prison_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_jute_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_1_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_1_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_1_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_2"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_saxon_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_saxon_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_saxon_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_saxon_prison_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_saxon_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_2_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_2_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_2_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_3"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_saxon_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_saxon_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_saxon_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_saxon_prison_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_saxon_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_3_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_3_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_3_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_4"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_engle_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_engle_infantryt3"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_engle_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_engle_prison_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_engle_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_4_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_4_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_4_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_5"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_saxon_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_saxon_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_saxon_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_saxon_prison_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_saxon_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_5_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_5_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_5_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_6"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_briton_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_briton_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_briton_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_briton_prisoner_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_briton_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_6_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_6_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_6_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_7"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_briton_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_briton_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_briton_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_briton_prisoner_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_briton_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_7_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_7_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_7_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_8"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_briton_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_briton_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_briton_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_briton_prisoner_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_briton_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_8_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_8_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_8_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_9"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_engle_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_engle_infantryt3"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_engle_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_engle_prison_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_engle_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_9_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_9_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_9_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_10"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_briton_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_briton_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_briton_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_briton_prisoner_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_briton_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_10_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_10_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_10_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_11"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_briton_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_briton_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_briton_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_briton_prisoner_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_briton_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_11_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_11_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_11_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_12"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_briton_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_briton_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_briton_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_briton_prisoner_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_briton_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_12_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_12_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_12_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_13"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_engle_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_engle_infantryt3"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_engle_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_engle_prison_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_engle_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_13_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_13_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_13_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_14"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_engle_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_engle_infantryt3"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_engle_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_engle_prison_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_engle_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_14_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_14_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_14_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_15"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_briton_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_briton_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_briton_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_briton_prisoner_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_briton_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_15_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_15_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_15_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_16"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_briton_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_briton_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_briton_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_briton_prisoner_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_briton_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_16_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_16_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_16_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_17"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_irish_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_irish_skirmishert3"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_irish_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_irish_prison_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_irish_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_17_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_17_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_17_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_18"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_briton_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_briton_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_briton_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_briton_prisoner_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_briton_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_18_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_18_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_18_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_19"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_irish_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_irish_skirmishert3"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_irish_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_irish_prison_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_irish_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_19_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_19_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_19_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_20"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_pict_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_pict_horsesquiret3"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_pict_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_pict_prison_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_pict_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_20_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_20_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_20_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_21"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_briton_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_briton_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_briton_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_briton_prisoner_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_briton_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_21_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_21_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_21_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_22"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_briton_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_briton_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_briton_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_briton_prisoner_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_briton_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_22_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_22_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_22_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_23"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_briton_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_briton_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_briton_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_briton_prisoner_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_briton_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_23_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_23_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_23_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_24"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_briton_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_briton_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_briton_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_briton_prisoner_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_briton_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_24_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_24_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_24_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_25"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_briton_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_briton_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_briton_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_briton_prisoner_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_briton_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_25_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_25_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_25_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_26"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_briton_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_briton_skirmishert4"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_briton_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_briton_prisoner_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_briton_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_26_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_26_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_26_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_27"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_irish_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_irish_skirmishert3"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_irish_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_irish_prison_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_irish_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_27_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_27_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_27_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_28"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_irish_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_irish_skirmishert3"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_irish_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_irish_prison_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_irish_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_28_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_28_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_28_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_29"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_irish_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_irish_skirmishert3"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_irish_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_irish_prison_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_irish_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_29_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_29_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_29_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_30"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_irish_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_irish_skirmishert3"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_irish_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_irish_prison_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_irish_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_30_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_30_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_30_reinforcements_c"),
            (else_try),
                (faction_slot_eq, ":faction_no", slot_faction_culture, "fac_culture_31"),

                (faction_set_slot, ":faction_no", slot_faction_deserter_troop, "trp_irish_deserter"),
                (faction_set_slot, ":faction_no", slot_faction_guard_troop, "trp_irish_skirmishert3"),
                (faction_set_slot, ":faction_no", slot_faction_messenger_troop, "trp_irish_messenger"),
                (faction_set_slot, ":faction_no", slot_faction_prison_guard_troop, "trp_irish_prison_guard"),
                (faction_set_slot, ":faction_no", slot_faction_castle_guard_troop, "trp_irish_castle_guard"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_a, "pt_kingdom_31_reinforcements_a"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_b, "pt_kingdom_31_reinforcements_b"),
                (faction_set_slot, ":faction_no", slot_faction_reinforcements_c, "pt_kingdom_31_reinforcements_c"),
            (try_end),
        (try_end),
    ]),
    
    ("initialize_item_info", [     
        # Setting food bonuses - these have been changed to incentivize using historical rations. Bread is the most cost-efficient
        #Staples#note these get overridden in simple triggers in a test on Aptil 2015
        (item_set_slot, "itm_bread", slot_item_food_bonus, 6),  #brought up from 4#gdw keep in mind that this does not expire so hardtack
        (item_set_slot, "itm_grain", slot_item_food_bonus, 3),  #new - can be boiled as porridge

        #Fat sources - preserved
        (item_set_slot, "itm_smoked_fish", slot_item_food_bonus, 6),#have you ever tasted dried fishgdwleftalone
        (item_set_slot, "itm_dried_meat", slot_item_food_bonus, 8),
        (item_set_slot, "itm_cheese", slot_item_food_bonus, 7),
        (item_set_slot, "itm_sausages", slot_item_food_bonus, 6),
        (item_set_slot, "itm_butter", slot_item_food_bonus, 7),  #brought down from 8

        #Fat sources - perishable
        (item_set_slot, "itm_chicken", slot_item_food_bonus, 8),  #brought up from 7
        (item_set_slot, "itm_cattle_meat", slot_item_food_bonus, 11),  #brought down from 7
        (item_set_slot, "itm_pork", slot_item_food_bonus, 9),  #brought down from 6

        #Produce
        (item_set_slot, "itm_raw_olives", slot_item_food_bonus, 11),#imported
        (item_set_slot, "itm_cabbages", slot_item_food_bonus, 4),
        (item_set_slot, "itm_raw_grapes", slot_item_food_bonus, 10),#spoil
        (item_set_slot, "itm_apples", slot_item_food_bonus, 5),  #brought down from 5

        #Sweet items
        (item_set_slot, "itm_mead", slot_item_food_bonus, 9),  #brought down from 8
        (item_set_slot, "itm_honey", slot_item_food_bonus, 9),  #brought down from 12

        (item_set_slot, "itm_wine", slot_item_food_bonus, 12),
        (item_set_slot, "itm_ale", slot_item_food_bonus, 9),

        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        #-#-#-#Hunting chief Mod begin#-#-#-#
        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        (item_set_slot, "itm_deer_meat", slot_item_food_bonus, 11),
        (item_set_slot, "itm_boar_meat", slot_item_food_bonus, 13),
        (item_set_slot, "itm_wolf_meat", slot_item_food_bonus, 11),
        (item_set_slot, "itm_goat_meat", slot_item_food_bonus, 11),
        (item_set_slot, "itm_goatb_meat", slot_item_food_bonus, 13),#createnewname
        (item_set_slot, "itm_wilddonkey_meat", slot_item_food_bonus, 12),
        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#
        #-#-#-#Hunting chief Mod end#-#-#-#
        #-#-#-#-#-#-#-#-#-#-#-#-#-#-#

        #Estandartes bonus de moral chief
        (item_set_slot, "itm_wessexbanner1", slot_item_food_bonus, 15),
        (item_set_slot, "itm_cavalrybannert2", slot_item_food_bonus, 16),
        (item_set_slot, "itm_spearbannert2", slot_item_food_bonus, 15),
        (item_set_slot, "itm_spearbanner4", slot_item_food_bonus, 15),
        (item_set_slot, "itm_spearbanner5", slot_item_food_bonus, 15),
        (item_set_slot, "itm_wessexbanner6", slot_item_food_bonus, 15),
        (item_set_slot, "itm_wessexbanner7", slot_item_food_bonus, 15),
        (item_set_slot, "itm_wessexbanner8", slot_item_food_bonus, 15),
        (item_set_slot, "itm_wessexbanner9", slot_item_food_bonus, 15),
        (item_set_slot, "itm_heraldicbannert3", slot_item_food_bonus, 16),


        #Item economic settings
        (item_set_slot, "itm_grain", slot_item_urban_demand, 20),
        (item_set_slot, "itm_grain", slot_item_rural_demand, 20),
        (item_set_slot, "itm_grain", slot_item_desert_demand, 20),
        (item_set_slot, "itm_grain", slot_item_production_slot, slot_center_acres_grain),
        (item_set_slot, "itm_grain", slot_item_production_string, "str_acres_grain"),
        (item_set_slot, "itm_grain", slot_item_base_price, 20),  #chief cambia

        (item_set_slot, "itm_bread", slot_item_urban_demand, 20),
        (item_set_slot, "itm_bread", slot_item_rural_demand, 30),
        (item_set_slot, "itm_bread", slot_item_desert_demand, 30),
        (item_set_slot, "itm_bread", slot_item_production_slot, slot_center_mills),
        (item_set_slot, "itm_bread", slot_item_production_string, "str_mills"),
        (item_set_slot, "itm_bread", slot_item_primary_raw_material, "itm_grain"),
        (item_set_slot, "itm_bread", slot_item_input_number, 2),
        (item_set_slot, "itm_bread", slot_item_output_per_run, 6),
        (item_set_slot, "itm_bread", slot_item_overhead_per_run, 12),
        (item_set_slot, "itm_bread", slot_item_base_price, 50),  #chief cambia
        (item_set_slot, "itm_bread", slot_item_enterprise_building_cost, 7500),  #chief cambiado

        (item_set_slot, "itm_ale", slot_item_urban_demand, 15),
        (item_set_slot, "itm_ale", slot_item_rural_demand, 25),
        (item_set_slot, "itm_ale", slot_item_desert_demand, 0),
        (item_set_slot, "itm_ale", slot_item_production_slot, slot_center_breweries),
        (item_set_slot, "itm_ale", slot_item_production_string, "str_breweries"),
        (item_set_slot, "itm_ale", slot_item_base_price, 100),
        (item_set_slot, "itm_ale", slot_item_primary_raw_material, "itm_grain"),
        (item_set_slot, "itm_ale", slot_item_input_number, 1),
        (item_set_slot, "itm_ale", slot_item_output_per_run, 2),
        (item_set_slot, "itm_ale", slot_item_overhead_per_run, 39),#gdw
        (item_set_slot, "itm_ale", slot_item_base_price, 250),  #chief cambia
        (item_set_slot, "itm_ale", slot_item_enterprise_building_cost, 16000),  #gdw cambia

        (item_set_slot, "itm_wine", slot_item_urban_demand, 35),
        (item_set_slot, "itm_wine", slot_item_rural_demand, 10),
        (item_set_slot, "itm_wine", slot_item_desert_demand, 25),
        (item_set_slot, "itm_wine", slot_item_production_slot, slot_center_wine_presses),
        (item_set_slot, "itm_wine", slot_item_production_string, "str_presses"),
        (item_set_slot, "itm_wine", slot_item_primary_raw_material, "itm_raw_grapes"),#What happened to base price here?gdw
        (item_set_slot, "itm_wine", slot_item_input_number, 1),  #chief cambia
        (item_set_slot, "itm_wine", slot_item_output_per_run, 2),
        (item_set_slot, "itm_wine", slot_item_overhead_per_run, 40),  #chief cambiA
        (item_set_slot, "itm_wine", slot_item_base_price, 450),  #chief cambia
        (item_set_slot, "itm_wine", slot_item_enterprise_building_cost, 24500),  #chief cambia

        (item_set_slot, "itm_mead", slot_item_urban_demand, 25),
        (item_set_slot, "itm_mead", slot_item_rural_demand, 20),
        (item_set_slot, "itm_mead", slot_item_desert_demand, 0),
        (item_set_slot, "itm_mead", slot_item_production_slot, slot_center_breweries),
        (item_set_slot, "itm_mead", slot_item_production_string, "str_presses"),
        (item_set_slot, "itm_mead", slot_item_base_price, 120),
        (item_set_slot, "itm_mead", slot_item_primary_raw_material, "itm_honey"),
        (item_set_slot, "itm_mead", slot_item_input_number, 1),  #chief cambia
        (item_set_slot, "itm_mead", slot_item_output_per_run, 2),
        (item_set_slot, "itm_mead", slot_item_overhead_per_run, 45),  #chief cambiA
        (item_set_slot, "itm_mead", slot_item_base_price, 325),  #chief cambia
        (item_set_slot, "itm_mead", slot_item_enterprise_building_cost, 20000),  #chief cambia gdwnot in game

        (item_set_slot, "itm_raw_grapes", slot_item_urban_demand, 13),
        (item_set_slot, "itm_raw_grapes", slot_item_rural_demand, 0),
        (item_set_slot, "itm_raw_grapes", slot_item_desert_demand, 0),
        (item_set_slot, "itm_raw_grapes", slot_item_production_slot, slot_center_acres_vineyard),
        (item_set_slot, "itm_raw_grapes", slot_item_production_string, "str_acres_orchard"),
        (item_set_slot, "itm_raw_grapes", slot_item_is_raw_material_only_for, "itm_wine"),
        (item_set_slot, "itm_raw_grapes", slot_item_base_price, 125),  #chief cambia

        (item_set_slot, "itm_apples", slot_item_urban_demand, 9),
        (item_set_slot, "itm_apples", slot_item_rural_demand, 5),
        (item_set_slot, "itm_apples", slot_item_desert_demand, 0),
        (item_set_slot, "itm_apples", slot_item_production_slot, slot_center_acres_vineyard),
        (item_set_slot, "itm_apples", slot_item_production_string, "str_acres_orchard"),
        (item_set_slot, "itm_apples", slot_item_base_price, 50),  #chief cambia

        (item_set_slot, "itm_smoked_fish", slot_item_urban_demand, 13),
        (item_set_slot, "itm_smoked_fish", slot_item_rural_demand, 18),
        (item_set_slot, "itm_smoked_fish", slot_item_desert_demand, 16),
        (item_set_slot, "itm_smoked_fish", slot_item_production_slot, slot_center_fishing_fleet),
        (item_set_slot, "itm_smoked_fish", slot_item_production_string, "str_boats"),

        (item_set_slot, "itm_salt", slot_item_urban_demand, 6),
        (item_set_slot, "itm_salt", slot_item_rural_demand, 3),
        (item_set_slot, "itm_salt", slot_item_desert_demand, -1),
        (item_set_slot, "itm_salt", slot_item_production_slot, slot_center_salt_pans),
        (item_set_slot, "itm_salt", slot_item_production_string, "str_pans"),

        (item_set_slot, "itm_dried_meat", slot_item_urban_demand, 10),
        (item_set_slot, "itm_dried_meat", slot_item_rural_demand, 10),
        (item_set_slot, "itm_dried_meat", slot_item_desert_demand, -1),
        (item_set_slot, "itm_dried_meat", slot_item_production_slot, slot_center_head_cattle),
        (item_set_slot, "itm_dried_meat", slot_item_production_string, "str_head_cattle"),

        (item_set_slot, "itm_cattle_meat", slot_item_urban_demand, 16),
        (item_set_slot, "itm_cattle_meat", slot_item_rural_demand, 5),
        (item_set_slot, "itm_cattle_meat", slot_item_desert_demand, -1),
        (item_set_slot, "itm_cattle_meat", slot_item_production_slot, slot_center_head_cattle),
        (item_set_slot, "itm_cattle_meat", slot_item_production_string, "str_head_cattle"),

        (item_set_slot, "itm_cheese", slot_item_urban_demand, 15),
        (item_set_slot, "itm_cheese", slot_item_rural_demand, 15),
        (item_set_slot, "itm_cheese", slot_item_desert_demand, 10),
        (item_set_slot, "itm_cheese", slot_item_production_slot, slot_center_head_cattle),
        (item_set_slot, "itm_cheese", slot_item_production_string, "str_head_cattle"),

        (item_set_slot, "itm_butter", slot_item_urban_demand, 10),
        (item_set_slot, "itm_butter", slot_item_rural_demand, 5),
        (item_set_slot, "itm_butter", slot_item_desert_demand, 2),
        (item_set_slot, "itm_butter", slot_item_production_slot, slot_center_head_cattle),
        (item_set_slot, "itm_butter", slot_item_production_string, "str_head_cattle"),

        (item_set_slot, "itm_leatherwork", slot_item_urban_demand, 20),
        (item_set_slot, "itm_leatherwork", slot_item_rural_demand, 10),
        (item_set_slot, "itm_leatherwork", slot_item_desert_demand, 10),
        (item_set_slot, "itm_leatherwork", slot_item_production_slot, slot_center_tanneries),
        (item_set_slot, "itm_leatherwork", slot_item_production_string, "str_tanneries"),
        (item_set_slot, "itm_leatherwork", slot_item_primary_raw_material, "itm_raw_leather"),
        (item_set_slot, "itm_leatherwork", slot_item_input_number, 3),
        (item_set_slot, "itm_leatherwork", slot_item_output_per_run, 3),
        (item_set_slot, "itm_leatherwork", slot_item_overhead_per_run, 43),
        (item_set_slot, "itm_leatherwork", slot_item_base_price, 400),  #chief cambia
        (item_set_slot, "itm_leatherwork", slot_item_enterprise_building_cost, 14500),  #chief cambia

        (item_set_slot, "itm_raw_leather", slot_item_urban_demand, 8),
        (item_set_slot, "itm_raw_leather", slot_item_rural_demand, 0),
        (item_set_slot, "itm_raw_leather", slot_item_desert_demand, 0),
        (item_set_slot, "itm_raw_leather", slot_item_production_slot, slot_center_head_cattle),
        (item_set_slot, "itm_raw_leather", slot_item_production_string, "str_head_cattle"),
        (item_set_slot, "itm_raw_leather", slot_item_is_raw_material_only_for, "itm_leatherwork"),
        (item_set_slot, "itm_raw_leather", slot_item_base_price, 275),  #chief cambia

        (item_set_slot, "itm_sausages", slot_item_urban_demand, 7),
        (item_set_slot, "itm_sausages", slot_item_rural_demand, 10),
        (item_set_slot, "itm_sausages", slot_item_desert_demand, -1),
        (item_set_slot, "itm_sausages", slot_item_production_slot, slot_center_head_sheep),
        (item_set_slot, "itm_sausages", slot_item_production_string, "str_head_sheep"),

        (item_set_slot, "itm_wool", slot_item_urban_demand, 0),
        (item_set_slot, "itm_wool", slot_item_rural_demand, 0),
        (item_set_slot, "itm_wool", slot_item_desert_demand, 0),
        (item_set_slot, "itm_wool", slot_item_production_slot, slot_center_head_sheep),
        (item_set_slot, "itm_wool", slot_item_production_string, "str_head_sheep"),
        (item_set_slot, "itm_wool", slot_item_is_raw_material_only_for, "itm_wool_cloth"),
        (item_set_slot, "itm_wool", slot_item_base_price, 225),  #chief cambia

        (item_set_slot, "itm_wool_cloth", slot_item_urban_demand, 16),
        (item_set_slot, "itm_wool_cloth", slot_item_rural_demand, 23),
        (item_set_slot, "itm_wool_cloth", slot_item_desert_demand, 5),
        (item_set_slot, "itm_wool_cloth", slot_item_production_slot, slot_center_wool_looms),
        (item_set_slot, "itm_wool_cloth", slot_item_production_string, "str_looms"),
        (item_set_slot, "itm_wool_cloth", slot_item_primary_raw_material, "itm_wool"),
        (item_set_slot, "itm_wool_cloth", slot_item_input_number, 1),
        (item_set_slot, "itm_wool_cloth", slot_item_output_per_run, 2),
        (item_set_slot, "itm_wool_cloth", slot_item_overhead_per_run, 29),
        (item_set_slot, "itm_wool_cloth", slot_item_base_price, 350),  #chief cambia
        (item_set_slot, "itm_wool_cloth", slot_item_enterprise_building_cost, 15000),  #chief cambia

        (item_set_slot, "itm_raw_flax", slot_item_urban_demand, 0),
        (item_set_slot, "itm_raw_flax", slot_item_rural_demand, 0),
        (item_set_slot, "itm_raw_flax", slot_item_desert_demand, 0),
        (item_set_slot, "itm_raw_flax", slot_item_production_slot, slot_center_acres_flax),
        (item_set_slot, "itm_raw_flax", slot_item_production_string, "str_acres_flax"),
        (item_set_slot, "itm_raw_flax", slot_item_is_raw_material_only_for, "itm_linen"),
        (item_set_slot, "itm_raw_flax", slot_item_base_price, 200),  #chief cambiado

        (item_set_slot, "itm_linen", slot_item_urban_demand, 22),
        (item_set_slot, "itm_linen", slot_item_rural_demand, 12),
        (item_set_slot, "itm_linen", slot_item_desert_demand, 15),
        (item_set_slot, "itm_linen", slot_item_production_slot, slot_center_linen_looms),
        (item_set_slot, "itm_linen", slot_item_production_string, "str_looms"),
        (item_set_slot, "itm_linen", slot_item_primary_raw_material, "itm_raw_flax"),
        (item_set_slot, "itm_linen", slot_item_input_number, 2),
        (item_set_slot, "itm_linen", slot_item_output_per_run, 2),
        (item_set_slot, "itm_linen", slot_item_overhead_per_run, 41),
        (item_set_slot, "itm_linen", slot_item_base_price, 450),  #chief cambiado
        (item_set_slot, "itm_linen", slot_item_enterprise_building_cost, 18500),  #chief cambia

        (item_set_slot, "itm_iron", slot_item_urban_demand, 0),
        (item_set_slot, "itm_iron", slot_item_rural_demand, 0),
        (item_set_slot, "itm_iron", slot_item_desert_demand, 0),
        (item_set_slot, "itm_iron", slot_item_production_slot, slot_center_iron_deposits),
        (item_set_slot, "itm_iron", slot_item_production_string, "str_deposits"),
        (item_set_slot, "itm_iron", slot_item_is_raw_material_only_for, "itm_tools"),
        (item_set_slot, "itm_iron", slot_item_base_price, 200),  #chief cambia
        #silver
        (item_set_slot, "itm_silver", slot_item_urban_demand, 0),
        (item_set_slot, "itm_silver", slot_item_rural_demand, 0),
        (item_set_slot, "itm_silver", slot_item_desert_demand, 0),
        (item_set_slot, "itm_silver", slot_item_production_slot, slot_center_iron_deposits),
        (item_set_slot, "itm_silver", slot_item_production_string, "str_deposits"),
        #stone
        (item_set_slot, "itm_mineral", slot_item_urban_demand, 0),
        (item_set_slot, "itm_mineral", slot_item_rural_demand, 0),
        (item_set_slot, "itm_mineral", slot_item_desert_demand, 0),
        (item_set_slot, "itm_mineral", slot_item_production_slot, slot_center_iron_deposits),
        (item_set_slot, "itm_mineral", slot_item_production_string, "str_deposits"),

        (item_set_slot, "itm_tools", slot_item_urban_demand, 24),
        (item_set_slot, "itm_tools", slot_item_rural_demand, 14),
        (item_set_slot, "itm_tools", slot_item_desert_demand, 7),
        (item_set_slot, "itm_tools", slot_item_production_slot, slot_center_smithies),
        (item_set_slot, "itm_tools", slot_item_production_string, "str_smithies"),
        (item_set_slot, "itm_tools", slot_item_primary_raw_material, "itm_iron"),
        (item_set_slot, "itm_tools", slot_item_input_number, 2),
        (item_set_slot, "itm_tools", slot_item_output_per_run, 2),
        (item_set_slot, "itm_tools", slot_item_overhead_per_run, 32),
        (item_set_slot, "itm_tools", slot_item_base_price, 450),  #chief cambia
        (item_set_slot, "itm_tools", slot_item_enterprise_building_cost, 15500),  #chief cambia

        (item_set_slot, "itm_pottery", slot_item_urban_demand, 15),
        (item_set_slot, "itm_pottery", slot_item_rural_demand, 5),
        (item_set_slot, "itm_pottery", slot_item_desert_demand, -1),
        (item_set_slot, "itm_pottery", slot_item_production_slot, slot_center_pottery_kilns),
        (item_set_slot, "itm_pottery", slot_item_production_string, "str_kilns"),

        (item_set_slot, "itm_oil", slot_item_urban_demand, 20),
        (item_set_slot, "itm_oil", slot_item_rural_demand, 15),
        (item_set_slot, "itm_oil", slot_item_desert_demand, -1),
        (item_set_slot, "itm_oil", slot_item_production_slot, slot_center_olive_presses),
        (item_set_slot, "itm_oil", slot_item_production_string, "str_presses"),
        (item_set_slot, "itm_oil", slot_item_primary_raw_material, "itm_raw_olives"),
        (item_set_slot, "itm_oil", slot_item_input_number, 5),
        (item_set_slot, "itm_oil", slot_item_output_per_run, 2),
        (item_set_slot, "itm_oil", slot_item_overhead_per_run, 63),#gdw
        (item_set_slot, "itm_oil", slot_item_base_price, 700),  #chief cambia
        (item_set_slot, "itm_oil", slot_item_enterprise_building_cost, 20000),  #chief cambia

        (item_set_slot, "itm_raw_olives", slot_item_urban_demand, 9),
        (item_set_slot, "itm_raw_olives", slot_item_rural_demand, 0),
        (item_set_slot, "itm_raw_olives", slot_item_desert_demand, 0),
        (item_set_slot, "itm_raw_olives", slot_item_production_slot, slot_center_acres_olives),
        (item_set_slot, "itm_raw_olives", slot_item_production_string, "str_olive_groves"),
        (item_set_slot, "itm_raw_olives", slot_item_is_raw_material_only_for, "itm_oil"),
        (item_set_slot, "itm_raw_olives", slot_item_base_price, 150),  #chief cambia

        (item_set_slot, "itm_velvet", slot_item_urban_demand, 10),
        (item_set_slot, "itm_velvet", slot_item_rural_demand, 0),
        (item_set_slot, "itm_velvet", slot_item_desert_demand, -1),
        (item_set_slot, "itm_velvet", slot_item_production_slot, slot_center_silk_looms),
        (item_set_slot, "itm_velvet", slot_item_production_string, "str_looms"),
        (item_set_slot, "itm_velvet", slot_item_primary_raw_material, "itm_wool"),
        (item_set_slot, "itm_velvet", slot_item_input_number, 2),
        (item_set_slot, "itm_velvet", slot_item_output_per_run, 2),
        (item_set_slot, "itm_velvet", slot_item_overhead_per_run, 35),
        (item_set_slot, "itm_velvet", slot_item_base_price, 650),  #chief cambia
        (item_set_slot, "itm_velvet", slot_item_secondary_raw_material, "itm_raw_dyes"),
        (item_set_slot, "itm_velvet", slot_item_enterprise_building_cost, 15000),  #cgdw

        (item_set_slot, "itm_rare_fabric", slot_item_urban_demand, 0),
        (item_set_slot, "itm_rare_fabric", slot_item_rural_demand, 0),
        (item_set_slot, "itm_rare_fabric", slot_item_production_slot, slot_center_silk_farms),
        (item_set_slot, "itm_rare_fabric", slot_item_production_string, "str_deposits"),

        (item_set_slot, "itm_raw_dyes", slot_item_urban_demand, 25),
        (item_set_slot, "itm_raw_dyes", slot_item_rural_demand, 10),
        (item_set_slot, "itm_raw_dyes", slot_item_desert_demand, -1),
        (item_set_slot, "itm_raw_dyes", slot_item_production_string, "str_caravans"),
        (item_set_slot, "itm_raw_dyes", slot_item_base_price, 400),  #chief cambia

        (item_set_slot, "itm_spice", slot_item_urban_demand, 25),
        (item_set_slot, "itm_spice", slot_item_rural_demand, 0),
        (item_set_slot, "itm_spice", slot_item_desert_demand, 5),
        (item_set_slot, "itm_spice", slot_item_production_string, "str_caravans"),

        (item_set_slot, "itm_furs", slot_item_urban_demand, 15),
        (item_set_slot, "itm_furs", slot_item_rural_demand, 5),
        (item_set_slot, "itm_furs", slot_item_desert_demand, -1),
        (item_set_slot, "itm_furs", slot_item_production_slot, slot_center_fur_traps),
        (item_set_slot, "itm_furs", slot_item_production_string, "str_traps"),

        (item_set_slot, "itm_honey", slot_item_urban_demand, 12),
        (item_set_slot, "itm_honey", slot_item_rural_demand, 3),
        (item_set_slot, "itm_honey", slot_item_desert_demand, -1),
        (item_set_slot, "itm_honey", slot_item_production_slot, slot_center_apiaries),
        (item_set_slot, "itm_honey", slot_item_production_string, "str_hives"),

        (item_set_slot, "itm_cabbages", slot_item_urban_demand, 12),
        (item_set_slot, "itm_cabbages", slot_item_rural_demand, 7),
        (item_set_slot, "itm_cabbages", slot_item_desert_demand, 7),
        (item_set_slot, "itm_cabbages", slot_item_production_slot, slot_center_household_gardens),
        (item_set_slot, "itm_cabbages", slot_item_production_string, "str_gardens"),

        ##      (item_set_slot, "itm_silver", slot_item_urban_demand, 7),
        ##      (item_set_slot, "itm_silver", slot_item_rural_demand, 7),
        ##      (item_set_slot, "itm_silver", slot_item_desert_demand, 7),
        ##      (item_set_slot, "itm_silver", slot_item_production_slot, slot_center_household_gardens),
        ##      (item_set_slot, "itm_silver", slot_item_production_string, "str_acres_oasis"),

        (item_set_slot, "itm_chicken", slot_item_urban_demand, 30),
        (item_set_slot, "itm_chicken", slot_item_rural_demand, 13),
        (item_set_slot, "itm_chicken", slot_item_desert_demand, -1),

        (item_set_slot, "itm_pork", slot_item_urban_demand, 40),
        (item_set_slot, "itm_pork", slot_item_rural_demand, 10),
        (item_set_slot, "itm_pork", slot_item_desert_demand, -1),

        # Setting book intelligence requirements
        (item_set_slot, "itm_book_tactics", slot_item_intelligence_requirement, 9),
        (item_set_slot, "itm_book_persuasion", slot_item_intelligence_requirement, 8),
        (item_set_slot, "itm_book_leadership", slot_item_intelligence_requirement, 7),
        (item_set_slot, "itm_book_intelligence", slot_item_intelligence_requirement, 10),
        (item_set_slot, "itm_book_trade_reference", slot_item_intelligence_requirement, 10),
        (item_set_slot, "itm_book_weapon_mastery", slot_item_intelligence_requirement, 9),
        (item_set_slot, "itm_book_engineering", slot_item_intelligence_requirement, 12),

        (item_set_slot, "itm_book_wound_treatment_reference", slot_item_intelligence_requirement, 9),#gdw10
        (item_set_slot, "itm_book_training", slot_item_intelligence_requirement, 9),#gdw10
        (item_set_slot, "itm_book_surgery", slot_item_intelligence_requirement, 9),   #gdw10
    ]),

    ("initialize_town_arena_info", [
        (party_set_slot,"p_town_1", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_1", slot_town_arena_melee_1_team_size,  1),
        (party_set_slot,"p_town_1", slot_town_arena_melee_2_num_teams,  4),
        (party_set_slot,"p_town_1", slot_town_arena_melee_2_team_size,  1),
        (party_set_slot,"p_town_1", slot_town_arena_melee_3_num_teams,  4),
        (party_set_slot,"p_town_1", slot_town_arena_melee_3_team_size,  1),

        (party_set_slot,"p_town_2", slot_town_arena_melee_1_num_teams,  4),
        (party_set_slot,"p_town_2", slot_town_arena_melee_1_team_size,  4),
        (party_set_slot,"p_town_2", slot_town_arena_melee_2_num_teams,  4),
        (party_set_slot,"p_town_2", slot_town_arena_melee_2_team_size,  6),
        (party_set_slot,"p_town_2", slot_town_arena_melee_3_num_teams,  4),
        (party_set_slot,"p_town_2", slot_town_arena_melee_3_team_size,  8),

        (party_set_slot,"p_town_3", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_3", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_3", slot_town_arena_melee_2_num_teams,  2),
        (party_set_slot,"p_town_3", slot_town_arena_melee_2_team_size,  8),
        (party_set_slot,"p_town_3", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_3", slot_town_arena_melee_3_team_size,  8),

        (party_set_slot,"p_town_4", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_4", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_4", slot_town_arena_melee_2_num_teams,  3),
        (party_set_slot,"p_town_4", slot_town_arena_melee_2_team_size,  8),
        (party_set_slot,"p_town_4", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_4", slot_town_arena_melee_3_team_size,  5),

        (party_set_slot,"p_town_5", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_5", slot_town_arena_melee_1_team_size,  3),
        (party_set_slot,"p_town_5", slot_town_arena_melee_2_num_teams,  2),
        (party_set_slot,"p_town_5", slot_town_arena_melee_2_team_size,  5),
        (party_set_slot,"p_town_5", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_5", slot_town_arena_melee_3_team_size,  8),

        (party_set_slot,"p_town_6", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_6", slot_town_arena_melee_1_team_size,  4),
        (party_set_slot,"p_town_6", slot_town_arena_melee_2_num_teams,  3),
        (party_set_slot,"p_town_6", slot_town_arena_melee_2_team_size,  4),
        (party_set_slot,"p_town_6", slot_town_arena_melee_3_num_teams,  3),
        (party_set_slot,"p_town_6", slot_town_arena_melee_3_team_size,  6),

        (party_set_slot,"p_town_7", slot_town_arena_melee_1_num_teams,  4),
        (party_set_slot,"p_town_7", slot_town_arena_melee_1_team_size,  4),
        (party_set_slot,"p_town_7", slot_town_arena_melee_2_num_teams,  4),
        (party_set_slot,"p_town_7", slot_town_arena_melee_2_team_size,  6),
        (party_set_slot,"p_town_7", slot_town_arena_melee_3_num_teams,  4),
        (party_set_slot,"p_town_7", slot_town_arena_melee_3_team_size,  8),

        (party_set_slot,"p_town_8", slot_town_arena_melee_1_num_teams,  3),
        (party_set_slot,"p_town_8", slot_town_arena_melee_1_team_size,  1),
        (party_set_slot,"p_town_8", slot_town_arena_melee_2_num_teams,  3),
        (party_set_slot,"p_town_8", slot_town_arena_melee_2_team_size,  3),
        (party_set_slot,"p_town_8", slot_town_arena_melee_3_num_teams,  3),
        (party_set_slot,"p_town_8", slot_town_arena_melee_3_team_size,  7),

        (party_set_slot,"p_town_9", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_9", slot_town_arena_melee_1_team_size,  2),
        (party_set_slot,"p_town_9", slot_town_arena_melee_2_num_teams,  2),
        (party_set_slot,"p_town_9", slot_town_arena_melee_2_team_size,  5),
        (party_set_slot,"p_town_9", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_9", slot_town_arena_melee_3_team_size,  8),

        (party_set_slot,"p_town_10", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_10", slot_town_arena_melee_1_team_size,  3),
        (party_set_slot,"p_town_10", slot_town_arena_melee_2_num_teams,  2),
        (party_set_slot,"p_town_10", slot_town_arena_melee_2_team_size,  5),
        (party_set_slot,"p_town_10", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_10", slot_town_arena_melee_3_team_size,  8),

        (party_set_slot,"p_town_11", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_11", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_11", slot_town_arena_melee_2_num_teams,  3),
        (party_set_slot,"p_town_11", slot_town_arena_melee_2_team_size,  4),
        (party_set_slot,"p_town_11", slot_town_arena_melee_3_num_teams,  3),
        (party_set_slot,"p_town_11", slot_town_arena_melee_3_team_size,  6),

        (party_set_slot,"p_town_12", slot_town_arena_melee_1_num_teams,  3),
        (party_set_slot,"p_town_12", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_12", slot_town_arena_melee_2_num_teams,  4),
        (party_set_slot,"p_town_12", slot_town_arena_melee_2_team_size,  6),
        (party_set_slot,"p_town_12", slot_town_arena_melee_3_num_teams,  4),
        (party_set_slot,"p_town_12", slot_town_arena_melee_3_team_size,  5),

        (party_set_slot,"p_town_13", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_13", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_13", slot_town_arena_melee_2_num_teams,  4),
        (party_set_slot,"p_town_13", slot_town_arena_melee_2_team_size,  5),
        (party_set_slot,"p_town_13", slot_town_arena_melee_3_num_teams,  4),
        (party_set_slot,"p_town_13", slot_town_arena_melee_3_team_size,  7),

        (party_set_slot,"p_town_14", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_14", slot_town_arena_melee_1_team_size,  4),
        (party_set_slot,"p_town_14", slot_town_arena_melee_2_num_teams,  2),
        (party_set_slot,"p_town_14", slot_town_arena_melee_2_team_size,  5),
        (party_set_slot,"p_town_14", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_14", slot_town_arena_melee_3_team_size,  6),

        (party_set_slot,"p_town_15", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_15", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_15", slot_town_arena_melee_2_num_teams,  3),
        (party_set_slot,"p_town_15", slot_town_arena_melee_2_team_size,  4),
        (party_set_slot,"p_town_15", slot_town_arena_melee_3_num_teams,  3),
        (party_set_slot,"p_town_15", slot_town_arena_melee_3_team_size,  6),

        (party_set_slot,"p_town_16", slot_town_arena_melee_1_num_teams,  3),
        (party_set_slot,"p_town_16", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_16", slot_town_arena_melee_2_num_teams,  4),
        (party_set_slot,"p_town_16", slot_town_arena_melee_2_team_size,  6),
        (party_set_slot,"p_town_16", slot_town_arena_melee_3_num_teams,  4),
        (party_set_slot,"p_town_16", slot_town_arena_melee_3_team_size,  5),

        (party_set_slot,"p_town_17", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_17", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_17", slot_town_arena_melee_2_num_teams,  4),
        (party_set_slot,"p_town_17", slot_town_arena_melee_2_team_size,  5),
        (party_set_slot,"p_town_17", slot_town_arena_melee_3_num_teams,  4),
        (party_set_slot,"p_town_17", slot_town_arena_melee_3_team_size,  7),

        (party_set_slot,"p_town_18", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_18", slot_town_arena_melee_1_team_size,  4),
        (party_set_slot,"p_town_18", slot_town_arena_melee_2_num_teams,  2),
        (party_set_slot,"p_town_18", slot_town_arena_melee_2_team_size,  5),
        (party_set_slot,"p_town_18", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_18", slot_town_arena_melee_3_team_size,  6),

        (party_set_slot,"p_town_19", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_19", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_19", slot_town_arena_melee_2_num_teams,  4),
        (party_set_slot,"p_town_19", slot_town_arena_melee_2_team_size,  4),
        (party_set_slot,"p_town_19", slot_town_arena_melee_3_num_teams,  4),
        (party_set_slot,"p_town_19", slot_town_arena_melee_3_team_size,  6),

        (party_set_slot,"p_town_20", slot_town_arena_melee_1_num_teams,  4),
        (party_set_slot,"p_town_20", slot_town_arena_melee_1_team_size,  2),
        (party_set_slot,"p_town_20", slot_town_arena_melee_2_num_teams,  4),
        (party_set_slot,"p_town_20", slot_town_arena_melee_2_team_size,  4),
        (party_set_slot,"p_town_20", slot_town_arena_melee_3_num_teams,  4),
        (party_set_slot,"p_town_20", slot_town_arena_melee_3_team_size,  6),

        (party_set_slot,"p_town_21", slot_town_arena_melee_1_num_teams,  3),
        (party_set_slot,"p_town_21", slot_town_arena_melee_1_team_size,  3),
        (party_set_slot,"p_town_21", slot_town_arena_melee_2_num_teams,  2),
        (party_set_slot,"p_town_21", slot_town_arena_melee_2_team_size,  6),
        (party_set_slot,"p_town_21", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_21", slot_town_arena_melee_3_team_size,  8),

        (party_set_slot,"p_town_22", slot_town_arena_melee_1_num_teams,  4),
        (party_set_slot,"p_town_22", slot_town_arena_melee_1_team_size,  3),
        (party_set_slot,"p_town_22", slot_town_arena_melee_2_num_teams,  3),
        (party_set_slot,"p_town_22", slot_town_arena_melee_2_team_size,  4),
        (party_set_slot,"p_town_22", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_22", slot_town_arena_melee_3_team_size,  6),

        (party_set_slot,"p_town_23", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_23", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_23", slot_town_arena_melee_2_num_teams,  2),
        (party_set_slot,"p_town_23", slot_town_arena_melee_2_team_size,  8),
        (party_set_slot,"p_town_23", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_23", slot_town_arena_melee_3_team_size,  8),

        (party_set_slot,"p_town_24", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_24", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_24", slot_town_arena_melee_2_num_teams,  3),
        (party_set_slot,"p_town_24", slot_town_arena_melee_2_team_size,  8),
        (party_set_slot,"p_town_24", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_24", slot_town_arena_melee_3_team_size,  5),

        (party_set_slot,"p_town_25", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_25", slot_town_arena_melee_1_team_size,  3),
        (party_set_slot,"p_town_25", slot_town_arena_melee_2_num_teams,  2),
        (party_set_slot,"p_town_25", slot_town_arena_melee_2_team_size,  5),
        (party_set_slot,"p_town_25", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_25", slot_town_arena_melee_3_team_size,  8),

        (party_set_slot,"p_town_26", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_26", slot_town_arena_melee_1_team_size,  4),
        (party_set_slot,"p_town_26", slot_town_arena_melee_2_num_teams,  3),
        (party_set_slot,"p_town_26", slot_town_arena_melee_2_team_size,  4),
        (party_set_slot,"p_town_26", slot_town_arena_melee_3_num_teams,  3),
        (party_set_slot,"p_town_26", slot_town_arena_melee_3_team_size,  6),

        (party_set_slot,"p_town_27", slot_town_arena_melee_1_num_teams,  4),
        (party_set_slot,"p_town_27", slot_town_arena_melee_1_team_size,  4),
        (party_set_slot,"p_town_27", slot_town_arena_melee_2_num_teams,  4),
        (party_set_slot,"p_town_27", slot_town_arena_melee_2_team_size,  6),
        (party_set_slot,"p_town_27", slot_town_arena_melee_3_num_teams,  4),
        (party_set_slot,"p_town_27", slot_town_arena_melee_3_team_size,  8),

        (party_set_slot,"p_town_28", slot_town_arena_melee_1_num_teams,  3),
        (party_set_slot,"p_town_28", slot_town_arena_melee_1_team_size,  1),
        (party_set_slot,"p_town_28", slot_town_arena_melee_2_num_teams,  3),
        (party_set_slot,"p_town_28", slot_town_arena_melee_2_team_size,  3),
        (party_set_slot,"p_town_28", slot_town_arena_melee_3_num_teams,  3),
        (party_set_slot,"p_town_28", slot_town_arena_melee_3_team_size,  7),

        (party_set_slot,"p_town_29", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_29", slot_town_arena_melee_1_team_size,  2),
        (party_set_slot,"p_town_29", slot_town_arena_melee_2_num_teams,  2),
        (party_set_slot,"p_town_29", slot_town_arena_melee_2_team_size,  5),
        (party_set_slot,"p_town_29", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_29", slot_town_arena_melee_3_team_size,  8),

        (party_set_slot,"p_town_30", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_30", slot_town_arena_melee_1_team_size,  3),
        (party_set_slot,"p_town_30", slot_town_arena_melee_2_num_teams,  2),
        (party_set_slot,"p_town_30", slot_town_arena_melee_2_team_size,  5),
        (party_set_slot,"p_town_30", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_30", slot_town_arena_melee_3_team_size,  8),

        (party_set_slot,"p_town_31", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_31", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_31", slot_town_arena_melee_2_num_teams,  3),
        (party_set_slot,"p_town_31", slot_town_arena_melee_2_team_size,  4),
        (party_set_slot,"p_town_31", slot_town_arena_melee_3_num_teams,  3),
        (party_set_slot,"p_town_31", slot_town_arena_melee_3_team_size,  6),

        (party_set_slot,"p_town_32", slot_town_arena_melee_1_num_teams,  3),
        (party_set_slot,"p_town_32", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_32", slot_town_arena_melee_2_num_teams,  4),
        (party_set_slot,"p_town_32", slot_town_arena_melee_2_team_size,  6),
        (party_set_slot,"p_town_32", slot_town_arena_melee_3_num_teams,  4),
        (party_set_slot,"p_town_32", slot_town_arena_melee_3_team_size,  5),

        (party_set_slot,"p_town_33", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_33", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_33", slot_town_arena_melee_2_num_teams,  4),
        (party_set_slot,"p_town_33", slot_town_arena_melee_2_team_size,  5),
        (party_set_slot,"p_town_33", slot_town_arena_melee_3_num_teams,  4),
        (party_set_slot,"p_town_33", slot_town_arena_melee_3_team_size,  7),

        (party_set_slot,"p_town_34", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_34", slot_town_arena_melee_1_team_size,  4),
        (party_set_slot,"p_town_34", slot_town_arena_melee_2_num_teams,  2),
        (party_set_slot,"p_town_34", slot_town_arena_melee_2_team_size,  5),
        (party_set_slot,"p_town_34", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_34", slot_town_arena_melee_3_team_size,  6),

        (party_set_slot,"p_town_35", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_35", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_35", slot_town_arena_melee_2_num_teams,  3),
        (party_set_slot,"p_town_35", slot_town_arena_melee_2_team_size,  4),
        (party_set_slot,"p_town_35", slot_town_arena_melee_3_num_teams,  3),
        (party_set_slot,"p_town_35", slot_town_arena_melee_3_team_size,  6),

        (party_set_slot,"p_town_36", slot_town_arena_melee_1_num_teams,  3),
        (party_set_slot,"p_town_36", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_36", slot_town_arena_melee_2_num_teams,  4),
        (party_set_slot,"p_town_36", slot_town_arena_melee_2_team_size,  6),
        (party_set_slot,"p_town_36", slot_town_arena_melee_3_num_teams,  4),
        (party_set_slot,"p_town_36", slot_town_arena_melee_3_team_size,  5),

        (party_set_slot,"p_town_37", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_37", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_37", slot_town_arena_melee_2_num_teams,  4),
        (party_set_slot,"p_town_37", slot_town_arena_melee_2_team_size,  5),
        (party_set_slot,"p_town_37", slot_town_arena_melee_3_num_teams,  4),
        (party_set_slot,"p_town_37", slot_town_arena_melee_3_team_size,  7),

        (party_set_slot,"p_town_38", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_38", slot_town_arena_melee_1_team_size,  4),
        (party_set_slot,"p_town_38", slot_town_arena_melee_2_num_teams,  2),
        (party_set_slot,"p_town_38", slot_town_arena_melee_2_team_size,  5),
        (party_set_slot,"p_town_38", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_38", slot_town_arena_melee_3_team_size,  6),

        (party_set_slot,"p_town_39", slot_town_arena_melee_1_num_teams,  2),
        (party_set_slot,"p_town_39", slot_town_arena_melee_1_team_size,  8),
        (party_set_slot,"p_town_39", slot_town_arena_melee_2_num_teams,  4),
        (party_set_slot,"p_town_39", slot_town_arena_melee_2_team_size,  4),
        (party_set_slot,"p_town_39", slot_town_arena_melee_3_num_teams,  4),
        (party_set_slot,"p_town_39", slot_town_arena_melee_3_team_size,  6),

        (party_set_slot,"p_town_40", slot_town_arena_melee_1_num_teams,  4),
        (party_set_slot,"p_town_40", slot_town_arena_melee_1_team_size,  2),
        (party_set_slot,"p_town_40", slot_town_arena_melee_2_num_teams,  4),
        (party_set_slot,"p_town_40", slot_town_arena_melee_2_team_size,  4),
        (party_set_slot,"p_town_40", slot_town_arena_melee_3_num_teams,  4),
        (party_set_slot,"p_town_40", slot_town_arena_melee_3_team_size,  6),

        (party_set_slot,"p_town_41", slot_town_arena_melee_1_num_teams,  3),
        (party_set_slot,"p_town_41", slot_town_arena_melee_1_team_size,  3),
        (party_set_slot,"p_town_41", slot_town_arena_melee_2_num_teams,  2),
        (party_set_slot,"p_town_41", slot_town_arena_melee_2_team_size,  6),
        (party_set_slot,"p_town_41", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_41", slot_town_arena_melee_3_team_size,  8),

        (party_set_slot,"p_town_42", slot_town_arena_melee_1_num_teams,  4),
        (party_set_slot,"p_town_42", slot_town_arena_melee_1_team_size,  3),
        (party_set_slot,"p_town_42", slot_town_arena_melee_2_num_teams,  3),
        (party_set_slot,"p_town_42", slot_town_arena_melee_2_team_size,  4),
        (party_set_slot,"p_town_42", slot_town_arena_melee_3_num_teams,  2),
        (party_set_slot,"p_town_42", slot_town_arena_melee_3_team_size,  6),
    ]),

    ("initialize_banner_info", [
        (try_for_range, ":cur_troop", active_npcs_begin, kingdom_ladies_end),
            (troop_set_slot, ":cur_troop", slot_troop_custom_banner_flag_type, -1),
            (troop_set_slot, ":cur_troop", slot_troop_custom_banner_map_flag_type, -1),
        (try_end),
        (troop_set_slot, "trp_player", slot_troop_custom_banner_flag_type, -1),
        (troop_set_slot, "trp_player", slot_troop_custom_banner_map_flag_type, -1),

        (troop_set_slot, "trp_player", slot_troop_custom_banner_bg_color_1, 0xFFFFFFFF),
        (troop_set_slot, "trp_player", slot_troop_custom_banner_bg_color_2, 0xFFFFFFFF),
        (troop_set_slot, "trp_player", slot_troop_custom_banner_charge_color_1, 0xFFFFFFFF),
        (troop_set_slot, "trp_player", slot_troop_custom_banner_charge_color_2, 0xFFFFFFFF),
        (troop_set_slot, "trp_player", slot_troop_custom_banner_charge_color_3, 0xFFFFFFFF),
        (troop_set_slot, "trp_player", slot_troop_custom_banner_charge_color_4, 0xFFFFFFFF),

        #Setting background colors for banners
        (troop_set_slot, "trp_banner_background_color_array", 0, 0xFF8f4531),
        (troop_set_slot, "trp_banner_background_color_array", 1, 0xFFd9d7d1),
        (troop_set_slot, "trp_banner_background_color_array", 2, 0xFF373736),
        (troop_set_slot, "trp_banner_background_color_array", 3, 0xFFa48b28),
        (troop_set_slot, "trp_banner_background_color_array", 4, 0xFF497735),
        (troop_set_slot, "trp_banner_background_color_array", 5, 0xFF82362d),
        (troop_set_slot, "trp_banner_background_color_array", 6, 0xFF793329),
        (troop_set_slot, "trp_banner_background_color_array", 7, 0xFF262521),
        (troop_set_slot, "trp_banner_background_color_array", 8, 0xFFd9dad1),
        (troop_set_slot, "trp_banner_background_color_array", 9, 0xFF524563),
        (troop_set_slot, "trp_banner_background_color_array", 10, 0xFF91312c),
        (troop_set_slot, "trp_banner_background_color_array", 11, 0xFFafa231),
        (troop_set_slot, "trp_banner_background_color_array", 12, 0xFF706d3c),
        (troop_set_slot, "trp_banner_background_color_array", 13, 0xFFd6d3ce),
        (troop_set_slot, "trp_banner_background_color_array", 14, 0xFF521c08),
        (troop_set_slot, "trp_banner_background_color_array", 15, 0xFF394584),
        (troop_set_slot, "trp_banner_background_color_array", 16, 0xFF42662e),
        (troop_set_slot, "trp_banner_background_color_array", 17, 0xFFdfded6),
        (troop_set_slot, "trp_banner_background_color_array", 18, 0xFF292724),
        (troop_set_slot, "trp_banner_background_color_array", 19, 0xFF58611b),
        (troop_set_slot, "trp_banner_background_color_array", 20, 0xFF313a67),
        (troop_set_slot, "trp_banner_background_color_array", 21, 0xFF9c924a),
        (troop_set_slot, "trp_banner_background_color_array", 22, 0xFF998b39),
        (troop_set_slot, "trp_banner_background_color_array", 23, 0xFF365168),
        (troop_set_slot, "trp_banner_background_color_array", 24, 0xFFd6d3ce),
        (troop_set_slot, "trp_banner_background_color_array", 25, 0xFF94a642),
        (troop_set_slot, "trp_banner_background_color_array", 26, 0xFF944131),
        (troop_set_slot, "trp_banner_background_color_array", 27, 0xFF893b34),
        (troop_set_slot, "trp_banner_background_color_array", 28, 0xFF425510),
        (troop_set_slot, "trp_banner_background_color_array", 29, 0xFF94452e),
        (troop_set_slot, "trp_banner_background_color_array", 30, 0xFF475a94),
        (troop_set_slot, "trp_banner_background_color_array", 31, 0xFFd1b231),
        (troop_set_slot, "trp_banner_background_color_array", 32, 0xFFe1e2df),
        (troop_set_slot, "trp_banner_background_color_array", 33, 0xFF997c1e),
        (troop_set_slot, "trp_banner_background_color_array", 34, 0xFFc6b74d),
        (troop_set_slot, "trp_banner_background_color_array", 35, 0xFFad9a18),
        (troop_set_slot, "trp_banner_background_color_array", 36, 0xFF212421),
        (troop_set_slot, "trp_banner_background_color_array", 37, 0xFF8c2021),
        (troop_set_slot, "trp_banner_background_color_array", 38, 0xFF4d7136),
        (troop_set_slot, "trp_banner_background_color_array", 39, 0xFF395d84),
        (troop_set_slot, "trp_banner_background_color_array", 40, 0xFF527539),
        (troop_set_slot, "trp_banner_background_color_array", 41, 0xFF9c3c39),
        (troop_set_slot, "trp_banner_background_color_array", 42, 0xFF42518c),
        (troop_set_slot, "trp_banner_background_color_array", 43, 0xFFa46a2c),
        (troop_set_slot, "trp_banner_background_color_array", 44, 0xFF9f5141),
        (troop_set_slot, "trp_banner_background_color_array", 45, 0xFF2c6189),
        (troop_set_slot, "trp_banner_background_color_array", 46, 0xFF556421),
        (troop_set_slot, "trp_banner_background_color_array", 47, 0xFF9d621e),
        (troop_set_slot, "trp_banner_background_color_array", 48, 0xFFdeded6),
        (troop_set_slot, "trp_banner_background_color_array", 49, 0xFF6e4891),
        (troop_set_slot, "trp_banner_background_color_array", 50, 0xFF865a29),
        (troop_set_slot, "trp_banner_background_color_array", 51, 0xFFdedfd9),
        (troop_set_slot, "trp_banner_background_color_array", 52, 0xFF524273),
        (troop_set_slot, "trp_banner_background_color_array", 53, 0xFF8c3821),
        (troop_set_slot, "trp_banner_background_color_array", 54, 0xFFd1cec6),
        (troop_set_slot, "trp_banner_background_color_array", 55, 0xFF313031),
        (troop_set_slot, "trp_banner_background_color_array", 56, 0xFF47620d),
        (troop_set_slot, "trp_banner_background_color_array", 57, 0xFF6b4139),
        (troop_set_slot, "trp_banner_background_color_array", 58, 0xFFd6d7d6),
        (troop_set_slot, "trp_banner_background_color_array", 59, 0xFF2e2f2c),
        (troop_set_slot, "trp_banner_background_color_array", 60, 0xFF604283),
        (troop_set_slot, "trp_banner_background_color_array", 61, 0xFF395584),
        (troop_set_slot, "trp_banner_background_color_array", 62, 0xFF313031),
        (troop_set_slot, "trp_banner_background_color_array", 63, 0xFF7e3f2e),
        (troop_set_slot, "trp_banner_background_color_array", 64, 0xFF343434),
        (troop_set_slot, "trp_banner_background_color_array", 65, 0xFF3c496b),
        (troop_set_slot, "trp_banner_background_color_array", 66, 0xFFd9d8d1),
        (troop_set_slot, "trp_banner_background_color_array", 67, 0xFF99823c),
        (troop_set_slot, "trp_banner_background_color_array", 68, 0xFF9f822e),
        (troop_set_slot, "trp_banner_background_color_array", 69, 0xFF393839),
        (troop_set_slot, "trp_banner_background_color_array", 70, 0xFFa54931),
        (troop_set_slot, "trp_banner_background_color_array", 71, 0xFFdfdcd6),
        (troop_set_slot, "trp_banner_background_color_array", 72, 0xFF9f4a36),
        (troop_set_slot, "trp_banner_background_color_array", 73, 0xFF8c7521),
        (troop_set_slot, "trp_banner_background_color_array", 74, 0xFF9f4631),
        (troop_set_slot, "trp_banner_background_color_array", 75, 0xFF793324),
        (troop_set_slot, "trp_banner_background_color_array", 76, 0xFF395076),
        (troop_set_slot, "trp_banner_background_color_array", 77, 0xFF2c2b2c),
        (troop_set_slot, "trp_banner_background_color_array", 78, 0xFF657121),
        (troop_set_slot, "trp_banner_background_color_array", 79, 0xFF7e3121),
        (troop_set_slot, "trp_banner_background_color_array", 80, 0xFF76512e),
        (troop_set_slot, "trp_banner_background_color_array", 81, 0xFFe7e3de),
        (troop_set_slot, "trp_banner_background_color_array", 82, 0xFF947921),
        (troop_set_slot, "trp_banner_background_color_array", 83, 0xFF4d7b7c),
        (troop_set_slot, "trp_banner_background_color_array", 84, 0xFF343331),
        (troop_set_slot, "trp_banner_background_color_array", 85, 0xFFa74d36),
        (troop_set_slot, "trp_banner_background_color_array", 86, 0xFFe7e3de),
        (troop_set_slot, "trp_banner_background_color_array", 87, 0xFFd6d8ce),
        (troop_set_slot, "trp_banner_background_color_array", 88, 0xFF3e4d67),
        (troop_set_slot, "trp_banner_background_color_array", 89, 0xFF9f842e),
        (troop_set_slot, "trp_banner_background_color_array", 90, 0xFF4d6994),
        (troop_set_slot, "trp_banner_background_color_array", 91, 0xFF4a6118),
        (troop_set_slot, "trp_banner_background_color_array", 92, 0xFF943c29),
        (troop_set_slot, "trp_banner_background_color_array", 93, 0xFF394479),
        (troop_set_slot, "trp_banner_background_color_array", 94, 0xFF343331),
        (troop_set_slot, "trp_banner_background_color_array", 95, 0xFF3f4d5d),
        (troop_set_slot, "trp_banner_background_color_array", 96, 0xFF4a6489),
        (troop_set_slot, "trp_banner_background_color_array", 97, 0xFF313031),
        (troop_set_slot, "trp_banner_background_color_array", 98, 0xFFd6d7ce),
        (troop_set_slot, "trp_banner_background_color_array", 99, 0xFFc69e00),
        (troop_set_slot, "trp_banner_background_color_array", 100, 0xFF638e52),
        (troop_set_slot, "trp_banner_background_color_array", 101, 0xFFdcdbd3),
        (troop_set_slot, "trp_banner_background_color_array", 102, 0xFFdbdcd3),
        (troop_set_slot, "trp_banner_background_color_array", 103, 0xFF843831),
        (troop_set_slot, "trp_banner_background_color_array", 104, 0xFFcecfc6),
        (troop_set_slot, "trp_banner_background_color_array", 105, 0xFFc39d31),
        (troop_set_slot, "trp_banner_background_color_array", 106, 0xFFcbb670),
        (troop_set_slot, "trp_banner_background_color_array", 107, 0xFF394a18),
        (troop_set_slot, "trp_banner_background_color_array", 108, 0xFF372708),
        (troop_set_slot, "trp_banner_background_color_array", 109, 0xFF9a6810),
        (troop_set_slot, "trp_banner_background_color_array", 110, 0xFFb27910),
        (troop_set_slot, "trp_banner_background_color_array", 111, 0xFF8c8621),
        (troop_set_slot, "trp_banner_background_color_array", 112, 0xFF975a03),
        (troop_set_slot, "trp_banner_background_color_array", 113, 0xFF2c2924),
        (troop_set_slot, "trp_banner_background_color_array", 114, 0xFFaa962c),
        (troop_set_slot, "trp_banner_background_color_array", 115, 0xFFa2822e),
        (troop_set_slot, "trp_banner_background_color_array", 116, 0xFF7b8a8c),
        (troop_set_slot, "trp_banner_background_color_array", 117, 0xFF3c0908),
        (troop_set_slot, "trp_banner_background_color_array", 118, 0xFFFF00FF),
        (troop_set_slot, "trp_banner_background_color_array", 119, 0xFF671e14),
        (troop_set_slot, "trp_banner_background_color_array", 120, 0xFF103042),
        (troop_set_slot, "trp_banner_background_color_array", 121, 0xFF4a4500),
        (troop_set_slot, "trp_banner_background_color_array", 122, 0xFF703324),
        (troop_set_slot, "trp_banner_background_color_array", 123, 0xFF24293c),
        (troop_set_slot, "trp_banner_background_color_array", 124, 0xFF5d6966),
        (troop_set_slot, "trp_banner_background_color_array", 125, 0xFFbd9631),
        (troop_set_slot, "trp_banner_background_color_array", 126, 0xFFc6b26b),
        (troop_set_slot, "trp_banner_background_color_array", 127, 0xFF394918),
        #chief mas banners
        (troop_set_slot, "trp_banner_background_color_array", 128, 0xFF425510),
        (troop_set_slot, "trp_banner_background_color_array", 129, 0xFF94452e),
        (troop_set_slot, "trp_banner_background_color_array", 130, 0xFF475a94),
        (troop_set_slot, "trp_banner_background_color_array", 131, 0xFFd1b231),
        (troop_set_slot, "trp_banner_background_color_array", 132, 0xFFe1e2df),
        (troop_set_slot, "trp_banner_background_color_array", 133, 0xFF997c1e),
        (troop_set_slot, "trp_banner_background_color_array", 134, 0xFFc6b74d),
        (troop_set_slot, "trp_banner_background_color_array", 35, 0xFFad9a18),
        (troop_set_slot, "trp_banner_background_color_array", 136, 0xFF212421),
        (troop_set_slot, "trp_banner_background_color_array", 137, 0xFF8c2021),
        (troop_set_slot, "trp_banner_background_color_array", 138, 0xFF4d7136),
        (troop_set_slot, "trp_banner_background_color_array", 39, 0xFF395d84),
        (troop_set_slot, "trp_banner_background_color_array", 140, 0xFF527539),
        (troop_set_slot, "trp_banner_background_color_array", 141, 0xFF9c3c39),
        (troop_set_slot, "trp_banner_background_color_array", 142, 0xFF42518c),
        (troop_set_slot, "trp_banner_background_color_array", 143, 0xFFa46a2c),
        (troop_set_slot, "trp_banner_background_color_array", 144, 0xFF9f5141),
        (troop_set_slot, "trp_banner_background_color_array", 145, 0xFF2c6189),
        (troop_set_slot, "trp_banner_background_color_array", 146, 0xFF556421),
        (troop_set_slot, "trp_banner_background_color_array", 147, 0xFF9d621e),
        (troop_set_slot, "trp_banner_background_color_array", 148, 0xFFdeded6),
        (troop_set_slot, "trp_banner_background_color_array", 149, 0xFF6e4891),
        (troop_set_slot, "trp_banner_background_color_array", 150, 0xFF865a29),
        (troop_set_slot, "trp_banner_background_color_array", 151, 0xFFdedfd9),
        (troop_set_slot, "trp_banner_background_color_array", 152, 0xFF524273),
        (troop_set_slot, "trp_banner_background_color_array", 153, 0xFF8c3821),
        (troop_set_slot, "trp_banner_background_color_array", 154, 0xFFd1cec6),
        (troop_set_slot, "trp_banner_background_color_array", 155, 0xFF313031),
        (troop_set_slot, "trp_banner_background_color_array", 156, 0xFF47620d),
        (troop_set_slot, "trp_banner_background_color_array", 157, 0xFF6b4139),
        (troop_set_slot, "trp_banner_background_color_array", 158, 0xFFd6d7d6),
        (troop_set_slot, "trp_banner_background_color_array", 159, 0xFF2e2f2c),
        (troop_set_slot, "trp_banner_background_color_array", 160, 0xFF604283),
        (troop_set_slot, "trp_banner_background_color_array", 161, 0xFF395584),
        (troop_set_slot, "trp_banner_background_color_array", 162, 0xFF313031),
        (troop_set_slot, "trp_banner_background_color_array", 163, 0xFF7e3f2e),
        (troop_set_slot, "trp_banner_background_color_array", 164, 0xFF343434),
        (troop_set_slot, "trp_banner_background_color_array", 165, 0xFF3c496b),
        (troop_set_slot, "trp_banner_background_color_array", 166, 0xFFd9d8d1),
        (troop_set_slot, "trp_banner_background_color_array", 167, 0xFF99823c),
        (troop_set_slot, "trp_banner_background_color_array", 168, 0xFF9f822e),
        (troop_set_slot, "trp_banner_background_color_array", 169, 0xFF393839),
        (troop_set_slot, "trp_banner_background_color_array", 170, 0xFFa54931),
        (troop_set_slot, "trp_banner_background_color_array", 171, 0xFFdfdcd6),
        (troop_set_slot, "trp_banner_background_color_array", 172, 0xFF9f4a36),
        (troop_set_slot, "trp_banner_background_color_array", 173, 0xFF8c7521),
        (troop_set_slot, "trp_banner_background_color_array", 174, 0xFF9f4631),
        (troop_set_slot, "trp_banner_background_color_array", 175, 0xFF793324),
        (troop_set_slot, "trp_banner_background_color_array", 176, 0xFF395076),
        (troop_set_slot, "trp_banner_background_color_array", 177, 0xFF2c2b2c),
        (troop_set_slot, "trp_banner_background_color_array", 178, 0xFF657121),
        (troop_set_slot, "trp_banner_background_color_array", 179, 0xFF7e3121),
        (troop_set_slot, "trp_banner_background_color_array", 180, 0xFF76512e),

        #Default banners
        (troop_set_slot, "trp_banner_background_color_array", 181, 0xFF212221),
        (troop_set_slot, "trp_banner_background_color_array", 182, 0xFF212221),
        (troop_set_slot, "trp_banner_background_color_array", 183, 0xFF2E3B10),
        (troop_set_slot, "trp_banner_background_color_array", 184, 0xFF425D7B),
        (troop_set_slot, "trp_banner_background_color_array", 185, 0xFF394608),
      ]),
        
        
    ("initialize_economic_information", [
        #All towns produce tools, pottery, and wool cloth for sale in countryside
        (try_for_range, ":town_no", towns_begin, towns_end),
            (store_random_in_range, ":random_average_20_variation_10", 10, 31),  #10,11,12,13,14,15,16,17,18,19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29 or 30
            (party_set_slot, ":town_no", slot_center_wool_looms, ":random_average_20_variation_10"),

            (store_random_in_range, ":random_average_2_variation_1", 1, 4),  #1, 2 or 3
            (party_set_slot, ":town_no", slot_center_breweries, ":random_average_2_variation_1"),

            (store_random_in_range, ":random_average_5_variation_3", 3, 9),  #2, 3, 4,5,6,7 or 8
            (party_set_slot, ":town_no", slot_center_pottery_kilns, ":random_average_5_variation_3"),

            (store_random_in_range, ":random_average_15_variation_9", 6, 25),  #6,7,8,9,10,11,12,13,14,15,16,17,18,19, 20, 21, 22, 23 or 24
            (party_set_slot, ":town_no", slot_center_smithies, ":random_average_15_variation_9"),

            (store_random_in_range, ":random_average_5_variation_3", 3, 9),  #2, 3, 4,5,6,7 or 8
            (party_set_slot, ":town_no", slot_center_mills, ":random_average_5_variation_3"),

            (store_random_in_range, ":random_average_2_variation_1", 1, 4),  #1, 2 or 3
            (party_set_slot, ":town_no", slot_center_tanneries, ":random_average_2_variation_1"),

            (store_random_in_range, ":random_average_1_variation_1", 0, 3),  #0,1 or 2
            (party_set_slot, ":town_no", slot_center_wine_presses, ":random_average_1_variation_1"),

            (store_random_in_range, ":random_average_2_variation_1", 1, 4),  #1, 2 or 3
            (party_set_slot, ":town_no", slot_center_olive_presses, ":random_average_2_variation_1"),

            (store_random_in_range, ":random_average_1000_variation_1000", 0, 2001),  #0..2000
            (party_set_slot, ":town_no", slot_center_acres_grain, ":random_average_1000_variation_1000"),  #0..2000

            (store_random_in_range, ":random_average_1000_variation_1000", 0, 2001),  #0..2000
            (party_set_slot, ":town_no", slot_center_acres_vineyard, ":random_average_1000_variation_1000"),  #0..2000
        (try_end),
      
        #chief anadido industria
        (party_set_slot, "p_town_1", slot_center_olive_presses, 1),    #Suno
        (party_set_slot, "p_town_1", slot_center_silk_looms, 10),        #Jelkaka
        (party_set_slot, "p_town_1", slot_center_wine_presses, 4),    #narra
        (party_set_slot, "p_town_1", slot_center_fishing_fleet, 25),    #Tihr
        ##
        (party_set_slot, "p_town_2", slot_center_silk_looms, 20),        #Jelkaka
        (party_set_slot, "p_town_2", slot_center_fishing_fleet, 25),    #Tihr
        (party_set_slot, "p_town_2", slot_center_wine_presses, 1),    #narra
        (party_set_slot, "p_town_2", slot_center_smithies, 18),        #Khudan
        ##
        (party_set_slot, "p_town_3", slot_center_mills, 15),            #Uxkhal
        (party_set_slot, "p_town_3", slot_center_wool_looms, 15),        #Reyvadin
        (party_set_slot, "p_town_3", slot_center_fishing_fleet, 25),    #Tihr
        ##
        (party_set_slot, "p_town_4", slot_center_pottery_kilns, 10),
        (party_set_slot, "p_town_4", slot_center_breweries, 35),
        (party_set_slot, "p_town_4", slot_center_smithies, 18),        #Khudan

        (party_set_slot, "p_town_5", slot_center_pottery_kilns, 12),
        (party_set_slot, "p_town_5", slot_center_breweries, 25),
        (party_set_slot, "p_town_5", slot_center_smithies, 8),        #Khudan
        (party_set_slot, "p_town_5", slot_center_fishing_fleet, 25),    #Tihr
        ##
        (party_set_slot, "p_town_20", slot_center_tanneries, 5),        #Darquba
        (party_set_slot, "p_town_20", slot_center_wool_looms, 31),        #Reyvadin

        (party_set_slot, "p_town_7", slot_center_mills, 15),            #Uxkhal
        (party_set_slot, "p_town_7", slot_center_pottery_kilns, 15),

        ##
        (party_set_slot, "p_town_8", slot_center_silk_looms, 10),        #Jelkaka
        (party_set_slot, "p_town_8", slot_center_pottery_kilns, 8),
        (party_set_slot, "p_town_8", slot_center_breweries, 2),
        ##
        (party_set_slot, "p_town_9", slot_center_breweries, 6),
        (party_set_slot, "p_town_9", slot_center_fishing_fleet, 5),    #Khudan
        ##
        (party_set_slot, "p_town_10", slot_center_tanneries, 15),        #Shariz
        (party_set_slot, "p_town_10", slot_center_wool_looms, 25),        #Reyvadin
        (party_set_slot, "p_town_10", slot_center_fishing_fleet, 25),    #Tihr
        ##
        (party_set_slot, "p_town_11", slot_center_smithies, 19),       #Curaw
        (party_set_slot, "p_town_11", slot_center_pottery_kilns, 10),
        (party_set_slot, "p_town_11", slot_center_breweries, 30),
        (party_set_slot, "p_town_11", slot_center_fishing_fleet, 10),    #Khudan
        ##
        (party_set_slot, "p_town_12", slot_center_silk_looms, 20),        #Jelkaka
        (party_set_slot, "p_town_12", slot_center_fishing_fleet, 25),    #Wercheg
        ##
        (party_set_slot, "p_town_13", slot_center_breweries, 6),
        (party_set_slot, "p_town_13", slot_center_fishing_fleet, 50),    #Rivacheg
        ##
        (party_set_slot, "p_town_14", slot_center_silk_looms, 20),        #Jelkaka
        (party_set_slot, "p_town_14", slot_center_pottery_kilns, 18),
        ##
        (party_set_slot, "p_town_15", slot_center_smithies, 20),        #Yalen
        (party_set_slot, "p_town_15", slot_center_pottery_kilns, 8),
        (party_set_slot, "p_town_15", slot_center_breweries, 25),
        (party_set_slot, "p_town_15", slot_center_fishing_fleet, 25),    #Yalen

        (party_set_slot, "p_town_16", slot_center_smithies, 30),        #Dhirim
        (party_set_slot, "p_town_16", slot_center_breweries, 5),
        (party_set_slot, "p_town_16", slot_center_tanneries, 4),        #Dhirim

        (party_set_slot, "p_town_17", slot_center_olive_presses, 15),    #Suno
        (party_set_slot, "p_town_17", slot_center_fishing_fleet, 25),    #Tihr

        (party_set_slot, "p_town_18", slot_center_smithies, 25),        #Yalen
        (party_set_slot, "p_town_18", slot_center_breweries, 5),
        (party_set_slot, "p_town_18", slot_center_tanneries, 4),

        (party_set_slot, "p_town_19", slot_center_breweries, 5),

        (party_set_slot, "p_town_20", slot_center_tanneries, 5),        #Darquba
        (party_set_slot, "p_town_20", slot_center_wool_looms, 31),        #Reyvadin

        (party_set_slot, "p_town_21", slot_center_breweries, 5),

        (party_set_slot, "p_town_22", slot_center_breweries, 6),

        (party_set_slot, "p_town_23", slot_center_smithies, 20),        #Yalen
        (party_set_slot, "p_town_23", slot_center_pottery_kilns, 8),
        (party_set_slot, "p_town_23", slot_center_breweries, 25),

        (party_set_slot, "p_town_24", slot_center_pottery_kilns, 15),
        (party_set_slot, "p_town_24", slot_center_fishing_fleet, 25),    #Tihr

        (party_set_slot, "p_town_25", slot_center_breweries, 6),
        (party_set_slot, "p_town_25", slot_center_fishing_fleet, 30),    #Jelkala

        (party_set_slot, "p_town_26", slot_center_breweries, 6),
        (party_set_slot, "p_town_26", slot_center_fishing_fleet, 10),    #Praven

        (party_set_slot, "p_town_27", slot_center_mills, 15),            #Uxkhal
        (party_set_slot, "p_town_27", slot_center_tanneries, 4),        #Shariz
        (party_set_slot, "p_town_27", slot_center_wool_looms, 31),        #Reyvadin

        (party_set_slot, "p_town_28", slot_center_smithies, 25),        #Reyvadin
        (party_set_slot, "p_town_28", slot_center_pottery_kilns, 18),
        (party_set_slot, "p_town_28", slot_center_breweries, 15),

        (party_set_slot, "p_town_29", slot_center_breweries, 6),
        (party_set_slot, "p_town_29", slot_center_fishing_fleet, 5),    #Khudan

        (party_set_slot, "p_town_30", slot_center_linen_looms, 25),        #Sargoth
        (party_set_slot, "p_town_30", slot_center_fishing_fleet, 30),    #Rivacheg
        (party_set_slot, "p_town_30", slot_center_breweries, 5),

        (party_set_slot, "p_town_31", slot_center_linen_looms, 15),        #Sargoth
        (party_set_slot, "p_town_31", slot_center_breweries, 15),

        (party_set_slot, "p_town_32", slot_center_linen_looms, 20),        #Sargoth
        (party_set_slot, "p_town_32", slot_center_breweries, 9),
        (party_set_slot, "p_town_32", slot_center_fishing_fleet, 40),    #Rivacheg

        (party_set_slot, "p_town_33", slot_center_linen_looms, 5),        #Sargoth
        (party_set_slot, "p_town_33", slot_center_breweries, 17),

        (party_set_slot, "p_town_34", slot_center_tanneries, 2),        #Shariz
        (party_set_slot, "p_town_34", slot_center_wool_looms, 39),        #Reyvadin

        (party_set_slot, "p_town_35", slot_center_linen_looms, 25),        #Sargoth
        (party_set_slot, "p_town_35", slot_center_breweries, 5),

        (party_set_slot, "p_town_36", slot_center_linen_looms, 15),        #Sargoth
        (party_set_slot, "p_town_36", slot_center_breweries, 15),

        (party_set_slot, "p_town_37", slot_center_tanneries, 4),        #Shariz
        (party_set_slot, "p_town_37", slot_center_wool_looms, 40),        #Ichamur

        (party_set_slot, "p_town_38", slot_center_wool_looms, 35),        #narra
        (party_set_slot, "p_town_38", slot_center_tanneries, 5),        #Shariz

        (party_set_slot, "p_town_39", slot_center_tanneries, 5),        #Shariz
        (party_set_slot, "p_town_39", slot_center_wool_looms, 35),        #Reyvadin
        (party_set_slot, "p_town_39", slot_center_fishing_fleet, 5),    #Shariz

        (party_set_slot, "p_town_40", slot_center_linen_looms, 17),        #Sargoth
        (party_set_slot, "p_town_40", slot_center_breweries, 6),

        (party_set_slot, "p_town_41", slot_center_breweries, 1),        #Ahmerrad

        (party_set_slot, "p_town_42", slot_center_tanneries, 5),        #Bariyye
        (party_set_slot, "p_town_42", slot_center_wine_presses, 4),    #narra


    
        (try_for_range, ":village_no", villages_begin, villages_end),
            (store_random_in_range, ":random_cattle", 20, 100),
            (party_set_slot, ":village_no", slot_center_head_cattle, ":random_cattle"),

            (store_random_in_range, ":random_sheep", 40, 200),
            (party_set_slot, ":village_no", slot_center_head_sheep, ":random_sheep"),

            # grain production
            (store_random_in_range, ":random_value_between_0_and_40000", 0, 40000),
            (store_random_in_range, ":random_value_between_0_and_average_20000", 0, ":random_value_between_0_and_40000"),
            (party_set_slot, ":village_no", slot_center_acres_grain, ":random_value_between_0_and_average_20000"),  #average : 10000, min : 0, max : 40000

            # grape production
            (store_random_in_range, ":random_value_between_0_and_2000", 0, 2000),
            (store_random_in_range, ":random_value_between_0_and_average_1000", 0, ":random_value_between_0_and_2000"),
            (val_div, ":random_value_between_0_and_average_1000", 5),
            (party_set_slot, ":village_no", slot_center_acres_vineyard, ":random_value_between_0_and_average_1000"),  #average : 500, min : 0, max : 2000

            # honey production
            (store_random_in_range, ":random_value_between_0_and_3", 0, 3),
            (party_set_slot, ":village_no", slot_center_apiaries, ":random_value_between_0_and_3"),

            # cabbage and fruit production
            (store_random_in_range, ":random_value_between_0_and_5", 0, 5),
            (party_set_slot, ":village_no", slot_center_household_gardens, ":random_value_between_0_and_5"),

            # bread production
            (store_random_in_range, ":random_value_between_0_and_3", 0, 3),
            (party_set_slot, ":village_no", slot_center_mills, ":random_value_between_0_and_3"),

            # pottery production
            (store_random_in_range, ":random_value_between_0_and_5", 0, 5),
            (party_set_slot, ":village_no", slot_center_pottery_kilns, ":random_value_between_0_and_5"),

            (try_begin),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_1"),  #Sargoth, flax
                (party_set_slot, ":village_no", slot_center_acres_olives, 1000),
                (party_set_slot, ":village_no", slot_center_acres_vineyard, 2000),
                (party_set_slot, ":village_no", slot_center_household_gardens, 10),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_2"),  #Wercheg
                (party_set_slot, ":village_no", slot_center_silk_farms, 2),
                (party_set_slot, ":village_no", slot_center_head_cattle, 200),  #leather

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_3"),  #veluca
                (party_set_slot, ":village_no", slot_center_head_cattle, 200),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_4"),  #suno
                (party_set_slot, ":village_no", slot_center_acres_grain, 12000),
                (party_set_slot, ":village_no", slot_center_salt_pans, 1),
                (party_set_slot, ":village_no", slot_center_silk_farms, 12),
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_5"),  #jelkala
                (party_set_slot, ":village_no", slot_center_acres_grain, 10000),
                (party_set_slot, ":village_no", slot_center_salt_pans, 3),
                (party_set_slot, ":village_no", slot_center_silk_farms, 12),
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_6"),  #praven
                (party_set_slot, ":village_no", slot_center_acres_grain, 6000),
                (party_set_slot, ":village_no", slot_center_fur_traps, 3),
                (party_set_slot, ":village_no", slot_center_head_sheep, 170),
                (party_set_slot, ":village_no", slot_center_silk_farms, 12),
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_7"),  #uxkhal
                (party_set_slot, ":village_no", slot_center_head_sheep, 450),
                (party_set_slot, ":village_no", slot_center_head_cattle, 100),
                (party_set_slot, ":village_no", slot_center_acres_grain, 10000),
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_8"),  #reyvadin
                (party_set_slot, ":village_no", slot_center_acres_grain, 8000),
                (party_set_slot, ":village_no", slot_center_acres_flax, 2000),
                (party_set_slot, ":village_no", slot_center_silk_farms, 12),
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_9"),  #khudan
                (party_set_slot, ":village_no", slot_center_iron_deposits, 40),
                (party_set_slot, ":village_no", slot_center_apiaries, 4),
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_10"),  #tulga
                (party_set_slot, ":village_no", slot_center_acres_grain, 5000),
                (party_set_slot, ":village_no", slot_center_fur_traps, 1),
                (party_set_slot, ":village_no", slot_center_head_sheep, 450),
                (party_set_slot, ":village_no", slot_center_silk_farms, 20),
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_11"),  #curaw
                (party_set_slot, ":village_no", slot_center_acres_grain, 12000),
                (party_set_slot, ":village_no", slot_center_salt_pans, 1),
                (party_set_slot, ":village_no", slot_center_silk_farms, 12),
                # (party_set_slot, ":village_no", slot_center_acres_olives, 0),
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_12"),  #rivacheg
                (party_set_slot, ":village_no", slot_center_head_cattle, 75),
                (party_set_slot, ":village_no", slot_center_acres_grain, 5000),
                (party_set_slot, ":village_no", slot_center_fur_traps, 4),
                (party_set_slot, ":village_no", slot_center_head_sheep, 150),
                (party_set_slot, ":village_no", slot_center_silk_farms, 10),
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_13"),  #Wercheg
                (party_set_slot, ":village_no", slot_center_iron_deposits, 47),
                (party_set_slot, ":village_no", slot_center_apiaries, 3),

            #14Halmar has a salt pan nearby
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_14"),  #Halmar
                (party_set_slot, ":village_no", slot_center_acres_grain, 8000),
                (party_set_slot, ":village_no", slot_center_acres_flax, 4000),
                (party_set_slot, ":village_no", slot_center_silk_farms, 2),
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_15"),  #yalen
                (party_set_slot, ":village_no", slot_center_acres_grain, 7000),
                (party_set_slot, ":village_no", slot_center_salt_pans, 12),
                (party_set_slot, ":village_no", slot_center_silk_farms, 10),
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_16"),  #dhirim
                (party_set_slot, ":village_no", slot_center_apiaries, 1),
                (party_set_slot, ":village_no", slot_center_acres_flax, 2000),
            #17 Ichamur
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_17"),  #ichamur
                (party_set_slot, ":village_no", slot_center_acres_grain, 9000),
                (party_set_slot, ":village_no", slot_center_iron_deposits, 24),
                (party_set_slot, ":village_no", slot_center_acres_vineyard, 1000),
                (party_set_slot, ":village_no", slot_center_acres_olives, 4000),

            #18 Narra
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_18"),  #narra
                (party_set_slot, ":village_no", slot_center_acres_flax, 2000),
                (party_set_slot, ":village_no", slot_center_apiaries, 1),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_19"),  #
                (party_set_slot, ":village_no", slot_center_iron_deposits, 15),
                (party_set_slot, ":village_no", slot_center_head_sheep, 10),
                (party_set_slot, ":village_no", slot_center_acres_grain, 1000),
                (party_set_slot, ":village_no", slot_center_acres_flax, 2000),
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_20"),  #
                (party_set_slot, ":village_no", slot_center_acres_grain, 2000),
                (party_set_slot, ":village_no", slot_center_fur_traps, 3),
                (party_set_slot, ":village_no", slot_center_head_sheep, 170),
                (party_set_slot, ":village_no", slot_center_silk_farms, 12),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_21"),  #Ahmerrad -- hillside
                (party_set_slot, ":village_no", slot_center_iron_deposits, 10),
                (party_set_slot, ":village_no", slot_center_head_sheep, 150),
                (party_set_slot, ":village_no", slot_center_acres_grain, 4000),
                (party_set_slot, ":village_no", slot_center_acres_flax, 4000),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_22"),  #Bariyye -- deep desert
                (party_set_slot, ":village_no", slot_center_iron_deposits, 52),
                (party_set_slot, ":village_no", slot_center_apiaries, 1),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_23"),  #veluca
                (party_set_slot, ":village_no", slot_center_acres_grain, 10000),
                (party_set_slot, ":village_no", slot_center_salt_pans, 8),
                (party_set_slot, ":village_no", slot_center_silk_farms, 2),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_24"),  #suno
                (party_set_slot, ":village_no", slot_center_head_sheep, 550),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_25"),  #jelkala
                (party_set_slot, ":village_no", slot_center_iron_deposits, 37),
                (party_set_slot, ":village_no", slot_center_apiaries, 5),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_26"),  #praven
                (party_set_slot, ":village_no", slot_center_acres_grain, 15000),
                (party_set_slot, ":village_no", slot_center_iron_deposits, 42),
                (party_set_slot, ":village_no", slot_center_apiaries, 4),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_27"),  #uxkhal
                (party_set_slot, ":village_no", slot_center_acres_grain, 15000),
                (party_set_slot, ":village_no", slot_center_fur_traps, 1),
                (party_set_slot, ":village_no", slot_center_head_sheep, 150),
                (party_set_slot, ":village_no", slot_center_silk_farms, 10),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_28"),  #reyvadin
                (party_set_slot, ":village_no", slot_center_head_cattle, 100),
                (party_set_slot, ":village_no", slot_center_acres_grain, 10000),
                (party_set_slot, ":village_no", slot_center_salt_pans, 8),
                (party_set_slot, ":village_no", slot_center_silk_farms, 10),

            (else_try),
            (party_slot_eq, ":village_no", slot_village_market_town, "p_town_29"),  #khudan
                (party_set_slot, ":village_no", slot_center_iron_deposits, 47),
                (party_set_slot, ":village_no", slot_center_apiaries, 3),

            (else_try),
            (party_slot_eq, ":village_no", slot_village_market_town, "p_town_30"),  #tulga
                (party_set_slot, ":village_no", slot_center_iron_deposits, 10),
                (party_set_slot, ":village_no", slot_center_head_sheep, 150),
                (party_set_slot, ":village_no", slot_center_acres_grain, 4000),
                (party_set_slot, ":village_no", slot_center_acres_flax, 4000),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_31"),  #curaw
                (party_set_slot, ":village_no", slot_center_iron_deposits, 6),
                (party_set_slot, ":village_no", slot_center_head_sheep, 50),
                (party_set_slot, ":village_no", slot_center_acres_grain, 2000),
                (party_set_slot, ":village_no", slot_center_acres_flax, 9000),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_32"),  #rivacheg
                (party_set_slot, ":village_no", slot_center_iron_deposits, 5),
                (party_set_slot, ":village_no", slot_center_head_sheep, 40),
                (party_set_slot, ":village_no", slot_center_acres_grain, 4000),
                (party_set_slot, ":village_no", slot_center_acres_flax, 6000),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_33"),  #Wercheg
                (party_set_slot, ":village_no", slot_center_iron_deposits, 10),
                (party_set_slot, ":village_no", slot_center_head_sheep, 150),
                (party_set_slot, ":village_no", slot_center_acres_grain, 4000),
                (party_set_slot, ":village_no", slot_center_acres_flax, 4000),

                #14Halmar has a salt pan nearby
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_34"),  #Halmar
                (party_set_slot, ":village_no", slot_center_acres_grain, 7000),
                (party_set_slot, ":village_no", slot_center_fur_traps, 3),
                (party_set_slot, ":village_no", slot_center_head_sheep, 250),
                (party_set_slot, ":village_no", slot_center_silk_farms, 20),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_35"),  #yalen
                (party_set_slot, ":village_no", slot_center_iron_deposits, 10),
                (party_set_slot, ":village_no", slot_center_head_sheep, 120),
                (party_set_slot, ":village_no", slot_center_acres_grain, 4000),
                (party_set_slot, ":village_no", slot_center_acres_flax, 5000),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_36"),  #dhirim
                (party_set_slot, ":village_no", slot_center_iron_deposits, 7),
                (party_set_slot, ":village_no", slot_center_acres_grain, 5000),
                (party_set_slot, ":village_no", slot_center_acres_flax, 5000),

                #17 Ichamur
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_37"),  #ichamur
                (party_set_slot, ":village_no", slot_center_acres_grain, 2000),
                (party_set_slot, ":village_no", slot_center_fur_traps, 3),
                (party_set_slot, ":village_no", slot_center_head_sheep, 250),
                (party_set_slot, ":village_no", slot_center_silk_farms, 50),

                #18 Narra
            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_38"),  #narra
                (party_set_slot, ":village_no", slot_center_acres_grain, 7000),
                (party_set_slot, ":village_no", slot_center_fur_traps, 3),
                (party_set_slot, ":village_no", slot_center_head_sheep, 250),
                (party_set_slot, ":village_no", slot_center_silk_farms, 20),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_39"),  #
                (party_set_slot, ":village_no", slot_center_acres_grain, 7000),
                (party_set_slot, ":village_no", slot_center_fur_traps, 3),
                (party_set_slot, ":village_no", slot_center_head_sheep, 250),
                (party_set_slot, ":village_no", slot_center_silk_farms, 20),
                (party_set_slot, ":village_no", slot_center_head_cattle, 30),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_40"),  #
                (party_set_slot, ":village_no", slot_center_iron_deposits, 10),
                (party_set_slot, ":village_no", slot_center_head_sheep, 150),
                (party_set_slot, ":village_no", slot_center_acres_grain, 4000),
                (party_set_slot, ":village_no", slot_center_acres_flax, 4000),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_41"),  #Ahmerrad -- hillside
                (party_set_slot, ":village_no", slot_center_acres_grain, 9000),
                (party_set_slot, ":village_no", slot_center_iron_deposits, 28),
                (party_set_slot, ":village_no", slot_center_head_sheep, 50),
                (party_set_slot, ":village_no", slot_center_head_cattle, 30),
                (party_set_slot, ":village_no", slot_center_salt_pans, 8),

            (else_try),
                (party_slot_eq, ":village_no", slot_village_market_town, "p_town_42"),  #Bariyye -- deep desert
                (party_set_slot, ":village_no", slot_center_acres_grain, 5000),
                (party_set_slot, ":village_no", slot_center_acres_vineyard, 2000),
                (party_set_slot, ":village_no", slot_center_iron_deposits, 10),
                (party_set_slot, ":village_no", slot_center_head_sheep, 50),
                (party_set_slot, ":village_no", slot_center_head_cattle, 30),
            (try_end),
        (try_end),
      
        #determining village productions which are bounded by castle by nearby village productions which are bounded by a town.
        (try_for_range, ":village_no", villages_begin, villages_end),
            (party_get_slot, ":bound_center", ":village_no", slot_village_bound_center),
            (is_between, ":bound_center", castles_begin, castles_end),

            (try_for_range, ":cur_production_source", slot_production_sources_begin, slot_production_sources_end),

                (assign, ":total_averaged_production", 0),
                (try_for_range, ":effected_village_no", villages_begin, villages_end),
                    (party_get_slot, ":bound_center", ":effected_village_no", slot_village_bound_center),
                    (is_between, ":bound_center", towns_begin, towns_end),

                    (store_distance_to_party_from_party, ":dist", ":village_no", ":effected_village_no"),
                    (le, ":dist", 72),

                    (party_get_slot, ":production", ":village_no", ":cur_production_source"),

                    (store_add, ":dist_plus_24", ":dist", 24),
                    (store_mul, ":production_mul_12", ":production", 12),
                    (store_div, ":averaged_production", ":production_mul_12", ":dist_plus_24"),  #if close (12/24=1/2) else (12/96=1/8)
                    (val_div, ":averaged_production", 2),  #if close (1/4) else (1/16)
                    (val_add, ":total_averaged_production", ":averaged_production"),
                (try_end),
                (party_set_slot, ":village_no", ":cur_production_source", ":total_averaged_production"),
            (try_end),
        (try_end),

        (party_set_slot, "p_village_40", slot_center_fishing_fleet, 15),  #Yaragar
        (party_set_slot, "p_village_64", slot_center_fishing_fleet, 15),  #Azgad
        (party_set_slot, "p_village_12", slot_center_fishing_fleet, 15),  #Haen
        (party_set_slot, "p_village_4", slot_center_fishing_fleet, 15),  #Buvran

        (party_set_slot, "p_village_51", slot_center_fishing_fleet, 15),  #Uslum
        (party_set_slot, "p_village_63", slot_center_fishing_fleet, 15),  #Bazeck
        (party_set_slot, "p_village_56", slot_center_fishing_fleet, 15),  #Ilvia
        (party_set_slot, "p_village_58", slot_center_fishing_fleet, 15),  #Glunmar

        (party_set_slot, "p_village_86", slot_center_fishing_fleet, 20),  #Ruvar
        (party_set_slot, "p_village_35", slot_center_fishing_fleet, 15),  #Ambean
        (party_set_slot, "p_village_44", slot_center_fishing_fleet, 15),  #Feacharin

        (party_set_slot, "p_village_28", slot_center_fishing_fleet, 15),  #Epeshe
        (party_set_slot, "p_village_83", slot_center_fishing_fleet, 15),  #Tismirr

        (party_set_slot, "p_village_139", slot_center_fishing_fleet, 15),  #Jelbegi
        (party_set_slot, "p_village_143", slot_center_fishing_fleet, 15),  #Fenada

        (party_set_slot, "p_village_7", slot_center_fishing_fleet, 15),  #Fisdnar
        (party_set_slot, "p_village_71", slot_center_fishing_fleet, 15),  #Tebandra
        (party_set_slot, "p_village_211", slot_center_fishing_fleet, 15),  #Ibdeles
        (party_set_slot, "p_village_193", slot_center_fishing_fleet, 15),  #Kwynn

        (party_set_slot, "p_village_192", slot_center_fishing_fleet, 25),  #Rizi - Estuary
        (party_set_slot, "p_village_136", slot_center_fishing_fleet, 15),  #Istiniar

        (party_set_slot, "p_village_118", slot_center_fishing_fleet, 15),  #Odasan
        (party_set_slot, "p_village_110", slot_center_fishing_fleet, 15),  #Ismirala
        (party_set_slot, "p_village_189", slot_center_fishing_fleet, 15),  #Udiniad

        (party_set_slot, "p_village_200", slot_center_fishing_fleet, 15),  #Jamiche
        (party_set_slot, "p_village_171", slot_center_fishing_fleet, 15),  #Jamiche

        (party_set_slot, "p_village_39", slot_center_fishing_fleet, 20),  #Ulburban
        (party_set_slot, "p_village_137", slot_center_fishing_fleet, 15),  #Pagundur
        (party_set_slot, "p_village_179", slot_center_fishing_fleet, 15),  #Jayek

        # Initialize pastureland
        (try_for_range, ":center", centers_begin, centers_end),
            (party_get_slot, ":head_cattle", ":center", slot_center_head_cattle),
            (party_get_slot, ":head_sheep", ":center", slot_center_head_sheep),
            (store_mul, ":num_acres", ":head_cattle", 4),
            (val_add, ":num_acres", ":head_sheep"),
            (val_add, ":num_acres", ":head_sheep"),
            (val_mul, ":num_acres", 6),
            (val_div, ":num_acres", 5),
            (store_random_in_range, ":random", 60, 150),
            (val_mul, ":num_acres", ":random"),
            (val_div, ":num_acres", 100),
            (party_set_slot, ":center", slot_center_acres_pasture, ":num_acres"),
        (try_end),

        # Initialize prices based on production, etc
        (try_for_range, ":unused", 0, 3),  #15 cycles = 45 days. For a village with -20 production, this should lead to approximate +1000, modified
            (call_script, "script_update_trade_good_prices"),  #changes prices based on production
        (try_end),

        #Initialize prosperity based on final prices
        (try_for_range, ":center_no", centers_begin, centers_end),
            (neg|is_between, ":center_no", castles_begin, castles_end),
            (store_random_in_range, ":random_prosperity_adder", -10, 10),
            (call_script, "script_get_center_ideal_prosperity", ":center_no"),
            (assign, ":prosperity", reg0),
            (val_add, ":prosperity", ":random_prosperity_adder"),
            (val_clamp, ":prosperity", 0, 100),
            (party_set_slot, ":center_no", slot_town_prosperity, ":prosperity"),
        (try_end),
        (call_script, "script_calculate_castle_prosperities_by_using_its_villages"),
    ]),
]
