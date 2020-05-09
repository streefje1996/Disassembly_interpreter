from token import *
from error import *
from typing import List
from typing import Union
from typing import Callable

# is_number :: str -> bool
def is_number(char : str) -> bool:
	return char in '-0987654321'

# get_token :: string -> token + error
def get_token(command : str) -> Union[token, error]:
	#operators
	if command in operator_tokens:
		return operator_token(operator_tokens[command])
	#compare
	elif command in compare_tokens:
		return compare_token(compare_tokens[command])
	#storage
	elif command in storage_tokens:
		return storage_token(storage_tokens[command])
	#commands
	elif command in command_tokens:
		return command_token(command_tokens[command])
	#flow
	elif command in flow_tokens:
		return flow_token(flow_tokens[command])
	#value
	elif all(map(is_number, command)):
		return value_token('VALUE', int(command))
	#label definition
	elif command[-1] == ':' and (not any(map(is_number, command))):
		return label_token(command[:-1])
	#label
	elif (not any(map(str.isdigit, command))):
		return label_token(command)

	#error
	return error(error_symbols.Invalid_token, command + ' is an invalid command')

# print_tokens :: callable -> callable
def print_tokens(func : Callable) -> Callable:
	def inner(cmd):
		result = func(cmd)
		print(result[0])
		return result
	return inner

# generate_tokens :: [string] -> [token + error]
@print_tokens
def generate_tokens(command : List[str]) -> List[Union[token, error]]:
	if (len(command) == 1):
		return [get_token(command[0])]
	head, *tail = command
	return [get_token(head)] + generate_tokens(tail)

