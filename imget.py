import  requests, os
from  bs4 import  BeautifulSoup
from  urllib.request import urlopen

url = 'https://www.slideshare.net/ssuser438746/jcconf-2015-tw'
html = requests.get(url)
html.encoding = "utf-8"

sp = BeautifulSoup(html.text, 'html.parser')

img_dir = "images/"
if not os.path.exists(img_dir):
    os.mkdir(img_dir)

all_links = sp.find_all(['a', 'img'])
for link in all_links:
    src = link.get('src')
    href = link.get('href')
    attrs = [src, src]
    for attr in attrs:
        if attr != None and('.jpg' in attr or '.png' in  attr):
            full_path = attr
            filename = full_path.split('/')[-1]
            ext = filename.split('.')[-1]
            filename = filename.split('.')[-2]
            if 'jpg' in ext:
                filename = filename + '.jpg'
            else:
                print(filename)
            try:
                image = urlopen(full_path)
                f = open(os.path.join(img_dir, filename), 'wb')
                f.write(image.read())
                f.closed()
            except:
                print("{} cannt read!".format(filename))
