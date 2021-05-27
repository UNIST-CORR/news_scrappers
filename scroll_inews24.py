from bs4 import BeautifulSoup
import requests
import sys
import re

url = "http://www.inews24.com/view/1370694"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"id":"articleBody"})):
    print(line, end="")

