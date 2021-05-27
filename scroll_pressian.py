from bs4 import BeautifulSoup
import requests
import sys
import re

url = "https://www.pressian.com/pages/articles/2021052715232357309#0DKU"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"class":"article_body"})):
    print(line, end="")

