from unittest import TestCase
from Calc import Calc


class TsetCalc(TestCase):

    def testMinu1(self):
        num1 = 72
        num2 = 24
        sum = 48
        calc = Calc()
        s = calc.minu(num1, num2)
        self.assertEqual(s, sum)

    def testMinu2(self):
        num1 = -72
        num2 = 24
        sum = -96
        calc = Calc()
        s = calc.minu(num1, num2)
        self.assertEqual(s, sum)

    def testMinu3(self):
        num1 = 72
        num2 = -24
        sum = 96
        calc = Calc()
        s = calc.minu(num1, num2)
        self.assertEqual(s, sum)

    def testMinu4(self):
        num1 = -72
        num2 = -24
        sum = -48
        calc = Calc()
        s = calc.minu(num1, num2)
        self.assertEqual(s, sum)

    def testMinu5(self):
        num1 = 72000000000000000000000000000000000000000000000000000000000000
        num2 = 24000000000000000000000000000000000000000000000000000000000000
        sum = 48000000000000000000000000000000000000000000000000000000000000
        calc = Calc()
        s = calc.minu(num1, num2)
        self.assertEqual(s, sum)
