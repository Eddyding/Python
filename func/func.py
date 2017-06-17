     #!/usr/bin/env python
# _*_ coding: UTF-8 _*_


'''

abs(x) 
all(i):i中所有的元素为True才会返回True
any(i):i中只要有一个元素为True就会返回True
bin(n): 把数值n转换为 2进制数字
bool(x):x如果是False,None or 空值就返回 False
chr(n):取得第n个ASCII码的字符

dir(x):检查x对象可以使用的方法.


divmod(a,b): 返回a/b的商和余数,以tuple的形式返回
enumerate(x):用枚举的形式,把变量x中的索引值和值 取出来,组合成tuple,而x必须像是list,dict这一类具有迭代特性的变量

eval(e):求字符串类型的表达式e的值.
float(n):将变量n转换成浮点型.

format():字符串格式化,输出映像

frozenset(): 用来创建不能被修改的集合变量

help(cmd):查询任一指令或 函数的用法
hex(n):把数值n转换成16进制
id(x):取得变量x的内存地址
input(msg):显示出信息msg,并要求用户输入数据

int(a):把变量a转换成整型数.
len(a):计算变量a的长度.但a必须是可以计算长度的类型.
max(a):返回变量a中最大值的元素
min(a):返回变量a中最小值的元素
oct(n):把数值n转换成8进制
open():打开文件
pow(x,y):x的y次方
print():

range(a,b,c) #[a..b-1],间隔为c
round(n):数值n四舍5入,取整数
sorted(a):把a的元素排序
str(n):把变量n转换成字符串类型
sum(a):计算a中元素的总和
type(x):返回x的类型


'''

a = 100
print(bin(a))
print(oct(a))
print(hex(a))

a=50
b=100
print("{}+{}={}".format(a,b,a+b))


a = range(1,10)
print(a)
#print(range(1,10))

b = range(5,100,5)
print(b)

c= range(1,101) #[1..101)  or [1..100]
print(c)
print("1+2+...+100={}".format(sum(c)))# 在format中的每一个参数会按顺序填入前方字符串中相对应的{}中。


'''
   
   def functionName:
   
'''
def add2number(a,b):
    return a + b
print(add2number(10,20))

def draw_bar(n,symbol="*"):
    for i in range(1,n+1):
    #print(symbol,end="") #在print 后面加上end="" or “,” ,目的是为了不让print换行
        print symbol,
    print #   # line feed
draw_bar(5)

draw_bar(symbol='#',n=10) #在调用时，也可以直接指定参数的变量名称，这样就不用管参数的顺序了。

def proc(*args): # var args ,让函数接受没有预先设置的参数个数
    for arg in args:
        print("arg:",arg)


proc(1,2,3) #Python 会以 tuple的方式来接收 所有调用的自变量，把args当成  tuple
proc(1,2)
proc("a","b")





    













