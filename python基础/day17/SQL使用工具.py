import pymysql

host = "localhost"
user = "root"
password = ""
database = "fuzhuang"


# class Tools(object):

def updata(sql, pram):               # 增、删、改
    # 连接数据库
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    # 创建控制台
    cursor = con.cursor()
    # 执行SQL语句
    cursor.execute(sql, pram)
    # 提交
    con.commit()

    # 关闭资源
    cursor.close()
    con.close()


def select(sql, pram=" "):              # 查询
    # 连接数据库
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    # 创建控制台
    cursor = con.cursor()
    # 执行SQL语句
    if pram == " ":
        cursor.execute(sql)
    else:
        cursor.execute(sql, pram)
    # 提取数据
    data = cursor.fetchall()

    # 关闭资源
    cursor.close()
    con.close()
    return data


