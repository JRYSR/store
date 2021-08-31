# 编写一个函数，传入一个列表，并统计每个数字出现的次数。
# 返回字典数据：{21:3,56:9,10:3}   （阿里一轮笔试题）
list1 = [12, 12, 12, 23, 24]


def sum1(list1):
    dict1 = {}
    for i in set(list1):
        dict1[i] = list1.count(i)
    return dict1


print(sum1(list1))
