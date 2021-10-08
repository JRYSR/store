import xlwt
import pymysql

conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='fuzhuang',
        charset="utf8"
        )

# 创建游标
cur = conn.cursor()

# 创建SQL语句 ： select * from tables
sql = 'select * from 12yue1'
# 执行SQL语句
cur.execute(sql)
date = cur.fetchall()
date1 = list(date)
cur.close()
conn.close()
# for i in range(len(date1)):
#     date1[i] = list(date1[i])
#     date1[i][0] = str(date1[i][0], encoding='utf8')
#     date1[i][1] = str(date1[i][1], encoding='utf8')
# print(date1)
#
# for i in range(len(date1)):
#     date1[i] = tuple(date1[i])
# date = tuple(date1)
# print(date)

# 创建工作簿对象
wb = xlwt.Workbook(encoding="utf-8")

# 创建工作表对象
sheet = wb.add_sheet('sheet1')


# 表头内容
titles = ('日期', '服装名称', '单价', '库存数量', '销售额')
title_style = xlwt.XFStyle()
font = xlwt.Font()
font.name = '行楷-简'
font.height = 40
font.bold = True
font.colour_index = 4
title_style.font = font
aligment = xlwt.Alignment()
aligment.horz = xlwt.Alignment.HORZ_CENTER
aligment.vert = xlwt.Alignment.VERT_CENTER
title_style.alignment = aligment

# 添加表头内容到表中

for col_index, title in enumerate(date):
    sheet.write(0, col_index, title, title_style)

for row_index, row in enumerate(cur.fetchall()):
    for col_index, value in enumerate(row):
        sheet.write(row_index+1, col_index, value)
print(titles)
# 保存Excel表，文件后缀名为.xlsx
wb.save('数据库.xlsx')
