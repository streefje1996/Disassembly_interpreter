from typing import Dict

#holds the current state of the program
class program_state:
	def __init__(self, storage : dict, execute_cmd_n : int, label_booklet : dict) :
		self.storage = storage
		self.execute_cmd_n = execute_cmd_n
		self.label_booklet = label_booklet