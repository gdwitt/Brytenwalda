import source.module_tableau_materials as m_tableau

from . import GenericEntity


class Tableau(GenericEntity):
    tag = 'tab'
    raw_objects = m_tableau.tableaus

    def __init__(self, index, id, flags, material, width, height, min_x, min_y, max_x, max_y, block):
        super(Tableau, self).__init__(index, id)
        self._flags = flags
        self._material = material
        self._width = width
        self._height = height
        self._min_x = min_x
        self._min_y = min_y
        self._max_x = max_x
        self._max_y = max_y
        self._block = block

    def export(self, compiler):
        result = "%s %d %s %d %d %d %d %d %d" % \
            (self._id, self._flags, self._material, self._width, self._height,
             self._min_x, self._min_y, self._max_x, self._max_y)
        result += compiler.process_statement_block(0, 1, self._block)
        result += '\n'
        return result
