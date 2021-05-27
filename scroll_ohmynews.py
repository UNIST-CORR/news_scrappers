from bs4 import BeautifulSoup
import requests
import sys
import re

url = "http://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0002746501&PAGE_CD=ET001&BLCK_NO=1&CMPT_CD=T0016"

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"class":"article_view"})):
    print(line, end="")

