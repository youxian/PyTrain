#-*- coding:utf-8 -*-
 
obj =  input("input charge word: ")
try:
	ft = float(obj)
	print ft
except ValueError:
	ft = "not convert string to float"
	print ft
except TypeError:
	ft = "argument must be a string or a number"
	print ft
except NameError:
	ft = " obj is not defined"
	print ft
except SyntaxError:
	ft =  "invalid syntax"
	print ft
 


