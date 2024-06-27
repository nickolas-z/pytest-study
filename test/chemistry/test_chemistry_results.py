from pytest import mark
import time

@mark.chemistry
class ChemistryTests:

    def test_result_1_completes_as_expected(self):
        time.sleep(5)
        print("Result 1 completed")
        assert True

    def test_result_2_completes_as_expected(self):
        time.sleep(5)
        print("Result 2 completed")
        assert True

    def test_result_3_completes_as_expected(self):
        time.sleep(5)
        print("Result 3 completed")
        assert True

    def test_result_4_completes_as_expected(self):
        time.sleep(5)
        print("Result 4 completed")
        assert True

