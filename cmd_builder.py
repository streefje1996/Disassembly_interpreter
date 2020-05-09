from typing import List
from typing import Callable
from storage import *
from typing import Union
from typing import Dict
from typing import Tuple
from token import *
from functions import *
from error import *

class command:
	def __init__(self, line_number: int, func : Callable):
		self.ln = line_number
		self.cmd = func

class operator_command(command):
	def __init__(self, line_number: int, func: Callable[[register, Union[register, int]], register], reg_name: storage_token, other: Union[storage_token, value_token]):
		command.__init__(self, line_number, func)		
		self.reg_name = reg_name
		self.other = other

class compare_command(command):
	def __init__(self, line_number: int, func : Callable[[Union[register, int], Union[register, int]],bool], lhs : Union[storage_token, value_token], rhs : Union[storage_token, value_token]):
		command.__init__(self, line_number, func)
		self.lhs = lhs
		self.rhs = rhs

class label_place(command):
	def __init__(self, line_number, label : label_token):
		command.__init__(self, line_number, None)
		self.label = label

class jump_command(command):
	def __init__(self, line_number : int, func : Callable[[str, Dict[str, int]], Union[int, error]], label : label_token):
		command.__init__(self, line_number, func)
		self.label = label

class flag_jump_command(command):
	def __init__(self, line_number : int, func : Callable[[str, Dict[str, int], bool, int], Union[int, error]], label : label_token):
		command.__init__(self, line_number, func)
		self.label = label

class store_command(command):
	def __init__(self, line_number : int, func : Callable[[List[int], Union[register,int]], List[int]], storage_name : str,  other: Union[storage_token, value_token]):
		command.__init__(self, line_number, func)
		self.storage_name = storage_name
		self.other = other

class print_command(command):
	def __init__(self, line_number : int, func : Callable[ [Union[ int, List[ int ]]], List[int]], other : Union[storage_token, value_token, command_token]):
		command.__init__(self, line_number, func)
		self.other = other

class get_command(command):
	def __init__(self, line_number : int, func : Callable[[List[int], register], Tuple[List[int],register]], storage_name : str,  reg_token: storage_token):
		command.__init__(self, line_number, func)
		self.storage_name = storage_name
		self.reg_token = reg_token

# build_command :: int -> [token] -> command + error
def build_command(line_number : int, tokens: List[token]) -> Union[command, error]:
	a, b, *tail = tokens

	#operators
	if (type(a) == storage_token):
		if (type(tail[0]) in (storage_token,value_token)):		
			if(b.symbol == 'PLUS'):
				return operator_command(line_number, add, a, tail[0])
			elif(b.symbol == 'MINUS'):
				return operator_command(line_number, subtract, a, tail[0])
			elif(b.symbol == 'MULTIPLY'):
				return operator_command(line_number, multiply, a, tail[0])
			elif(b.symbol == 'DIVIDE'):
				return operator_command(line_number, divide, a, tail[0])
			elif(b.symbol == 'ASSIGN'):
				return operator_command(line_number, assign, a, tail[0])


	if (type(a) in (storage_token, value_token)):
		if (type(tail[0]) in (storage_token,value_token)):
			if(b.symbol == 'EQUAL'):
				return compare_command(line_number, equals, a, tail[0])
			elif(b.symbol == 'NOT_EQUAL'):
				return compare_command(line_number, not_equals, a, tail[0])
			elif(b.symbol == 'BIGGER'):
				return compare_command(line_number, bigger, a, tail[0])
			elif(b.symbol == 'SMALLER'):
				return compare_command(line_number, smaller, a, tail[0])


	if (type(a) == command_token):
		if a.symbol == 'QUEUE_STORE':
			return store_command(line_number, store, 'queue', b)
		if a.symbol == 'STACK_STORE':
			return store_command(line_number, store, 'stack', b)
		if a.symbol == 'QUEUE_GET':
			return get_command(line_number, pop_queue, 'queue', b)
		if a.symbol == 'STACK_GET':
			return get_command(line_number, pop_stack, 'stack', b)
		if a.symbol == 'PRINT':
			if b.symbol == 'STACK':
				return print_command(line_number, print_stack, b)
			elif b.symbol == 'QUEUE':
				return print_command(line_number, print_queue, b)
			elif type(b) == storage_token:
				return print_command(line_number, print_value, b)
			elif type(b) == value_token:
				return print_command(line_number, print_value, b)


	if (type(a) == label_token):
		return label_place(line_number, a)

	if (type(a) == flow_token):
		if (a.symbol == 'JUMP'):
			return jump_command(line_number, jump, b)
		elif (a.symbol == 'JUMP_TRUE'):
			return flag_jump_command(line_number, jump_true, b)
		elif (a.symbol == 'JUMP_FALSE'):
			return flag_jump_command(line_number, jump_false, b)

