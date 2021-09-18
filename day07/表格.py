import xlrd

# 打开文件
wb = xlrd.open_workbook(filename=r"F:\python自动化测试\day07_mysql工具类与excel读取\2020年每个月的销售情况.xlsx")

# 确定选项卡
# month = input("请输入月份数字(1-12)：")
# for month in range(1, 13):
#     sheet = wb.sheet_by_name("%s月"%(month))

# # 获取表格有多少行，多少列
# rows = sheet.nrows
# cols = sheet.ncols
# info = "行：%s，列：%s"
# print(info%(rows, cols))
# print("行：%s，列：%s"%(rows, cols))

# 获取每一行的数据并打印
sumyear = 0
for month in range(1, 13):
    sheet = wb.sheet_by_name("%s月"%(month))
    rows = sheet.nrows
    cols = sheet.ncols
    sum = 0
    for i in range(1, rows):
        income = sheet.row_values(i)
        sum += income[2] * income[4]
    sumyear += sum
    # print("%s月销售总额：￥%s"%(month, round(sum, 2)))
print("2020年全年销售总额：￥%s"%round(sumyear, 2))


# 获取每一列的数据并打印
# for i in range(0, cols):
#     print(sheet.col_values(i))

dic = {"1": 0}
dic["1"] = dic["1"] + 12
print(dic)

season1 = [2, 3, 4]
season2 = [5, 6, 7]
season3 = [8, 9, 10]
for month6 in range(1, 13):
    if month6 in season1:
        print(month6, end="-")
    elif month6 in season2:
        print(month6, end="*")
    elif month6 in season3:
        print(month6, end="+")
    else:
        print(month6, end="/")

dic1 = {"1": 1, "2": 2}
a = input("请输入键：")
b = int(input("请输入值："))
dic1[a] += b
print(dic1)
