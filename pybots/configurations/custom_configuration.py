from pybots.configurations.base_configuration import BaseConfiguration


class CustomConfiguration(BaseConfiguration):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        super().__init__()
