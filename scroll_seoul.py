from bs4 import BeautifulSoup
import requests
import sys
import re

url = "http://www.seoul.co.kr/news/newsView.php?id=20210527500077"



response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.content.decode('euc-kr', 'replace'), 'html.parser')
for line in str(soup.find(attrs={"id":"atic_txt1"})):
    print(line, end="")
    

