import json
from pytest import fixture
from selenium import webdriver

data_path = 'test_data.json'

def load_test_data(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data

# @fixture(scope='session')
@fixture(params=[webdriver.Chrome, webdriver.Edge])
def chrome_browser(request):
    driver = request.param
    drvr = driver()
    # browser = webdriver.Chrome()
    yield drvr
    drvr.quit()

@fixture(params=load_test_data(data_path))
def tv_brand(request):
    data = request.param
    return data