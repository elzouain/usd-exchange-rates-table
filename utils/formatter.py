from tabulate import tabulate
from content import dom_scraper, find_selected_region


def print_formatted_table():
    headers = ['Convert from', 'Convert to', 'Country', 'Rate']
    print('\n{} USD CONVERSION RATES IN {} {}'.format("-" * 10, find_selected_region().upper(), "-" * 10))
    print(tabulate(dom_scraper.extract_rates_data(), headers=headers, tablefmt="fancy_grid", numalign='left'))
