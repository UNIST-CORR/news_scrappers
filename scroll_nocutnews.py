from bs4 import BeautifulSoup
import requests
import sys
import re

url = "https://www.nocutnews.co.kr/news/5560124_%EA%B2%BD%EC%B0%B0-%EC%82%AC%EC%B9%AD%EA%B9%8C%EC%A7%80%E2%80%A6%EB%8F%84-%EB%84%98%EB%8A%94-%E6%95%85%EC%86%90%EC%A0%95%EB%AF%BC-%EA%B0%80%EC%A7%9C%EB%89%B4%EC%8A%A4"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"id":"pnlContent"})):
    print(line, end="")

