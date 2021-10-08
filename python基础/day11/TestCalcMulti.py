from unittest import TestCase
from Calc import Calc


class TsetCalc(TestCase):

    def testMulti1(self):
        num1 = 72
        num2 = 24
        sum = 1728
        calc = Calc()
        s = calc.multi(num1, num2)
        self.assertEqual(s, sum)

    def testMulti2(self):
        num1 = -72
        num2 = 24
        sum = -1728
        calc = Calc()
        s = calc.multi(num1, num2)
        self.assertEqual(s, sum)

    def testMulti3(self):
        num1 = 72
        num2 = -24
        sum = -1728
        calc = Calc()
        s = calc.multi(num1, num2)
        self.assertEqual(s, sum)

    def testMulti4(self):
        num1 = -72
        num2 = -24
        sum = 1728
        calc = Calc()
        s = calc.multi(num1, num2)
        self.assertEqual(s, sum)

    def testMulti5(self):
        num1 = 72000000000000000000000000000000000000000000000000000000000000
        num2 = 24000000000000000000000000000000000000000000000000000000000000
        sum = 1728000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        calc = Calc()
        s = calc.multi(num1, num2)
        self.assertEqual(s, sum)
