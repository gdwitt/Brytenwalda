import logging
from collections import OrderedDict

import source.header_common as h_common

from .animation import Animation
from .dialog import Dialog
from .faction import Faction
from .info_page import InfoPage
from .item import Item
from .map_icon import MapIcon
from .menu import Menu
from .mesh import Mesh
from .mission_template import MissionTemplate
from .particle_system import ParticleSystem
from .party import Party
from .party_template import PartyTemplate
from .postfx import PostFX
from .presentation import Presentation
from .quest import Quest
from .scene import Scene
from .scene_prop import SceneProp
from .script import Script
from .simple_trigger import SimpleTrigger
from .skill import Skill
from .skin import Skin
from .sound import Sound
from .string import String
from .tableau import Tableau
from .track import Track
from .trigger import Trigger
from .troop import Troop


ALL_TYPES = [
    Animation, Dialog, Faction, InfoPage, Item, MapIcon, Menu, Mesh, MissionTemplate,
    ParticleSystem, ParticleSystem, Party, PartyTemplate, PostFX, Presentation,
    Quest, Scene, SceneProp, Script, SimpleTrigger, Skill, Skin, Sound, String,
    Tableau, Track, Trigger, Troop,
]


# a map tag -> object_type
TAG_TO_OBJECT_TYPE = dict()

for object_type in ALL_TYPES:
    if object_type.tag:
        tag = object_type.tag
        if object_type == Menu:
            tag = 'mnu'  # Menu uses a different tag on the code (don't know why)
        elif object_type == MissionTemplate:
            tag = 'mt'
        elif object_type == Tableau:
            tag = 'tableau'
        TAG_TO_OBJECT_TYPE[tag] = object_type

# populate each object_type with objects.
index_is_id = {Dialog, SimpleTrigger, Trigger}

data_is_spliced = {Troop: 16}


def create_objects(types=ALL_TYPES):
    logging.info('Creating objects...')
    for object_type in ALL_TYPES:
        logging.info('Create "%s"' % object_type.__name__)
        object_type.objects = OrderedDict()

        for data in object_type.raw_objects:
            # choose index
            if object_type in index_is_id:
                id = len(object_type.objects)
            else:
                id = data[0]

            if object_type in data_is_spliced:
                data = data[:data_is_spliced[object_type]]

            if id in object_type.objects:
                logging.warning('%s "%s" is duplicated' % (object_type.__name__, id))
                object_type.objects[id] = object_type(object_type.objects[id].index, *data)
            else:
                object_type.objects[id] = object_type(len(object_type.objects), *data)


FILE_NAMES = {
    Animation: 'actions.txt',
    Dialog: 'conversation.txt',
    Faction: 'factions.txt',
    Menu: 'menus.txt',
    InfoPage: 'info_pages.txt',
    Item: 'item_kinds1.txt',
    MapIcon: 'map_icons.txt',
    Mesh: 'meshes.txt',
    MissionTemplate: 'mission_templates.txt',
    Track: 'music.txt',
    ParticleSystem: 'particle_systems.txt',
    Party: 'parties.txt',
    PartyTemplate: 'party_templates.txt',
    PostFX: 'postfx.txt',
    Presentation: 'presentations.txt',
    Quest: 'quests.txt',
    SceneProp: 'scene_props.txt',
    Scene: 'scenes.txt',
    Script: 'scripts.txt',
    SimpleTrigger: 'simple_triggers.txt',
    Skill: 'skills.txt',
    Skin: 'skins.txt',
    Sound: 'sounds.txt',
    String: 'strings.txt',
    Tableau: 'tableau_materials.txt',
    Trigger: 'triggers.txt',
    Troop: 'troops.txt',
}

HEADERS = {
    Animation: '',
    Dialog: 'dialogsfile version 2',
    Faction: 'factionsfile version 1',
    Menu: 'menusfile version 1',
    InfoPage: 'infopagesfile version 1',
    Item: 'itemsfile version 3',
    MapIcon: 'map_icons_file version 1',
    Mesh: '',
    MissionTemplate: 'missionsfile version 1',
    Track: '',
    ParticleSystem: 'particle_systemsfile version 1',
    Party: 'partiesfile version 1',
    PartyTemplate: 'partytemplatesfile version 1',
    PostFX: 'postfx_paramsfile version 1',
    Presentation: 'presentationsfile version 1',
    Quest: 'questsfile version 1',
    SceneProp: 'scene_propsfile version 1',
    Scene: 'scenesfile version 1',
    Script: 'scriptsfile version 1',
    SimpleTrigger: 'simple_triggers_file version 1',
    Skill: '',
    Skin: 'skins_file version 1',
    Sound: 'soundsfile version 3',
    String: 'stringsfile version 1',
    Tableau: '',
    Trigger: 'triggersfile version 1',
    Troop: 'troopsfile version 2',
}


TAG_TO_TAG_ID = {
    'str': h_common.tag_string,
    'itm': h_common.tag_item,
    'trp': h_common.tag_troop,
    'fac': h_common.tag_faction,
    'qst': h_common.tag_quest,
    'pt': h_common.tag_party_tpl,
    'p': h_common.tag_party,
    'scn': h_common.tag_scene,
    'mt': h_common.tag_mission_tpl,
    'mnu': h_common.tag_menu,
    'script': h_common.tag_script,
    'psys': h_common.tag_particle_sys,
    'spr': h_common.tag_scene_prop,
    'prsnt': h_common.tag_presentation,
    'snd': h_common.tag_sound,
    'icon': h_common.tag_map_icon,
    'skl': h_common.tag_skill,
    'track': h_common.tag_track,
    'mesh': h_common.tag_mesh,
    'anim': h_common.tag_animation,
    'tableau': h_common.tag_tableau,
}
