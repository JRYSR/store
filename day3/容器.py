'''
元组：(1,42465,62,2,24,92,49,2492,498,24,10)
列表：[45,410,45,1,05,05,10,5,015,0,1924]
字典：{
    "010":"北京",
    "020":"上海"
}
集合：{1,05,18,8,01,50,180,1,8,01}

'''

names = ["jason jia","frank","bob","alice","格里安抚","刘晶宇","张关","阴园园"]

# 增
names.append("旺财")

# 删除
del names[0]

# 修改
names[0] = "田鸡"

# 查询
n = names[5]
print(names)
# enumerate 枚举
for key, value in enumerate(names):  # 0 田鸡    1 bob
    print(key, value)

























