#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

#Python 3

'''
os.system or shutil
os.system(cmd) # 交由os执行.

cmd: 可以执行os命令的字符串
比如: ls -al 


如果需要命令执行的输出结果,使用 commands模块 
'''

import os

os.system("ls -al .")
os.system("cp file2.py file3.py")
os.system("cat ossystemme.py")

os.system("clear")
