# USD Exchange Rates Table

### Description
Displays a table containing USD exchange rate per country, as in the example below:

| Convert from  | Convert to | Country         | Rate       |
| ------ |------------|-----------------|------------|
| USD | ARS        | Argentine Peso  | 180.951    |
| USD | BSD        | Bahamian Dollar | 1          |

### Configuration
By default, the values will be scraped from https://www.exchange-rates.org/currentRates/A/USD.
To change it, modify `conf/config.ini`.

### Libraries
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) `4.11.1`
- [Requests](https://pypi.org/project/requests/) `2.28.2`
- [Tabulate](https://pypi.org/project/tabulate/) `0.9.0`

### Virtual Environment
In the command line, run `venv/Scripts/activate` to start the virtual environment.<br>
Run `deactivate` to stop it.
