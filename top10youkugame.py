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
myDriver.get("http://top.youku.com/rank/detail/?m=99&type=2")
myDriver.implicitly_wait(15)
time.sleep(15)
#房间名 房间号 主播名 主播号 人气值 印象标签 房间链接 房间封面
#while True:
soup = bs(myDriver.page_source, "lxml")

#names = soup.find_all("span", {"class": "common_w-card_views-num"})
div = soup.find("div", {"class": "exp-left"})
#print(div)
div1 = div.find_all("dl", limit=10)
#div = soup.find_all("div", {"class": "exp-left"})
#print(div1)

i = 1
for child in div1:
    link = child.a['href']
    title = child.img['title']
    paltform = "youku"
    type = "gametop10"
    content = title
    cover_pic = child.img['src']
    rank = i
    ol = child.find_all("dd", {"class": "detail"})[0].find("a").contents[0]
    memo1 = ''
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
    # print(link)
    # print(title)
    # print(paltform)
    # print(content)

    # i = i + 1
    # if i >= 11:
    #     break

     

myDriver.close()
myDriver.quit()
#display.stop()
