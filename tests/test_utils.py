import re

from utils.page_parser import *


class TestUtils:
    def test_default_url(self):
        url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9(" \
                      ")@:%_\\+.~#?&\\/=]*)$"
        url = read_config_url(ConfigFilePath.DEFAULT, 'default_url')
        assert re.match(url_pattern, url) is not None, "The string in 'default_url' section is not a valid URL."

    def test_invalid_config_file_path(self):
        valid_url = read_config_url(ConfigFilePath.DEFAULT, 'default_url')
        invalid_url = read_config_url("content/config.ini", 'default_url')
        assert valid_url == invalid_url

    def test_invalid_config_file_section(self):
        valid_url = read_config_url(ConfigFilePath.DEFAULT, 'default_url')
        invalid_url = read_config_url(ConfigFilePath.DEFAULT, 'my_urls')
        assert valid_url == invalid_url

    def test_soup(self):
        soup = prepare_soup()
        assert isinstance(soup, BeautifulSoup)
