from lexur import generate_tokens
from program_state import program_state
from runner import execute_program
from storage import storage
from disassembly_parser import *

test = ['reg.5', '=', '4', '/n', 'reg.5', 'jmp', 'JASMIJN', '/n', '+', '20', '/n', 'JASMIJN:', '/n', 'reg.5', '+', '2']

generated_tokens = generate_tokens(test)

#print(generated_tokens[10])

cmds = parse(generated_tokens)

booklet = get_labels(cmds)

state = program_state(storage,0,booklet)

a = execute_program(cmds, state)

print(a.storage['REG5'].value)



