from bs4 import BeautifulSoup
import requests
import sys
import re

url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=009&aid=0004799256"

def isHangul(text):
    #Check the Python Version
    pyVer3 =  sys.version_info >= (3, 0)

    if pyVer3 : # for Ver 3 or later
        encText = text
    else: # for Ver 2.x
        if type(text) is not unicode:
            encText = text.decode('utf-8')
        else:
            encText = text

    hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', encText))

    if text == ' ':
        return True

    return hanCount > 0

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
soup = BeautifulSoup(response.text, "html.parser")
for line in str(soup.find(attrs={"id":"articleBodyContents"})):
    if isHangul(line):
        print(line, end="")

