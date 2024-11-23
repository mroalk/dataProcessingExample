import requests
import pandas as pd
import lxml
import html5lib

from json import dumps, loads

from pandas.io.stata import stata_epoch

# Goals:
# 1. Scrape table from a website.
# 2. Load into Pandas
# 3. Clean DF
# 4. Convert into json/exportable format.
# 5. Find way to programmatically load into Tableau for presentation?

# Lakes touch multiple countries. Idea won't work.
#url = 'https://en.wikipedia.org/wiki/List_of_lakes_by_depth'
url = 'https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States'
dfs = pd.read_html(url)

# Walking through the object via Python showed that dfs[2] was the desired table.
stateCapitals = dfs[2]
# Removing columns we aren't going to use.
stateCapitalsTrimmed = stateCapitals.drop(
    [('Population (2020 US Census)','CSA'),('Population (2020 US Census)','MSA/μSA')],
    axis=1)
# Flattening the Multi-index since it no longer holds value.
stateCapitalsTrimmed.columns = stateCapitalsTrimmed.columns.get_level_values(0)

# Splitting
jobj = stateCapitals.to_json()