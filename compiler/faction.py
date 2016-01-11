####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################
import logging

from collections import OrderedDict

import source.process_common as p_common
import source.module_factions as m_factions

from .generic_entity import GenericEntity


class Faction(GenericEntity):
    tag = 'fac'
    raw_objects = m_factions.factions

    _all_relations = OrderedDict()

    @classmethod
    def process_relations(cls, factions):
        # init with zeros
        for faction_no_tag_id in factions:
            faction = factions[faction_no_tag_id]
            cls._all_relations[faction.index] = OrderedDict()
            for faction2_no_tag_id in factions:
                faction2 = factions[faction2_no_tag_id]
                cls._all_relations[faction.index][faction2.index] = 0

        for faction_no_tag_id in factions:
            faction = factions[faction_no_tag_id]

            # fill diagonal value with coherence
            cls._all_relations[faction.index][faction.index] = faction.coherence

            # fill non-diagonal with relations
            for faction2_no_tag_id in factions:
                if faction2_no_tag_id not in cls.objects:
                    raise Exception('Faction "%s" not defined.' % faction2_no_tag_id)
                faction2 = cls.objects[faction2_no_tag_id]

                if faction2_no_tag_id in faction.relations:
                    if faction2 == faction:
                        logging.warning('Faction "%s" contains a relation with itself. '
                                        'Overwriting its "coherence" value.' % faction.id)

                    r_value = faction.relations[faction2_no_tag_id]
                    inverse_r_value = cls._all_relations[faction2.index][faction.index]

                    if inverse_r_value != 0 and inverse_r_value != r_value:
                        logging.warning(
                            'Faction "{0}" (A) contains a relation with faction "{1}" (B) (A->B: {2}) '
                            'and vice-versa (B->A: {3}), but the values are different. '
                            'Faction relations are symmetrical: using value of B->A ({3}). '
                            'Remove one or make them equal.'
                                .format(faction.no_tag_id, faction2.no_tag_id,
                                        r_value, inverse_r_value))
                    else:
                        cls._all_relations[faction.index][faction2.index] = r_value
                        cls._all_relations[faction2.index][faction.index] = r_value

    def __init__(self, index, id, name, flags, coherence, relations, ranks, color=0xAAAAAA):
        super(Faction, self).__init__(index, id)
        self._name = name
        self._flags = flags
        self._coherence = coherence
        self._relations = dict(relations)
        self._ranks = ranks
        self._color = color

    @property
    def coherence(self):
        return self._coherence

    @property
    def relations(self):
        return self._relations

    @classmethod
    def all_relations(cls):
        if not cls._all_relations:
            cls.process_relations(cls.objects)
        return cls._all_relations

    def export(self, compiler):
        result = "%s %s %d %d \n" % (
            p_common.convert_to_identifier(self._id),
            p_common.replace_spaces(self._name),
            self._flags, self._color)

        relations = self.all_relations()[self.index]
        for relation in relations:
            result += " %f " % relations[relation]
        result += "\n"

        result += "%d " % len(self._ranks)
        for rank in self._ranks:
            result += " %s " % (p_common.replace_spaces(rank))

        return result
