####################################################################################################################
#  Each scene record contains the following fields:
#  1) Scene id {string}: used for referencing scenes in other files. The prefix scn_ is automatically added before each scene-id.
#  2) Scene flags {int}. See header_scenes.py for a list of available flags
#  3) Mesh name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  4) Body name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  5) Min-pos {(float,float)}: minimum (x,y) coordinate. Player can't move beyond this limit.
#  6) Max-pos {(float,float)}: maximum (x,y) coordinate. Player can't move beyond this limit.
#  7) Water-level {float}.
#  8) Terrain code {string}: You can obtain the terrain code by copying it from the terrain generator screen
#  9) List of other scenes accessible from this scene {list of strings}.
#     (deprecated. This will probably be removed in future versions of the module system)
#     (In the new system passages are used to travel between scenes and
#     the passage's variation-no is used to select the game menu item that the passage leads to.)
# 10) List of chest-troops used in this scene {list of strings}. You can access chests by placing them in edit mode.
#     The chest's variation-no is used with this list for selecting which troop's inventory it will access.
# 11) todo: find out what this is.
####################################################################################################################
import logging

from source.process_common import convert_to_identifier, replace_spaces

import source.module_scenes as m_scenes

from . import GenericEntity


class Scene(GenericEntity):
    tag = 'scn'
    raw_objects = m_scenes.scenes

    def __init__(self, index, id, flags, mesh, body, min_pos, max_pos, water_level,
                 terrain_code, passages, chest_troops, outer_scene=''):
        super(Scene, self).__init__(index, id)
        self._flags = flags
        self._mesh = mesh
        self._body = body
        self._min_pos = min_pos
        self._max_pos = max_pos
        self._water_level = water_level
        self._terrain_code = terrain_code
        self._passages = passages
        self._chest_troops = chest_troops
        self._outer_scene = outer_scene

    @classmethod
    def get_scene_index(cls, passage):
        scene_no = 0
        found = 0
        if passage == "exit":
            scene_no = 100000
        elif passage == "":
            scene_no = 0
        elif passage in cls.objects:
            return cls.objects[passage].index
        elif not found:
            raise Exception("Error passage '%s' not found." % passage)
        return scene_no

    def export(self, compiler):
        result = ''

        result += "%s %s %d %s %s %f %f %f %f %f %s " % \
                  (convert_to_identifier(self._id),
                   replace_spaces(self._no_tag_id),
                   self._flags, self._mesh, self._body, self._min_pos[0],
                   self._min_pos[1], self._max_pos[0], self._max_pos[1],
                   self._water_level,
                   self._terrain_code)

        result += "\n  %d " % len(self._passages)
        for passage in self._passages:
            result += " %d " % self.get_scene_index(passage)

        result += "\n  %d " % len(self._chest_troops)
        for chest_troop in self._chest_troops:
            troop_no = compiler.index(chest_troop, tag='trp')
            if troop_no == 0:
                logging.error('Unable to find chest-troop "%s" in scene "%s"' %
                              (chest_troop, self._id))
            result += " %d " % troop_no
        result += "\n"

        if self._outer_scene:
            result += " %s " % self._outer_scene
        else:
            result += " 0 "
        result += '\n'

        return result
