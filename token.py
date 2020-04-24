class token:
	"""an token object"""

	def __init__(self, type : str, value = None):
		self.type = type
		self.value = value

	def __str__(self):
		if self.value != none:
			return "token type: " + self.type + " with value: " + self.value
		return "token type: " + self.type


tokens = {
	#operators
	'=': 'ASSIGN',
	'+': 'PLUS',
	'-': 'MINUS',
	'*': 'MULTIPLY',
	'/': 'DIVIDE',
	#storage
	'stack.store': 'STACK_STORE',
	'stack.get': 'STACK_GET',
	'queue.store': 'QUEUE_STORE',
	'queue.get': 'QUEUE_GET',
	'reg.0': 'REG0',
	'reg.1': 'REG1',
	'reg.2': 'REG2',
	'reg.3': 'REG3',
	'reg.4': 'REG4',
	'reg.5': 'REG5',
	'reg.6': 'REG6',
	'reg.7': 'REG7',
	'reg.8': 'REG8',
	'reg.9': 'REG9',
	#flow
	'/n' : 'NEW_LINE'
	}
