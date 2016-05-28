#-*- coding:utf-8 -*-

def safe_float(obj):
	try:
		ft=float(obj)
	except Exception, e:
		raise e

obj = input("input charge word: ")
print safe_float(obj)
