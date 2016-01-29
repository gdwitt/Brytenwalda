from source.header_operations import *

from source.header_dialogs import anyone, plyr

from source.module_constants import slot_troop_occupation, \
    slot_troop_playerparty_history, pp_history_dismissed


dialogs = [
    [anyone, "member_separate", [
        (gt, "$npc_quit_morale", 30),
    ], "Oh really? Well, I'm not just going to wait around here. I'm going to "
       "go to the towns to look for work. Is that what you want?",
     "member_separate_confirm",
     []],

    [anyone, "member_separate", [],
     "Well, actually, there was something I needed to tell you.",
     "companion_quitting", [
         (assign, "$player_can_refuse_npc_quitting", 0),
         (assign, "$player_can_persuade_npc", 0),
     ]],

    [anyone|plyr,"member_separate_confirm", [],
     "That's right. We need to part ways.", "member_separate_yes",[]],
    [anyone|plyr,"member_separate_confirm", [],
     "No, I'd rather have you at my side.", "do_member_trade",[]],

    [anyone, "member_separate_yes", [],
     "Well. I'll be off, then. Look me up if you need me.", "close_window", [
         (troop_set_slot, "$g_talk_troop", slot_troop_occupation, 0),
         (troop_set_slot, "$g_talk_troop", slot_troop_playerparty_history, pp_history_dismissed),
         (remove_member_from_party, "$g_talk_troop"),
     ]],
]
