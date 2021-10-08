dict1 = {"k1": "v1", "k2": "v2", "k3": "v3"}
#1、请循环遍历出所有的key
for key1 in dict1.keys():
    print(key1, end=" ")
print()
#2、请循环遍历出所有的value
for value1 in dict1.values():
    print(value1, end=" ")
print()
# 3、请在字典中增加一个键值对,"k4":"v4"
dict1["k4"] = "v4"
print(dict1)

