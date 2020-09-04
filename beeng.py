from requests_html import HTMLSession
from pathlib import Path
import requests
import time
import json
import shutil

hostname = 'https://beeng.net'
session = HTMLSession()

def get_chap(url):
  r = session.get(url)
  chap = r.html.find('.listChapters a', first=False)
  return chap
def get_truyen(url):
  r = session.get(url)
  name_chap = r.html.find('.detail h4', first=True).text
  return name_chap
def get_name_chap(url):
  r = session.get(url)
  name_chap = r.html.find('.comicDetail img', first=False)[1].attrs['alt']
  return name_chap

def get_img(chapter_url):
  r = session.get(chapter_url)
  get_img =r.html.find('.comicDetail img', first=False)
  limg = []
  for l in get_img:
    limg.append(l.attrs['src'])
  return limg

def dl_img(img_url,tentruyen,chapterfol,chap_url,numfile):
    vtm = img_url.split('.')[-1]
    filename = str(numfile+1) + '.' + vtm
    Path(tentruyen+"/"+chapterfol).mkdir(parents=True, exist_ok=True)
    headers = {
    'referer': chap_url,
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41"
    }
    response = requests.get(img_url,stream=True,headers=headers)
    file_img = open(tentruyen + "/" + chapterfol + "/" + filename, "wb")
    shutil.copyfileobj(response.raw, file_img)

