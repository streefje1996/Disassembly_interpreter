from typing import List
from typing import Callable
from storage import *
from typing import Union
from typing import Dict
from token import *
from error import *

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

# jump :: str -> dict -> int + error
def jump(label : str, label_booklet : Dict[str, int]) -> Union[int, error]:
	if label in label_booklet:
		return label_booklet[label]
	return error(error_symbols.Invalid_label)