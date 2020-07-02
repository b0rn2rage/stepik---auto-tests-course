from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import formula

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    book = browser.find_element_by_id('book')
    book.click()
    element_x = browser.find_element_by_id('input_value').text
    result = formula.calc(element_x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(result))
    button = browser.find_element_by_id('solve')
    button.click()
finally:
    time.sleep(8)
    browser.quit()
