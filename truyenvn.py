from requests_html import HTMLSession
import requests
import time
from pathlib import Path
import json
import shutil

hostname = 'https://truyenvn.com'
session = HTMLSession()

def get_chap(url):
  r = session.get(url)
  chapter_link =r.html.find('#chapterList a', first=False)
  return chapter_link
  #get all chapter

def get_id(url):
  r = session.get(url)
  chapter_id =r.html.find('.comment-form input', first=False)[4].attrs['value']
  return chapter_id
  #get id chapter for get images

def get_img(chapter_id):
  url = "https://truyenvn.com/wp-admin/admin-ajax.php"
  payload = "action=z_do_ajax&_action=load_imgs_for_chapter&p="+str(chapter_id)
  headers = {
      'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0",
      'accept': "application/json, text/javascript, /; q=0.01",
      'accept-language': "en-US,en;q=0.5",
      'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
      'x-requested-with': "XMLHttpRequest",
      'origin': "https://truyenvn.com/",
      'connection': "keep-alive",
      }
  response = requests.request("POST", url, data = payload, headers = headers)
  json_response=response.json()
  data = json_response.get('mes')
  list_img=[]
  for i in data:
      list_img.append(i.get('url'))
  return list_img
  #get all img in chapter

def get_truyen(url):
  r = session.get(url)
  name = r.html.find('.info h1', first=True).text
  return name
  # get nam manga

def get_name_chap(url):
  r = session.get(url)
  name_chap = r.html.find('.name span', first=True).text
  return name_chap
  
def dl_img(img_url,tentruyen,chapterfol,chap_url,namefile):
    vtm = img_url.split('.')[-1]
    filename = str(namefile+1) + '.' + vtm
    Path(tentruyen+"/"+chapterfol).mkdir(parents=True, exist_ok=True)
    headers = {
    'referer': chap_url,
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41"
    }
    response = requests.get(img_url,stream=True,headers=headers)
    file_img = open(tentruyen + "/" + chapterfol + "/" + filename, "wb")
    shutil.copyfileobj(response.raw, file_img)

