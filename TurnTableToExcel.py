import pandas
import requests
from bs4 import BeautifulSoup

# 抓取網址
url = "http://localhost:63342/imget/school.html?_ijt=14n42u2q8339kj1tbk9jhklpip"
# Table所在網頁前面
url2 = "https://www.caac.ccu.edu.tw/caac105/105apply_3qx_ColQry/"
res = requests.get(url)
# 編碼
res.encoding = "utf-8"
soup = BeautifulSoup(res.text, 'html.parser')
# 取得連結
a = soup.find_all('a')

for link in a:
    href = link.get("href")
    name = str(link).split(">")[1]
    n = name.split("<")[0]

    h = url2 + href
    dfs = pandas.read_html(h)
    cur = dfs[0]

    writer = pandas.ExcelWriter(n + '.xlsx')
    cur.to_excel(writer, 'Sheet5')
    writer.save()
