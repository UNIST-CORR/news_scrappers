from bs4 import BeautifulSoup
import requests
import sys
import re

url = "http://www.kwnews.co.kr/nview.asp?s=101&aid=221052600157"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"id":"kwnews_body"})):
    print(line, end="")

