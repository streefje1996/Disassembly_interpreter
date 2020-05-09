from lexur import generate_tokens
from lexur import get_token
from program_state import program_state
from runner import execute_program
from storage import storage
from disassembly_parser import *
from typing import TextIO

file = open('main.jes', 'r')

raw_file = file.readlines()

file.close()

# read_file :: [str] -> [str]
def read_file(raw : List[str]) -> List[str]:
	if (len(raw) == 0):
		return []

	head, *tail = raw

	new_list = head.split()
	if (len(new_list) > 0):
		return new_list + ['/n'] + read_file(tail)
	return read_file(tail)
	
disassembly_file = read_file(raw_file)

#using map
#generated_tokens = list(map(get_token, disassembly_file)) 

#not using map
generated_tokens = generate_tokens(disassembly_file)

if not any(map(lambda a: True if type(a) == error else False, generated_tokens)):

	cmds = parse(generated_tokens)

	booklet = get_labels(cmds)

	state = program_state(storage,0,booklet)

	a = execute_program(cmds, state)

else:
	print('error in token')



