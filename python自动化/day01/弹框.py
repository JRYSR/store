from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(r"F:/pythonProject/python自动化/day01/练习的html/弹框的验证/dialogs.html")
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="alert"]').click()
time.sleep(3)
driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="confirm"]').click()
time.sleep(3)
driver.switch_to.alert.accept()
driver.find_element_by_xpath('//*[@id="confirm"]').click()
time.sleep(3)
driver.switch_to.alert.dismiss()

driver.quit()
