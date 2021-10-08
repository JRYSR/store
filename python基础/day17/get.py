import unittest
import os
from HTMLTestRunner import HTMLTestRunner

#
tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="TestICBCGet.py")

HTMLTestRunner.HTMLTestRunner(
    title="工行取款的测试报告",
    description="aaaa",
    verbosity=1,
    stream=open(file="test report of ICBC_get.html", mode="w+", encoding="utf-8")
).run(tests)
