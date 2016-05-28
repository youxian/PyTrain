#-*- coding:utf-8 -*-

numbers = [1,2,2,1,2]

length = len(numbers)
sum=0
for num in numbers:
	sum=sum+num
 
for  index  in range(length):
	formal = 0
	after = 0
	i=0
	for i in range(index):
		formal += numbers[i-1]  
	after=sum-formal - numbers[index]
	if formal == after:
		print index, numbers[ :index], numbers[index+1:]
		break


for  index  in range(length):
	print index, numbers[index]

