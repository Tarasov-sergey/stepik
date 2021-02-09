from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
import os

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("trollface")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc(int(x)))

    button = browser.find_element_by_class_name("btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()