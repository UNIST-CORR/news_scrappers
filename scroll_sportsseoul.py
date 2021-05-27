from bs4 import BeautifulSoup
import requests
import sys
import re

url = "http://www.sportsseoul.com/news/read/1044252"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"class":"news_text"})):
    print(line, end="")

