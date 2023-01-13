from bs4 import BeautifulSoup
from configparser import ConfigParser
from tabulate import tabulate
import requests

file = 'config.ini'
config = ConfigParser()
config.read(file)
URL = config['default'].get('url')

if __name__ == '__main__':
    soup = BeautifulSoup(requests.get(URL).text, 'html.parser')
    table = soup.find('div', {'class': 'table-responsive'}).find('table')
    all_content = []
    for tr in table.find('tbody').find_all('tr'):
        content = ["", "", "", ""]
        td = tr.find_all('td')
        for i in range(len(td) - 1):
            if i == 0:
                content[0] = td[i].text.strip()
            if i == 1:
                content[1] = td[i].find('span', {'class': 'code'}).text.strip()
                content[2] = td[i].find('span', {'class': 'full'}).text.strip()
            if i == 2:
                content[3] = td[i].text.strip().replace(" ", "")
        all_content.append(content)

    headerTitles = ['Convert from', 'Convert to', 'Country', 'Rate']
    print(tabulate(all_content, headers=headerTitles, tablefmt="fancy_grid", numalign='left'))
