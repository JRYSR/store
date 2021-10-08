import pymysql

# 连接数据库
con = pymysql.connect(host="localhost", user="root", password="", database="company")
print(con)


def insert():
    cursor = con.cursor()
    sql_insert = "insert into t_employees value (%s, %s, %s, %s, Now(), %s, %s, %s)"
    empno, ename, job, MGR, sal, comm, deptno = input("请输入要插入的数据：").split(",")
    if empno.isdecimal() and MGR.isdecimal() and sal.isdecimal and comm.isdecimal() and deptno.isdecimal():
        empno = int(empno)
        MGR = int(MGR)
        sal = int(sal)
        comm = int(comm)
        deptno = int(deptno)
    date_insert = [empno, ename, job, MGR, sal, comm, deptno]
    cursor.execute(sql_insert, date_insert)
    con.commit()
    cursor.close()


def deldate():
    ename = input("请输入需要删除的员工姓名：")
    cursor = con.cursor()
    sql_del = "delete from t_employees where ename = %s"
    date_del = [ename]
    cursor.execute(sql_del, date_del)
    con.commit()
    cursor.close()


def update():
    ename = input("请输入员工姓名：")
    sal1 = input("请输入员工薪水增加幅度：")
    if sal1.isdigit():
        sal1 = float(sal1)
    cursor = con.cursor()
    sql_update = "update t_employees set sal = sal + %s where ename = %s"
    date_upodate = [sal1, ename]
    cursor.execute(sql_update, date_upodate)
    con.commit()
    cursor.close()


def select():
    # 创建控制台
    cursor = con.cursor()

    # 准备一条sql语句
    sql = "select * from t_employees where ename = %s"
    ename = input("请输入查询员工姓名：")
    date = [ename]

    # 执行sql语句
    cursor.execute(sql, date)

    # 提取查询的数据
    data = cursor.fetchall()
    for i in data:
        print(i)
    cursor.close()


def main():
    while True:
        print("""
            ------------------
                1.添加数据
                2.删除数据
                3.修改数据
                4.查询数据
            ------------------
        """)
        choose = input("请输入操作选项:")
        if choose.isdecimal():
            if choose == "1":
                insert()
            elif choose == "2":
                deldate()
            elif choose == "3":
                update()
            elif choose == "4":
                select()
            else:
                print("请输入正确操作选项！！！")
        else:
            print("请输入正确操作选项！！！")



main()
