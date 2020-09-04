from requests_html import HTMLSession
from pathlib import Path
import requests
import time
import json
import shutil

hostname = 'http://truyenqq.com'
session = HTMLSession()

def get_chap(url):
  r = session.get(url)
  chapter_link =r.html.find('.works-chapter-list a', first=False)
  return chapter_link
def get_truyen(url):
  r = session.get(url)
  tentruyen =r.html.find('.block01 h1', first=True).text
  return tentruyen
def get_name_chap(url):
  r = session.get(url)
  name_chap =r.html.find('h1', first=True).text
  return name_chap
def get_img(chapter_url):
  r = session.get(chapter_url)
  get_img =r.html.find('.story-see-content img', first=False)
  limg = []
  for l in get_img:
    limg.append(l.attrs['src'])
  return limg

def dl_img(img_url,tentruyen,chapterfol,chap_url,numfile):
    filename = str(numfile+1) + '.jpg'
    Path(tentruyen+"/"+chapterfol).mkdir(parents=True, exist_ok=True)
    headers = {
    'referer': chap_url,
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41"
    }
    response = requests.get(img_url,stream=True,headers=headers)
    file_img = open(tentruyen + "/" + chapterfol + "/" + filename, "wb")
    shutil.copyfileobj(response.raw, file_img)

      
  