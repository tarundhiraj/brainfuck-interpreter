from brainfuck_interpreter import BrainfuckProgram

with open('input.bf', 'r') as bf_input_file:
    bf_input = bf_input_file.read().replace('\n', '')

program = BrainfuckProgram(bf_input)
print program.run()
