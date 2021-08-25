# 编程实现下列图形的打印
n = int(input("请输入要打印的三角形行数："))
for i in range(1, n+1):
    print(" " * (n - i), end="")
    for x in range(i):
        print("*", end=" ")
    print(" ")