from source.header_operations import *
from source.header_common import *
from source.header_presentations import tf_center_justify, tf_scrollable, tf_left_align
from source.header_triggers import ti_on_presentation_load, ti_on_presentation_event_state_change

from source.module_constants import towns_begin, towns_end, \
    centers_begin, centers_end, spt_town, slot_troop_renown

# relevant slots: "slot_town_bank_deadline", "slot_town_bank_debt",
# "slot_town_bank_assets", "slot_town_player_acres"


simple_triggers = [
  (24 * 14,
   [
    (neq, "$g_infinite_camping", 1),
    (assign, ":end", towns_end),
    (try_for_range, ":center_no", towns_begin, ":end"),
        (this_or_next|party_slot_ge, ":center_no", "slot_town_player_acres", 1),
        (this_or_next|party_slot_ge, ":center_no", "slot_town_bank_assets", 1),
        (party_slot_ge, ":center_no", "slot_town_bank_debt", 1),
        (assign, ":end", towns_begin), # break
    (try_end),
    # Display update banking if player has any affairs with the bank
    (eq, ":end", towns_begin),
    (start_presentation, "prsnt_bank_quickview"),
    ]),

  (12,
   [
    # Not paying debts has consequences
    (try_for_range, ":town_no", towns_begin, towns_end),
        (party_get_slot, ":debt", ":town_no", "slot_town_bank_debt"),

        # If debt and deadline passed
        (gt, ":debt", 0),
        (party_get_slot, ":deadline", ":town_no", "slot_town_bank_deadline"),
        (store_current_hours, ":date"),
        (ge, ":date", ":deadline"),

        # debt causes -5 relations with town.
        (call_script, "script_change_player_relation_with_center", ":town_no", -5, 0xff3333),

        (try_begin),
            # add 40% interest rate
            (lt, ":debt", 100000),
            (val_mul, ":debt", 14),
            (val_div, ":debt", 10),
            (try_begin),
                # Debt is capped to 100k
                (gt, ":debt", 100000),
                (assign, ":debt", 100000),
            (try_end),
            (str_store_party_name, s1, ":town_no"),
            (str_store_party_name, s2, ":debt"),
            (display_message, "@You missed the deadline to pay back your debts in {s1}. "
                              "It grew 40% to {s2}."),
        (else_try),
            # debt = 100000 causes -2 relation with faction.
            (assign, ":debt", 100000),
            (store_faction_of_party, ":faction_no", ":town_no"),
            (call_script, "script_change_player_relation_with_faction_ex", ":faction_no", -2),
            (str_store_party_name, s1, ":town_no"),
            (display_message, "@Your debt in {s1} is now so high that the King himself has taken notice. "
                              "He has frozen your debt, but is displeased with the situation.", 0xff3333),
        (try_end),

        (val_add, ":deadline", 24*14),
        (party_set_slot, ":town_no", "slot_town_bank_debt", ":debt"),
        (party_set_slot, ":town_no", "slot_town_bank_deadline", ":deadline"),

    (try_end),
   ]),
]

town_menu_options = [
    ("town_bank",
       [
           (party_slot_eq, "$current_town", "slot_party_type", spt_town),
           (neq, "$freelancer_state", 1),
       ],
       "Visit the landlords and moneylenders.",
       [
            (assign, reg10, 0),  # todo: why this assign?
            (start_presentation, "prsnt_bank"),
       ]
    ),
]

reports = [
    ("view_bank_report",[],"View Financial Report",
        [(start_presentation, "prsnt_bank_quickview"),]),
]

presentations = [
  ("bank", 0, "mesh_load_window", [
    (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        (try_begin),
            (party_get_slot, ":assets", "$current_town", "slot_town_bank_assets"),
            (troop_add_gold, "trp_player", ":assets"),
            (party_set_slot, "$current_town", "slot_town_bank_assets", 0),
        (try_end),

        (str_store_party_name, s1, "$current_town"),


        (create_text_overlay, reg0, "@This area of {s1} can best be described as the very core of the town.^^\
                                     You can almost see the strings that are being pulled from here, the money that comes and goes at seemingly endless rates. \
                                     Here you can buy the land that is cultivated outside the towns gates and benefit from the ones working hard.\
                                     Of course you might not have the scillingas required to do so, but the moneylenders are known to have some spare change.", tf_center_justify),
        (position_set_x, pos1, 475),
        (position_set_y, pos1, 600),
        (overlay_set_position, reg0, pos1),

        (position_set_x, pos2, 800),
        (position_set_y, pos2, 900),
        (overlay_set_size, reg0, pos2),

        (party_get_slot, ":population", "$current_town", "slot_center_population"),
        (party_get_slot, ":land_town", "$current_town", "slot_town_acres"),
        (party_get_slot, ":land_player", "$current_town", "slot_town_player_acres"),
        (store_add, ":land_total", ":land_town", ":land_player"),
        (assign, reg1, ":population"),
        (assign, reg2, ":land_total"),
        (assign, reg3, ":land_player"),

        (party_get_slot, ":debt", "$current_town", "slot_town_bank_debt"),
        (assign, reg4, ":debt"),

        (assign, reg5, 0),  # Slider storage / acres        Buy
        (assign, reg6, 0),  # Slider storage / money        Borrow
        (assign, reg7, 0),  # Slider storage / acres        Build
        (assign, reg8, 0),  # Slider storage / money        Pay back

        (party_get_slot, ":prosp_mod", "$current_town", "slot_town_prosperity"),
        (store_mul, ":price_mod", ":prosp_mod", 10),
        (val_sub, ":price_mod", 500),
        (store_add, reg9, 2000, ":price_mod"),  # Buy Price
        (store_add, reg10, 950, ":price_mod"),  # Sell Price
        (store_add, reg11, 3000, ":price_mod"),  # Build Price
        # reg12 used for buy/sell switch
        (store_sub, ":rent_mod", ":prosp_mod", 50),
        (store_add, reg13, ":rent_mod", 100),  # Rent Revenue

        (create_text_overlay, "$g_presentation_obj_19", "@{reg1} people live in {s1}. There are currently {reg2} acres of land available for cultivation to provide them with \
 food and other goods. You own {reg3} acres of land in this town. You currently owe the moneylenders of {s1} {reg4} scillingas. The interest rate is 20% and the contract period amounts \
 to 2 weeks. If you dont manage to pay off your debt until the deadline, the interest is raised to 40%. Buying an existing acre costs {reg9} scillingas, while it sells for {reg10} scillingas. Building a new one requires {reg11} scillingas.\
 The rent paid to landowners currently accumulates to {reg13} scillingas per acre every 2 weeks and has to be collected in the town. Land wont be rented if a town is already well supplied.",tf_center_justify),
        (position_set_x, pos1, 475),
        (position_set_y, pos1, 450),
        (overlay_set_position, "$g_presentation_obj_19", pos1),

        (position_set_x, pos2, 900),
        (position_set_y, pos2, 1000),
        (overlay_set_size, "$g_presentation_obj_19", pos2),

        (try_begin),
            (eq, reg12, 2222),
            (str_store_string, s2, "@Choose how many acres you wish to sell :"),
        (else_try),
            (str_store_string, s2, "@Choose how many acres you wish to buy :"),
        (try_end),

        # Landlords buy
        (create_button_overlay, "$g_presentation_obj_16", "@{s2}",tf_center_justify),
        (position_set_x, pos1, 250),
        (position_set_y, pos1, 350),
        (overlay_set_position, "$g_presentation_obj_16", pos1),

        (store_troop_gold, ":funds", "trp_player"),
        (store_div, ":funds_build", ":funds", reg11),
        (val_div, ":funds", reg9),
        (val_min, ":funds", ":land_town"),

        (try_begin),
            (eq, reg12, 2222),
            (party_get_slot, ":sell_no", "$current_town", "slot_town_player_acres"),
            (assign, ":funds", ":sell_no"),
        (try_end),

    (create_slider_overlay, "$g_presentation_obj_1", 0, ":funds"),
        (position_set_x, pos1, 250),
        (position_set_y, pos1, 310),
        (overlay_set_position, "$g_presentation_obj_1", pos1),

    (create_text_overlay, "$g_presentation_obj_2", "@0"),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_obj_2", pos1),

    (create_button_overlay, "$g_presentation_obj_3", "@Buy Land", tf_center_justify),
        (position_set_x, pos1, 250),
        (position_set_y, pos1, 275),
        (overlay_set_position, "$g_presentation_obj_3", pos1),

    (create_text_overlay, reg0, "@Choose how much money you wish to borrow :", tf_center_justify),
        (position_set_x, pos1, 725),
        (position_set_y, pos1, 350),
        (overlay_set_position, reg0, pos1),

    # if player has a fief or renown > 500:
    #   money = 250*Prosperity + Relationship*100 - Debt
    # else:
    #   money = min(250*Prosperity, 5000) + Relationship*100 - Debt
    # if combined debt > 50k:
    #   money = 0
    (assign, ":fief_count", 0),
    (try_for_range, ":cur_center", centers_begin, centers_end),
        (party_slot_eq, ":cur_center", "slot_town_lord", "trp_player"),
        (val_add, ":fief_count", 1),
    (try_end),

    (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
    (party_get_slot, ":prosperity", "$current_town", "slot_town_prosperity"),

    (store_mul, ":money", ":prosperity", 250),
    (try_begin),
        (lt, ":fief_count", 1),
        (lt, ":renown", 500),
        (gt, ":money", 5000),
        (assign, ":money", 5000),
    (try_end),

    # relations factor
    (party_get_slot, ":player_relation", "$current_town", "slot_center_player_relation"),
    (store_mul, ":trust", ":player_relation", 100),
    (val_add, ":money", ":trust"),

    # debt factor
    (val_sub, ":money", ":debt"),

    # if negative: 0
    (try_begin),
        (lt, ":money", 0),
        (assign, ":money", 0),
    (try_end),

    # If debt > 50k: money = 0
    (try_begin),
        (assign, reg25, 0),
        (try_for_range, ":town_no", towns_begin, towns_end),
            (party_get_slot, ":debt_all", ":town_no", "slot_town_bank_debt"),
            (val_add, reg25, ":debt_all"),
        (try_end),
        (ge, reg25, 50000),
        (assign, ":money", 0),
    (try_end),

    (create_slider_overlay, "$g_presentation_obj_4", 0, ":money"),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 310),
        (overlay_set_position, "$g_presentation_obj_4", pos1),

    (create_text_overlay, "$g_presentation_obj_5", "@0"),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 300),
        (overlay_set_position, "$g_presentation_obj_5", pos1),

    (create_button_overlay, "$g_presentation_obj_6", "@Borrow", tf_center_justify),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 275),
        (overlay_set_position, "$g_presentation_obj_6", pos1),

    # Landlord / Buy and Build
    (create_text_overlay, "$g_presentation_obj_7", "@Buy and prepare uncultivated land :", tf_center_justify),
        (position_set_x, pos1, 250),
        (position_set_y, pos1, 200),
        (overlay_set_position, "$g_presentation_obj_7", pos1),


    (create_slider_overlay, "$g_presentation_obj_8", 0, ":funds_build"),
        (position_set_x, pos1, 250),
        (position_set_y, pos1, 160),
        (overlay_set_position, "$g_presentation_obj_8", pos1),

    (create_text_overlay, "$g_presentation_obj_9", "@0"),
        (position_set_x, pos1, 400),
        (position_set_y, pos1, 150),
        (overlay_set_position, "$g_presentation_obj_9", pos1),

    (create_button_overlay, "$g_presentation_obj_10", "@Prepare Land", tf_center_justify),
        (position_set_x, pos1, 250),
        (position_set_y, pos1, 125),
        (overlay_set_position, "$g_presentation_obj_10", pos1),


    (create_text_overlay, "$g_presentation_obj_11", "@Pay off your debt :",tf_center_justify),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 200),
        (overlay_set_position, "$g_presentation_obj_11", pos1),

        (store_troop_gold, ":funds", "trp_player"),
        (try_begin),
            (lt, ":debt", ":funds"),
            (assign, ":funds", ":debt"),
        (try_end),

    (create_slider_overlay, "$g_presentation_obj_12", 0, ":funds"),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 160),
        (overlay_set_position, "$g_presentation_obj_12", pos1),

    (create_text_overlay, "$g_presentation_obj_13", "@0"),
        (position_set_x, pos1, 850),
        (position_set_y, pos1, 150),
        (overlay_set_position, "$g_presentation_obj_13", pos1),

    (create_button_overlay, "$g_presentation_obj_14", "@Make Payment", tf_center_justify),
        (position_set_x, pos1, 700),
        (position_set_y, pos1, 125),
        (overlay_set_position, "$g_presentation_obj_14", pos1),

    (create_game_button_overlay, "$g_presentation_obj_15", "@Done", 0),
        (position_set_x, pos1, 880),
        (position_set_y, pos1, 25),
        (overlay_set_position, "$g_presentation_obj_15", pos1),
    ]),

    (ti_on_presentation_event_state_change,
        [
        (store_trigger_param_1, ":object"),
        (store_trigger_param_2, ":value"),

        (try_begin),
            # Show chosen amount of land
            (eq, ":object", "$g_presentation_obj_1"),
            (assign, reg5, ":value"),
            (overlay_set_text, "$g_presentation_obj_2", "@{reg5}"),
        (else_try),
            # Sell/Buy chosen amount of land
            (eq, ":object", "$g_presentation_obj_3"),
            (try_begin),
                (eq, reg12, 2222),
                (try_begin),
                    (gt, reg5, 0),
                    (store_mul, ":price", reg5, reg10),
                    (troop_add_gold, "trp_player", ":price"),
                    (party_get_slot, ":land_town", "$current_town", "slot_town_acres"),
                    (val_add, ":land_town", reg5),
                    (party_set_slot, "$current_town", "slot_town_acres", ":land_town"),
                    (party_get_slot, ":land_player", "$current_town", "slot_town_player_acres"),
                    (val_sub, ":land_player", reg5),
                    (party_set_slot, "$current_town", "slot_town_player_acres", ":land_player"),
                    (start_presentation, "prsnt_bank"),
                (else_try),
                    (display_message, "@You cant sell 0 acres of land."),
                (try_end),
            (else_try),
                (try_begin),
                    (gt, reg5, 0),
                    (store_mul, ":cost", reg5, reg9),
                    (troop_remove_gold, "trp_player", ":cost"),
                    (party_get_slot, ":land_town", "$current_town", "slot_town_acres"),
                    (val_sub, ":land_town", reg5),
                    (party_set_slot, "$current_town", "slot_town_acres", ":land_town"),
                    (party_get_slot, ":land_player", "$current_town", "slot_town_player_acres"),
                    (val_add, ":land_player", reg5),
                    (party_set_slot, "$current_town", "slot_town_player_acres", ":land_player"),
                    (start_presentation, "prsnt_bank"),
                (else_try),
                    (display_message, "@You cant buy 0 acres of land."),
                (try_end),
            (try_end),
        (else_try),
            # Show chosen amount of money
            (eq, ":object", "$g_presentation_obj_4"),
            (assign, reg6, ":value"),
            (overlay_set_text, "$g_presentation_obj_5", "@{reg6}"),
        (else_try),
            # Borrow chosen amount of money
            (eq, ":object", "$g_presentation_obj_6"),
            (try_begin),
                (gt, reg6, 0),
                (party_get_slot, ":debt", "$current_town", "slot_town_bank_debt"),
                (try_begin),
                    (le, ":debt", 0),
                    (store_current_hours, ":date"),
                    (val_add, ":date", 24*14*2), # First Deadline / 4 weeks / then 2 weeks (see simple_triggers)
                    (party_set_slot, "$current_town", "slot_town_bank_deadline", ":date"),
                (try_end),
                (troop_add_gold, "trp_player", reg6),
                (val_mul, reg6, 120),
                (val_div, reg6, 100),
                (val_add, ":debt", reg6),
                (party_set_slot, "$current_town", "slot_town_bank_debt", ":debt"),
                (start_presentation, "prsnt_bank"),
            (else_try),
                (display_message, "@You cant borrow 0 scillingas."), #chief cambia
            (try_end),
        (else_try),
            #    Show chosen amount of land    //    2nd Option
            (eq, ":object", "$g_presentation_obj_8"),
            (assign, reg7, ":value"),
            (overlay_set_text, "$g_presentation_obj_9", "@{reg7}"),
        (else_try),
            #    Buy chosen amount of land    //    2nd Option
            (eq, ":object", "$g_presentation_obj_10"),
            (try_begin),
                (gt, reg7, 0),
                (store_mul, ":cost", reg7, reg11),
                (troop_remove_gold, "trp_player", ":cost"),
                (party_get_slot, ":land_player", "$current_town", "slot_town_player_acres"),
                (val_add, ":land_player", reg7),
                (party_set_slot, "$current_town", "slot_town_player_acres", ":land_player"),
                (start_presentation, "prsnt_bank"),
            (else_try),
                (display_message, "@You cant buy 0 acres of land."),
            (try_end),
        (else_try),
            # Show chosen amount of money
            (eq, ":object", "$g_presentation_obj_12"),
            (assign, reg8, ":value"),
            (overlay_set_text, "$g_presentation_obj_13", "@{reg8}"),
        (else_try),
            # Pay back chosen amount of money
            (eq, ":object", "$g_presentation_obj_14"),
            (try_begin),
                (gt, reg8, 0),
                (troop_remove_gold, "trp_player", reg8),
                (party_get_slot, ":debt", "$current_town", "slot_town_bank_debt"),
                (val_sub, ":debt", reg8),
                (party_set_slot, "$current_town", "slot_town_bank_debt", ":debt"),
                (try_begin),
                    (le, ":debt", 0),
                    (party_set_slot, "$current_town", "slot_town_bank_deadline", 0),
                (try_end),
                (start_presentation, "prsnt_bank"),
            (else_try),
                (display_message, "@You cant pay back 0 scillingas."), #chief
            (try_end),
        (else_try),
            # Switch Buy/Sell
            (eq, ":object", "$g_presentation_obj_16"),
            (try_begin),
                (neq, reg12, 2222),
                (assign, reg12, 2222),
                (start_presentation, "prsnt_bank"),
            (else_try),
                (assign, reg12, 0),
                (start_presentation, "prsnt_bank"),
            (try_end),
        (else_try),
            # Leave
            (eq, ":object", "$g_presentation_obj_15"),
            (presentation_set_duration, 0),
        (try_end),
        ]),
      ]),

  ("bank_quickview", 0, "mesh_cpov",
   [
     (ti_on_presentation_load,
      [
        (presentation_set_duration, 999999),
        (set_fixed_point_multiplier, 1000),

        ###HEADLINES###
        (assign, ":x_poshl", 155),
        (assign, ":y_pos", 581),
        (assign, ":jq_size", pos0),
        (position_set_x, ":jq_size", 720),
        (position_set_y, ":jq_size", 775),

        (create_text_overlay, reg1, "@Town", tf_center_justify),
        (overlay_set_size, reg1, ":jq_size"),
         (position_set_x, pos1, ":x_poshl"),
        (position_set_y, pos1, ":y_pos"),
        (overlay_set_position, reg1, pos1),

        (create_text_overlay, reg1, "@Acres", tf_center_justify),
           (overlay_set_size, reg1, ":jq_size"),
        (val_add, ":x_poshl", 120),
         (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg1, pos1),

        (create_text_overlay, reg1, "@Owned", tf_center_justify),
           (overlay_set_size, reg1, ":jq_size"),
        (val_add, ":x_poshl", 108),
         (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg1, pos1),

        (create_text_overlay, reg1, "@Balance", tf_center_justify),
           (overlay_set_size, reg1, ":jq_size"),
        (val_add, ":x_poshl", 112),
         (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg1, pos1),

        (create_text_overlay, reg1, "@Assets", tf_center_justify),
           (overlay_set_size, reg1, ":jq_size"),
        (val_add, ":x_poshl", 105),
         (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg1, pos1),

        (create_text_overlay, reg1, "@Debt", tf_center_justify),
           (overlay_set_size, reg1, ":jq_size"),
        (val_add, ":x_poshl", 105),
         (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg1, pos1),

        (create_text_overlay, reg1, "@Deadline", tf_center_justify),
           (overlay_set_size, reg1, ":jq_size"),
        (val_add, ":x_poshl", 120),
         (position_set_x, pos1, ":x_poshl"),
        (overlay_set_position, reg1, pos1),


        (str_clear, s0),
        (create_text_overlay, reg0, s0, tf_scrollable),
        (position_set_x, pos1, 10),
        (position_set_y, pos1, 100),
        (overlay_set_position, reg0, pos1),
        (position_set_x, pos1, 900),
        (position_set_y, pos1, 450),
        (overlay_set_area_size, reg0, pos1),
        (set_container_overlay, reg0),

        (assign, ":jq_value", 100),
        (assign, ":jq_size", 0),
        (assign, ":x_pos", 0),
        (assign, ":y_pos", 947),
        (str_clear, s9),
        (str_clear, s8),

        (assign, reg2, 0), # total_acres
        (assign, reg3, 0), # player_acres
        (assign, reg4, 0), # balance
        (assign, reg5, 0), # assets
        (assign, reg6, 0), # debt
        (assign, reg7, 0), # deadline

        (try_for_range, ":center_no", towns_begin, towns_end),
            (party_get_slot, ":land_town", ":center_no", "slot_town_acres"),
            (party_get_slot, ":land_player", ":center_no", "slot_town_player_acres"),
            (party_get_slot, ":assets", ":center_no", "slot_town_bank_assets"),
            (party_get_slot,":debt",":center_no","slot_town_bank_debt"),
            (party_get_slot, ":deadline", ":center_no", "slot_town_bank_deadline"),
            (party_get_slot, ":population", ":center_no", "slot_center_population"),
            (party_get_slot, ":prosperity", ":center_no", "slot_town_prosperity"),

            (store_add, ":land_total", ":land_town", ":land_player"),

            (store_div, ":acres_needed", ":population", 200),
            (store_sub, ":surplus", ":land_total", ":acres_needed"),
            (store_sub, ":revenue", ":prosperity", 50),
            (val_add, ":revenue", 100),
            (assign, ":rent_player", 0),
            (assign, ":upkeep_player", 0),
            (try_begin),
                (gt, ":land_player", 0),                    #     Fix El problema chief estaba por aqui, igual Duh lo ha arreglado
                (try_begin),                        #    Player Balance
                    (le, ":land_total", ":acres_needed"),
                    (store_mul, ":rent_player", ":land_player", ":revenue"),
                (else_try),
                    (store_mul, ":penalty", ":surplus", -1),
                    (val_add, ":penalty", ":revenue"),
                    (try_begin),
                        (ge, ":penalty", 85),
                        (store_mul, ":rent_player", ":land_player", ":penalty"),
                    (else_try),
                        (store_sub, ":non_rented", ":surplus", 15),
                        (val_sub, ":land_player", ":non_rented"),
                        (store_mul, ":rent_player", ":land_player", 85),
                        (store_mul, ":upkeep_player", ":non_rented", -50),
                    (try_end),
                (try_end),
            (try_end),

            (store_add, ":balance", ":rent_player", ":upkeep_player"),

            (val_add, ":jq_value", 1),

            #center center name
            (val_add, ":x_pos", 118),
            (str_store_party_name,s9, ":center_no"),
            (str_store_string, s1, "@{s9}"),
            (create_text_overlay, reg1, s1, tf_left_align),
            (position_set_x, pos3, ":x_pos"),
            (position_set_y, pos3, ":y_pos"),
            (overlay_set_position, reg1, pos3),
            (position_set_x, pos3, 750),
            (position_set_y, pos3, 850),
            (overlay_set_size, reg1, pos3),

            #center land in acres
            (val_add, ":x_pos", 135),
            (assign, reg2, ":land_total"),
            (create_text_overlay, reg1, "@{reg2}", tf_left_align),
            (position_set_x, pos3, ":x_pos"),
            (position_set_y, pos3, ":y_pos"),
            (overlay_set_position, reg1, pos3),
            (position_set_x, pos3, 750),
            (position_set_y, pos3, 850),
            (overlay_set_size, reg1, pos3),

            #Player land in city
            (val_add, ":x_pos", 113),
            (assign, reg3, ":land_player"),
            (str_store_string, s1, "@{reg3}"),
            (create_text_overlay, reg1, s1, tf_left_align),
            (position_set_x, pos3, ":x_pos"),
            (position_set_y, pos3, ":y_pos"),
            (overlay_set_position, reg1, pos3),
            (position_set_x, pos3, 750),
            (position_set_y, pos3, 850),
            (overlay_set_size, reg1, pos3),

            #city Balance
            (val_add, ":x_pos", 110),
            (assign, reg4, ":balance"),
            (str_store_string, s1, "@{reg4}"),
            (create_text_overlay, reg1, s1, tf_left_align),
            (position_set_x, pos3, ":x_pos"),
            (position_set_y, pos3, ":y_pos"),
            (overlay_set_position, reg1, pos3),
            (position_set_x, pos3, 750),
            (position_set_y, pos3, 850),
            (overlay_set_size, reg1, pos3),

            #Player assets in city
            (val_add, ":x_pos", 110),
            (assign, reg4, ":assets"),
            (str_store_string, s1, "@{reg4}"),
            (create_text_overlay, reg1, s1, tf_left_align),
            (position_set_x, pos3, ":x_pos"),
            (position_set_y, pos3, ":y_pos"),
            (overlay_set_position, reg1, pos3),
            (position_set_x, pos3, 750),
            (position_set_y, pos3, 850),
            (overlay_set_size, reg1, pos3),

            #city Debt
            (val_add, ":x_pos", 105),
            (assign, reg5, ":debt"),
            (str_store_string, s1, "@{reg5}"),
            (create_text_overlay, reg1, s1, tf_left_align),
            (position_set_x, pos3, ":x_pos"),
            (position_set_y, pos3, ":y_pos"),
            (overlay_set_position, reg1, pos3),
            (position_set_x, pos3, 750),
            (position_set_y, pos3, 850),
            (overlay_set_size, reg1, pos3),

            #city Deadline
            (val_add, ":x_pos", 105),
            (try_begin),
                (gt, ":deadline", 0),
                (call_script, "script_game_get_date_text", 1, ":deadline"),
            (else_try),
                (str_store_string, s1, "@None"),
            (try_end),
            (create_text_overlay, reg1, s1, tf_left_align),
            (position_set_x, pos3, ":x_pos"),
            (position_set_y, pos3, ":y_pos"),
            (overlay_set_position, reg1, pos3),
            (position_set_x, pos3, 750),
            (position_set_y, pos3, 850),
            (overlay_set_size, reg1, pos3),

            (assign, ":x_pos", 0),
            (assign, ":x_poshl", 165),
            (val_sub, ":y_pos", 23), # linebreak
            (ge, ":x_pos", 950),
            (assign, ":x_pos", 0),
            (val_sub, ":y_pos", 23),
        (try_end), # Center-Bank Loop End

        (set_container_overlay, -1),

         #Back to menu - graphical button
        (create_game_button_overlay, "$g_jq_Return_to_menu", "@_Return to menu_"),
        (position_set_x, pos1, 500),
        (position_set_y, pos1, 23),
        (overlay_set_position, "$g_jq_Return_to_menu", pos1),
        (assign, "$g_jq_Back_to_shop", 0), ##BUGFIX - savegame compatability
        (assign, "$jq_nr", 0), ##BUGFIX - savegame compatability

      ]),
    (ti_on_presentation_event_state_change,
     [
        (store_trigger_param_1, ":object"),
        (try_begin),
            (eq, ":object", "$g_jq_Return_to_menu"),
            (presentation_set_duration, 0),
        (try_end),
        ]),
    ]),
]
