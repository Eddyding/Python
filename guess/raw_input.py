#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

'''
input
raw_input


python3中 raw_input() 变成了 input()

list tuple, dict set



把 一个英文句子 拆成字母(字符)所组成的列表,使用list()

list 中可以有不同的数据类型.


list lst

lst *n  

lst[n1:n2]

lst[n1:n2:k]

del lst[n1:n2]
lst[n1:n2]=n
lst[n1:n2:k] = n
len(lst) 
min(lst)
max(lst)
lst.index(n) 
lst.count(n)




'''

#raw_input = raw_input("raw_input:")
#input = input("raw_input:")


a_list = [1,3,4,5]
print(a_list)
print(type(a_list))

str_list=['P','y','t','h','o','n']
print(str_list)

str_msg= "I Love Python"
b_list = str_msg.split() # 空格作为分割符
print(b_list)

str_msg= "I Love Python"
b_list = list(str_msg)
print(b_list)



k1= ['book',10]
k2=['campus',15]
key=[k1,k2]
print(key)
print(key[1])
print(key[1][1]) #类似2维数组


print("Python" in k1)

print("book" in k1)


x=list(range(10))
print(x)
y=x[1:7]
print(y)
y=x[1:7:2]
print(y)


msg="Here is the test string"
lst=list(msg)
print(lst)
print(lst.index('e'))
print(lst.count('e'))

'''

list lst; x is list element or another list var
lst.append(x) # x 作为一个元素
lst.extend(x) # x 中所有元素,附加到列表后面,
lst.insert(n,x)  
lst.pop()  #可以加参数,指定特定的index
lst.remove(x)
lst.reverse()
lst.sort()

'''
'''
diff append & extend
'''
lsta=[1,2,3,4,5]
lstc=[1,2,3,4,5]
lstb=[6,6,6]
lsta.append(lstb)
print(lsta)
lstc.extend(lstb)
print(lstc)



lst=[0,1,2,3,4,5]

lst.append(9)
lst.append('x')
print(lst)
print(lst.pop())
print(lst)
print(lst.pop(0))
print(lst)


'''
tuple:无法修改
()




dict:{}  
var={} or var=dict()

在字典变量中,没有顺序概念

d:dict
d.clear() 
d1=d.copy()
d.get(key)
d.items()  # [(key,value),...]
d.keys()
d.update(d2)
d.values()


'''

tpl=tuple(range(10))
print(type(tpl))
print(tpl)
#print(tpl.sort())

keywords={}
keywords['book']=10
keywords['campus']=15
keywords['cook']=1
keywords['Python']=11
print(keywords)  #随机顺序
print(keywords['Python'])



week={}
week['Monday']='星期一'
week['Tuesday']='星期二'
week['Wednesday']='星期三'
week['Thursday']='星期四'
week['Friday']='星期五'
week['Saturday']='星期六'
week['Sunday']='星期天'

print(week)
print(week['Friday'])
print(week.keys())
print(week.values())

d2={}
d2['Sunday']='礼拜天'
week.update(d2)
print(week)

print(week.items())



'''
set:
dictvar = { } ---dict
setvar = {1,2,3}  or setvar=set()
dictvar2={'a':1,'b':2}

可以是不同的数据类型,没有顺序概念.同一个元素只能出现一次.
'''
dictvar = { }
dictvar2={'a':1,'b':2}
setvar = {1,2,3}
print(type(setvar))
print(type(dictvar))
print(type(dictvar2))

'''
&    |   ^
and  or  xor

'''
a={1,2,3,4,5}
b={1,3,5,7,9}
print(a & b)
print(a)
print(b)

print(a | b)
print(a ^ b)
a = [1,2,3]
b = [1,2,3]
print(a == b) #是否相等
print(a is b) #是否为同一个对象

b=a
print(a == b)
print(a is b)
b=a.copy()
print(a == b)
print(a is b)


a={1,2,3}
b = a
print(a)
print(b)
b.add(4)
print(a)
print(b)
print(a is b)

a={1,2,3}
b = a.copy()
print(a)
print(b)
b.add(4)
print(a)
print(b)
print(a is b)




a=[1,2,3]
b = a
b.append(4)
print(a)
print(b)
print(a is b)
a='string 1'  #基本类型,不会有此种情况发生
b = a
print(a == b)
print(a is b)
b=b.upper()
print(a)
print(b)


