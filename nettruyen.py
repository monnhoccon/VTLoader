from requests_html import HTMLSession
import requests
import time
from pathlib import Path
import json
import shutil

hostname = 'http://www.nettruyen.com & http://nhattruyen.com'
session = HTMLSession()

def get_chap(url):
  r = session.get(url)
  chapter_link =r.html.find('.list-chapter ul li a', first=False)
  return chapter_link
  #get all chapter

def get_img(url):
  r = session.get(url)
  data =r.html.find('.reading-detail img', first=False)
  list_img=[]
  for i in data:
    get_i = i.attrs
    if(hasattr(get_i, 'data-cdn') == False):
      list_img.append(i.attrs['src'])
    else:
      list_img.append(i.attrs['data-cdn'])  
  return list_img
  #get all img in chapter

def get_truyen(url):
  r = session.get(url)
  name = r.html.find('h1', first=True).text
  return name
  # get nam manga

def get_name_chap(url):
  r = session.get(url)
  name_chap = r.html.find('.txt-primary span', first=True).text
  return name_chap
  
def dl_img(img_url,tentruyen,chapterfol,chap_url):
    filename = img_url.split('/')[-1]
    Path(tentruyen+"/"+chapterfol).mkdir(parents=True, exist_ok=True)
    headers = {
    'referer': chap_url,
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41"
    }
    response = requests.get(img_url,stream=True,headers=headers)
    file_img = open(tentruyen + "/" + chapterfol + "/" + filename, "wb")
    shutil.copyfileobj(response.raw, file_img)

if __name__ == '__main__':
  url = 'http://nhattruyen.com/truyen-tranh/nguoi-choi-loi-28854'
  all_chap = get_chap(url)
  for chap in reversed(all_chap):
    chap_url = chap.attrs['href']
    all_img = get_img(chap_url)
    for i in all_img:
      dl_img(i,get_truyen(url),get_name_chap(chap_url).split('-')[1],chap_url)