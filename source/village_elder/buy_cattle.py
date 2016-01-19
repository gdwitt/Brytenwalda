from source.header_common import *
from source.header_dialogs import anyone, plyr
from source.module_constants import *
from source.header_operations import *


_NUMBER = {
    1: "One.",
    2: "Two.",
    3: "Three.",
    4: "Four.",
    5: "Five.",
}


def _buy_cattle_dialog(cattle_number):
    return [anyone | plyr, "village_elder_buy_cattle_2", [
        (party_get_slot, ":num_cattle", "$g_encountered_party", slot_village_number_of_cattle),
        (ge, ":num_cattle", cattle_number),
        (store_troop_gold, ":gold", "trp_player"),
        (store_mul, ":cost", "$temp", cattle_number),
        (ge, ":gold", ":cost")
    ], _NUMBER[cattle_number], "village_elder_buy_cattle_complete", [
        (call_script, "script_buy_cattle_from_village", "$g_encountered_party", cattle_number, "$temp"),
     ]]


dialogs = [

    [anyone, "village_elder_buy_cattle", [
        (party_get_slot, reg5, "$g_encountered_party", slot_village_number_of_cattle),
        (gt, reg5, 0),
        (store_item_value, ":cattle_cost", "itm_cattle_meat"),
        (call_script, "script_game_get_item_buy_price_factor", "itm_cattle_meat"),
        (val_mul, ":cattle_cost", reg0),
        # Multiplied by 2 and divided by 100
        (val_div, ":cattle_cost", 50),
        (assign, "$temp", ":cattle_cost"),
        (assign, reg6, ":cattle_cost"),
    ],
     "We have {reg5} heads of cattle, each for {reg6} scillingas. How many do you want to buy?",
     "village_elder_buy_cattle_2", []],

    [anyone, "village_elder_buy_cattle", [],
     "I am afraid we have no cattle left in the village {sir/madam}.",
     "village_elder_buy_cattle_2", []],

    # all are state `"village_elder_buy_cattle_2"`
    _buy_cattle_dialog(1),
    _buy_cattle_dialog(2),
    _buy_cattle_dialog(3),
    _buy_cattle_dialog(4),
    _buy_cattle_dialog(5),
    # all send to state `"village_elder_buy_cattle_complete"`

    [anyone | plyr, "village_elder_buy_cattle_2", [],
     "Forget it.", "village_elder_pretalk", []],

    [anyone, "village_elder_buy_cattle_complete", [],
     "I will tell the herders to round up the animals and bring them to you, "
     "{sir/madam}. I am sure you will be satisfied with your purchase.",
     "village_elder_pretalk", []],
]
