import source.process_common as p_common

from . import GenericEntity

import source.module_strings as m_strings


class String(GenericEntity):
    tag = 'str'
    raw_objects = m_strings.strings

    def __init__(self, index, id, string):
        super(String, self).__init__(index, id)
        self._string = string

    def export(self, compiler):
        return "%s %s\n" % (p_common.convert_to_identifier(self._id),
                            p_common.replace_spaces(self._string))
