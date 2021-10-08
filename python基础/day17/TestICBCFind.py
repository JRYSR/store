from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack

from ICBC import find

import xlrd

wb = xlrd.open_workbook(filename=r"/数据/开户.xlsx")
sheet = wb.sheet_by_name("Sheet5")
rows = sheet.nrows
date = list()
for i in range(1, rows):
    date.append(sheet.row_values(i))


@ddt
class TestICBC(TestCase):

    @data(*date)
    @unpack
    def testFind(self, a, b, c, d, e, f, g, h, i):
        s = find(str(int(a)), str(int(c)))
        self.assertEqual(s, i)