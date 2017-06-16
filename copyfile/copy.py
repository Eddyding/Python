#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
# MAC OS,



'''

Python是解释型语言,翻译一行,就执行一行;因此

在程序运行过程中,只要任何一行出现错误,程序就会立刻显示错误信息并停止运行.
这种方式虽然在调试上比较低效,(因为一次只会发生一个错误)
但是却很容易知道错误发生的原因 以及位置.


==  or  ===

' '   or "   " 




 '''
import os,shutil,glob

source_dir = "images/"  #

disk = os.statvfs("/")
freespace =disk.f_bsize * disk.f_blocks;

pngfiles = glob.glob(source_dir + "*.png")
jpgfiles = glob.glob(source_dir + "*.jpg")
giffiles = glob.glob(source_dir + "*.gif")

allfiles = pngfiles + jpgfiles + giffiles

allfilessize = 0

for f in allfiles:
	allfilessize += os.path.getsize(f) 

if  allfilessize > freespace:
	print("磁盘空间不足")
	exit(1)

target_dir = source_dir + "output"

if os.path.exists(target_dir):
	print("目标文件夹已经存在")
	exit(1)

os.mkdir(target_dir)
imageno=0

for f in allfiles:
	dirname,filename = f.split('/')
	mainname,extname = filename.split('.')
	targetfile = target_dir + '/' + str(imageno) + '.'+ extname
	shutil.copyfile(f,targetfile)
	imageno +=1


