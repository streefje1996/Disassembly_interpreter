from typing import List
from typing import Callable
from storage import *
from typing import Union
from typing import Dict
from typing import Tuple
from token import *
from error import *

#operators
#=================================================================
# add :: register -> register + int -> register
def add(lhs : register, rhs : Union[register, int]):
	if type(rhs) == register:
		return register(lhs.name, lhs.value + rhs.value)
	return register (lhs.name, lhs.value + rhs)

# subtract :: register -> register + int -> register
def subtract(lhs : register, rhs : Union[register, int]):
	if type(rhs) == register:
		return register(lhs.name, lhs.value - rhs.value)
	return register (lhs.name, lhs.value - rhs)

# multiply :: register -> register + int -> register
def multiply(lhs : register, rhs : Union[register, int]):
	if type(rhs) == register:
		return register(lhs.name, lhs.value * rhs.value)
	return register (lhs.name, lhs.value * rhs)

# divide :: register -> register + int -> register
def divide(lhs : register, rhs : Union[register, int]):
	if type(rhs) == register:
		return register(lhs.name, int(lhs.value / rhs.value))
	return register (lhs.name, int(lhs.value / rhs))

# assign :: register -> register + int -> register
def assign(lhs : register, rhs : Union[register, int]):
	if type(rhs) == register:
		return register(lhs.name, rhs.value)
	return register (lhs.name, rhs)

#compare
#=================================================================
# equals :: register + int -> register + int -> bool
def equals(lhs : Union[register, int], rhs : Union[register, int]) -> bool:
	if type(lhs) == register:
		if type(rhs) == register:
			return lhs.value == rhs.value
		return lhs.value == rhs
	if type(rhs) == register:
		return lhs == rhs.value
	return lhs == rhs

# not_equals :: register + int -> register + int -> bool
def not_equals(lhs : Union[register, int], rhs : Union[register, int]) -> bool:
	if type(lhs) == register:
		if type(rhs) == register:
			return lhs.value != rhs.value
		return lhs.value != rhs
	if type(rhs) == register:
		return lhs != rhs.value
	print (lhs != rhs)
	return lhs != rhs

# bigger :: register + int -> register + int -> bool
def bigger(lhs : Union[register, int], rhs : Union[register, int]) -> bool:
	if type(lhs) == register:
		if type(rhs) == register:
			print(lhs.value > rhs.value)
			return lhs.value > rhs.value
		return lhs.value > rhs
	if type(rhs) == register:
		return lhs > rhs.value
	return lhs > rhs

# smaller :: register + int -> register + int -> bool
def smaller(lhs : Union[register, int], rhs : Union[register, int]) -> bool:
	if type(lhs) == register:
		if type(rhs) == register:
			return lhs.value < rhs.value
		return lhs.value < rhs
	if type(rhs) == register:
		return lhs < rhs.value
	return lhs < rhs


#special
#=================================================================
# store :: [int] -> register + int -> [int]
def store(storable : List[int], other : Union[register, int]) -> List[int]:
	if (len(storable) == 0):
		if type(other) == register:
			return [other.value]
		return [other]

	head, *tail = storable
	return [head] + store(tail, other)

# pop_stack :: [int] -> register -> ([int], register)
def pop_stack(stack : List[int], reg : register) -> Tuple[List[int],register]:
	if len(stack) == 0:
		return ([], register(reg.name, reg.value))
	if len(stack) == 1:
		return ([], register(reg.name, stack[0]))

	head, *tail = stack
	new_stack = pop_stack(tail,reg)
	return ([head] + new_stack[0], new_stack[1])

# pop_queue :: [int] -> register -> ([int], register)
def pop_queue(queue : List[int], reg : register) -> Tuple[List[int],register]:
	if (len(queue) == 0):
		return ([], register(reg.name,reg.value))
	if (len(queue) == 1):
		return ([], register(reg.name,queue[0]))
	if (len(queue) == 2):
		return ([queue[1]], register(reg.name,queue[0]))

	head, *tail = queue
	new_queue = pop_queue(tail, reg)
	return ([new_queue[1].value] + new_queue[0], register(new_queue[1].name,head))


def print_stack(stack : Union[int, List[int]]) -> List[int]:
	if len(stack) == 0:
		return []
	result = pop_stack(stack, register('nameless',0))
	print(result[1].value)
	return print_stack(result[0])

def print_queue(queue : Union[int, List[int]]) -> List[int]:
	if len(queue) == 0:
		return []
	result = pop_queue(queue, register('nameless',0))
	print(result[1].value)
	return print_queue(result[0])

def print_value(value : Union[int, List[int]]) -> List[int]:
	print(value)
	return []

				

#flow
#=================================================================
# jump :: str -> dict -> int + error
def jump(label : str, label_booklet : Dict[str, int]) -> Union[int, error]:
	if label in label_booklet:
		return label_booklet[label]
	return error(error_symbols.Invalid_label)

def jump_true(label : str, label_booklet : Dict[str, int], flag : bool, current : int) -> Union[int, error]:
	if flag == True:
		if label in label_booklet:
			return label_booklet[label]
		return error(error_symbols.Invalid_label)
	return current

def jump_false(label : str, label_booklet : Dict[str, int], flag : bool, current : int) -> Union[int, error]:
	if flag == False:
		if label in label_booklet:
			return label_booklet[label]
		return error(error_symbols.Invalid_label)
	return current