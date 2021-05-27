from bs4 import BeautifulSoup
import requests
import sys
import re

url = "https://www.sedaily.com/NewsView/22MHYWSIAV"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"class":"article_view"})):
    print(line, end="")

