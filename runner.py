from cmd_builder import *
from typing import List
from program_state import program_state
import copy

# execute_command :: command -> program_state -> program_state
def execute_command(cmd : command, state : program_state) -> program_state:
	new_state = copy.deepcopy(state)
	if (type(cmd) == operator_command):
		if (cmd.other == storage_token):
			new_state.storage[cmd.reg_name.symbol] = cmd.cmd(state.storage[cmd.reg_name.symbol], state.storage[cmd.other.symbol])
		else:
			new_state.storage[cmd.reg_name.symbol] = cmd.cmd(state.storage[cmd.reg_name.symbol], cmd.other.value)

	#needs top happen after all code except when jumping
	new_state.execute_cmd_n += 1

	if (type(cmd) == jump_command):
		#TODO -> FIX AUTO INT     vvv
		new_state.execute_cmd_n = cmd.cmd(cmd.label.symbol, state.label_booklet)
	return new_state

# execute_program :: [command] -> program_state -> program_state
def execute_program(commands : List[command], state : program_state):
	if (state.execute_cmd_n >= len(commands)):
		return state

	new_state = execute_command(commands[state.execute_cmd_n], state)

	return execute_program(commands, new_state)


