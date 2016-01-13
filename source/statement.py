

class StatementBlock(object):

    def __init__(self, *args):
        self._statement_block = args

    def __iter__(self):
        return iter(self._statement_block)

    def __len__(self):
        length = 0
        for statement in self._statement_block:
            if isinstance(statement, StatementBlock):
                length += len(statement)
            else:
                length += 1
        return length
