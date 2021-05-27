from bs4 import BeautifulSoup
import requests
import sys
import re

url = "https://www.yonhapnewstv.co.kr/news/MYH20210527013400038"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"id":"articleBody"})):
    print(line, end="")

