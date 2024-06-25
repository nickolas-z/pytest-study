
from pytest import mark

@mark.tv
class TelevisionTests:
    def test_television_turns_on(self, tv_brand):
        print(f"TV is on: {tv_brand}")
    @mark.skip
    def test_browser_can_navigate_to_training_ground(self, chrome_browser):
        chrome_browser.get('https://techstepacademy.com/training-ground')
        assert True