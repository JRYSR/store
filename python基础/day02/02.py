# 从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数
sum = 0
max = 0
aver = 0
count = 0
while count < 10:
    a = int(input("请输入整数："))
    if a >= max:
        max = a
    sum = sum + a
    count = count + 1
aver = sum / count
print(max, sum, aver)