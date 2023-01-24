import re

from content import read_selected_region_tab
from utils.config_reader import *


class TestUtils:
    def test_config_url(self):
        url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9(" \
                      ")@:%_\\+.~#?&\\/=]*)$"
        assert re.match(url_pattern, ConfigReader().get_url()) is not None, "The string in 'default_url' section is not a valid URL."

    def test_soup(self):
        soup = ConfigReader().get_soup()
        assert isinstance(soup, BeautifulSoup)

    def test_america_region_tab(self):
        c = ConfigReader.get_instance()
        c.set_region("america")
        assert read_selected_region_tab() == "North and South America"

    def test_asia_region_tab(self):
        c = ConfigReader.get_instance()
        c.set_region("asia")
        assert read_selected_region_tab() == "Asia and Pacific"

    def test_africa_region_tab(self):
        c = ConfigReader.get_instance()
        c.set_region("africa")
        assert read_selected_region_tab() == "Africa"

    def test_europe_tab(self):
        c = ConfigReader.get_instance()
        c.set_region("europe")
        assert read_selected_region_tab() == "Europe"

    def test_middle_east_tab(self):
        c = ConfigReader.get_instance()
        c.set_region("middle_east")
        assert read_selected_region_tab() == "Middle East and Central Asia"
