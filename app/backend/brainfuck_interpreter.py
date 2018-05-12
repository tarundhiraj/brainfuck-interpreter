import ply.yacc as yacc
import ply.lex as lex

"""
@author: sohilladhani
"""

"""
Globals
"""

g_number_of_cells = 3000
g_program_output_list = []
"""
    Lexer code starts here
"""

tokens = (
    'INCREMENT',
    'DECREMENT',
    'GO_LEFT',
    'GO_RIGHT',
    'WRITE',
    'READ',
    'OPEN_LOOP',
    'CLOSE_LOOP',
)

t_INCREMENT = r'\+'
t_DECREMENT = r'-'
t_GO_LEFT = r'<'
t_GO_RIGHT = r'>'
t_WRITE = r'\.'
t_READ = r','
t_OPEN_LOOP = r'\['
t_CLOSE_LOOP = r'\]'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


"""
    Lexer code ends here
"""

"""
    Parser Grammar starts here
"""


def p_commands(p):
    """
    commands : command
             | commands command
    """
    if len(p) == 2:
        p[0] = Commands()
        p[0].commands = [p[1]]
        return

    if not p[1]:
        p[1] = Commands()

    p[1].commands.append(p[2])
    p[0] = p[1]


def p_command(p):
    """
    command : INCREMENT
            | DECREMENT
            | GO_LEFT
            | GO_RIGHT
            | WRITE
            | READ
            | loop
    """
    if isinstance(p[1], str):
        p[0] = Command(p[1])
    else:
        p[0] = p[1]


def p_loop(p):
    """
    loop : OPEN_LOOP commands CLOSE_LOOP
    """
    p[0] = Loop(p[2])


def p_error(p):
    print("Syntax error in input!")


"""
Parser Grammar ends here

"""

"""
AST code starts here

"""


class Command:
    def __init__(self, command):
        self.command = command

    def run(self, src_program):
        global g_program_output_list

        if isinstance(self.command, Loop):
            self.command.run(src_program)

        if self.command == '+':
            src_program.data[src_program.location] += 1
        if self.command == '-':
            src_program.data[src_program.location] -= 1
        if self.command == '<':
            src_program.location -= 1
        if self.command == '>':
            src_program.location += 1
        if self.command == '.':
            g_program_output_list.append(chr(src_program.data[src_program.location]))


class Commands:
    def __init__(self):
        self.commands = []

    def run(self, program):
        for command in self.commands:
            command.run(program)


class Loop:
    def __init__(self, commands):
        self.commands = commands

    def run(self, program):
        while program.data[program.location] != 0:
            self.commands.run(program)

    def __str__(self):
        return '[' + str(self.commands) + ']'


"""
AST code ends here

"""


class BrainfuckProgram:
    def __init__(self, src_program):
        self.src_program = src_program

    def run(self):
        global g_program_output_list
        self.data = [0] * g_number_of_cells
        self.location = 0
        commands = self.parse(self.src_program)
        commands.run(self)
        bf_output = ''.join(g_program_output_list)
        g_program_output_list = []
        return bf_output

    def parse(self, src_program):
        lexer = lex.lex()
        parser = yacc.yacc()
        return parser.parse(src_program)

# Usage:
# source = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
# program = BrainfuckProgram(source)
# print program.run()
