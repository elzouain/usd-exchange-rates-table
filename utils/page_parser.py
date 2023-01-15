from bs4 import BeautifulSoup
from configparser import ConfigParser
import os
import requests
from utils.configuration_files import ConfigFilePath


def read_config_url(config_file, conf_section):
    if not isinstance(config_file, ConfigFilePath):
        print('Only values from ' + ConfigFilePath + " can be passed to this function. Reverting to DEFAULT path.")
        config_file = ConfigFilePath.DEFAULT
    config = ConfigParser()
    file = os.getcwd() + config_file.value
    config.read(file)
    return config[conf_section].get('url')


def prepare_soup():
    requested_text = requests.get(read_config_url(ConfigFilePath.DEFAULT, 'default_url')).text
    return BeautifulSoup(requested_text, 'html.parser')
