import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver


def calc(x, y):
    return int(x)+int(y)


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)
    first = browser.find_element_by_id('num1').text
    second = browser.find_element_by_id('num2').text
    result = calc(first, second)
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(result))
    button = browser.find_element_by_class_name('btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
