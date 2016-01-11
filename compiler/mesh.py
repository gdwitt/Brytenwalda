####################################################################################################################
#  Each mesh record contains the following fields:
#  1) Mesh id: used for referencing meshes in other files. The prefix mesh_ is automatically added before each mesh id.
#  2) Mesh flags. See header_meshes.py for a list of available flags
#  3) Mesh resource name: Resource name of the mesh
#  4) Mesh translation on x axis: Will be done automatically when the mesh is loaded
#  5) Mesh translation on y axis: Will be done automatically when the mesh is loaded
#  6) Mesh translation on z axis: Will be done automatically when the mesh is loaded
#  7) Mesh rotation angle over x axis: Will be done automatically when the mesh is loaded
#  8) Mesh rotation angle over y axis: Will be done automatically when the mesh is loaded
#  9) Mesh rotation angle over z axis: Will be done automatically when the mesh is loaded
#  10) Mesh x scale: Will be done automatically when the mesh is loaded
#  11) Mesh y scale: Will be done automatically when the mesh is loaded
#  12) Mesh z scale: Will be done automatically when the mesh is loaded
####################################################################################################################
import source.process_common as p_common
import source.module_meshes as m_meshes

from .generic_entity import GenericEntity


def export_tuple_f(iterable):
    result = ''
    for x in iterable:
        result += '%f ' % x
    return result


class Mesh(GenericEntity):
    tag = 'mesh'
    raw_objects = m_meshes.meshes

    def __init__(self, index, id, flags, resource_name, x, y, z, rot_x, rot_y, rot_z, scale_x, scale_y, scale_z):
        super(Mesh, self).__init__(index, id)
        self._flags = flags
        self._resource_name = resource_name

        self._trans = (x, y, z)
        self._rot = (rot_x, rot_y, rot_z)
        self._scale = (scale_x, scale_y, scale_z)

    def export(self, compiler):
        result = "%s %d %s " % (self.id, self._flags, p_common.replace_spaces(self._resource_name))
        result += ' '.join(['%f' % i for i in self._trans + self._rot + self._scale])
        result += '\n'
        return result
