from token import *
from typing import List
from typing import Callable
from typing import Dict
from storage import *
from typing import Union
from cmd_builder import build_command
from cmd_builder import *

# where_is_new_line :: [token] -> int
def where_is_new_line(tokens : List[token]) -> int:
	if (tokens[0].symbol == 'NEW_LINE' or len(tokens) == 1):
		return 1
	head, *tail = tokens
	return where_is_new_line(tail) + 1

# parse :: [token] -> [command]
def parse(tokens: List[token], line_number : int = 1) -> List[command]:
	if (len(tokens) == 0):
		return []
	here_is_new_line = where_is_new_line(tokens)
	cmd = build_command(line_number, tokens[:here_is_new_line])
	return [cmd] + parse(tokens[here_is_new_line:], line_number+1)

# get_labels :: [commands] -> dict
def get_labels(commands : List[command]) -> Dict[str, int]:
	if len(commands) == 0:
		return dict()

	head, *tail = commands

	result = get_labels(tail)

	if (type(head) == label_place):
		result[head.label.symbol] = head.ln - 1

	return result

