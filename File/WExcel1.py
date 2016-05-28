# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd

Fname = u"百度热词.xls"
def open_excel(file= Fname):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)


def excel_table_byindex(file=Fname,colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    print "nrows: ",nrows," ncols:",ncols
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):

         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                print "row[i]: ", row[i]
                app[colnames[i]] = row[i] 
             list.append(app)
    return list


def main(): 

   tables = excel_table_byindex()
   for row in tables:
       print  row[U"资源名称"] 

if __name__=="__main__":
    main()