from unittest import TestCase
from Calc import Calc


class TsetCalc(TestCase):

    def testDivision1(self):
        num1 = 72
        num2 = 24
        sum = 3
        calc = Calc()
        s = calc.division(num1, num2)
        self.assertEqual(s, sum)

    def testDivision2(self):
        num1 = -72
        num2 = 24
        sum = -3
        calc = Calc()
        s = calc.division(num1, num2)
        self.assertEqual(s, sum)

    def testDivision3(self):
        num1 = 72
        num2 = -24
        sum = -3
        calc = Calc()
        s = calc.division(num1, num2)
        self.assertEqual(s, sum)

    def testDivision4(self):
        num1 = -72
        num2 = -24
        sum = 3
        calc = Calc()
        s = calc.division(num1, num2)
        self.assertEqual(s, sum)

    def testDivision5(self):
        num1 = 72000000000000000000000000000000000000000000000000000000000000
        num2 = 24000000000000000000000000000000000000000000000000000000000000
        sum = 3
        calc = Calc()
        s = calc.division(num1, num2)
        self.assertEqual(s, sum)
