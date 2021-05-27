from bs4 import BeautifulSoup
import requests
import sys
import re

url = "https://www.yna.co.kr/view/AKR20210525110500063?section=politics/all&site=major_news01"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"class":"story-news article"})):
    print(line, end="")

