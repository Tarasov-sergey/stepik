from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
import os

link = "http://suninjuly.github.io/alert_accept.html"

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element_by_class_name("btn")
    btn.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id("input_value").text

    browser.find_element_by_id("answer").send_keys(calc(int(x)))

    button = browser.find_element_by_class_name("btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()