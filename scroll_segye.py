from bs4 import BeautifulSoup
import requests
import sys
import re

url = "https://www.segye.com/newsView/20210527512460"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"class":"viewBox"})):
    print(line, end="")

