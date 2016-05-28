#-*- coding:utf-8 -*-

hello = 'hello, I`am a beautiful girl'
print hello[0], hello[-1]

Year=raw_input("Year: ")[3]
print "Year is ",Year



def printMonth():
	months=['January','February','March','April','May','June','July','Agust','September','October','November','December']


	Year_name = raw_input("Year_name: ")
	Month_name = raw_input("Month_name: ")
	Day_name = raw_input("Day_name: ")

	Month_name = int(Month_name)
	Day_name = int(Day_name)

	Month_name = months[Month_name-1]
	print "Month_name , Day_name,Year_name :",Month_name , Day_name,Year_name

printMonth()