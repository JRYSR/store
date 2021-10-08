import unittest
import os
from HTMLTestRunner import HTMLTestRunner

#
tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="TestICBCTran.py")

HTMLTestRunner.HTMLTestRunner(
    title="工行转款的测试报告",
    description="aaaa",
    verbosity=1,
    stream=open(file="test report of ICBC_tran.html", mode="w+", encoding="utf-8")
).run(tests)
