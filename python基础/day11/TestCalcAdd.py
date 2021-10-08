from unittest import TestCase
from Calc import Calc


class TsetCalc(TestCase):

    def testAdd1(self):
        num1 = 72
        num2 = 24
        sum = 96
        calc = Calc()
        s = calc.add(num1, num2)
        self.assertEqual(s, sum)

    def testAdd2(self):
        num1 = -72
        num2 = 24
        sum = -48
        calc = Calc()
        s = calc.add(num1, num2)
        self.assertEqual(s, sum)

    def testAdd3(self):
        num1 = 72
        num2 = -24
        sum = 48
        calc = Calc()
        s = calc.add(num1, num2)
        self.assertEqual(s, sum)

    def testAdd4(self):
        num1 = -72
        num2 = -24
        sum = -96
        calc = Calc()
        s = calc.add(num1, num2)
        self.assertEqual(s, sum)

    def testAdd5(self):
        num1 = 72000000000000000000000000000000000000000000000000000000000000
        num2 = 24000000000000000000000000000000000000000000000000000000000000
        sum = 96000000000000000000000000000000000000000000000000000000000000
        calc = Calc()
        s = calc.add(num1, num2)
        self.assertEqual(s, sum)
