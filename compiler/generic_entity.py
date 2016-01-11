

class GenericEntity(object):
    tag = ''
    raw_objects = []
    objects = dict()

    def __init__(self, index, id):
        self._index = index
        self._no_tag_id = id
        if self.tag:
            self._id = '%s_%s' % (self.tag, id)
        else:
            self._id = id

    @property
    def id(self):
        return self._id

    @property
    def no_tag_id(self):
        return self._no_tag_id

    @property
    def index(self):
        return self._index

    @property
    def statement_blocks(self):
        return []

    def export(self, compiler):
        raise NotImplementedError('Class "%s" has no export method' %
                                  self.__class__.__name__)
