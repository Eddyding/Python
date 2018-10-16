# _*_ coding:utf-8 _*_


'''
 Python will default to ASCII as standard encoding if no other encoding hints are given.
 
 Python Enhancement Proposals (PEPs)
 
 The PSF: Python Software Foundation

 The Python Software Foundation is the organization behind Python.
 
 Become a member of the PSF and help advance the software and our mission.
 
 # _*_ coding:utf-8 _*_

1.必须将编码注释放在第一行或者第二行

2.可选格式有

# coding=<encoding name>  

or

#!/usr/bin/python
# -*- coding: <encoding name> -*-


or
#!/usr/bin/python
# vim: set fileencoding=<encoding name> :


但是再往下看，发现其实只要注释里面有coding 和对应的编码就可以了，例如

#!/usr/bin/python
# vim: set fileencoding=<encoding name> :

\%^.*\n.∗\?#.*coding[:=]\s*[0-9A-Za-z-_.]\+.*$  


但是大致如下必须有coding:[编码]或者coding=[编码]才行，这个应该可以视作为标准的声明方式吧。

# -*- coding:utf-8 -*-
如果要在python2的py文件里面写中文，则必须要添加一行声明文件编码的注释，否则python2会默认使用ASCII编码。

在python中，glob模块是用来查找匹配的文件的
在查找的条件中，需要用到Unix shell中的匹配规则：

'''

import glob


import os


disk = os.statvfs("/")

totalspace = disk.f_bsize * disk.f_blocks;# byte

totalspaceinKB = disk.f_bsize * disk.f_blocks / 1024 # KB


totalspaceinMB = totalspaceinKB / 1024 # MB

totalspaceinGB = totalspaceinMB / 1024 # GB




print totalspace

print totalspaceinKB

print totalspaceinMB

print totalspaceinGB


'''
在MAC OS & LINUX 获取磁盘空间大小

os.statvfs() 方法用于返回包含文件描述符fd的文件的文件系统的信息。

import os
disk = os.statvfs("/")
freespace = disk.f_bsize * f_blocks;

获取单个文件大小：

import os
filesize = os.path.getsize(filename)

检查某个文件夹（目录）是否存在的方法：

os.path.exists(dirname)

创建文件夹的办法：
os.mkdir(dirname)


复制文件的办法：
import shutil
shutil.copyfile(src,dst)

'''
#png_files = glob.glob("*.png")





