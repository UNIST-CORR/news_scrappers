from bs4 import BeautifulSoup
import requests
import sys
import re

url = "https://www.hani.co.kr/arti/international/international_general/996891.html?_fr=mt1"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"class":"article-text-font-size"})):
    print(line, end="")

