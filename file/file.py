#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

#Python 3

import os.path

'''

os.path  glob   os.walk, os.system shutil

improt os.path

abspath    提供任何一个路径 或 文件名,会返回 完整的路径名称
basename   返回路径名称的最后一个文件名  或 目录名称
dirname    返回指定路径名称的上层完整路径名称

exists   检查某一指定的路径 或文件是否存在
getsize  返回指定文件的文件大小(byte)
isabs   检查指定的路径是否为完整路径名称(绝对路径)
isfile  检查指定的路径是否为文件
isdir 检查指定的路径是否为目录
split 把绝对路径的文件 和 上层路径分开(取出文件名)
splitdrive  把绝对路径的磁盘驱动器 和 下层路径分开(取出磁盘驱动器)

join  把路径和文件名正确的结合成完整路径



__file__


glob: 用来处理文件列表非常好用的外部模块.


import glob
glob.glob("路径名称") :获取一个文件列表,可以使用通配符*


'''
a = os.path.abspath("file.py")
print(a)

a = os.path.basename("file.py")
print(a)	

a = os.path.dirname("file.py")
print(os.path.dirname("file.py"))



a = os.path.basename("jj")
print(a)

a = os.path.abspath(".")
print(a)

a = os.path.basename(".")
print(a)
a = os.path.dirname(".")
print(a)

a = os.path.split("file.py")
print(a)

a = os.path.splitdrive("file.py")
print(a)


a = os.path.abspath(__file__)
print(a)



import glob

files= glob.glob("*.py")
for f in files:
	print(f)




