import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='function')
def browser():
    print('\nЗапуск браузера')
    browser = webdriver.Chrome()
    yield browser
    print('\nЗакрытие браузера')
    browser.quit()


class TestCorrectAnswer:

    @pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                      'https://stepik.org/lesson/236896/step/1',
                                      'https://stepik.org/lesson/236897/step/1',
                                      'https://stepik.org/lesson/236898/step/1',
                                      'https://stepik.org/lesson/236899/step/1',
                                      'https://stepik.org/lesson/236903/step/1',
                                      'https://stepik.org/lesson/236904/step/1',
                                      'https://stepik.org/lesson/236905/step/1'])
    def test_params(self, browser, link):
        browser.get(link)
        print(f'\nТекущий url страницы - {link}')
        textarea = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.textarea.string-quiz__textarea')))
        answer = math.log(int(time.time() - 67))
        textarea.send_keys(str(answer))
        submit_button = browser.find_element_by_class_name('submit-submission')
        submit_button.click()
        check_message = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))
        check_message = check_message.text
        assert check_message == 'Correct!', f'Отображается некорректное сообщение {check_message}'
