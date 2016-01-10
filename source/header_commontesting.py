#----------------------------
# OPMASKS
#----------------------------
op_num_value_bits = 24 + 32

tag_register = 1
tag_variable = 2
tag_string = 3
tag_item = 4
tag_troop = 5
tag_faction = 6
tag_quest = 7
tag_party_tpl = 8
tag_party = 9
tag_scene = 10
tag_mission_tpl = 11
tag_menu = 12
tag_script = 13
tag_particle_sys = 14
tag_scene_prop = 15
tag_sound = 16
tag_local_variable = 17
tag_map_icon = 18
tag_skill = 19
tag_mesh = 20
tag_presentation = 21
tag_quick_string = 22
tag_track = 23
tag_tableau = 24
tag_animation = 25
tags_end = 26

opmask_register = tag_register << op_num_value_bits  #72057594037927936
opmask_variable = tag_variable << op_num_value_bits  #144115188075855872
opmask_string = tag_string << op_num_value_bits  #216172782113783808
opmask_item_index = tag_item << op_num_value_bits  #288230376151711744
opmask_troop_index = tag_troop << op_num_value_bits  #360287970189639680
opmask_faction_index = tag_faction << op_num_value_bits  #432345564227567616
opmask_quest_index = tag_quest << op_num_value_bits  #504403158265495552
opmask_p_template_index = tag_party_tpl << op_num_value_bits  #576460752303423488
opmask_party_index = tag_party << op_num_value_bits  #648518346341351424
opmask_scene_index = tag_scene << op_num_value_bits  #720575940379279360
opmask_mission_tpl_index = tag_mission_tpl << op_num_value_bits  #792633534417207296
opmask_menu_index = tag_menu << op_num_value_bits  #864691128455135232
opmask_script = tag_script << op_num_value_bits  #936748722493063168
opmask_particle_sys = tag_particle_sys << op_num_value_bits  #1008806316530991104
opmask_scene_prop = tag_scene_prop << op_num_value_bits  #1080863910568919040
opmask_sound = tag_sound << op_num_value_bits  #1152921504606846976
opmask_local_variable = tag_local_variable << op_num_value_bits  #1224979098644774912
opmask_map_icon = tag_map_icon << op_num_value_bits  #1297036692682702848
opmask_skill = tag_skill << op_num_value_bits  #1369094286720630784
opmask_mesh = tag_mesh << op_num_value_bits  #1441151880758558720
opmask_presentation = tag_presentation << op_num_value_bits  #1513209474796486656
opmask_quick_string = tag_quick_string << op_num_value_bits  #1585267068834414592
opmask_track = tag_track << op_num_value_bits  #1657324662872342528
opmask_tableau = tag_tableau << op_num_value_bits  #1729382256910270464
opmask_animation = tag_animation << op_num_value_bits  #1801439850948198400