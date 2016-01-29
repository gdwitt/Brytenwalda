#############################
#  Each skill contains the following fields:
#  1) Skill id (string): used for referencing skills in other files. The prefix skl_ is automatically added before each skill-id .
#  2) Skill name (string).
#  3) Skill flags (int). See header_skills.py for a list of available flags
#  4) Maximum level of the skill (int).
#  5) Skill description (string): used in character window for explaining the skills.
#
####################################################################################################################
import source.process_common as p_common
import source.module_skills as m_skills

from .generic_entity import GenericEntity


class Skill(GenericEntity):
    tag = 'skl'
    raw_objects = m_skills.skills

    def __init__(self, index, id, name, flags, max_level, description):
        super(Skill, self).__init__(index, id)
        self._name = name
        self._flags = flags
        self._max_level = max_level
        assert(isinstance(description, str))
        self._description = description

    def export(self, compiler):
        result = "%s %s " % (self.id, p_common.replace_spaces(self._name))
        result += "%d %d %s\n" % (self._flags, self._max_level,
                                  self._description.replace(" ", "_"))
        return result
