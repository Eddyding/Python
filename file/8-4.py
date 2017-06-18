# _*_ coding: utf-8 _*_
#程序 8-4.py (Python 3 version)

import sys

if len(sys.argv)<2:
    print("使用方法：python 8-4.py 成绩文件")
    exit(1)


'''

写入文件, write(字符串)
文本文件操作的write函数只接受字符串.
当要写入的数据不是字符串时,要用str()转换.

'''
no=1
scores=dict()
while True:
    score = int(input('请输入第{}号的成绩:(-1结束)'.format(no)))
    if score == -1: break;
    scores[no] = score
    no += 1    

with open(sys.argv[1],'w') as fp:
    fp.write(str(scores))
print("{}已存储完毕".format(sys.argv[1]))
