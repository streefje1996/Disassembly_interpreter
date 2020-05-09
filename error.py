from enum import Enum

#error types
error_symbols = Enum('error_symbols' ,'Invalid_token Invalid_command Unknown Invalid_label')

#class for holding errors
class error:
	def __init__(self, symbol : error_symbols, info : str = None):
		self.symbol = symbol
		self.info = info

	def __str__(self):		
		if (self.info != None):
			return str(self.symbol) + ': ' + self.info
		return str(self.symbol)

	def __repr__(self):
		return self.__str__()

