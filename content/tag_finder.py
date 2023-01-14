from utils.page_parser import parse_url


def extra_data():
    soup = parse_url()
    table = soup.find('div', {'class': 'table-responsive'}).find('table')
    table_content = []
    for tr in table.find('tbody').find_all('tr'):
        row_data = ["", "", "", ""]
        td = tr.find_all('td')
        for i in range(len(td) - 1):
            if i == 0:
                # i.e USD
                row_data[0] = td[i].text.strip()
            if i == 1:
                # i.e DOP
                row_data[1] = td[i].find('span', {'class': 'code'}).text.strip()
                # i.e Dominincan Republic
                row_data[2] = td[i].find('span', {'class': 'full'}).text.strip()
            if i == 2:
                # i.e 56.10
                row_data[3] = td[i].text.strip().replace(" ", "")
        table_content.append(row_data)
    return table_content
