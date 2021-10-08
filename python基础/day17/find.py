import unittest
import os
from HTMLTestRunner import HTMLTestRunner

#
tests = unittest.defaultTestLoader.discover(os.getcwd(), pattern="TestICBCFind.py")

HTMLTestRunner.HTMLTestRunner(
    title="工行查询的测试报告",
    description="aaaa",
    verbosity=1,
    stream=open(file="test report of ICBC_find.html", mode="w+", encoding="utf-8")
).run(tests)
