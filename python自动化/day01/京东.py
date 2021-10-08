from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.jd.com")
driver.maximize_window()
driver.find_element_by_id("key").send_keys("歼20")
driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()

time.sleep(10)
driver.quit()
