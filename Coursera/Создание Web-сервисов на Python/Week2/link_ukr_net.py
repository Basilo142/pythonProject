from bs4 import BeautifulSoup
import requests
result = requests.get('https://www.ukr.net/')
html = result.text
soup = BeautifulSoup(html, 'lxml')
topic = [
    section for section in soup.find_all('h2', 'feed__section--title')
]
print(result.text)