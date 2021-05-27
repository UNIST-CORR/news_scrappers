from bs4 import BeautifulSoup
import requests
import sys
import re

url = "https://www.news1.kr/articles/?4320087"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.content.decode('utf-8', 'replace'), 'html.parser')
for line in str(soup.find(attrs={"class":"detail sa_area"})):
    print(line, end="")

