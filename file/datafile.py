#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

#Python 3

'''
fp = open("文件名",”文件打开模式“)

文件打开模式: r,w ,a

在大部分的应用中，都是以文本文件的方式来存取文件的内容，也就是说，以 字符串的类型来  查看文件的内容。


read()  : 一次性把 所有内容 以字符串的形式读入变量中。
readline(): 一次只读取文件的一行内容。
readlines(): 把每一行拆开 放在每一个不同的字符串变量中，并以列表的方式汇集在一起。


'''


import this  # build-in

print("------------")
fp = open("zop.txt","r")

zops = fp.readlines()

fp.close()


i =1
print("The zen of python")
for zen in zops:
    print("Zen {}:{}".format(i,zen),end="")
    i +=1
