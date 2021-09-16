import random
import pymysql

# 创建连接
con = pymysql.connect(host="localhost", user="root", password="", database="银行账户管理系统")
print(con)

print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、存钱              ------------|")
print("|------------3、取钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
# 开户逻辑
bank_name = "中国工商银行"


#                第一个对应第一个 不是名称对应名称
def bank_adduser(account):
    cursor = con.cursor()
    sql = "select count(*) from  bank"
    cursor.execute(sql)
    date = cursor.fetchall()
    cursor.close()
    if date[0][0] >= 100:
        return 3
    cursor = con.cursor()
    sql = "select account from  bank"
    cursor.execute(sql)
    date = cursor.fetchall()
    cursor.close()
    if account in date:
        return 2
    return 1


def adduser():  # 定义了一个方法
    username = input("请输入您的用户名：")
    password = input("请输入您的密码(6位阿拉伯数字)：")
    print("请输入您的地址：")
    country = input("\t\t请输入您的国家：")
    province = input("\t\t请输入您的省份：")
    street = input("\t\t请输入您的街道：")
    door = input("\t\t请输入您的门牌号：")
    while True:
        account = random.randint(10000000, 99999999)
        cursor = con.cursor()
        sql_adduser = "select account from bank"
        cursor.execute(sql_adduser)
        bank = cursor.fetchall()
        if account not in bank:
            break
        cursor.close()
    if password.isdecimal():
        if len(password) == 6:
            stast = bank_adduser(account)
            if stast == 3:
                print("你去别的银行吧")
            elif stast == 2:
                print("开户失败，你别重复")
            elif stast == 1:
                cursor = con.cursor()
                sql_insert = "insert into bank value (%s, %s, %s, %s, %s, %s, %s, %s, NOW(), %s)"
                date = [account, username, password, country, province, street, door, 0, bank_name]
                cursor.execute(sql_insert, date)
                con.commit()
                cursor.close()
        else:
            print("密码长度必须是6位！！！")
    else:
        print("密码必须是阿拉伯数字！！！")


def save():
    save_account = input("请输入存款账号：")
    if save_account.isdecimal():
        save_password = input("请输入存款账号密码：")
        if save_password.isdecimal():
            save_account = int(save_account)
            save_password = int(save_password)
        else:
            print("密码格式错误！！！")
    else:
        print("账号格式错误！！！")
    cursor = con.cursor()
    sql_select = "select * from bank where account = %s and passw = %s"
    date = [save_account, save_password]
    cursor.execute(sql_select, date)
    t = cursor.fetchall()
    cursor.close()
    if len(t) != 0:
        save_money = input("请输入存款金额：")
        if save_money.isdecimal():
            save_account = int(save_account)
            cursor = con.cursor()
            sql_save = "update bank set money = money + %s where account = %s and passw = %s"
            date = [save_money, save_account, save_password]
            cursor.execute(sql_save, date)
            con.commit()
            cursor.close()
        else:
            print("请正确输入存款金额！！！")
    else:
        print("账号不存在！！！")


def get():
    get_account = input("请输入账号：")
    if get_account.isdecimal():
        get_account = int(get_account)
        sql_get = "select account from bank where account = %s"
        date1 = [get_account]
        cursor = con.cursor()
        cursor.execute(sql_get, date1)
        t1 = cursor.fetchall()
        cursor.close()
        if t1 is not None:
            get_password = input("请输入账号密码：")
            if get_password.isdecimal() and len(get_password) == 6:
                get_password = int(get_password)
                sql_get = "select * from bank where account = %s and passw = %s"
                date2 = [get_account, get_password]
                cursor = con.cursor()
                cursor.execute(sql_get, date2)
                t2 = cursor.fetchall()
                cursor.close()
                print(t2)
                get_money = input("请输入取款金额：")
                if get_money.isdecimal():
                    get_money = int(get_money)
                else:
                    print("请正确输入取款金额！！！")
                if get_money <= t2[0][7]:
                    cursor = con.cursor()
                    sql_get = "update bank set money = money - %s where account = %s and passw = %s"
                    date3 = [get_money, get_account, get_password]
                    cursor.execute(sql_get, date3)
                    con.commit()
                    cursor.close()
                else:
                    print("余额不足！！！")
            else:
                print("密码错误！！！")
        else:
            print("账号不存在！！！")
    else:
        print("账号格式错误！！！")


def find():
    cursor = con.cursor()
    find_account = input("请输入查询账号：")
    if find_account.isdecimal():
        find_account = int(find_account)
        sql_find_account = "select account from bank where account = %s"
        date = [find_account]
        cursor.execute(sql_find_account, date)
        t1 = cursor.fetchall()
        cursor.close()
        if t1 is not None:
            find_account_password = input("请输入密码：")
            if len(find_account_password) == 6:
                if find_account_password.isdecimal():
                    find_account_password = int(find_account_password)
                    cursor = con.cursor()
                    sql_find_account = "select * from bank where account = %s and passw = %s"
                    date = [find_account, find_account_password]
                    cursor.execute(sql_find_account, date)
                    t2 = cursor.fetchall()
                    cursor.close()
                    if t2 is not None:
                        info = """
                        account:{}
                        username:{}
                        passw:{}
                        country:{}
                        province:{}
                        street:{}
                        door:{}
                        money:{}
                        registerdate:{}
                        bankname:{}
                        """
                        print(info.format(t2[0][0], t2[0][1], t2[0][2], t2[0][3], t2[0][4], t2[0][5], t2[0][6], t2[0][7], t2[0][8], t2[0][9],))
                    else:
                        print("密码错误！！！")
                else:
                    print("密码格式错误！！！")
        else:
            print("查询账号不存在！！！")
    else:
        print("账号格式错误！！！")


def tran():
    out_account = input("请输入转出账号：")
    if out_account.isdecimal():
        out_account = int(out_account)
        cursor = con.cursor()
        sql_out = "select account from bank where account = %s"
        date_out = [out_account]
        cursor.execute(sql_out, date_out)
        t_out1 = cursor.fetchall()
        if t_out1 is not None:
            out_password = input("请输入密码：")
            if out_password.isdecimal() and len(out_password) == 6:
                out_password = int(out_password)
                sql_out = "select * from bank where account = %s and passw = %s"
                date2 = [out_account, out_password]
                cursor = con.cursor()
                cursor.execute(sql_out, date2)
                t_out2 = cursor.fetchall()
                cursor.close()
                in_account = input("请输入转入账号：")
                cursor = con.cursor()
                if in_account.isdecimal():
                    in_account = int(in_account)
                    sql_in_account = "select account from bank where account = %s"
                    date = [in_account]
                    cursor.execute(sql_in_account, date)
                    t_in1 = cursor.fetchall()
                    cursor.close()
                    if t_in1 is not None:
                        out_money = input("请输入转款金额：")
                        if out_money.isdecimal():
                            out_money = int(out_money)
                            if out_money <= t_out2[0][7]:
                                cursor = con.cursor()
                                sql_out = "update bank set money = money - %s where account = %s and passw = %s"
                                date3 = [out_money, out_account, out_password]
                                cursor.execute(sql_out, date3)
                                sql_in = "update bank set money = money + %s where account = %s"
                                date4 = [out_money, in_account]
                                cursor.execute(sql_in, date4)
                                con.commit()
                                cursor.close()
                            else:
                                print("余额不足！！！")
                        else:
                            print("请正确输入取款金额！！！")
                    else:
                        print("转入账号不存在！！！")
                else:
                    print("请输入正确的账号！！！")
            else:
                print("密码错误！！！")
        else:
            print("转出账号不存在！！！")
    else:
        print("账号格式错误！！！")


while True:
    begin = input("请选择业务:")
    if begin == "1":  # 您输入的业务等于1执行开户操作
        print(1, "开户")
        adduser()
    elif begin == "2":
        print(2, "存钱")
        save()
    elif begin == "3":
        print(3, "取钱")
        get()
    elif begin == "4":
        print(4, "转账")
        tran()
    elif begin == "5":
        print(5, "查询")
        find()
    else:
        print(6, "、退出")
        con.close()
        break
