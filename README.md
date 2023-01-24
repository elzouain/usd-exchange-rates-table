# USD Exchange Rates Table

### Description
Displays a table containing USD exchange rate per country, as in the example below:

| Convert from  | Convert to | Country         | Rate       |
| ------ |------------|-----------------|------------|
| USD | ARS        | Argentine Peso  | 180.951    |
| USD | BSD        | Bahamian Dollar | 1          |

### Usage
Simply run `py main.py`.<br>
You can change the region by using the `-r <region>` flag (default = america).<br>
The possible options include:
- `africa`
- `america`
- `asia`
- `europe`
- `middle_east`

You can also set the max amount of rows using the `-m <row_count>` flag.<br>
The available URLs are contained in `/conf/config.ini` 

### Libraries
- [Python](https://www.python.org/) `3.11.1`
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) `4.11.1`
- [pytest](https://docs.pytest.org/en/7.2.x/contents.html) `7.2.1`
- [Requests](https://pypi.org/project/requests/) `2.28.2`
- [Tabulate](https://pypi.org/project/tabulate/) `0.9.0`

### Virtual Environment
In the command line, run `venv/Scripts/activate` to start the virtual environment.
Use `deactivate` to stop it.<br>
On Windows PowerShell, if you get the `UnauthorizedAccess` error, run `Set-ExecutionPolicy remotesigned`.

### Testing
Run `pytest .` to execute tests.
