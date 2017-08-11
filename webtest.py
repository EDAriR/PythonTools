import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

url = "https://web.sun2u.com/Login"

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')

# a = soup.findAll("div", {"class": "thumbnailWithOverlay"})

# for image in a:https://web.sun2u.com/Login
#     # image = urlopen(a['src'])
#     name = a['href'].split('/')[0]
print(soup)

'''
# 編碼
res.encoding = "utf-8"
a = soup.findAll("a", {"class": "qa-item-subject-link"})
span = soup.select('span[class^=hl]')
author = soup.select('div[class^=author]')
date = soup.select('div[class^=date]')
title = soup.select('div[class^=title]')

for s in span:

    i=0
    j=i+1
    print(s)
    print("--------")
    print(title[j])
    print("--------")
    print(span[j])
    print("--------")'''

'''for image in images:
    img = urlopen(image['href'])
    name = image['href'].split('/')[3]

    with open('./images/' + str(name), 'wb') as f:
        f.write(img.read())'''
