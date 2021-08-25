# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形
# （结果判断：等腰，等边，直角，普通，不能形成三角形。）
a = int(input("请输入三角形的一条边："))
b = int(input("请输入三角形的一条边："))
c = int(input("请输入三角形的一条边："))
if (a + b > c) and (a + c > b) and (b + c > a):
    if (a == b) and (b == c) and (a == c):
        print("等边三角形")
    elif (a == b) or (a == c) or (b == c):
        print("等腰三角形")
    elif (a * a + b * b == c * c) or (b * b + c * c == a * a) or (a * a + c * c == b * b):
        print("直角三角形")
    else:
        print("普通三角形")
else:
    print("不能形成三角形")