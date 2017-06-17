#!/usr/bin/env python
# _*_ coding: UTF-8 _*_




#Python 3

import re



'''

 if :
 elif :
 else:
 
'''



a,b = 4,8
max_number = a
if b > a: max_number = b
print(max_number)


max_number2 = a if a > b else b
print(max_number2)




import random
x = random.randint(1,6)  #[1..6]
print(x)

while x != 6:
    x = random.randint(1,6)
    print(x)


alist = [1,3,5,8,10]
for  x in alist:
    print(x,end="")


print()
stock={'book':10,'pen':3,'eraser':6,'ruler':2}
for key,value in stock.items():
    if value < 5:
        print("({},{})".format(key,value))



for i in range(2,7,4):
    for j in range(1,10):  #{:>2} 右对齐，占2位
        print("{}*{}={:>2}   ".format(i,j,i*j),end="")
        print("{}*{}={:>2}   ".format(i+1,j,(i+1)*j),end="")
        print("{}*{}={:>2}   ".format(i+2,j,(i+2)*j),end="")
        print("{}*{}={:>2}   ".format(i+3,j,(i+3)*j))
    print()




print('xxxxxxxxx')

for i in range(2,7,4):
    for j in range(1,10):  #{:>2} 右对齐，占2位
        for k in range(i,i+4):
            print("{}*{}={:>2}   ".format(k,j,k*j),end="")
        print()
    print()



