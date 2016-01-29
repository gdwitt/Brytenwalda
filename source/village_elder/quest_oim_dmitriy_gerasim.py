from source.header_operations import *
from source.header_dialogs import anyone, plyr

from source.module_constants import slot_quest_current_state


dialogs = [
    [anyone | plyr, "village_elder_talk", [
        (eq, "$g_talk_troop", "trp_village_82_elder"),
        (check_quest_active, "qst_oim_dmitriy_gerasim"),
        (quest_slot_eq, "qst_oim_dmitriy_gerasim", slot_quest_current_state, 0)
    ],
     "I have heard tell that Veracius Evangelic lives here. Where can I find him?",
     "oim_start_quest_trakay_icon", [
         (quest_set_slot, "qst_oim_dmitriy_gerasim", slot_quest_current_state, 1)
     ]],

    [anyone | plyr, "village_elder_talk", [
        (eq, "$g_talk_troop", "trp_village_107_elder"),
        (eq, "qst_oim_dmitriy_gerasim", 2),
    ], "Old man, are you perhaps Veracius Evangelic?",
     "oim_dmitriy_gerasim_start_dlg_1", []],

    [anyone, "oim_dmitriy_gerasim_start_dlg_1", [],
     "Perhaps so. And what business of yours would that be?",
     "oim_dmitriy_gerasim_start_dlg_2", []],

    [anyone | plyr, "oim_dmitriy_gerasim_start_dlg_2", [],
     "I heard you were a follower of Pelagius.", "oim_dmitriy_gerasim_start_dlg_3", []],

    [anyone, "oim_dmitriy_gerasim_start_dlg_3", [],
     "Perhaps so, perhaps not. And why would you be curious?",
     "oim_dmitriy_gerasim_start_dlg_4", []],

    [anyone | plyr, "oim_dmitriy_gerasim_start_dlg_4", [],
     "I want to know if he truly was the famosus roman Pelagius or not.",
     "oim_dmitriy_gerasim_start_dlg_5", []],

    [anyone, "oim_dmitriy_gerasim_start_dlg_5", [],
     "A lot of time have passed since those days. All who lived in those "
     "troubled times have long passed into the grave. Roma today call him a "
     "traitor and an heretic...",
     "oim_dmitriy_gerasim_start_dlg_6", []],

    [anyone, "oim_dmitriy_gerasim_start_dlg_6", [],
     "I see you are a warrior. You really wish to know of Pelagius?",
     "oim_dmitriy_gerasim_last_2", []],

    [anyone | plyr, "oim_dmitriy_gerasim_last_2", [],
     "Yes, old man, that is my wish.", "oim_dmitriy_gerasim_last_3", []],

    [anyone, "oim_dmitriy_gerasim_last_3", [],
     "Very well, I will tell what I can. Pelagius was born about 354 in "
     "Britannia, and about 380 he moved to Rome to write and teach about his "
     "ascetic practices. He denied the need for divine aid in performing good "
     "works and he denied the original sin of Adam. By it, Pelagius was declared "
     "a heretic by the Council of Carthage, where he traveled when Alaric, the "
     "gothic, sacked Rome in 410. His new doctrine will became known as "
     "Pelagianism.", "oim_dmitriy_gerasim_last_4", []],

    [anyone | plyr, "oim_dmitriy_gerasim_last_4", [], "I see.",
     "oim_dmitriy_gerasim_last_5", []],

    [anyone, "oim_dmitriy_gerasim_last_5", [],
     "He died near of Jerusalem around 420. But his death did not end his teachings like you can see.",
     "oim_dmitriy_gerasim_last_6", []],

    [anyone | plyr, "oim_dmitriy_gerasim_last_6", [], "Thank you, old man.",
     "oim_dmitriy_gerasim_last_19", []],

    [anyone, "oim_dmitriy_gerasim_last_19", [],
     "Spare me your thanks. today you have learned something very important.",
     "close_window", [
         (jump_to_menu, "mnu_auto_return_to_map"),
         (finish_mission),
         (call_script, "script_end_quest", "qst_oim_dmitriy_gerasim"),
     ]],
]
