#-*- coding:utf-8  -*-

class EqualToZero(Exception): pass

class SplitZero(object):
	
	"""docstring for ClassName"""
	def splitzero(self, num):
		if num>0:
			return "num is bigger than zero"
		elif num<0:
			return "num is smaller than zero"
		else:
			raise EqualToZero

