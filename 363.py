import math
import time
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture(scope='function')
def browser():
    print('Запускаем браузер')
    browser = webdriver.Chrome()
    yield browser
    print('Закрываем браузер')
    browser.quit()


class TestCorrectAnswer():

    @pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                      'https://stepik.org/lesson/236896/step/1',
                                      'https://stepik.org/lesson/236897/step/1',
                                      'https://stepik.org/lesson/236898/step/1',
                                      'https://stepik.org/lesson/236899/step/1',
                                      'https://stepik.org/lesson/236903/step/1',
                                      'https://stepik.org/lesson/236904/step/1',
                                      'https://stepik.org/lesson/236905/step/1'])
    def test_params(self, browser, link):
        current_link = f'{link}'
        browser.get(current_link)
        print(f'Текущий url страницы - {current_link}')
        time.sleep(5)
        try:
            textarea = browser.find_element_by_css_selector('.textarea.string-quiz__textarea')
        except NoSuchElementException:
            print('textarea не найден!')
        answer = math.log(int(time.time() - 77.3))
        textarea.send_keys(str(answer))
        submit_button = browser.find_element_by_class_name('submit-submission')
        submit_button.click()
        time.sleep(5)
