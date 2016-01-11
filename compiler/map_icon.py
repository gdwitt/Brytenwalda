####################################################################################################################
#  Each map icon record contains the following fields:
#  1) Map icon id: used for referencing map icons in other files.
#     The prefix icon_ is automatically added before each map icon id.
#  2) Map icon flags. See header_map icons.py for a list of available flags
#  3) Mesh name.
#  4) Scale.
#  5) Sound.
#  6) Offset x position for the flag icon.
#  7) Offset y position for the flag icon.
#  8) Offset z position for the flag icon.
####################################################################################################################
import source.module_map_icons as m_map_icons

from .generic_entity import GenericEntity


class MapIcon(GenericEntity):
    tag = 'icon'
    raw_objects = m_map_icons.map_icons

    def __init__(self, index, id, flags, name, scale, sound, offset_x=0, offset_y=0, offset_z=0):
        super(MapIcon, self).__init__(index, id)
        self._flags = flags
        self._name = name
        self._scale = scale
        self._sound = sound

        if isinstance(offset_x, list):
            self._triggers = offset_x
            assert(offset_y == 0)
            assert(offset_z == 0)
        else:
            self._triggers = []
            self._offset = (offset_x, offset_y, offset_z)

    def export(self, compiler):
        #todo: why is it `compiler.get_index(*self._sound.split('_', 1))` instead
        # of `compiler._get_identifier_value(self._sound)`?
        if isinstance(self._sound, int):
            sound_index = self._sound
        else:
            sound_index = compiler.index(self._sound)

        result = '%s %d %s %f %d ' % (self.no_tag_id, self._flags, self._name,
                                      self._scale, sound_index)
        if not self._triggers:
            result += '%f %f %f ' % (self._offset[0], self._offset[1], self._offset[2])
        else:
            result += '0 0 0 '
        result += compiler.process_simple_triggers(self._triggers)

        result += "\n"
        return result
