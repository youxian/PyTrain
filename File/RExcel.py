#-*- coding: utf8 -*-

import xlrd

fname = u"百度热词.xls"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name("Sheet1")
except:
    print "no sheet in %s named Sheet1" % fname
#获取行数
nrows = sh.nrows
print type(nrows)
#获取列数
ncols = sh.ncols
print "nrows %d, ncols %d" % (nrows,ncols)


for i in nrows:
	for j in ncols:
		print sh.cell_value(i,j)
#获取第一行第一列数据 
cell_value = sh.cell_value(1,1)
print "cell_value:",cell_value

# row_list = []
# #获取各行数据
# for i in range(1,nrows):
#     row_data = sh.row_values(i)
#     print unicode(row_data)
#     row_list.append(row_data)

