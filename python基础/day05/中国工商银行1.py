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
    if account in bank:  # 如变量在容器内执行下面的代码
        return 2
    bank[account] = {
        "username": username,
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
    password = input("请输入您的密码(6位阿拉伯数字)：")
    print("请输入您的地址：")
    country = input("\t\t请输入您的国家：")
    province = input("\t\t请输入您的省份：")
    street = input("\t\t请输入您的街道：")
    door = input("\t\t请输入您的门牌号：")
    t = True
    while t:
        account = random.randint(10000000, 99999999)
        if account not in bank:
            t = False
    if password.isdecimal():
        if len(password) == 6:
            stast = bank_adduser(account, username, password, country, province, street, door)
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
                print(info % (bank[account]['username'], account, bank[account]['country'], bank[account]['province'],
                              bank[account]['street'], bank[account]['door'], bank[account]["money"], bank_name))
        else:
            print("密码长度必须是6位！！！")
    else:
        print("密码必须是阿拉伯数字！！！")
    # print(bank)
    #        调用方法   （元素，，，，，，，，，）
    # if stast == 3:
    #     print("你去别的银行吧")
    # elif stast == 2:
    #     print("开户失败，你别重复")
    # elif stast == 1:
    #     info = '''
    #                 ------------个人信息------------
    #                 用户名:%s
    #                 账号：%s
    #                 密码：*****
    #                 国籍：%s
    #                 省份：%s
    #                 街道：%s
    #                 门牌号：%s
    #                 余额：%s
    #                 开户行名称：%s
    #             '''
    #     # 每个元素都可传入%
    #     print(info % (bank[account]['username'], account, bank[account]['country'], bank[account]['province'],
    #                   bank[account]['street'], bank[account]['door'], bank[account]["money"], bank_name))


def login(save_account, save_password):
    save_account = int(save_account)
    save_password = int(save_password)
    if save_account in bank:
        if save_password == int(bank[save_account]['password']):
            return 1  # 登录成功
        else:
            return 2  # 密码错误
    else:
        return 3  # 账号不存在


def save():
    l = 0
    save_account = input("请输入存款账号：")
    if save_account.isdecimal():
        save_password = input("请输入存款账号密码：")
        if save_password.isdecimal():
            l = login(save_account, save_password)
        else:
            print("密码格式错误！！！")
    else:
        print("账号格式错误！！！")
    if l == 1:
        save_money = input("请输入存款金额：")
        if save_money.isdecimal():
            save_account = int(save_account)
            bank[save_account]['money'] = int(save_money) + int(bank[save_account]['money'])
        else:
            print("请正确输入存款金额！！！")
        print("账号：{}，用户名：{}，余额：{}元".format(save_account, bank[save_account]['username'], bank[save_account]['money']))
    elif l == 2:
        print("密码错误！！！")
    else:
        print("账号不存在！！！")


def get():
    l = 0
    get_account = input("请输入取款账号：")
    if get_account.isdecimal():
        get_password = input("请输入取款账号密码：")
        if get_password.isdecimal():
            l = login(get_account, get_password)
        else:
            print("密码格式错误！！！")
    else:
        print("账号格式错误！！！")
    if l == 1:
        get_money = input("请输入取款金额：")
        if get_money.isdecimal():
            get_money = int(get_money)
            if int(bank[int(get_account)]['money']) >= get_money:
                get_account = int(get_account)
                bank[get_account]['money'] = int(bank[get_account]['money']) - get_money
                return 0  # 正常
            else:
                return 3  # 钱不够
        else:
            print("请正确输入取款金额！！！")

    elif l == 2:
        return 2  # 密码错误
    else:
        return 1  # 账号不存在


def trans():
    l_out = 0
    out_account = input("请输入转出账号：")
    if out_account.isdecimal():
        out_password = input("请输入转出账号密码：")
        if out_password.isdecimal():
            l_out = login(out_account, out_password)
        else:
            print("密码格式错误！！！")
    else:
        print("账号格式错误！！！")
    if l_out == 1:
        in_account = input("请输入转入账号：")
        if int(in_account) in bank:
            in_money = input("请输入转入金额：")
            if in_money.isdecimal():
                in_money = int(in_money)
                if int(bank[int(out_account)]['money']) >= in_money:
                    out_account = int(out_account)
                    in_account = int(in_account)
                    bank[out_account]['money'] = int(bank[out_account]['money']) - in_money
                    bank[in_account]['money'] = int(bank[in_account]['money']) + in_money
                    return 0  # 正常
                else:
                    return 3  # 钱不够
            else:
                print("请正确输入取款金额！！！")
        else:
            return 4  # 转入账号不存在
    elif l_out == 2:
        return 2  # 密码错误
    else:
        return 1  # 账号不存在


def find():
    l_find = 0
    l_account = input("请输入查询账号：")
    if l_account.isdecimal():
        l_password = input("请输入查询账号密码：")
        if l_password.isdecimal():
            l_find = login(l_account, l_password)
            if l_find == 1:
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
                l_account = int(l_account)
                print(info % (bank[l_account]['username'], l_account, bank[l_account]['country'],
                              bank[l_account]['province'], bank[l_account]['street'], bank[l_account]['door'],
                              bank[l_account]["money"], bank_name))
            elif l_find == 2:
                return 2
            else:
                return 3


# {'frank': {'account': 88474479, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1',
# 'money': 0, 'bank_name': '狼腾测试猿银行'}}
# begin = input("请选择业务:")
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
        g = get()
        if g == 0:
            print("取款成功！！！")
        elif g == 1:
            print("账号不存在！！！")
        elif g == 2:
            print("密码错误！！！")
        else:
            print("账号余额不足！！！")
    elif begin == "4":
        print(4, "转账")
        tr = trans()
        if tr == 0:
            print("转账成功！！！")
        elif tr == 1:
            print("转出账号不存在！！！")
        elif tr == 2:
            print("密码错误！！！")
        elif tr == 3:
            print("余额不足！！！")
        else:
            print("转入账号不存在！！！")
    elif begin == "5":
        print(5, "查询")
        f = find()
        if f == 2:
            print("密码错误！！！")
        elif f == 3:
            print("账户不存在！！！")
        else:
            print("查询成功！！！")
    else:
        print(6, "、退出")
        break
