#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

#Python 3

'''
'''


print("------------")

zops=[]

with open("zop.txt","r") as fp:
	zops = fp.readlines()  #with自动帮我们关闭文件

i =1
print("The zen of python")
for zen in zops:
    print("Zen {}:{}".format(i,zen),end="")
    i +=1
