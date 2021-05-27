from bs4 import BeautifulSoup
import requests
import sys
import re

url = "https://www.fnnews.com/news/202105270937315541"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"id":"article_content"})):
    print(line, end="")

