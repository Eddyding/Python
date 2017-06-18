# _*_ coding: utf-8 _*_
#程序 8-8.py (Python 3 version)


'''
    
    在Python 中，存取SQLite 数据库，需要先导入import sqlite3
    然后通过connect连接数据库，再以execute执行SQL指令的方式来操作数据库的内容。
    
    

conn = sqlite3.connect(db)   #连接数据库db,db是数据库文件
conn.commit() # 把之前的改变确实反映到数据库中。
conn.rollback()  #取消当前变更。恢复到上一次commit时的状态。
conn.close()  #关闭数据库连接


cursor = conn.execute(sql)  # 执行sql指令

cursor.fetchone() #取得当前的一行数据。
cursor.fetchall() #取得剩余的所有数据。


   
'''
import sqlite3

def disp_menu():
    print("学生数据编辑")
    print("------------")
    print("1.新增")
    print("2.编辑")
    print("3.删除")
    print("4.显示所有学生")
    print("0.结束")
    print("------------")

def append_data():
    while True:
        no = int(input("请输入学生座号(-1停止输入):"))
        if no == -1: break
        name = input("请输入学生姓名:")
        sqlstr = "select * from student where stdno={};".format(no)
        cursor = conn.execute(sqlstr)
        if len(cursor.fetchall()) > 0:
            print("您输入的座号已经有数据了")
        else:
            sqlstr = "insert into student values({},'{}');".format(no,name)
            conn.execute(sqlstr)
            conn.commit()


def edit_data():
    no = input("请输入要编辑的学生座号:")
    sqlstr = "select * from student where stdno={};".format(no)
    cursor = conn.execute(sqlstr)
    rows = cursor.fetchall()
    if len(rows) > 0:
        print("当前的学生姓名:",rows[0][1])
        name = input("请输入学生姓名：")
        sqlstr = "update student set name='{}' where stdno={};".format(name, no)
        conn.execute(sqlstr)
        conn.commit()
    else:
        print("找不到要编辑的学生座号")

def del_data():
    no = input("请输入要删除的学生座号:")
    sqlstr = "select * from student where stdno={};".format(no)
    cursor = conn.execute(sqlstr)
    rows = cursor.fetchall()
    if len(rows) > 0:
        print("你当前要删除的是座号{}的{}".format(rows[0][0], rows[0][1]))
        answer = input("确定要删除吗？(y/n)")
        if answer == 'y' or answer == 'Y':
            sqlstr = "delete from student where stdno={};".format(no)
            conn.execute(sqlstr)
            conn.commit()
            print("已删除指定的学生...")
    else:
        print("找不到要删除的学生")

def disp_data():
    cursor = conn.execute('select * from student;')
    for row in cursor:
        print("No {}: {}".format(row[0],row[1]))

conn = sqlite3.connect('scores.sqlite')

while True:
    disp_menu()
    choice = int(input("请输入您的选择:"))
    if choice == 0 : break
    if choice == 1: 
        append_data()
    elif choice == 2:
        edit_data()
    elif choice == 3:
        del_data()
    elif choice == 4:
        disp_data()
    else: break
    x = input("请按Enter键回主菜单")
