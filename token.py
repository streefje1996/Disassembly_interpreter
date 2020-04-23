class token(object):
	"""an token object"""

	def __init__(self, type : str, value = None):
		self.type = type
		self.value = value

	def __str__(self):
		if self.value != none:
			return "token type: " + self.type + " with value: " + self.value
		return "token type: " + self.type


operator_tokens = (
	'ASSIGN',
	'PLUS',
	'MINUS',
	'MULTIPLY',
	'DIVIDE'	
	)

storage_tokens = (
	'STACK_STORE',
	'STACK_GET',
	'QUEUE_STORE',
	'QUEUE_GET',
	'REG0',
	'REG1',
	'REG2',
	'REG3',
	'REG4',
	'REG5',
	'REG6',
	'REG7',
	'REG8',
	'REG9'
	)
