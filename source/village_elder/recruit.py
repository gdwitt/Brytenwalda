from source.header_common import *
from source.header_dialogs import anyone, plyr
from source.header_operations import *


dialogs = [

    [anyone, "village_elder_recruit_start", [
        (call_script, "script_compute_village_recruits", -1),
        (le, reg0, 0),
        ], "I don't think anyone would be interested, {sir/madam}. Is there "
           "anything else I can do for you?", "village_elder_talk", []
     ],

    [anyone, "village_elder_recruit_start", [
        (call_script, "script_compute_village_recruits", -1),
        (ge, reg5, 0),
        (store_add, reg7, reg5, -1),
        ], "I can think of {reg5} whom I suspect would jump at the chance. If you "
           "could pay {reg0} scillingas "
           "{reg7?each for their equipment:for his equipment}. Does that suit you?",
     "village_elder_recruit_decision", []
     ],

    [anyone | plyr, "village_elder_recruit_decision", [
        (ge, reg5, 1),
        (store_add, reg7, reg5, -1),
        ], "Tell {reg7?them:him} to make ready.", "village_elder_pretalk", [
         (call_script, "script_village_recruit_volunteers", reg5)]
     ],

    [anyone | plyr, "village_elder_recruit_decision", [
        (lt, reg3, 1),
        ], "No, I have no space in my party right now.", "village_elder_pretalk", []
     ],

    [anyone | plyr, "village_elder_recruit_decision", [
        (lt, reg4, 1),
        ], "No, I don't have enough money right now.", "village_elder_pretalk", []
     ],

    [anyone | plyr, "village_elder_recruit_decision", [],
     "No, not right now.", "village_elder_pretalk", []
     ],
]
