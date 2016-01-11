####################################################################################################################
# Simple triggers are the alternative to old style triggers. They do not preserve state, and thus simpler to maintain.
#
#  Each simple trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked. gdwThis is in hours and it doesn't appear to allow a delay to be set
##gdw the game starts at 6 am I'm told
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################
import source.module_simple_triggers as m_s_triggers

from .generic_entity import GenericEntity


class SimpleTrigger(GenericEntity):
    raw_objects = m_s_triggers.simple_triggers

    def __init__(self, index, frequency, block):
        super(SimpleTrigger, self).__init__(index, index)
        self._frequency = frequency
        self._block = block

    def export(self, compiler):
        result = "%f " % self._frequency
        result += compiler.process_statement_block(0, 1, self._block)
        result += '\n'
        return result

    @property
    def statement_blocks(self):
        return [self._block]
