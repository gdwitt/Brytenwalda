from source.header_scenes import *


scenes = [
  ("multi_scene_1",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007a3b20005795e0000706d0000381800000bbc", #multiplayer chief
    [],[],"sea_outer_terrain_1"),
  ("multi_scene_2",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007941f0005415000007e650000225f00003b3e", #multiplayer chief
    [],[],"sea_outer_terrain_1"),
  ("multi_scene_3",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0", #dun tauro multiplayer chief chief
    [],[],"sea_outer_terrain_2"),
  ("multi_scene_4",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000230084fac00057d5f00002ba900004a7a000060be", #multiplayer chief
    [],[],"outer_terrain_plain"),
  ("multi_scene_5",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023002a1ba0004210900003ca000006a8900007a7b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_6",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000002300494b200048524000059e80000453300001d32",
    [],[],"outer_terrain_plain"),
  ("multi_scene_7",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023007a3b20005795e0000706d0000381800000bbc", #din arth
    [],[],"outer_terrain_plain"),
  ("multi_scene_8",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130025cb20006097f00005b1400000e2f00005fd9", #multiplayer chief
    [],[],"outer_terrain_plain"),
  ("multi_scene_9",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300010c800054d5c00004af000005d3f00002ca0", #multiplayer chief
    [],[],"outer_terrain_plain"),
  ("multi_scene_10",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013001b2320004a52900004d390000518c00001ab1", #multiplayer chief
    [],[],"outer_terrain_plain"),
  ("multi_scene_11",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000003001ce100006097d0000134c000016d8000042a2", #multiplayer chief
    [],[],"outer_terrain_plain"),
  ("multi_scene_12",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013005213200077dda0000733300002edf000052ba",
    [],[],"outer_terrain_beach"), #multiplayer chief
  ("multi_scene_13",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002541c00062d8b00000a01000068cb00006d9b", #multiplayer chief
    [],[],"outer_terrain_plain"),
  ("multi_scene_14",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000030000000c00d2348000000008000000000000000", #multiplater chief
    [],[],"sea_outer_terrain_2"),
  ("multi_scene_15",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000000500b1d158005394c00001230800072880000018f",
    [],[],"outer_terrain_desert"),
  ("multi_scene_16",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000023009629a0005615800005564000023590000579e", #multiplayer chief
    [],[],"outer_terrain_plain"),
  ("multi_scene_17",sf_generate,"none", "none", (0,0),(100,100),-100,"0x0000000130025cb20006097f00005b1400000e2f00005fd9", #multiplayer chief
    [],[],"outer_terrain_plain"),
  ("multi_scene_18",sf_generate|sf_muddy_water,"none", "none", (0,0),(100,100),-100,"0x0000000230029cb2000709c200003c9500004b9b00002f4d", #multiplayer chief
    [],[],"outer_terrain_plain"),
  ("multi_scene_19",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
  ("multi_scene_20",sf_generate,"none", "none", (0,0),(100,100),-100,"0x000000013002ab630004651800000d7a00007f3100002701",
    [],[],"outer_terrain_plain"),

  ("random_multi_plain_medium",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000033c6005004006c62500003efe00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_multi_plain_large",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x000000033c6005004006c62500003efe00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_multi_steppe_medium", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x000000033c6005004006c62500003efe00004b34000059be",
    [],[], "outer_terrain_plain"),
  ("random_multi_steppe_large", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100, 100), -0.5, "0x00000000408305e30006c625000033bd000065b400002904",
    [],[], "outer_terrain_snow"),

  ("coop_random_lrg_plain",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000333e00563800aa6a40004406900002920001e4f81",    [],[], "outer_terrain_plain"),#0x0000000135600d53000aa6a40004406900002920001e4f81
  ("coop_random_lrg_steppe", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(240, 240), -0.5, "0x00000003220005630009fe7f0004406900002920001e4f81",    [],[], "outer_terrain_steppe"),#0x0000000122000b630009fe7f0004406900002920001e4f81
  ("coop_random_lrg_snow",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000344c00563000aa6a40004406900002920001e4f81",    [],[], "outer_terrain_snow"),
  ("coop_random_lrg_desert",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x0000000350000563000aa6a40004406900002920001e4f81",    [],[], "outer_terrain_desert_b"),
  ("coop_random_lrg_steppe_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003ac60d8630009fe7f0004406900002920001e4f81",    [],[], "outer_terrain_plain"),
  ("coop_random_lrg_plain_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003bc600563800aa6a40004406900002920001e4f81",    [],[], "outer_terrain_plain"),
  ("coop_random_lrg_snow_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003cc600563800aa6a40004406900002920001e4f81",    [],[], "outer_terrain_snow"),
  ("coop_random_lrg_desert_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(240,240),-0.5,"0x00000003dc600563000a769d0000034e00004b34000059be",    [],[], "outer_terrain_desert"),

  ("coop_random_med_plain",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(100,100),-0.5,"0x0000000339400563000649920004406900002920000056d7",    [],[], "outer_terrain_plain"),#0x0000000135600d53000aa6a40004406900002920001e4f81
  ("coop_random_med_steppe", sf_generate|sf_randomize|sf_auto_entry_points, "none", "none", (0,0),(100,100), -0.5, "0x0000000321c00563000649900004406900002920000056d7",    [],[], "outer_terrain_steppe"),#0x0000000122000b630009fe7f0004406900002920001e4f81
  ("coop_random_med_snow",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(100,100),-0.5,"0x00000003434005630006418e0004406900002920001e4f81",    [],[], "outer_terrain_snow"),
  ("coop_random_med_desert",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(100,100),-0.5,"0x00000003500005630006619c0004406900002920001e4f81",    [],[], "outer_terrain_desert_b"),
  ("coop_random_med_steppe_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(100,100),-0.5,"0x00000003ac60c56300063d8f0004406900002920001e4f81",    [],[], "outer_terrain_plain"),
  ("coop_random_med_plain_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(100,100),-0.5,"0x00000003bc600563800659960004406900002920001e4f81",    [],[], "outer_terrain_plain"),
  ("coop_random_med_snow_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(100,100),-0.5,"0x00000003cc6005630006358b0004406900002920001e4f81",    [],[], "outer_terrain_snow"),
  ("coop_random_med_desert_forest",sf_generate|sf_randomize|sf_auto_entry_points,"none", "none", (0,0),(100,100),-0.5,"0x00000003dc6005630006298c0000034e00004b34000059be",    [],[], "outer_terrain_desert"),

  ("multiplayer_maps_end",sf_generate,"none", "none", (0,0),(100,100),-100,"0x00000001300389800003a4ea000058340000637a0000399b",
    [],[],"outer_terrain_plain"),
]
