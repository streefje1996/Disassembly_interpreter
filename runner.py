from cmd_builder import *
from typing import List
from program_state import program_state
import copy

# debug_deco :: callable -> callable
def debug_deco(func : Callable) -> Callable:
	def inner(cmd : command, state : program_state):
		print('command: ', cmd, ' resulted in the following program state:')
		result = func(cmd, state)
		print(result)
		return result
	return inner

# execute_command :: command -> program_state -> program_state
@debug_deco
def execute_command(cmd : command, state : program_state) -> program_state:
	new_state = copy.deepcopy(state)
	if (type(cmd) == operator_command):
		if (type(cmd.other) == storage_token):
			new_state.storage[cmd.reg_name.symbol] = cmd.cmd(state.storage[cmd.reg_name.symbol], state.storage[cmd.other.symbol])
		else:
			new_state.storage[cmd.reg_name.symbol] = cmd.cmd(state.storage[cmd.reg_name.symbol], cmd.other.value)

	if (type(cmd) == compare_command):
		if type(cmd.lhs) == storage_token:
			#lhs = register
			if type(cmd.rhs) == storage_token:
				#rhs = register
				new_state.storage['bool flag'] = cmd.cmd(state.storage[cmd.lhs.symbol], state.storage[cmd.rhs.symbol])
			else:
				#rhs = int
				new_state.storage['bool flag'] = cmd.cmd(state.storage[cmd.lhs.symbol], cmd.rhs.value)
		else:
			#lhs = int
			if type(cmd.rhs) == storage_token:
				#rhs = register
				new_state.storage['bool flag'] = cmd.cmd(cmd.lhs.value, state.storage[cmd.rhs.symbol])
			else:
				#rhs = int
				new_state.storage['bool flag'] = cmd.cmd(cmd.lhs.value, cmd.rhs.value)

	if (type(cmd) == store_command):
		if type(cmd.other) == storage_token:
			new_state.storage[cmd.storage_name] = cmd.cmd(state.storage[cmd.storage_name], state.storage[cmd.other.symbol])
		else:
			new_state.storage[cmd.storage_name] = cmd.cmd(state.storage[cmd.storage_name], cmd.other.value)

	if (type(cmd) == get_command):
		result = cmd.cmd(state.storage[cmd.storage_name], state.storage[cmd.reg_token.symbol])
		new_state.storage[cmd.storage_name] = result[0]
		new_state.storage[cmd.reg_token.symbol] = result[1]

	if (type(cmd) == print_command):
		if type(cmd.other) == command_token:
			new_state.storage[cmd.other.symbol.lower()] = cmd.cmd(state.storage[cmd.other.symbol.lower()])
		elif type(cmd.other) == storage_token:
			cmd.cmd(state.storage[cmd.other.symbol].value)
		elif type(cmd.other) == value_token:
			cmd.cmd(cmd.other.value)



	#needs top happen after all code, except when jumping
	new_state.execute_cmd_n += 1

	if (type(cmd) == jump_command):
		new_state.execute_cmd_n = cmd.cmd(cmd.label.symbol, state.label_booklet)
	elif (type(cmd) == flag_jump_command):
		new_state.execute_cmd_n = cmd.cmd(cmd.label.symbol, state.label_booklet, state.storage['bool flag'], new_state.execute_cmd_n)
	return new_state

# execute_program :: [command] -> program_state -> program_state
def execute_program(commands : List[command], state : program_state):
	if (state.execute_cmd_n >= len(commands)):
		return state

	new_state = execute_command(commands[state.execute_cmd_n], state)

	return execute_program(commands, new_state)


