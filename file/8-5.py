# _*_ coding: utf-8 _*_
#程序 8-5.py (Python 3 version)


'''
ast 模块:
ast.literal_eval()
ast.literal_eval(filedata)


只要在文件中 以字符串类型存储的字典格式正确,通过ast.literal_eval(filedata)
就可以正确的把 filedata 转换成 字典类型 供后续程序代码使用.


'''
import sys, ast

if len(sys.argv)<2:
    print("使用方法：python 8-5.py 成绩文件")
    exit(1)

scores = dict()
with open(sys.argv[1],'r') as fp:
    filedata = fp.read()
    scores = ast.literal_eval(filedata)

# 
print("以下是{}成绩文件的字典类型:".format(sys.argv[1]))
print(scores)
