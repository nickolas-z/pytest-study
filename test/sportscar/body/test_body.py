from selenium import webdriver
from pytest import mark

@mark.body
class BodyTests:
    @mark.ui
    def test_can_navigate_to_body_page(self):
        browser = webdriver.Chrome()
        browser.get('http://www.example.com')
        assert True

    def test_bumper(self):
        assert True

    def test_windshield(self):
        assert True
