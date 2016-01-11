####################################################################################################################
#  Each trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Delay interval: Time to wait before applying the consequences of the trigger
#    After its conditions have been evaluated as true.
# 3) Re-arm interval. How much time must pass after applying the consequences of the trigger for the trigger to become active again.
#    You can put the constant ti_once here to make sure that the trigger never becomes active again after it fires once.
# 4) Conditions block (list). This must be a valid operation block. See header_operations.py for reference.
#    Every time the trigger is checked, the conditions block will be executed.
#    If the conditions block returns true, the consequences block will be executed.
#    If the conditions block is empty, it is assumed that it always evaluates to true.
# 5) Consequences block (list). This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################
import source.module_triggers as m_triggers

from .generic_entity import GenericEntity


class Trigger(GenericEntity):
    raw_objects = m_triggers.triggers

    def __init__(self, index, frequency, delay, rearm, conditions, consequences):
        super(Trigger, self).__init__(index, index)
        self._frequency = frequency
        self._delay = delay
        self._rearm = rearm
        self._conditions = conditions
        self._consequences = consequences

    def export(self, compiler):
        result = "%f %f %f " % (self._frequency, self._delay, self._rearm)
        result += compiler.process_statement_block(0, 1, self._conditions)
        result += compiler.process_statement_block(0, 1, self._consequences)
        result += '\n'
        return result

    @property
    def statement_blocks(self):
        return [self._conditions, self._consequences]
