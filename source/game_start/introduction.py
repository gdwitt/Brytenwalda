from ..header_game_menus import *


menus = [
    ("introduction_1", 0,
     "My name is Mildgyd The Old, and if you delve into this world, I recommend "
     "you listen carefully...^^Britain. The Britons call her Ynys Prydein, "
     "the Irish call her Alba while the Angles and Saxons gave the name of "
     "Englaland to the lands they conquered. The old isle has seen many "
     "conquerors and invaders, and for centuries the blood of warriors has "
     "fed the earth. First the Britons were here. Then the Romans came and "
     "they subdued the island they called Britannia. Some of the Britons "
     "became Roman themselves, and in the north the legions kept fighting the "
     "barbarians for many years. But one day, the empire fell and the legions "
     "withdrew from the island.^^What remained of Roman Britain was raided by "
     "Picts and Irishmen alike. The great wall built by the Romans from the "
     "sea of Ireland to the sea of Germany was no longer of any use, and their "
     "forts were deserted. The Britons, who had worshipped the God "
     "of the Christians were the prey of the barbarians and their internecine "
     "wars. To help them against their foes, they invited among them the fierce "
     "Saxons. But it was not long before they broke the alliance and rose against "
     "those who had welcomed them. For many years wars scorched the land, and "
     "strong leaders left their legacies: Emrys, Arthur, Urien in the north. "
     "Among them, Arthur had achieved the greatest success, slaughtering the "
     "Jutes and the Saxons at Mynydd Badon and forcing them into a lasting peace "
     "for 50 years.^^But the worst foes of the Britons were the Britons "
     "themselves, and their kings spent more time killing each other than "
     "fighting the invaders. This was enough for the Angles and Saxons to "
     "conquer more and more land in Britain, taking one realm after another.",
     "none",
     [(set_background_mesh, "mesh_pic_extra_combate")],

     [("introduction_yes", [], "Continue...",
       [(jump_to_menu, "mnu_introduction_1_1")]),]
     ),

    (
        "introduction_1_1", 0,
        "Saxon kingdoms replaced them, and Britons fell under the rule of Saxon "
        "masters. Mercia, Wessex, Kent, East Anglia and Bernicia are today the most "
        "powerful kingdoms of the foreigners. After Urien Rheged was slain the "
        "kings of Bernicia brought the Old North to its knees. That was so, until "
        "Cadwallon of Gwynedd and Penda of Mercia joined forces and crushed the "
        "Angles of Bernicia and Deira and killed the Brytenwalda Edwin at "
        "Haethfelth. For one year the king of Gwynedd ravaged the realms north of "
        "the Humber, before being killed by Oswald, the new king of Bernicia.^^ With "
        "his Briton allies Cadafael of Gwynedd and Cynddylan Pengwern, Penda the "
        "pagan king of Mercia is gathering his warbands for a new campaign against "
        "the Bernicians. From the far north, echoes the clash of swords between the "
        "Scots of Dal Riada, the Picts of Fortriu and the men of Alt Cluit. In the "
        "south the Britons of Dumnonia and Gwent are facing the threat of the "
        "Gaewissae and Hwicce. The warlords of Ireland are fighting each other to "
        "become the new Ard Ruire.^^ My story is not over, warrior. It is for you "
        "to continue, to become a warlord praised by the bards for centuries to "
        "come, to lead this island to its fate. Once again women shall be widowed "
        "and horses carry arms instead of hay. Again the echoes of shouts from "
        "assaulting warriors shall fill the air, and the earth lie barren before "
        "scattering armies. Again mortal enemies shall rise equipped in armour.^^ "
        "Ravens are calling, wolves are howling, spears clash and shields answer.",
        "none",
        [(set_background_mesh, "mesh_pic_extra_combate")],

        [
            ("introduction_yes2", [], "Continue...",
             [(jump_to_menu, "mnu_introduction_2")]),

            ("start", [], "Enter Brytenwalda...",
             [(jump_to_menu, "mnu_start_game_1")]),
        ]
    ),

    ("introduction_2", 0, "                              BRYTENWALDA PRESENTS:",
     "none",
     [(set_background_mesh, "mesh_pic_extra_intro1")],

     [
         ("introduction_yes3", [], "Enter Brytenwalda...",
          [(jump_to_menu, "mnu_introduction_3")]),

         ("start", [], "Enter Brytenwalda...",
          [(jump_to_menu, "mnu_start_game_1")]),
     ]),

    ("introduction_3", 0,
     "In the first centuries after the departure of Roman troops, the ancient "
     "province of Britannia faced one of the biggest threats in its history...^^"
     " Taking advantage of the weakness of Britain, the Irish from the west and "
     "the Picts from the north threw themselves in like wolves onto prey to "
     "loot the remains of a once wealthy empire.^^ From Europe several "
     "Germanic peoples arrived: Jutes, Angles and Saxons, and to a lesser"
     " extent, lower Frisians and other tribes. First came the warriors, "
     "thousands of them, invited by the Britons to help them against the "
     "raiding Picts and Irish. But the Anglo-Saxons rebelled and subdued the "
     "ground with anger and fire. Then came whole families, settlers of the new "
     "kingdoms created by the warriors. Conquered Britons adopted their cultures "
     "and language. This is the origin of what will become England.^^ By the "
     "7th century, the Anglo-Saxons ruled the eastern half of the island, and "
     "mighty kingdoms clashed together. The strongest king among the Angles "
     "and Saxons was known as Brytenwalda: Master of Britain. In year 636 AD, "
     "the title was held by Oswald, king of Bernicia, the northernmost kingdom "
     "of the Angles. The Britons of Gwynedd wanted to take revenge on him for "
     "the death of their king Cadwallon, and the pagan king Penda of Mercia "
     "wanted to take his power.^ It is a heroic age, a time of fear and steel.",
     "none",
     [(set_background_mesh, "mesh_pic_extra_intro2"),],
     [
         ("introduction_yes4", [], "Enter Brytenwalda!",
          [(jump_to_menu, "mnu_start_game_1")]),
     ]
     ),
]
