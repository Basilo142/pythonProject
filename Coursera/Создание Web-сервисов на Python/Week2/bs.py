import requests
resp = requests.get('http://wikipedia.org/')
html = resp.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
tags = soup('a', 'other-project-link')
print(tags)
