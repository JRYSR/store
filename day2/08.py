# 使用while循环实现99乘法表的打印
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}X{}={}".format(j, i, i * j), end=" ")
    print("")