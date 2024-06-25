
from pytest import mark

@mark.env
class EnvTests:
    @mark.wip(reason='Work in progress')
    def test_enviroment_is_dev(self, app_config):
        assert app_config.base_url == 'https://www.google.com'
        assert app_config.app_port == 8080

    @mark.skip(reason='Not a dev environment')
    def test_enviroment_is_qa(self, app_config):
        assert app_config.base_url == 'https://www.amazon.com'
        assert app_config.app_port == 8081

    @mark.xfail(reason='Env is not a stage')
    def test_enviroment_is_staging(self, app_config):
        base_url = app_config.base_url
        assert base_url == 'staging'
        # assert app_config.app_port == 8080