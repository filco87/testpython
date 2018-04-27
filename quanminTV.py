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

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('no-sandbox')


myDriver = webdriver.Chrome(path,chrome_options=chrome_options)
myDriver.get("https://www.quanmin.tv/game/all")
myDriver.implicitly_wait(10)
#房间名 房间号 主播名 主播号 人气值 印象标签 房间链接 房间封面
#while True:
soup = bs(myDriver.page_source, "lxml")

#names = soup.find_all("span", {"class": "common_w-card_views-num"})
i = 1
div = soup.find_all("div", {"class": "common_w-card"},limit = 20)
for child in div:
     #link = child.a['href']
     title = child.find("p", {"class": "common_w-card_title"}).contents[0]
     paltform = "全民TV"
     type = "热度"
     content = child.find("a", {"class": "common_w-card_category"}).contents[0]
     cover_pic = child.img['src']
     rank = i
     ol = child.find("span", {"class": "common_w-card_views-num"}).contents[0]
     
     ctime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
     nickname = child.find("span", {"class": "common_w-card_host-name"}).contents[0]
     roomnum = child.find(
         "a", {"class": "common_w-card_href"})['href'][17:]
     roomname = title
     chour = time.strftime('%Y-%m-%d %H', time.localtime(time.time()))
     database.query_dic({
         'insert': 'popular_feelings_data',
         'domain_array': [
             'title', 'paltform', 'type', 'content', 'cover_pic', 'rank', 'ol',  'ctime',  'nickname',  'room_number',  'room_name',  'chour'
         ],
         'value_array': [
             title, paltform, type, content, cover_pic, rank, ol,  ctime, nickname, roomnum, roomname,chour
         ]
     })
     
myDriver.close()
myDriver.quit()
#display.stop()
