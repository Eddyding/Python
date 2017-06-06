# _*_ coding:utf-8 _*_

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


import os
disk = os.statvfs("/")
freespace = disk.f_bsize * f_blocks;

'''



#png_files = glob.glob("*.png")





