import time


def test_check_button_add(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_css_selector(".btn-add-to-basket"), "Button not found"