from enum import Enum


class ConfigurationFile(Enum):
    DEFAULT = '/conf/config.ini'

    def __str__(self):
        return str(self.value)
