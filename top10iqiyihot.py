#!/usr/bin/python3
import urllib.request
import ssl
import time
# import MySQLdb
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from pyvirtualdisplay import Display
from db import MySQL
database = MySQL()
ssl._create_default_https_context = ssl._create_unverified_context

#display = Display(visible=0, size=(800, 800))
#display.start()

path = "/usr/local/bin/chromedriver"
#path = "C:\\chromedriver\\chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('no-sandbox')
myDriver = webdriver.Chrome(path, chrome_options=chrome_options)
myDriver.get("http://top.iqiyi.com/rebobang.html")
time.sleep(5)
#房间名 房间号 主播名 主播号 人气值 印象标签 房间链接 房间封面
#while True:
soup = bs(myDriver.page_source, "html5lib")

#names = soup.find_all("span", {"class": "common_w-card_views-num"})
div = soup.find_all("dl", {"class": "fl clearfix topDetails-con"})


#popular_zy_top5
#print(div);
i = 1
for child in div:
     link = child.a['href']
     title = child.a['title']
     paltform = "爱奇艺"
     type = "hottop10"
     content = child.h3.string
     cover_pic = child.img['src']
     rank = i
     #ol = child.find("em", {"class": ""}).contents[0]
     ol = ""
     memo1 = child.find("em", {"class": "mr15"}).contents[0]
     ctime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

     database.query_dic({
         'insert': 'popular_zy_top5',
         'domain_array': [
             'title', 'link', 'paltform', 'type', 'content', 'cover_pic', 'rank', 'ol', 'memo1', 'ctime'
         ],
         'value_array': [
             title, link, paltform, type, content, cover_pic, rank, ol, memo1, ctime
         ]
     })
    #  print(title)
    #  print(link)
    #  print(paltform)
    #  print(content)
    #  print(cover_pic)
    #  print(rank)
    #  print(ol)
  
     i = i + 1
     if i >= 11:
         break

     #print(child.em[1].contents[0])
#     print(child.find("p", {"class": "common_w-card_title"}).contents[0])
#     print(child.find("span", {"class": "common_w-card_host-name"}).contents[0])

myDriver.close()
myDriver.quit()
#display.stop()
