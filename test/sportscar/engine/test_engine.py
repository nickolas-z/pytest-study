import time
from pytest import mark

@mark.ui
@mark.smoke
@mark.engine
def test_can_navigate_to_engine_page(chrome_browser):
    first_browser = chrome_browser
    first_browser.get('https://www.amazon.com/')
    time.sleep(2)
    second_browser = chrome_browser
    second_browser.get('https://www.google.com/')
    time.sleep(2)
    assert True
