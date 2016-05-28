#-*- coding: utf-8 -*-


# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（所谓嵌套）。
# 列表用[ ]标识。是python最通用的复合数据类型。看这段代码就明白。
# 列表中的值得分割也可以用到变量[头下标:尾下标]，就可以截取相应的列表，从左到右索引默认0开始的，从右到左索引默认-1开始，下标可以为空表示取到头或尾。
# 加号（+）是列表连接运算符，星号（*）是重复操作

numlist = ['a123',456,'sdc','cyt','@#&^%']
tinylist = [123,'helen']
print numlist,tinylist

numlist[0]="zbf"
print numlist
for i in numlist:
	print i  
print numlist[1:3]
print tinylist*2
print numlist+tinylist