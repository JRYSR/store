import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
# driver.find_element_by_id("kw").send_keys("055")
# driver.find_element_by_id("su").click()
driver.find_element_by_xpath("//*[@id='kw']").send_keys("055")
driver.find_element_by_xpath("//*[@id='su']").click()

time.sleep(10)

driver.quit()
