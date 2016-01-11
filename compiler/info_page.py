####################################################################################################################
#  Each quest record contains the following fields:
#  1) Info page id: used for referencing info pages in other files. The prefix ip_ is automatically added before each info page id.
#  2) Info page name: Name displayed in the info page screen.
#
####################################################################################################################
import source.process_common as p_common
import source.module_info_pages as m_info_pages

from .generic_entity import GenericEntity


class InfoPage(GenericEntity):
    tag = 'ip'
    raw_objects = m_info_pages.info_pages

    def __init__(self, index, id, name, description):
        super(InfoPage, self).__init__(index, id)
        self._name = name
        self._description = description

    def export(self, compiler):
        return "%s %s %s\n"% (self.id, p_common.replace_spaces(self._name),
                              p_common.replace_spaces(self._description))
