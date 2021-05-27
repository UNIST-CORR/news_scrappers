from bs4 import BeautifulSoup
import requests
import sys
import re

url = "https://www.hankyung.com/it/article/202105274858g"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"id":"articletxt"})):
    print(line, end="")

