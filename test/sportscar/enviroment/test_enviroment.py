
from pytest import mark

@mark.env
class EnvTests:
    def test_enviroment_is_qa(self, app_config):
        # if env == 'dev':
        #     print('This is a dev environment')
        # assert env == 'qa'
        assert app_config.base_url == 'https://www.amazon.com'
        assert app_config.app_port == 8081

    def test_enviroment_is_dev(self, app_config):
        # if env == 'qa':
        #     print('This is a qa environment')
        # assert env == 'dev'    
        assert app_config.base_url == 'https://www.google.com'
        assert app_config.app_port == 8080