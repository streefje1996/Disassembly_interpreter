from typing import List
from typing import Callable
from storage import *
from typing import Union
from typing import Dict
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

class label_place(command):
	def __init__(self, line_number, label : label_token):
		command.__init__(self, line_number, None)
		self.label = label

class jump_command(command):
	def __init__(self, line_number : int, func : Callable[[str, Dict[str, int]], Union[int, error]], label : label_token):
		command.__init__(self, line_number, func)
		self.label = label

# build_command :: int -> [token] -> command + error
def build_command(line_number : int, tokens: List[token]) -> Union[command, error]:
	a, b, *tail = tokens

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
	elif (type(a) == label_token):
		return label_place(line_number, a)

	elif (type(a) == flow_token):
		if (a.symbol == 'JUMP'):
			return jump_command(line_number, jump, b)

