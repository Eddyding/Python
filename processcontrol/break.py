#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

#Python 3
for i in range(2,9):
	if i != 2 and i != 6:continue
	for j in range(1,10):
		for k in range(i,i+4):
			print("{}*{}={:>2}   ".format(k,j,k*j),end="")
		print()
	print()	




import random
while True:
	x = random.randint(1,6)
	print(x)
	if x == 6: break



names=['Tom','Richard','Jane','Mary','John']
for i,name in enumerate(names):
	print("No.{}:{}".format(i,name))



'''
Iterator: 

map:
map(执行用的函数,容器变量)
函数会把每一个在容器变量中的元素都读取出来,放到执行用的
函数中当作参数 ,再把返回值合并到一个容器变量中.


filter:
filter(执行用的函数,容器变量)
函数会把每一个元素逐一取出来,交由第一个参数中所指定的函数计算,
再根据结果是True or False来决定次元素要不要留下来.

'''

def pick(x):
	fruits = ['Apple','Banana',"Orange",'cherry',"Pine Apple",'berry']
	return fruits[x]


alist = [1,4,2,5,0,3,4,4,2]
choices = map(pick,alist)
for choice in choices:
	print(choice)




