from token import *
from typing import List

# get_token :: string -> token
def get_token(command : str) -> token:
	if command in tokens:
		return token(tokens[command])
	elif any(map(str.isdigit, command)):
		return token('VALUE', int(command))
	pass



# generate_tokens :: [string] -> [token]
def generate_tokens(command : List[str]) -> List[token]:
	if (len(command) == 1):
		return [get_token(command)]
	head, *tail = command
	return [get_token(head)] + generate_tokens(tail)