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

import commands


os.system("ls -al .")
os.system("cp file2.py file3.py")
os.system("cat ossystemme.py")

#os.system("clear")

print(commands.getstatusoutput("ls -al ."))


'''
    
shutil :高级的目录和文件操作模块

copyfile(s,d)  把文件s 复制为 文件d(仅复制文件内容，不含属性)
copy(s,d)   把文件s 复制为 文件d(含文件的权限属性)

copy2(s,d)  把文件s 复制为 文件d(含所有的文件属性)
copytree(s,d)  把整个目录s(包含里面所有的内容)复制一份到d
rmtree(p)   删除p这个目录以及里面所有的内容
move(s,d)  把s这个目录或 文件  搬移 到 d


删除文件：os.remove(file) 

删除一个空目录： os.rmdir(dir)

'''
