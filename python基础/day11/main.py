from HTMLTestRunner import HTMLTestRunner
import unittest

tests = unittest.defaultTestLoader.discover(r"/python基础/day11", pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title="计算器测试报告",
    description="""
    表1  计算器加法测试报告
    表2  计算器减法测试报告
    表3  计算器乘法测试报告
    表4  计算器除法测试报告
    """,
    verbosity=1,
    stream = open(file="计算器测试报告.html", mode="w+", encoding="utf-8")
)

runner.run(tests)
