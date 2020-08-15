import selenium
from selenium import webdriver
import pytest
import appium



driver = webdriver.Chrome()
driver.get("http://www.baidu.com")


driver.find_element_by_id("kw").send_keys("李白")

driver.find_element_by_id("su").click()

assert '11' == '22'

