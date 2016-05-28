#-*- coding:utf-8 -*-

 
obj =  input("input charge word: ") 
try:
	ft = float(obj)
except (ValueError,TypeError,NameError):
	ft = "agument must be a string or a number"
	print ft

 