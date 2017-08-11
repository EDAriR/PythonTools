import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

url = "https://www.ptt.cc/bbs/BabyMother/M.1496905705.A.834.html"

res = requests.get(url, headers=headers)
res.encoding = "utf-8"
soup = BeautifulSoup(res.text, 'html.parser')

images = soup.select('a[href^=http://i.imgur.com]')

for image in images:
    img = urlopen(image['href'])
    name = image['href'].split('/')[3]

    #需建立資料夾images
    with open('./images/' + str(name), 'wb') as f:

        f.write(img.read())


