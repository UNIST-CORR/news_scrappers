from bs4 import BeautifulSoup
import requests
import sys
import re

url = "https://www.ytn.co.kr/_ln/0108_202105271454369686"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"class":"article"})):
    print(line, end="")

