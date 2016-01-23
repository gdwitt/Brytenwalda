####################################################################################################################
#  Each scene prop record contains the following fields:
#  1) Scene prop id: used for referencing scene props in other files. The prefix spr_ is automatically added before each scene prop id.
#  2) Scene prop flags. See header_scene_props.py for a list of available flags
#  3) Mesh name: Name of the mesh.
#  4) Physics object name:
#  5) Triggers: Simple triggers that are associated with the scene prop
####################################################################################################################
import source.header_scene_props as h_scene_props
import source.module_scene_props as m_scene_props

from .generic_entity import GenericEntity


class SceneProp(GenericEntity):
    tag = 'spr'
    raw_objects = m_scene_props.scene_props

    def __init__(self, index, id, flags, mesh_name, object_name, triggers):
        super(SceneProp, self).__init__(index, id)
        self._flags = flags
        self._mesh_name = mesh_name
        self._object_name = object_name
        self._triggers = triggers

    def export(self, compiler):
        result = "%s %d %d %s %s " % (self._id, self._flags,
                                      h_scene_props.get_spr_hit_points(self._flags),
                                      self._mesh_name, self._object_name)
        result += compiler.process_simple_triggers(
            "%s.%s" % (self.__class__.__name__, self.no_tag_id), self._triggers)
        result += "\n"
        return result

    @property
    def statement_blocks(self):
        return [self._triggers]
