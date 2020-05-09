from typing import Dict

#holds the current state of the program
class program_state:
	def __init__(self, storage : dict, execute_cmd_n : int, label_booklet : dict) :
		self.storage = storage
		self.execute_cmd_n = execute_cmd_n
		self.label_booklet = label_booklet

	def __str__(self):
		string = 'state: \n'
		#storage
		string += 'storage: \n '
		string += 'stack: ' + str(self.storage['stack']) + ' \n '
		string += 'queue: ' + str(self.storage['queue']) + ' \n '
		string += 'REG0: ' + str(self.storage['REG0']) + '\n '
		string += 'REG1: ' + str(self.storage['REG1']) + '\n '
		string += 'REG2: ' + str(self.storage['REG2']) + '\n '
		string += 'REG3: ' + str(self.storage['REG3']) + '\n '
		string += 'REG4: ' + str(self.storage['REG4']) + '\n '
		string += 'REG5: ' + str(self.storage['REG5']) + '\n '
		string += 'REG6: ' + str(self.storage['REG6']) + '\n '
		string += 'REG7: ' + str(self.storage['REG7']) + '\n '
		string += 'REG8: ' + str(self.storage['REG8']) + '\n '
		string += 'REG9: ' + str(self.storage['REG9']) + '\n '
		string += 'flag: ' + str(self.storage['bool flag']) + ' \n'
		#execute cmd
		string += 'next command #: ' + str(self.execute_cmd_n + 1) 

		return string

	def __repr__(self):
		return self.__str__()