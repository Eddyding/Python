#!/usr/bin/env python
# _*_ coding: UTF-8 _*_


#Python 3


def draw(n,symbol="*"):
    for i in range(1,n+1):
        print(symbol,end="") #在print 后面加上end="" or “,” ,目的是为了不让print换行
    print() #   # line feed
