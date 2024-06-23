# pytest-study
[Elegant Automation Frameworks with Python and Pytest](https://www.udemy.com/course/elegant-automation-frameworks-with-python-and-pytest/?couponCode=KEEPLEARNING)

## Sources
- [Git](https://github.com/nickolas-z/pytest-study)
- [claude promt about requirements.txt](https://claude.ai/chat/5f20c6eb-1a08-4a19-be9c-11e4e544e667)

To save requirements:
- pip freeze | grep -E 'pytest|selenium' > requirements.txt

To show list pkg:
- pip list

To install requirements:
- pip install -r requirements.txt

## Test with marker
```python
from pytest import mark
...
@mark.engine
```
```shell
pytest -m engine
pytest -m "engine or entertainment"
```
## Save results to file
- `pytest --html="results.html"`
- `pytest --junitxml="results.xml"`

# References
- [Full pytest documentation](https://docs.pytest.org/en/7.1.x/contents.html)
- [Fixture availability](https://docs.pytest.org/en/7.1.x/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files)