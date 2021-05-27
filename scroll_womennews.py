from bs4 import BeautifulSoup
import requests
import sys
import re

url = "http://www.womennews.co.kr/news/articleView.html?idxno=211994"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"id":"article-view-content-div"})):
    print(line, end="")

