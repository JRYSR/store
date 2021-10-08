import random

bank = {
    10000000: {
        "username": "张三",
        "password": 123456,
        "country": "中国",
        "province": "河南省",
        "street": "洛阳街",
        "door": "洛001",
        "money": 1000,
        "bank_name": "中国工商银行"
    },
    10000001: {
        "username": "李四",
        "password": 123456,
        "country": "中国",
        "province": "河北省",
        "street": "承德街",
        "door": "承001",
        "money": 1000,
        "bank_name": "中国工商银行"
    },
    10000002: {
        "username": "王五",
        "password": 123456,
        "country": "中国",
        "province": "山西省",
        "street": "大同街",
        "door": "大001",
        "money": 1000,
        "bank_name": "中国工商银行"
    }
}  # 创建一个空的字典


# 开户逻辑
# bank_name = "中国工商银行"


#                第一个对应第一个 不是名称对应名称
def bank_adduser(username, password, country, province, street, door, bank_name):
    while True:
        account = random.randint(10000000, 99999999)
        if account not in bank:
            break
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


def save(account, password, money):
    if account.isdecimal():
        account = int(account)
        if account in bank:
            if password.isdecimal():
                password = int(password)
                if password == bank[account]["password"]:
                    if money.isdecimal():
                        money = int(money)
                        if money > 0:
                            bank[account]["money"] += money
                            return 0
                        else:
                            return 1
                    else:
                        return 2
                else:
                    return 3
            else:
                return 4
        return 5
    else:
        return 6


def get(account, password, get_money):
    if account.isdecimal():
        account = int(account)
        if account in bank:
            if password.isdecimal():
                password = int(password)
                if password == bank[account]["password"]:
                    if get_money.isdecimal():
                        get_money = int(get_money)
                        if bank[account]["money"] > get_money:
                            bank[account]["money"] -= get_money
                            return 0
                        else:
                            return 1
                    else:
                        return 2
                else:
                    return 3
            else:
                return 4
        return 5
    else:
        return 6


def trans(out_account, in_account, password, in_money):
    if out_account.isdecimal():
        out_account = int(out_account)
        if out_account in bank:
            if password.isdecimal():
                password = int(password)
                if password == bank[out_account]["password"]:
                    if in_account.isdecimal():
                        in_account = int(in_account)
                        if in_account in bank:
                            if in_money.isdecimal():
                                in_money = int(in_money)
                                if 0 < in_money <= bank[out_account]["money"]:
                                    bank[out_account]["money"] -= in_money
                                    bank[in_account]["money"] += in_money
                                    return 0
                                else:
                                    return 1
                            else:
                                return 2
                        else:
                            return 3
                    else:
                        return 4
                else:
                    return 5
            else:
                return 6
        else:
            return 7
    else:
        return 8


def find(account, password):
    if account.isdecimal():
        account = int(account)
        if account in bank:
            if password.isdecimal():
                password = int(password)
                if password == bank[account]["password"]:
                    return 0
                else:
                    return 1
            else:
                return 2
        else:
            return 3
    else:
        return 4

