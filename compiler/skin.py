####################################################################################################################
#  Each skin record contains the following fields:
#  1) Skin id: used for referencing skins.
#  2) Skin flags. Not used yet. Should be 0.
#  3) Body mesh.
#  4) Calf mesh (left one).
#  5) Hand mesh (left one).
#  6) Head mesh.
#  7) Face keys (list)
#  8) List of hair meshes.
#  9) List of beard meshes.
# 10) List of hair textures.
# 11) List of beard textures.
# 12) List of face textures.
# 13) List of voices.
# 14) Skeleton name
# 15) Scale (doesn't fully work yet)
# 16) Blood particles 1 (do not add this if you wish to use the default particles)
# 17) Blood particles 2 (do not add this if you wish to use the default particles)
# 17) Face key constraints (do not add this if you do not wish to use it)
####################################################################################################################
import source.process_common as p_common
import source.module_skins as m_skins

from .generic_entity import GenericEntity


class Skin(GenericEntity):
    tag = ''
    raw_objects = m_skins.skins

    def __init__(self, index, id, flags, body, calf, hand, head, faces, hair_meshes,
                 beard_meshes, hair_textures, beard_textures, face_textures, voices,
                 skeleton, scale, blood_particles1=0, blood_particles2=0, face_constraints=()):
        super(Skin, self).__init__(index, id)
        self._flags = flags
        self._body = body
        self._calf = calf
        self._hand = hand
        self._head = head
        self._faces = faces
        self._hair_meshes = hair_meshes
        self._beard_meshes = beard_meshes
        self._hair_textures = hair_textures
        self._beard_textures = beard_textures
        self._face_textures = face_textures
        self._voices = voices
        self._skeleton = skeleton
        self._scale = scale
        self._blood_particles = (blood_particles1, blood_particles2)
        self._face_constraints = face_constraints

    def export(self, compiler):
        result = "%s %d\n %s %s %s\n" % (self._no_tag_id, self._flags, self._body,
                                         self._calf, self._hand)
        result += " %s %d " % (self._head, len(self._faces))
        for face_key in self._faces:
            result += "skinkey_%s %d %d %f %f %s " % \
                      (p_common.convert_to_identifier(face_key[4]),
                       face_key[0],
                       face_key[1],
                       face_key[2],
                       face_key[3],
                       p_common.replace_spaces(face_key[4]))

        result += "\n%d\n" % len(self._hair_meshes)
        for mesh_name in self._hair_meshes:
            result += " %s " % mesh_name

        result += "\n %d\n" % len(self._beard_meshes)
        for bmn in self._beard_meshes:
            result += "  %s\n" % bmn
        result += '\n'

        result += " %d " % len(self._hair_textures)
        for tex in self._hair_textures:
            result += " %s " % tex
        result += "\n"

        result += " %d " % len(self._beard_textures)
        for tex in self._beard_textures:
            result += " %s " % tex
        result += "\n"

        result += " %d "%len(self._face_textures)
        for tex in self._face_textures:
            color = tex[1]
            hair_mats = tex[2]
            hair_colors = []
            if len(tex) > 3:
                hair_colors = tex[3]
            result += " %s %d %d %d "%(tex[0], color, len(hair_mats),
                                       len(hair_colors))
            for hair_mat in hair_mats:
                result += " %s "%(p_common.replace_spaces(hair_mat))
            for hair_color in hair_colors:
                result += " %d " % hair_color
        result += "\n"

        result += " %d " % len(self._voices)
        for voice_rec in self._voices:
            result += " %d %s " % (voice_rec[0], voice_rec[1])
        result += "\n"

        result += " %s %f " % (self._skeleton, self._scale)
        result += "\n%d %d\n" % (compiler.index(self._blood_particles[0]),
                                 compiler.index(self._blood_particles[1]))

        result += "%d\n" % len(self._face_constraints)
        for constraint in self._face_constraints:
            result += "\n%f %d %d " % (constraint[0], constraint[1],
                                       (len(constraint) - 2))
            for i_pair in range(len(constraint)):
                if i_pair > 1:
                    result += " %f %d" % (constraint[i_pair][0],
                                          constraint[i_pair][1])
        result += "\n"
        return result
