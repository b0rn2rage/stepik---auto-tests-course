import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)
    troll_button = browser.find_element_by_css_selector('button.trollface')
    troll_button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    element_x = browser.find_element_by_id('input_value').text
    result = calc(element_x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(result))
    second_button = browser.find_element_by_class_name('btn')
    second_button.click()
finally:
    time.sleep(8)
    browser.quit()
