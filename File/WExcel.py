#-*- coding: utf8 -*-

import xlrd
from pyExcelerator import *

w= Workbook()
ws=w.add_sheet("hey,hand")
i = 0
j = 0
while i<2:
	i=i+1
	ws.write(i,1,"bit") 
w.save("2.xls")
