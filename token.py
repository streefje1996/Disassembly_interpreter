class token:
	"""an token object"""
	def __init__(self, symbol : str):
		self.symbol = symbol


	def __str__(self):
		return "token symbol: " + self.symbol

class value_token(token):
	def __init__(self, symbol : str, value):
		token.__init__(self, symbol)
		self.value = value

	def __str__(self):
		return "token symbol: " + self.symbol + " with value: " + str(self.value)

class operator_token(token):
	def __init__(self, symbol):
		token.__init__(self,symbol)

class storage_token(token):
	def __init__(self, symbol):
		token.__init__(self,symbol)

class flow_token(token):
	def __init__(self, symbol):
		token.__init__(self,symbol)

class label_token(token):
	def __init__(self, symbol):
		token.__init__(self,symbol)

operator_tokens = {
	'=': 'ASSIGN',
	'+': 'PLUS',
	'-': 'MINUS',
	'*': 'MULTIPLY',
	'/': 'DIVIDE'
	}

storage_tokens = {
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
	'reg.9': 'REG9'
	}

flow_tokens = {
	'/n' : 'NEW_LINE',
	'jmp' : 'JUMP',
	'jmpt' : 'JUMP_TRUE',
	'jmpf' : 'JUMP_FAlSE'
	}
