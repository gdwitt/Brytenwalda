####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################
import source.module_music as m_music

from . import GenericEntity


class Track(GenericEntity):
    tag = 'track'
    raw_objects = m_music.tracks

    def __init__(self, index, id, filename, flags, continue_flags=0):
        super(Track, self).__init__(index, id)
        self._filename = filename
        self._flags = flags
        self._continue_flags = continue_flags

    def export(self, compiler):
        return "%s %d %d\n" % (self._filename, self._flags,
                               (self._flags | self._continue_flags))
