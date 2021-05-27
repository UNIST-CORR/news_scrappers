from bs4 import BeautifulSoup
import requests
import sys
import re

url = "https://www.wowtv.co.kr/NewsCenter/News/Read?menuSeq=459&subMenu=latest&wowcode=&Class=&articleId=AKR20210527136200009"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"class":"box-news-body"})):
    print(line, end="")

