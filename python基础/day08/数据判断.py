def is_num(date):
    if "." in date:
        date_num1 = date.split(".")
        if date_num1[0].isdecimal() is True and date_num1[1].isdecimal() is True:
            return 1
        else:
            return 0
    elif date.isdecimal():
        return 1
    else:
        return 0


def main():
    date = input("请输入数据：")
    state = is_num(date)
    if state == 1:
        print(date)
    else:
        print("{}不是数值！！！".format(date))


main()
