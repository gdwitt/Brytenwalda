from source.header_common import *
from source.header_dialogs import anyone, plyr
from source.module_constants import *
from source.header_operations import *
from source.statement import StatementBlock


_compute_volunteers_block = StatementBlock(
    (party_get_slot, ":num_volunteers", "$current_town", slot_center_volunteer_troop_amount),
    (party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
    (val_min, ":num_volunteers", ":free_capacity"),
    (store_troop_gold, ":gold", "trp_player"),
    (call_script, "script_cost_per_village_recruit"),
    (store_div, ":gold_capacity", ":gold", reg0),
    (val_min, ":num_volunteers", ":gold_capacity"),
)

dialogs = [

    [anyone, "village_elder_recruit_start", [
        _compute_volunteers_block,
        (le, ":num_volunteers", 0),
    ], "I don't think anyone would be interested, {sir/madam}. Is there anything "
     "else I can do for you?", "village_elder_talk", []],

    [anyone, "village_elder_recruit_start", [
        _compute_volunteers_block,
        (assign, "$temp", ":num_volunteers"),
        (assign, reg5, ":num_volunteers"),
        (store_add, reg7, ":num_volunteers", -1),
    ], "I can think of {reg5} whom I suspect would jump at the chance. If you "
       "could pay {reg0} scillingas "
       "{reg7?each for their equipment:for his equipment}. Does that suit you?",
     "village_elder_recruit_decision", []],

    [anyone | plyr, "village_elder_recruit_decision", [
        (assign, ":num_volunteers", "$temp"),
        (ge, ":num_volunteers", 1),
        (store_add, reg7, ":num_volunteers", -1)
    ],
     "Tell {reg7?them:him} to make ready.", "village_elder_pretalk", [
         (call_script, "script_village_recruit_volunteers_recruit")]
     ],

    [anyone | plyr, "village_elder_recruit_decision", [
        (party_slot_ge, "$current_town", slot_center_volunteer_troop_amount, 1)],
     "No, not now.", "village_elder_pretalk", []],
]
