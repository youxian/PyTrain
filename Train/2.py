#-*- coding:utf-8 -*-
import random
import sys
sys.path.append('D:/PyWorkSpace/Train')   
import sumN



print u"输入一个数字"
n=input()
tag = random.randint(0,1)
print u"求和: ",sumN.sumN(n)
print u"求和: ",sumN.sumN1(n)
# if(tag==0):
# 	print "求和: ",sumN.sumN(n)
# 	print "求和: ",sumN.sumN1(n)
# else:
# 	print "pluse"