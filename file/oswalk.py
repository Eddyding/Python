#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

#Python 3

'''

如果要能够把指定的文件夹中所有的文件名以及所属的子文件夹中所有的文件也全部都找出来,用os.walk


os.walk:

返回一个由3个元素的tuple所组成的列表:

tuple(文件夹名称,下一层文件夹列表,本文件夹内所有的文件列表)



os.system or shutil
os.system(cmd) # 交由os执行.

cmd: 可以执行os命令的字符串
比如: ls -al 

'''

import os
sam= os.walk(".")

for dirname,subdir,files in sam:
	print(dirname)
	print(subdir)
	print(files)

sam= os.walk(".")
for dirname,subdir,files in sam:
	for filename in files:
		print(os.path.abspath(filename))
