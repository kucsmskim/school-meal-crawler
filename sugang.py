import requests
from bs4 import BeautifulSoup

url = 'http://sugang.korea.ac.kr/'
source_code = requests.get(url)
html = source_code.content
print(html)