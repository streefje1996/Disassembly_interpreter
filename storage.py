class register:
	def __init__(self, register_name, value):
		self.name = register_name
		self.value = value

storage = {
	#user vars
	'stack'			: [None] * 100,
	'queue'			: [None] * 100,
	'REG0'			: register('REG0', 0),
	'REG1'			: register('REG1', 0),
	'REG2'			: register('REG2', 0),
	'REG3'			: register('REG3', 0),
	'REG4'			: register('REG4', 0),
	'REG5'			: register('REG5', 0),
	'REG6'			: register('REG6', 0),
	'REG7'			: register('REG7', 0),
	'REG8'			: register('REG8', 0),
	'REG9'			: register('REG9', 0),
	#not user vars
	'bool flag'		: bool,
	'jump stack'	: [None] * 100
	}

