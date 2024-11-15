import requests

from bs4 import BeautifulSoup


#
l = requests.get('https://en.wikipedia.org/wiki/List_of_lakes_by_depth')
soup = BeautifulSoup(l.content,'html.parser')