####################################################################################################################
#   Each mission-template is a tuple that contains the following fields:
#  1) Mission-template id (string): used for referencing mission-templates in other files.
#     The prefix mt_ is automatically added before each mission-template id
#
#  2) Mission-template flags (int): See header_mission-templates.py for a list of available flags
#  3) Mission-type(int): Which mission types this mission template matches.
#     For mission-types to be used with the default party-meeting system,
#     this should be 'charge' or 'charge_with_ally' otherwise must be -1.
#
#  4) Mission description text (string).
#  5) List of spawn records (list): Each spawn record is a tuple that contains the following fields:
#    5.1) entry-no: Troops spawned from this spawn record will use this entry
#    5.2) spawn flags.
#    5.3) alter flags. which equipment will be overriden
#    5.4) ai flags.
#    5.5) Number of troops to spawn.
#    5.6) list of equipment to add to troops spawned from here (maximum 8).
#  6) List of triggers (list).
#     See module_triggers.py for infomation about triggers.
#
#  Please note that mission templates is work in progress and can be changed in the future versions.
#
####################################################################################################################
import source.process_common as p_common
import source.header_triggers as h_triggers
import source.module_mission_templates as m_mission_templates

from .generic_entity import GenericEntity


class MissionTemplate(GenericEntity):
    tag = 'mst'
    raw_objects = m_mission_templates.mission_templates

    def __init__(self, index, id, flags, mission_type, description, groups,
                 triggers):
        super(MissionTemplate, self).__init__(index, id)
        self._flags = flags
        self._mission_type = mission_type
        self._description = description
        assert isinstance(groups, list)
        self._groups = groups
        assert isinstance(triggers, list)
        self._triggers = triggers

    def export(self, compiler):
        result = "%s %s %d  %d\n" % (p_common.convert_to_identifier(self.id),
                                    p_common.convert_to_identifier(self.no_tag_id),
                                    self._flags, self._mission_type)
        result += "%s \n" % self._description.replace(" ","_")

        # export groups
        result += "\n%d " % len(self._groups)
        for group in self._groups:
            if len(group[5]) > 8:
                Exception('Too many item_overrides in Mission template "%s"' %
                          self.id)

            result += "%d %d %d %d %d %d  " % (group[0],
                                               group[1],
                                               group[2],
                                               group[3],
                                               group[4],
                                               len(group[5]))
            for item_override in group[5]:
                # todo: add_tag_use(tag_uses,tag_item,item_override)
                # todo: why get_index?
                result += "%d " % compiler.index(item_override)
            result += "\n"

        # export triggers
        statement_name = "%s.%s" % (self.__class__.__name__, self.no_tag_id)
        result += "%d\n" % len(self._triggers)
        for trigger in self._triggers:
            trigger_statement_name = statement_name + ".Trigger(%.1f %.1f %.1f)" % (
                trigger[h_triggers.trigger_check_pos],
                 trigger[h_triggers.trigger_delay_pos],
                 trigger[h_triggers.trigger_rearm_pos]
            )

            result += "%f %f %f " % (trigger[h_triggers.trigger_check_pos],
                                     trigger[h_triggers.trigger_delay_pos],
                                     trigger[h_triggers.trigger_rearm_pos])
            result += compiler.process_statement_block(
                trigger_statement_name + '[conditions]', 1,
                trigger[h_triggers.trigger_conditions_pos])
            result += compiler.process_statement_block(
                trigger_statement_name + '[consequences]', 1,
                trigger[h_triggers.trigger_consequences_pos])
            result += '\n'
        result += '\n\n'
        return result

    @property
    def statement_blocks(self):
        s = []
        for trigger in self._triggers:
            s.append(trigger[h_triggers.trigger_conditions_pos])
            s.append(trigger[h_triggers.trigger_consequences_pos])
        return s
