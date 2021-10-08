import xlrd
import pymysql
import time
#打开数据所在的工作簿，以及选择存有数据的工作表
book = xlrd.open_workbook(r"F:\python自动化测试\day07_mysql工具类与excel读取\2020年每个月的销售情况.xlsx")
sheet = book.sheet_by_index(0)
#建立一个MySQL连接
conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        db='fuzhuang',
        port=3306,
        charset='utf8'
        )
# 获得游标
cur = conn.cursor()
# 创建插入SQL语句
query = 'insert into 12yue1 (日期,服装名称,单价,库存数量,销售额) values (%s, %s, %s, %s, %s)'
# 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题行
for r in range(1, sheet.nrows):
      日期 = sheet.cell(r, 0).value
      服装名称 = sheet.cell(r, 1).value
      单价 = sheet.cell(r, 2).value
      库存数量 = sheet.cell(r, 3).value
      销售额 = sheet.cell(r, 4).value
      values = (日期,服装名称,单价,库存数量,销售额)
      # 执行sql语句
      cur.execute(query, values)
cur.close()
conn.commit()
conn.close()
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("导入 " +columns + " 列 " + rows + " 行数据到MySQL数据库!")