#!/usr/bin/env python
# _*_ coding: UTF-8 _*_


#Python 3


def add2number(a,b):
    global d
    c = a + b
    d = a + b
    print("在函数中，(c={},d={})".format(c,d))
    return c

c = 10
d = 99
print("在函数调用前，(c={},d={})".format(c,d))
print("{}+{}={}".format(2,2,add2number(2,2)))
print("在函数调用后，(c={},d={})".format(c,d))



'''
    #lambda ： 出现一行语句，用完就丟的自定义函数的做法
    
    
    # lambda 参数1，参数2，....: 语句内容


等价于

    def fun(参数1，参数2，....):
        retun 语句内容
'''


x = range(1,10)
y = map(lambda i: i**3,x)
print(y)
for i,value in enumerate(y):
    print("{}^3={}".format(i,value))
