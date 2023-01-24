import getopt
import os, requests
import sys
from configparser import ConfigParser
from bs4 import BeautifulSoup
from utils.configuration_files import ConfigFilePath


class ConfigReader(object):
    __config_file_path = ConfigFilePath.DEFAULT
    __instance = None
    __max_rows = None
    __region = "america"
    __soup = None
    __url = None

    @staticmethod
    def get_instance():
        if ConfigReader.__instance is None:
            ConfigReader()
        return ConfigReader.__instance

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(ConfigReader, cls).__new__(cls)
            cls.__instance.set_region(cls.__instance.read_sys_args().get("-r"))
            cls.__instance.set_max_rows(cls.__instance.read_sys_args().get("-m"))
        return cls.__instance

    def get_max_rows(self):
        return self.__max_rows

    def get_region(self):
        return self.__region

    def get_soup(self):
        return self.__soup

    def get_url(self):
        return self.__url

    def set_max_rows(self, rows):
        self.__max_rows = rows

    def set_region(self, region):
        self.__region = region
        self.__url = self.parse_config_url()
        self.__soup = self.make_soup()

    def make_soup(self):
        requested_text = requests.get(self.__url).text
        return BeautifulSoup(requested_text, 'html.parser')

    def parse_config_url(self):
        config = ConfigParser()
        file = os.getcwd() + self.__config_file_path.value
        config.read(file)
        return config["urls"].get(self.__region)

    @staticmethod
    def read_sys_args():
        default_values = {"-r": "america", "-m": 15}
        try:
            opts, args = getopt.getopt(sys.argv[1:], "r:m:")
            if len(opts) == 0:
                raise Exception()
            else:
                for o, a in opts:
                    if o == "-r":
                        r_temp = {"-r": a}
                        default_values.pop("-r")
                        default_values.update(r_temp)
                    if o == "-m":
                        m_temp = {"-m": int(a)}
                        default_values.pop("-m")
                        default_values.update(m_temp)
        except Exception as err:
            print(err)
        return default_values
