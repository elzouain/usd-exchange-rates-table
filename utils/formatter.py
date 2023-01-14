from tabulate import tabulate

from content import tag_finder


def print_formatted_table():
    headers = ['Convert from', 'Convert to', 'Country', 'Rate']
    print(tabulate(tag_finder.extra_data(), headers=headers, tablefmt="fancy_grid", numalign='left'))