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


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('no-sandbox')
myDriver = webdriver.Chrome(chrome_options=chrome_options)
myDriver.get("http://tv.sohu.com/hotshow/")

#房间名 房间号 主播名 主播号 人气值 印象标签 房间链接 房间封面
#while True:
soup = bs(myDriver.page_source, "html5lib")

#names = soup.find_all("span", {"class": "common_w-card_views-num"})
div = soup.find_all("ul", {"class": "rList"}, limit=2)[1]
div1 = div.find_all("li")
#print(div1)
i = 1
for child in div1:
    
    link = child.a["href"]
    title = child.a.string
    paltform = "sohu"
    type = "top5"
    content = title
    cover_pic = ''
    rank = i
    ol = child.find("span", {"class": "vTotal"}).contents[0]
    memo1 = child.find("span", {"class": "vRank"})["title"]
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
    i = i + 1
    if i >= 6:
        break

myDriver.close()
myDriver.quit()
#display.stop()
