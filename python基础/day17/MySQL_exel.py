import xlwt
from SQL使用工具 import updata,select

def write_file():
    book = xlwt.Workbook(encoding='utf-8') #创建Workbook，相当于创建Excel

    # 创建sheet，Sheet1为表的名字，cell_overwrite_ok为是否覆盖单元格
    sheet1 = book.add_sheet(u'Sheet1', cell_overwrite_ok=True)
    sql = 'select * from 12yue'
    data = list(select(sql))  # 把第一层元组转换为列表
    data1 = []
    for i in range(len(data)):
        data1.append(list(data[i]))  # 把第二层元组转化为列表  完成转化

    # #向表中添加数据
    # sheet1.write(0, 0, 'Englishname')
    # sheet1.write(1, 0, 'Hellen')
    # sheet1.write(0, 1, '中文名字')
    # sheet1.write(1, 1, '海伦')

    # data = {
    #         "序号": ["姓名", "语文", "数学", "英语"],
    #         "1": ["张三", 130, 120, 100],
    #         "2": ["李四", 100, 110, 120],
    #         "3": ["王五", 125, 135, 135]
    #        }

    # r = 0
    row = len(data1)
    col = len(data1[0])
    titles = ('日期', '服装名称', '单价', '库存数量', '销售额')
    for i in range(0,row):
        for j in range(0,col):
            if i == 0:
                sheet1.write(i,j,titles[j],set_style('Arial', 220, True))
            else:
                sheet1.write(i,j,data1[i-1][j])

    #sheet_merge() 合并单元格

    book.save(r'数据库.xls')
    print("操作成功!")


def set_style(name, height, bold = False):


    style = xlwt.XFStyle()   #初始化样式

    font = xlwt.Font()   #创建字体, Font定义字体的大小、颜色
    font.name = name    #字体名称
    font.bold = bold   #粗体
    # font.italic = True  #斜体
    font.height = height  #字体大小
    # font.colour_index = 4  # 字体颜色

    borders = xlwt.Borders()  #单元格边框线
    borders.left = xlwt.Borders.THIN   #设置边框线粗细
    borders.right = xlwt.Borders.THIN
    borders.top = xlwt.Borders.THIN
    borders.bottom = xlwt.Borders.THIN
    # borders.right_colour = 1  #设置边框线颜色
    # borders.left_colour = 1
    # borders.top_colour = 1
    # borders.bottom_colour = 1

    alignment = xlwt.Alignment() #设置字体在单元格中的位置
    alignment.horz =  xlwt.Alignment.HORZ_CENTER  #水平居左
    alignment.vert = xlwt.Alignment.VERT_CENTER  #垂直居中

    pat = xlwt.Pattern()  #设置单元格背景颜色
    pat.pattern = xlwt.Pattern.SOLID_PATTERN
    pat.pattern_fore_colour = 5   #黄色

    style.font = font
    style.borders = borders
    style.alignment = alignment
    style.pattern = pat

    return style


if __name__ == '__main__':
    write_file()











































