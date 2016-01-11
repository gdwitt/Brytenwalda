from compiler import Compiler, create_objects


compiler = Compiler('./output')

create_objects()
compiler.compile()
