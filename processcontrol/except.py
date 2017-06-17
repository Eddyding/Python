#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

#Python 3

# TypeError: unorderable types: str() < int()
age=int(input("What is your age?"))
if age < 15:
	print("Too Young")



'''

try:

except:






删除某一指定的文件名
import os
os.remove('filename')





import os
try:
os.remove('filename')
except:
	print("无法删除指定文件")





import os
try:
os.remove('filename')
except FileNotFoundError:
	print("无法删除指定文件:找不到文件")
except PermissionError:
	print("无法删除指定文件:文件权限或种类错误")
except :
	print("无法删除指定文件:未知错误")




'''
while True:
	try:
		age = int(input("What is your age?"))
		break
	except:
		print("Please input a number")

if age < 15:
	print("Too Young")


# fp = open("Hell.txt","r")

import os,sys

import os
try:
	os.remove('Hello.txt')
except FileNotFoundError:
	print("无法删除指定文件:找不到文件")
except PermissionError:
	print("无法删除指定文件:文件权限或种类错误")
except :
	print("无法删除指定文件:未知错误")

