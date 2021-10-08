import random

print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、存钱              ------------|")
print("|------------3、取钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
bank = {}  # 创建一个空的字典
# 开户逻辑
bank_name = "中国工商银行"


#                第一个对应第一个 不是名称对应名称
def bank_adduser(account, username, password, country, province, street, door):
    if len(bank) > 100:
        return 3
    if username in bank:  # 如变量在容器内执行下面的代码
        return 2
    bank[username] = {
        "account": account,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "money": 0,
        "bank_name": bank_name
    }
    return 1


def adduser():  # 定义了一个方法
    username = input("请输入您的用户名：")
    password = input("请输入您的密码：")
    print("请输入您的地址：")
    country = input("\t\t请输入您的国家：")
    province = input("\t\t请输入您的省份：")
    street = input("\t\t请输入您的街道：")
    door = input("\t\t请输入您的门牌号：")
    account = random.randint(10000000, 99999999)
    stast = bank_adduser(account, username, password, country, province, street, door)
    #        调用方法   （元素，，，，，，，，，）
    if stast == 3:
        print("你去别的银行吧")
    elif stast == 2:
        print("开户失败，你别重复")
    elif stast == 1:
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))


def login(name1, account1, password1):
    if name1 in bank:
        if account1.isdecimal():
            account1 = int(account1)
        if account1 == bank[name1]['account']:
            if password1 == bank[name1]['password']:
                # print("登录成功！！！")
                return 0
            else:
                # print("密码错误！！！")
                return 2
        else:
            # print("账号错误！！！")
            return 1
    else:
        # print("用户不存在！！！")
        return 1


def save():
    name1 = input("请输入用户名：")
    account1 = input("请输入账号：")
    password1 = input("请输入账号密码：")
    a = login(name1, account1, password1)
    if a == 0:
        save_money = input("请输入存款金额：")
        if save_money.isdecimal():
            bank[name1]['money'] = save_money
        else:
            print("请以阿拉伯数字的形式输入存款金额！！！")
    else:
        print("用户不存在！！！")


def get():
    name1 = input("请输入用户名：")
    account1 = input("请输入账号：")
    password1 = input("请输入账号密码：")
    a = login(name1, account1, password1)
    if a == 0:
        get_money = input("请输入取款金额：")
        if get_money.isdecimal():
            get_money = int(get_money)
            money1 = int(bank[name1]['money'])
            if money1 >= get_money:
                bank[name1]['money'] = money1 - get_money
                print("您已经成功取款{}元，账号余额{}元".format(get_money, bank[name1]['money']))
            else:
                # print("您的账户余额不足！！！")
                return 3
        else:
            print("请以阿拉伯数字的形式输入取款金额！！！")


def trans():
    name1 = input("请输入用户名：")
    account1 = input("请输入账号：")
    password1 = input("请输入账号密码：")
    a = login(name1, account1, password1)
    if a == 0:
        f = find()
        if f == 0:
            trans_money = input("请输入转款金额：")
            if trans_money.isdecimal():
                bank[name1]['money'] = int(bank[name1]['money']) - int(trans_money)
                trans_name = input("请输入用户名")
                bank[trans_name]['money'] = trans_money
            else:
                print("正确请输入转款金额！！！")
        else:
            print("转款对象不存在！！！")
    elif a == 1:
        print("用户不存在！！！")
    elif a == 2:
        print("密码错误！！！")


def find():
    name2 = input("请输入查询对象用户名：")
    account2 = input("请输入查询用户账号：")
    password2 = input("请输入密码：")
    if name2 in bank:
        if account2.isdecimal():
            account2 = int(account2)
            if account2 == int(bank[name2]['account']):
                if password2 == bank[name2]['password']:
                    info = '''
                                        ------------个人信息------------
                                        用户名:%s
                                        账号：%s
                                        密码：*****
                                        国籍：%s
                                        省份：%s
                                        街道：%s
                                        门牌号：%s
                                        余额：%s
                                        开户行名称：%s
                                    '''
                    # 每个元素都可传入%
                    print(info % (name2, account2, bank[name2]['country'], bank[name2]['province'],
                                  bank[name2]['street'], bank[name2]['door'], bank[name2]['money'], bank_name))
                    return 0
                else:
                    print("密码错误！！！")
            print("账号不存在！！！")
        else:
            print("请正确输入账号！！！")
            return 1
    else:
        print("用户不存在！！！")
        return 2


# {'frank': {'account': 88474479, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1',
# 'money': 0, 'bank_name': '狼腾测试猿银行'}}
# begin = input("请选择业务:")
while True:
    begin = input("请选择业务:")
    if begin == "1":  # 您输入的业务等于1执行开户操作
        adduser()
    elif begin == "2":
        save()
    elif begin == "3":
        g1 = get()
        if g1 == 3:
            print("余额不足！！！")
    elif begin == "4":
        trans()
    elif begin == "5":
        find()
    else:
        print(6, "、退出")
        break
