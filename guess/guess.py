#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
# Python 3



'''

python3

print 自动换行


'''

'''

"""

"""


a,b,c = 38,49,13


查询一个变量当前类型.
type()


// 整除
** 次方

a,b  = b,a


input
raw_input

'''


import random

game_count=0
all_counts=[]


s='''
 lsjlf
 lsjfl
'''
print (s)


s="""
沙发
安防 
"""

print (s)
while True:
	game_count += 1
	guess_counts =  0  #
	answer = random.randint(0,99)
	while True:
		guess = int(input("请猜一个数字(0-99):"))
		guess_counts += 1 
		if guess == answer:
			print("恭喜你猜中了")
			print("你总共猜了"+ str(guess_counts)+"次")
			all_counts.append(guess_counts)
			break;
		elif guess > answer:
			print("你猜的数字太大了")
		else:
			print("你猜的数字太小了")
	onemore = input("还要再玩吗(y/n)?") #python 3执行才不会出错
	if onemore != 'Y' and onemore != 'y':
	 print("欢迎下次再来")
	 print("你的成绩如下:")
	 print(all_counts)
	 print("一共玩了多少次:")
	 print(len(all_counts)) #数组元素个数
	 print(game_count)
	 print("平均猜中次数"+\
			str(sum(all_counts)/float(len(all_counts))))
	 break;

