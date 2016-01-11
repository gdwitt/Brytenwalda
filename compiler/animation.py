####################################################################################################################
#  There are two animation arrays (one for human and one for horse). Each animation in these arrays contains the following fields:
#  1) Animation id (string): used for referencing animations in other files. The prefix anim_ is automatically added before each animation-id .
#  2) Animation flags: could be anything beginning with acf_ defined in header_animations.py
#  3) Animation master flags: could be anything beginning with amf_ defined in header_animations.py
#  4) Animation sequences (list).
#  4.1) Duration of the sequence.
#  4.2) Name of the animation resource.
#  4.3) Beginning frame of the sequence within the animation resource.
#  4.4) Ending frame of the sequence within the animation resource.
#  4.5) Sequence flags: could be anything beginning with arf_ defined in header_animations.py
#
####################################################################################################################
import source.module_animations as m_animations

from .generic_entity import GenericEntity


class Animation(GenericEntity):
    tag = 'anim'
    raw_objects = m_animations.animations

    def __init__(self, index, id, flags, master_flags, *sequence):
        super(Animation, self).__init__(index, id)
        self._flags = flags
        self._master_flags = master_flags
        self._sequence = sequence

    def export(self, _):
        result = " %s %d %d " % (self._no_tag_id, self._flags, self._master_flags)

        result += " %d\n" % len(self._sequence)

        for elem in self._sequence:
            result += "  %f %s %d %d %d " % (elem[0], elem[1], elem[2], elem[3],
                                             elem[4])
            if len(elem) > 5:
                result += "%d " % elem[5]
            else:
                result += "0 "
            if len(elem) > 6:
                result += "%f %f %f " % tuple(elem[6])
            else:
                result += "%f %f %f " % tuple([0, 0, 0])
            if len(elem) > 7:
                result += "%f " % elem[7]
            else:
                result += "%f " % 0
            result += '\n'

        return result
