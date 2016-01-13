import logging
import sys

from compiler import Compiler, create_objects

# setup the logging output
root = logging.getLogger()
root.handlers = []
root.setLevel(logging.DEBUG)

# file handler logs all messages
fh = logging.FileHandler('./logs/compilation.log', 'w')
fh.setLevel(logging.DEBUG)
# console handler logs WARNING or worse
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.WARNING)
formatter = logging.Formatter('%(levelname)s:%(name)s: %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
root.addHandler(fh)
root.addHandler(ch)


compiler = Compiler('./output', log_dir='./logs')

create_objects()
compiler.compile()
