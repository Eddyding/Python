#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

#Python 3

import sys


#程序执行时,命令行参数可以在程序中使用sys.argv来取得

print("参数长度={}".format(len(sys.argv)))
i=0
for arg in sys.argv:
	print("第{}个参数是{}".format(i,arg))
	i +=1
