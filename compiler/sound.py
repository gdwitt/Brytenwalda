from collections import OrderedDict

import source.module_sounds as m_sounds

from . import GenericEntity


class Sound(GenericEntity):
    tag = 'snd'
    raw_objects = m_sounds.sounds

    # a map "sample_name" -> (index, flags) created by `cls.process_samples`
    # and used by `cls.get_sample_index` and `cls.export_samples`.
    _samples = OrderedDict()

    @classmethod
    def get_sample_index(cls, sound_file):
        if not cls._samples:
            cls.process_samples(cls.objects)
        return cls._samples[sound_file][0]

    @classmethod
    def process_samples(cls, sounds):
        for sound_id in sounds:
            sound = sounds[sound_id]
            for sound_file in sound.files:
                if sound_file[0] not in cls._samples:
                    cls._samples[sound_file[0]] = (len(cls._samples), sound.flags)

    @classmethod
    def export_samples(cls):
        if not cls._samples:
            cls.process_samples(cls.objects)
        result = "%d\n" % len(cls._samples)
        for sample in cls._samples:
            result += " %s %d\n" % (sample, cls._samples[sample][1])

        return result

    def __init__(self, index, id, flags, files):
        super(Sound, self).__init__(index, id)
        self._flags = flags

        self._files = []
        for sound_file in files:
            if not isinstance(sound_file, list):
                sound_file = [sound_file, 0]
            self._files.append(sound_file)

    @property
    def flags(self):
        return self._flags

    @property
    def files(self):
        return self._files

    def export(self, _):
        result = "%s %d %d " % (self.id, self.flags, len(self.files))
        for sample in self.files:
            result += "%d %d " % (self.get_sample_index(sample[0]), sample[1])
        result += "\n"

        return result
