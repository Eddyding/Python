#!/usr/bin/env  python

p = (4,5)
x,y = p
print (x,y)

data = ['ACME', 50, 91.1,(2012,12,21)]
name, shares, price, date = data
print (name, shares ,price, date)

name, shares, price,(year,mon,day) = data
print (name, shares ,price, day ,mon, year)


p = (4,5)
# x,y,z = p # ValueError: need more than 2 values to unpack

s = 'Hello'
a, b, c, d, e = s
print (a, b, c, d, e)

# comment not support chinese 
_, shares, price, _ = data
print (shares, price)

# *

def drop_first_last(grades):
    first,*middle, last = grades
    return avg(middle)

grades = [12, 33, 33, 44]
var = drop_first_last(grades)
print (var)






