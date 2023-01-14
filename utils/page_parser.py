from bs4 import BeautifulSoup
from configparser import ConfigParser
import os
import requests
from utils.configuration_files import ConfigurationFile


def read_config_url(config_file, conf_section):
    if not isinstance(config_file, ConfigurationFile):
        print('Only values from ' + ConfigurationFile + " can be passed to this method. Reverting to DEFAULT.")
        config_file = ConfigurationFile.DEFAULT
    config = ConfigParser()
    file = os.getcwd() + config_file.value
    config.read(file)
    return config[conf_section].get('url')


def parse_url():
    requested_text = requests.get(read_config_url(ConfigurationFile.DEFAULT, 'default_url')).text
    return BeautifulSoup(requested_text, 'html.parser')
