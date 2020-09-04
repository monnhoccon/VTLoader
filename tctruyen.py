from requests_html import HTMLSession
import requests
import time
from pathlib import Path
import json
import shutil

hostname = 'https://tctruyen.com'
session = HTMLSession()

def get_chap(url):
  r = session.get(url)
  chapter_link =r.html.find('.comic-list-chapter div.box div a', first=False)
  return chapter_link
  #get all chapter

def get_truyen(url):
  r = session.get(url)
  name = r.html.find('.comic-description h1', first=True).text
  return name
  # get nam manga

def get_img(chapter_url):
  r = session.get(chapter_url)
  get_img =r.html.find('#contain-chapter img', first=False)
  limg = []
  for l in get_img:
    limg.append(l.attrs['data-src'])
  return limg
  #get all img in chapter

def dl_img(img_url,tentruyen,chapterfol,chap_url,namefile):
    Path(tentruyen + "/" + chapterfol).mkdir(parents=True, exist_ok=True)
    headers = {
      'referer': chap_url,
      'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44"
      }
    if(namefile==0):
      filename=str(namefile + 1)+".jpg"
      url = img_url.split("?")[0]
      querystring = {"data": img_url.split("=")[1]}
      response = requests.request("GET", img_url,stream=True, headers=headers, params=querystring)
    else:
      filename = str(namefile)+ '.jpg'
      response = requests.request("GET", img_url,stream=True, headers=headers)
    response.raw.decode_content = True
    file_img = open(tentruyen + "/" + chapterfol + "/" + filename, "wb")
    shutil.copyfileobj(response.raw, file_img)  

if __name__ == '__main__':
  url ="https://tctruyen.com/truyen-tranh/dai-chua-te"
  all_chap = get_chap(url)
  for chap in reversed(all_chap):
    chap_url = chap.attrs['href']
    chuong = chap_url.split("/")[-1].split(".")[0]
    print(chap_url)
    all_img = get_img(chap_url)
    for i in range(len(all_img)):
      print(i)
      link_img = all_img[i]
      print(link_img)
      if (link_img.find('data-comic') == 28):
        ai = i
      else:
        ai = i + 1
      dl_img(link_img,get_truyen(url),chuong,chap_url,ai)

      