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
#chrome_options.add_argument('user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"')
myDriver = webdriver.Chrome(path, chrome_options=chrome_options)
myDriver.get("https://v.qq.com/x/hotlist/search/?channel=10001")
time.sleep(5)
#房间名 房间号 主播名 主播号 人气值 印象标签 房间链接 房间封面
#while True:
soup = bs(myDriver.page_source, "html5lib")

#names = soup.find_all("span", {"class": "common_w-card_views-num"})
div = soup.find_all("li", {"class": "item_list"})


#popular_zy_top5
#print(div);
i = 1
for child in div:
     if i == 1:
        i = i + 1
        continue
     link = child.find("a", {"class": "name"})['href']
     title = child.find("a", {"class": "name"})['title']
     paltform = "腾讯"
     type = "hottop10"
     content = title
     cover_pic = ''
     rank = i - 1
     ol = child.find("div", {"class": "bar"}).span['style'][7:]
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
    #  print(link)
    #  print(title)
    #  print(paltform)
    #  print(content)
     i = i + 1
     if i >= 12:
         break


myDriver.close()
myDriver.quit()
#display.stop()
