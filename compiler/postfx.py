####################################################################################################################
#  Each postfx_param contains the following fields:
#  1) id (string):
#  2) flags (int).
#  3) tonemap operator type (0,1,2,3)
#  4) shader parameters1 [ HDRRange, HDRExposureScaler, LuminanceAverageScaler, LuminanceMaxScaler ]
#  5) shader parameters2 [ BrightpassTreshold, BrightpassPostPower, BlurStrenght, BlurAmount ]
#  6) shader parameters3 [ AmbientColorCoef, SunColorCoef, SpecularCoef, -reserved ]
####################################################################################################################
import source.module_postfx as m_postfx

from . import GenericEntity


class PostFX(GenericEntity):
    tag = 'pfx'
    raw_objects = m_postfx.postfx_params

    def __init__(self, index, id, flags, tone_map, shader_param1, shader_param2, shader_param3):
        super(PostFX, self).__init__(index, id)
        self._flags = flags
        self._tone_map = tone_map
        self._shader_param = (shader_param1, shader_param2, shader_param3)

    def export(self, compiler):
        result = "%s %d %d" % (self.id, self._flags, self._tone_map)

        for param in self._shader_param:
            result += "  %f %f %f %f" % (param[0], param[1], param[2], param[3])
        result += '\n'
        return result
