from compiler import Compiler, create_objects


compiler = Compiler('./output', log_dir='./logs')

create_objects()
compiler.compile()
