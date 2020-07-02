import time
import formula
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/math.html'
    browser.get(link)
    element_x = browser.find_element_by_id('input_value').text
    result = formula.calc(element_x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(result))
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_id('robotsRule')
    radiobutton.click()
    button = browser.find_element_by_class_name('btn')
    button.click()
finally:
    time.sleep(5)
    browser.quit()
