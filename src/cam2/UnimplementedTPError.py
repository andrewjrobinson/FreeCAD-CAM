'''
Created on 02/10/2012

@author: arobinson
'''
from TPError import TPError

class UnimplementedTPError(TPError):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return "Unimplemented Tool Path Runner: '%s'" % self.name
	
	