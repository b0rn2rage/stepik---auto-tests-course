import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(link)
    button = browser.find_element_by_class_name('btn')
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    element_x = browser.find_element_by_id('input_value').text
    result = calc(element_x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(result))
    second_button = browser.find_element_by_class_name('btn')
    second_button.click()
finally:
    time.sleep(8)
    browser.quit()
