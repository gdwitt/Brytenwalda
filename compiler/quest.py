####################################################################################################################
#  Each quest record contains the following fields:
#  1) Quest id: used for referencing quests in other files. The prefix qst_ is automatically added before each quest-id.
#  2) Quest Name: Name displayed in the quest screen.
#  3) Quest flags. See header_quests.py for a list of available flags
#  4) Quest Description: Description displayed in the quest screen.
#
# Note that you may call the opcode setup_quest_text for setting up the name and description
####################################################################################################################
import source.module_quests as m_quests

from .generic_entity import GenericEntity


class Quest(GenericEntity):
    tag = 'qst'
    raw_objects = m_quests.quests

    def __init__(self, index, id, name, flags, description):
        super(Quest, self).__init__(index, id)
        self._name = name
        self._flags = flags
        self._description = description

    def export(self, compiler):
        result = "%s %s %d %s \n" % (self._id, self._name.replace(" ", "_"),
                                     self._flags, self._description.replace(' ', '_'))
        return result
