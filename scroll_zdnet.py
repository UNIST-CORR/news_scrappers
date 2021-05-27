from bs4 import BeautifulSoup
import requests
import sys
import re

url = "https://zdnet.co.kr/view/?no=20210526144409"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"id":"content-20210526144409"})):
    print(line, end="")

