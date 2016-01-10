
class LazyFlag(object):
    """
    This class allows to call items defined by an id within notation of
    "a|b". For example `'icon_player'|pf_limit_members` is not a valid syntax,
    and should be changed for `LazyFlag('icon_player')|pf_limit_members`
    """
    def __init__(self, id, lhs=0, rhs=0):
        self._id = id
        self._lhs = lhs
        self._rhs = rhs

    def __ror__(self, other):
        return LazyFlag(self._id, lhs=self._lhs | other, rhs=self._rhs)

    def __or__(self, other):
        return LazyFlag(self._id, lhs=self._lhs, rhs=self._rhs | other)

    def as_int(self, to_int):
        return self._lhs | to_int(self._id) | self._rhs

    def as_index(self, compiler):
        return self._lhs | compiler.index(self._id) | self._rhs


if __name__ == '__main__':

    def converter(a):
        return {'trp1': 1, 'trp2': 2, 'trp3': 3}[a]

    assert(LazyFlag('trp1').as_int(converter) == 1)

    assert((LazyFlag('trp2')|1108).as_int(converter) == 1110)

    assert((200|LazyFlag('trp2')|1108).as_int(converter) == 1246)
