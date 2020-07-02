import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/execute_script.html'
    browser.get(link)
    element_x = browser.find_element_by_id('input_value').text
    result = calc(element_x)
    browser.execute_script("window.scrollBy(0, 150);")
    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(result))
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radio = browser.find_element_by_id('robotsRule')
    radio.click()
    button = browser.find_element_by_class_name('btn')
    button.click()
finally:
    time.sleep(5)
    browser.quit()
