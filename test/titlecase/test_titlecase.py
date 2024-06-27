from pytest import mark
from titlecase import title_case

@mark.titlecase
class TitleCaseTests:
    def test_lower_text_is_uppercased(self):
        initial_text = 'this is no test'
        expected_text = 'This Is No Test'
        returned_text = title_case(initial_text)
        assert returned_text == expected_text
