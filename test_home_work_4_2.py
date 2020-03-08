from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


def test_autozation_pozitiv():
    link = "http://selenium1py.pythonanywhere.com/ru/"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(20)
    browser.maximize_window()
    wait = WebDriverWait(browser, 20)

    browser.find_element_by_css_selector('#login_link').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#register_form button')))
    name = time.strftime("%Y%m%d%H%M", time.localtime())
    browser.find_element_by_css_selector('#id_registration-email').send_keys(name + '@qwer.ru')
    browser.find_element_by_css_selector('#id_registration-password1').send_keys('2020varakin2020')
    browser.find_element_by_css_selector('#id_registration-password2').send_keys('2020varakin2020')
    browser.find_element_by_css_selector('#register_form button').click()
    assert browser.find_element_by_css_selector('#messages div div').text == 'Спасибо за регистрацию!'
