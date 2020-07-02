import os
import time
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)
    current_dir = os.path.abspath((os.path.dirname(__file__)))
    file_path = os.path.join(current_dir, 'file.txt')
    first_name = browser.find_element_by_name('firstname')
    first_name.send_keys('John')
    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('Snow')
    email = browser.find_element_by_name('email')
    email.send_keys('winter@gmail.com')
    choose_file = browser.find_element_by_id('file')
    choose_file.send_keys(file_path)
    button = browser.find_element_by_class_name('btn')
    button.click()
finally:
    time.sleep(8)
    browser.quit()