from bs4 import BeautifulSoup
import requests
import sys
import re

url = "http://www.ichannela.com/news/main/news_detailPage.do?publishId=000000251665"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"id":"articleSection"})):
    print(line, end="")

