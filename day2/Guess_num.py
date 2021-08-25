import random
money = 100
random_num = random.randint(0, 1000)
while money > 0:
    num1 = int(input("请输入一个整数："))
    if num1 > random_num:
        print("你猜的数字大了")
        money = money - 10
    elif num1 < random_num:
        print("你猜的数字小了")
        money = money - 10
    else:
        print("这个整数是：", random_num)
        print("您剩余的钱为{:}元".format(money))
        break