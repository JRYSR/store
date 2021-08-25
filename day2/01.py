# 实现输入10个数字，并打印10个数的求和结果
sum = 0
count = 0
while count < 10:
    a = int(input("请输入整数："))
    sum = sum + a
    count = count + 1
print(sum)