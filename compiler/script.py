import source.module_scripts as m_scripts
import source.process_common as p_common

from . import GenericEntity


class Script(GenericEntity):
    tag = 'script'
    raw_objects = m_scripts.scripts

    def __init__(self, index, id, block):
        super(Script, self).__init__(index, id)
        if not isinstance(block, list):
            raise TypeError('Second argument of script "%s" must be a list.' % id)
        self._block = block

    def export(self, compiler):
        result = ''
        id = p_common.convert_to_identifier(self._no_tag_id)
        result += "%s -1\n" % id
        result += compiler.process_statement_block(id, False, self._block)
        result += '\n'
        return result

    @property
    def statement_blocks(self):
        return [self._block]
