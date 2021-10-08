import xlrd

# 打开文件
wb = xlrd.open_workbook(filename=r"F:\python自动化测试\day07_mysql工具类与excel读取\2020年每个月的销售情况.xlsx")


def fun():
    type_list = list()
    for month in range(1, 13):
        sheet = wb.sheet_by_name("%s月" % month)
        rows = sheet.nrows
        for a in range(1, rows):
            income = sheet.row_values(a)
            type_list.append(income[1])
    typelists = set(type_list)
    type_list = list(typelists)
    # print(typelist)
    return type_list


def fun1():
    sum_year = 0
    for month in range(1, 13):
        sheet = wb.sheet_by_name("%s月" % month)
        rows = sheet.nrows
        sum = 0
        for i in range(1, rows):
            income = sheet.row_values(i)
            sum += income[2] * income[4]
        sum_year += sum
    # print("2020年全年销售总额：￥%s" % round(sumyear, 2))
    return sum_year


def fun2(cloth_type):
    count = 0
    for month1 in range(1, 13):
        sheet = wb.sheet_by_name("%s月" % month1)
        rows = sheet.nrows
        for i1 in range(1, rows):
            date = sheet.row_values(i1)
            count += date[4]
    print("2020年全年销售服装{}件".format(int(count)))
    sale_year = dict()
    for name in cloth_type:
        count1 = 0
        income1 = 0
        for month2 in range(1, 13):
            sheet = wb.sheet_by_name("%s月" % month2)
            rows = sheet.nrows
            for i2 in range(1, rows):
                date = sheet.row_values(i2)
                if date[1] == name:
                    count1 += date[4]
                    income1 += date[2] * date[4]
                    sale_year[name] = {
                        "销售数量": count1,
                        "销售金额": round(income1, 2)
                    }
    # print(sale_year)
    sale_year_percent = dict()
    for name in cloth_type:
        percent = round(sale_year[name]["销售数量"] / count * 100, 2)
        sale_year_percent[name] = percent
    # print("各种类衣服年销售占比(单位%%)：%s"%sale_year_percent)
    return sale_year_percent, sale_year


def fun3(cloth_type):
    month_percent = dict()
    for month3 in range(1, 13):
        count300 = 0
        count301 = 0
        count302 = 0
        count303 = 0
        count304 = 0
        count305 = 0
        count306 = 0
        count307 = 0
        count308 = 0
        count309 = 0
        count310 = 0
        count311 = 0
        count312 = 0
        month_count = 0
        sheet = wb.sheet_by_name("%s月" % month3)
        rows = sheet.nrows
        for day in range(1, rows):
            date = sheet.row_values(day)
            month_count += date[4]
            if date[1] == "休闲裤":
                count300 += date[4]
            elif date[1] == "铅笔裤":
                count301 += date[4]
            elif date[1] == "卫衣":
                count302 += date[4]
            elif date[1] == "皮草":
                count303 += date[4]
            elif date[1] == "衬衫":
                count304 += date[4]
            elif date[1] == "皮衣":
                count305 += date[4]
            elif date[1] == "风衣":
                count306 += date[4]
            elif date[1] == "小西装":
                count307 += date[4]
            elif date[1] == "马甲":
                count308 += date[4]
            if date[1] == "T血":
                count309 += date[4]
            elif date[1] == "牛仔裤":
                count310 += date[4]
            elif date[1] == "羽绒服":
                count311 += date[4]
            else:
                count312 += date[4]
            info = "%s月"
            month_percent[info % month3] = {
                "休闲裤本月销售占比": round(count300 / month_count * 100, 2),
                "铅笔裤本月销售占比": round(count301 / month_count * 100, 2),
                "卫衣本月销售占比": round(count302 / month_count * 100, 2),
                "皮草本月销售占比": round(count303 / month_count * 100, 2),
                "衬衫本月销售占比": round(count304 / month_count * 100, 2),
                "皮衣本月销售占比": round(count305 / month_count * 100, 2),
                "风衣本月销售占比": round(count306 / month_count * 100, 2),
                "小西装本月销售占比": round(count307 / month_count * 100, 2),
                "马甲本月销售占比": round(count308 / month_count * 100, 2),
                "T血本月销售占比": round(count309 / month_count * 100, 2),
                "牛仔裤本月销售占比": round(count310 / month_count * 100, 2),
                "羽绒服本月销售占比": round(count311 / month_count * 100, 2),
                "棉衣本月销售占比": round(count312 / month_count * 100, 2),
                "本月销售总量": month_count
            }
    # print(month_percent)
    return month_percent


def fun4(sum_income, sale_year, cloth_type):
    income_year = dict()
    for name in cloth_type:
        income_year[name] = round(sale_year[name]["销售金额"] / sum_income * 100, 2)
    return income_year


def fun5(sale_year_percent):
    date = max(sale_year_percent, key=sale_year_percent.get)
    return date


def fun6(cloth_type):
    season11 = {
        "休闲裤": 0,
        "铅笔裤": 0,
        "卫衣": 0,
        "皮草": 0,
        "衬衫": 0,
        "皮衣": 0,
        "风衣": 0,
        "小西装": 0,
        "马甲": 0,
        "T血": 0,
        "牛仔裤": 0,
        "羽绒服": 0,
        "棉衣": 0,
    }
    season12 = {
        "休闲裤": 0,
        "铅笔裤": 0,
        "卫衣": 0,
        "皮草": 0,
        "衬衫": 0,
        "皮衣": 0,
        "风衣": 0,
        "小西装": 0,
        "马甲": 0,
        "T血": 0,
        "牛仔裤": 0,
        "羽绒服": 0,
        "棉衣": 0,
    }
    season13 = {
        "休闲裤": 0,
        "铅笔裤": 0,
        "卫衣": 0,
        "皮草": 0,
        "衬衫": 0,
        "皮衣": 0,
        "风衣": 0,
        "小西装": 0,
        "马甲": 0,
        "T血": 0,
        "牛仔裤": 0,
        "羽绒服": 0,
        "棉衣": 0,
    }
    season14 = {
        "休闲裤": 0,
        "铅笔裤": 0,
        "卫衣": 0,
        "皮草": 0,
        "衬衫": 0,
        "皮衣": 0,
        "风衣": 0,
        "小西装": 0,
        "马甲": 0,
        "T血": 0,
        "牛仔裤": 0,
        "羽绒服": 0,
        "棉衣": 0,
    }
    season1 = [2, 3, 4]
    season2 = [5, 6, 7]
    season3 = [8, 9, 10]
    for month6 in range(1, 13):
        sheet = wb.sheet_by_name("%s月" % month6)
        rows = sheet.nrows
        if month6 in season1:
            for row in range(1, rows):
                date = sheet.row_values(row)
                if date[1] in cloth_type:
                    season11[date[1]] += int(date[4])
        elif month6 in season2:
            for row in range(1, rows):
                date = sheet.row_values(row)
                if date[1] in cloth_type:
                    season12[date[1]] += int(date[4])
        elif month6 in season3:
            for row in range(1, rows):
                date = sheet.row_values(row)
                if date[1] in cloth_type:
                    season13[date[1]] += int(date[4])
        else:
            for row in range(1, rows):
                date = sheet.row_values(row)
                if date[1] in cloth_type:
                    season14[date[1]] += int(date[4])
    max1 = max(season11, key=season11.get)
    max2 = max(season12, key=season12.get)
    max3 = max(season13, key=season13.get)
    max4 = max(season14, key=season14.get)
    return season11, season12, season13, season14,max1, max2, max3, max4


def fun7(sale_year_percent):
    date = min(sale_year_percent, key=sale_year_percent.get)
    return date


def main():
    cloth_type = fun()
    # print(cloth_type)
    sum_income = fun1()
    print("2020年全年销售总额：￥%s" % round(sum_income, 2))
    print()
    sale_year_percent, sale_year = fun2(cloth_type)
    print("各种类衣服年销售件数年占比(单位%%)：%s" % sale_year_percent)
    print()
    month_percent = fun3(cloth_type)
    print("各种类衣服每月销售件数月占比(单位%%)：%s" % month_percent)
    print()
    income_year = fun4(sum_income, sale_year, cloth_type)
    print("各种类衣服年销售金额占比(单位%%)：%s" % income_year)
    print()
    max = fun5(sale_year_percent)
    print("最畅销的衣服是：", max)
    print()
    season1, season2, season3, season4, season1max, season2max, season3max, season4max = fun6(cloth_type)
    print(season1)
    print("第一季度最畅销的衣服是：%s" % season1max)
    print(season2)
    print("第二季度最畅销的衣服是：%s" % season2max)
    print(season3)
    print("第三季度最畅销的衣服是：%s" % season3max)
    print(season4)
    print("第四季度最畅销的衣服是：%s" % season4max)
    print()
    min = fun7(sale_year_percent)
    print("全年销量最低的衣服是：", min)


main()
