from token import *
from error import *
from typing import List
from typing import Union


# get_token :: string -> token + error
def get_token(command : str) -> Union[token, error]:
	#operators
	if command in operator_tokens:
		return operator_token(operator_tokens[command])
	#storage
	elif command in storage_tokens:
		return storage_token(storage_tokens[command])
	#flow
	elif command in flow_tokens:
		return flow_token(flow_tokens[command])
	#value
	elif all(map(str.isdigit, command)):
		return value_token('VALUE', int(command))
	#label definition
	elif command[-1] == ':' and (not any(map(str.isdigit, command))):
		return label_token(command[:-1])
	#label
	elif (not any(map(str.isdigit, command))):
		return label_token(command)

	#error
	return error(error_symbols.Invalid_token, command + ' is an invalid command')



# generate_tokens :: [string] -> [token + error]
def generate_tokens(command : List[str]) -> List[Union[token, error]]:
	if (len(command) == 1):
		return [get_token(command[0])]
	head, *tail = command
	return [get_token(head)] + generate_tokens(tail)