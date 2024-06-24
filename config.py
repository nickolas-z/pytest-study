class Config:
    def __init__(self, env):
        SUPPORTED_ENVS = ['dev', 'qa']
        if env.lower() not in SUPPORTED_ENVS:
            raise ValueError(f'env must be one of {SUPPORTED_ENVS}')
        
        self.base_url = {
            'dev': 'https://www.google.com',
            'qa': 'https://www.amazon.com',
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 8081,
        }[env]