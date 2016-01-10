####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id.
#    7.2) Minimum number of troops in the stack.
#    7.3) Maximum number of troops in the stack.
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################
import logging

import source.process_common as p_common
import source.module_party_templates as m_party_templates

from . import GenericEntity


class PartyTemplate(GenericEntity):
    tag = 'pt'
    raw_objects = m_party_templates.party_templates

    def __init__(self, index, id, name, flags, menu, faction, personality, members):
        super(PartyTemplate, self).__init__(index, id)
        self._name = name
        self._flags = flags
        self._menu = menu
        self._faction = faction
        self._personality = personality
        if len(members) > 6:
            logging.warning('Number of members in party template "%s" exceeds 6.'
                            'Using the first 6.' % self._id)
        self._members = members[:6]

    def export(self, compiler):

        if isinstance(self._flags, int):
            flags = self._flags
        else:
            flags = self._flags.as_index(compiler)

        result = "%s %s %d %d %d %d "%(p_common.convert_to_identifier(self._id),
                                       p_common.replace_spaces(self._name),
                                       flags,
                                       compiler.index(self._menu),
                                       compiler.index(self._faction),
                                       self._personality)

        for member in self._members:
            result += "%d %d %d " % (compiler.index(member[0]),
                                     member[1], member[2])
            if len(member) == 4:
                result += "%d " % member[3]
            elif len(member) > 4:
                logging.warning('Troop in party template "%s" has more than 4 '
                                'parameters. Extra parameters ignored.' % self._id)
            else:
                result += "0 "
        for i in range(6 - len(self._members)):
            result += '-1 '

        result += '\n'
        return result
