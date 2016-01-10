####################################################################################################################
#Each party record contains the following fields:
#1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id.
#   11.2) Number of troops in this stack.
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################
import source.process_common as p_common
import source.module_parties as m_parties

from . import GenericEntity


class Party(GenericEntity):
    tag = 'p'
    raw_objects = m_parties.parties

    def __init__(self, index, id, name, flags, menu, template, faction,
                 personality, ai_behavior, ai_target, init_position, members, bearing=0):
        super(Party, self).__init__(index, id)
        self._name = name
        self._flags = flags
        self._menu = menu
        self._template = template
        self._faction = faction
        self._personality = personality
        self._ai_behavior = ai_behavior
        self._ai_target = ai_target
        self._init_position = init_position
        self._members = members
        self._bearing = bearing

    def export(self, compiler):
        #if (party[5] >= 0):
        #  add_tag_use(tag_uses,tag_faction,party[5])

        if isinstance(self._flags, int):
            flags = self._flags
        else:
            flags = self._flags.as_index(compiler)

        result = " 1 %d %d " % (self.index, self.index)
        result += "%s %s %d " % (p_common.convert_to_identifier(self.id),
                                 p_common.replace_spaces(self._name),
                                 flags)
        if isinstance(self._menu, str):
            menu_index = compiler.index(self._menu)
        else:
            menu_index = self._menu
        result += "%d " % menu_index

        result += "%d %d %d %d %d " % (compiler.index(self._template),
                                       compiler.index(self._faction),
                                       self._personality, self._personality,
                                       self._ai_behavior)

        if isinstance(self._ai_target, str):
            ai_target_index = compiler.index(self._ai_target)
        else:
            ai_target_index = self._ai_target

        result += "%d %d " % (ai_target_index, ai_target_index)

        result += "%f %f " % (self._init_position[0], self._init_position[1])
        result += "%f %f " % (self._init_position[0], self._init_position[1])
        result += "%f %f 0.0 " % (self._init_position[0], self._init_position[1])

        result += "%d " % len(self._members)
        for member in self._members:
            # todo: add_tag_use(tag_uses,tag_troop,member[0])
            result += "%d %d 0 %d " % (compiler.index(member[0]),
                                       member[1], member[2])

        result += "\n%.4f\n" % ((3.1415926 / 180.0) * self._bearing)

        return result
