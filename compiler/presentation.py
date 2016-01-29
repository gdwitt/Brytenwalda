####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################
import source.module_presentations as m_presentations

from .generic_entity import GenericEntity


class Presentation(GenericEntity):
    tag = 'prsnt'
    raw_objects = m_presentations.presentations

    def __init__(self, index, id, flags, mesh, triggers):
        super(Presentation, self).__init__(index, id)
        self._flags = flags
        self._mesh = mesh
        self._triggers = triggers

    def export(self, compiler):
        result = "%s %d %d " % (self._id, self._flags, compiler.index(self._mesh))
        result += compiler.process_simple_triggers(self.name, self._triggers)
        result += '\n'
        return result

    @property
    def statement_blocks(self):
        return [self._triggers]
