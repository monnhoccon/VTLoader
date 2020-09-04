from requests_html import HTMLSession
import requests
import time
from pathlib import Path
import json
import shutil

hostname ="https://truyentranh24.com"
session = HTMLSession()

def get_truyen(url):
  r = session.get(url)
  ten_truyen = r.html.find('h1',first=True).text
  return ten_truyen
def get_name_chap(url):
  r = session.get(url)
  name_chap = r.html.find('h1',first=True).text
  return name_chap

def get_id(url):
  r = session.get(url)
  chap_id = r.html.find('.manga-poster img', first=False)[0].attrs['data-id']
  return chap_id

def get_chap(id):
  url = "https://truyentranh24.com/api/mangas/"+id+"/chapters"
  headers = {
      'cookie': "__cfduid=d644a35bd029ddabbfd099344b57cf00c1598866363",
      'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41",
      'x-requested-with': "XMLHttpRequest",
      'referer': "https://truyentranh24.com/"
      }
  response = requests.request("GET", url, headers=headers)
  
  data = response.json()
  chap = data['chapters']
  slug_chap =[]
  for i in reversed(chap):
    slug_chap.append(i.get('slug'))
  return slug_chap

def get_img(chapter_url):
  r = session.get(chapter_url)
  get_img =r.html.find('.chapter-content img', first=False)
  limg = []
  for l in get_img:
    limg.append(l.attrs['data-src'])
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


  


      
        
      
  