from bs4 import BeautifulSoup
import requests
import sys
import re

url = "https://www.edaily.co.kr/news/read?newsId=02840486629053184&mediaCodeNo=257"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"class":"news_body"})):
    print(line, end="")

