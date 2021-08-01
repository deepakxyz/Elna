import click 
import os
from el.core.levels import Level


'''
Test Commands
el create-shot 
'''
class CreateShot():

	@classmethod
	def check(cls):
		if Level.check():
			return True
		else:
			return False

	@classmethod
	def create_shot(cls):
		pass