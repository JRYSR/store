from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r"F:/pythonProject/python自动化/day01/练习的html/跳转页面/pop.html")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_id("goo").click()

driver.close()
