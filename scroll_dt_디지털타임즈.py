from bs4 import BeautifulSoup
import requests
import sys
import re

url = "http://www.dt.co.kr/contents.html?article_no=2021052702109958044003"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"class":"art_txt"})):
    print(line, end="")

