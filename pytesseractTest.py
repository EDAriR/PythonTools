# python的验证码识别的工具。是一个很好用图像识别的工具pytesseract

from PIL import Image
import pytesseract as ocr
import urllib.request as urlreq
from io import BytesIO

from PIL import Image
import pytesseract


def img_to_str(image_path, lang='chi_tra'):
    return pytesseract.image_to_string(Image.open(image_path), lang)


print(img_to_str('image2/10.jpg', lang='chi_tra'))
# resp = urlreq.urlopen('http://www.wisedream.net/res/img/ocr-test.png')
# img = Image.open("D:\EDPython\PythonTools\image2\1.jpg")
# print(ocr.image_to_string(img, lang='chi_sim'))
