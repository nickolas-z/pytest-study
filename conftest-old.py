from pytest import fixture
from selenium import webdriver

@fixture(scope='session')
#@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser
    # Teardown
    print('I am tearing down this browser')

