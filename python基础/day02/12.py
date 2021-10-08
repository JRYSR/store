# 用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
# 求阶乘：
# jie = 1
# n = int(input("请输入一个整数："))
# for i in range(1, n + 1):
#     jie = jie * i
# print(jie)

jie = 1
sum = 0
for i in range(1, 21):
    jie = 1
    for j in range(1, i + 1):
        jie = jie * j
    sum = sum + jie
print(sum)