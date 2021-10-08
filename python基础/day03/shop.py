"""
    10张机械革命优惠券，9折
        20张老干妈优惠券，1折
        15张辣条的优惠券，2折
    先随机抽取一张，最终结算的时候使用这个优惠券。
"""
import random
coupons = random.randint(1, 45)
count = 1
print(coupons)

# 1.准备商品
shop = [
    ["机械革命", 9000],  # shop[chose][1]
    ["Think pad", 4500],
    ["Mac book pro", 12000],
    ["洗衣粉", 20],
    ["西瓜", 2],
    ["老干妈", 15],
    ["卫龙辣条", 3.5]
]
# 2.准备足够的钱
money = input("请输入初始余额：")
money = int(money)  # "5" --> 5

# 3.准备空的购物车
mycart = []

# 4.开始购物：
while True:  # 死循环
    # 展示商品
    for key, value in enumerate(shop):
        print(key, value)

    # 输入
    chose = input("请输入您想要的商品编号：")
    if chose.isdigit():  # "5" --> 5
        chose = int(chose)
        # 商品是否存在
        if chose > len(shop):  # len()
            print("对不起，您输入商品不存在！别瞎弄！")
        else:
            # 金钱是否足够
            if money < shop[chose][1]:
                print("穷鬼，对不起，钱不够，到其他地方买去！")
            else:
                mycart.append(shop[chose])
                if coupons in range(1, 11):
                    if chose == 0 and count == 1:
                        money = money - shop[chose][1] * 0.9
                        count = 0
                    else:
                        money = money - shop[chose][1]
                elif coupons in range(11, 31):
                    if chose == 5 and count == 1:
                        money = money - shop[chose][1] * 0.9
                        count = 0
                    else:
                        money = money - shop[chose][1]
                elif coupons in range(31, 46):
                    if chose == 6 and count == 1:
                        money = money - shop[chose][1] * 0.9
                        count = 0
                    else:
                        money = money - shop[chose][1]
                print("恭喜，成功添加购物车!,您的余额还剩：￥", money)

    elif chose == 'q' or chose == 'Q':
        print("欢迎下次光临！拜拜了您嘞！")
        break
    else:
        print("对不起，输入非法，请重新输入！别瞎弄！")

# 打印购物小条
print("以下是您的购物小条，请拿好：")
print("--------------Jason 商城------------------")
for key, value in enumerate(mycart):
    print(key, value)
print("您的钱包余额还剩：￥", money)
print("-----------------------------------------")
good = set(tuple(_) for _ in mycart)
for key, value in enumerate(good):
    print(key, value)
