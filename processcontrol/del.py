#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

#Python 3

import os,sys


try:
	os.remove('Hello.txt')
except Exception as e:  # 通过Exception 捕捉所有例外
	print(e)

	e_type,e_value,e_tb = sys.exc_info()
	print("种类: {}\n消息: {}\n信息: {}".format(e_type,e_value,e_tb))
