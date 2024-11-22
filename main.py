import requests
import pandas as pd
import lxml
import html5lib

from json import dumps, loads
# Switching to Pandas instead of BS4.

url = 'https://en.wikipedia.org/wiki/List_of_lakes_by_depth'
dfs = pd.read_html(url)

#Walking through the object via Python showed that dfs[1] was the desired table.
deepest = dfs[1]
jobj = deepest.to_json()