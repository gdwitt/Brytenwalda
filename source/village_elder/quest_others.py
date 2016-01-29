from source.header_operations import *
from source.header_dialogs import anyone, plyr


dialogs = [
    [anyone | plyr, "village_elder_talk", [
        (eq, "$g_talk_troop", "trp_village_82_elder"),
        (check_quest_succeeded, "qst_oim_trakay_icon"),
        (neg | check_quest_finished, "qst_oim_trakay_icon"),
    ], "I come to talk about the icon...", "oim_tracai_icon_done", []
     ],

    [anyone | plyr, "village_elder_talk", [
        (eq, "$g_talk_troop", "trp_village_82_elder"),
        (check_quest_failed, "qst_oim_trakay_icon"),
        (neg | check_quest_finished, "qst_oim_trakay_icon")
    ], "I come to talk about the icon...", "oim_tracai_icon_failed", []
     ],
]
