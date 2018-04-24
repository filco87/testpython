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
myDriver.get("http://top.youku.com/rank/detail/?m=85&type=1")

#房间名 房间号 主播名 主播号 人气值 印象标签 房间链接 房间封面
#while True:
soup = bs(myDriver.page_source, "lxml")

#names = soup.find_all("span", {"class": "common_w-card_views-num"})
div = soup.find("div", {"class": "exp-left"})
print(div)
div1 = div.find_all("dl")
#div = soup.find_all("div", {"class": "exp-left"})
#print(div1)

i = 1
for child in div1:
    link = child.a['href']
    title = child.img['title']
    paltform = "youku"
    type = "top5"
    content = title
    cover_pic = child.img['src']
    rank = i
    ol = child.find("dd", {"class": "detail"}).find_all("a")[1]
    # # # #  memo1 = child.find("em", {"class": "mr15"}).contents[0]
    # # # ctime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(link)
    print(title)
    print(paltform)
    print(type)
    print(cover_pic)
    print(ol)
    i = i + 1
    if i >= 6:
        break
    #  database.query_dic({
    #      'insert': 'popular_zy_top5',
    #      'domain_array': [
    #          'title', 'link', 'paltform', 'type', 'content', 'cover_pic', 'rank', 'ol', 'memo1', 'ctime'
    #      ],
    #      'value_array': [
    #          title, link, paltform, type, content, cover_pic, rank, ol, memo1, ctime
    #      ]
    #  })
    #print(child.a['href'])
    #  print(child.a['title'])
    #  print(child.h3.string)
    #  print(child.img['src'])
    #  print(child.find("em", {"class": "mr15"}).contents[0])
    #  print(child.find("em", {"class": ""}).contents[0])
    #  #                 ).next_sibling.next_sibling.contents[0])
    #  #print(child.find("p").find("em")[1].contents[0]) next_sibling
     #if child.find("a", {"class": "name"}).contents[0] is None:
    
    #  link = child.find("a", {"class": "name"})['href']
    #  title = child.find("a", {"class": "name"})['title']
    #  paltform = "腾讯"
    #  type = "top5"
    #  content = title
    #  cover_pic = ''
    #  rank = i
    #  ol = child.find("div", {"class": "bar"}).span['style'][7:]
    #  memo1 = ''
    #  ctime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    #  database.query_dic({
    #      'insert': 'popular_zy_top5',
    #      'domain_array': [
    #          'title', 'link', 'paltform', 'type', 'content', 'cover_pic', 'rank', 'ol', 'memo1', 'ctime'
    #      ],
    #      'value_array': [
    #          title, link, paltform, type, content, cover_pic, rank, ol, memo1, ctime
    #      ]
    #  })
    

     

myDriver.close()
myDriver.quit()
#display.stop()
