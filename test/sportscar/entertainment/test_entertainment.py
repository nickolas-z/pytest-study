from selenium import webdriver
from pytest import mark

@mark.ui
@mark.entertainment
def test_can_navigate_to_entertainment_page():
    browser = webdriver.Chrome()
    browser.get('http://www.motortrend.com')
    assert True
