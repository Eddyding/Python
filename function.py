#!/usr/bin/python  
# #!/usr/bin/env python


'''

没有加#!/usr/bin/python

那是因为系统默认该脚本是shell脚本，把它当shell语句执行，当然失败了。

加上:

#!/usr/bin/python

有时候写#!/usr/bin/python还是不行，很简单因为python解释器没装在usr/bin目录，改成其所在目录就行了，或者更通用的方法是：#!/usr/bin/env python



'''


"""

脚本语言的第一行，目的就是指出，你想要你的这个文件中的代码用什么可执行程序去运行它，就这么简单

#!/usr/bin/python是告诉操作系统执行这个脚本的时候，调用/usr/bin下的python解释器；

#!/usr/bin/env python这种用法是为了防止操作系统用户没有将python装在默认的/usr/bin路径里。
当系统看到这一行的时候，首先会到env设置里查找python的安装路径，再调用对应路径下的解释器程序完成操作。

#!/usr/bin/python相当于写死了python路径;
#!/usr/bin/env python会去环境设置寻找python目录,推荐这种写法



"""

def test():
	print 'Hello china!'
if __name__ == "__main__":
	test()
