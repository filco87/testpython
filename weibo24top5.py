#!/usr/bin/python3
import urllib.request
import ssl
# import MySQLdb
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from pyvirtualdisplay import Display

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('no-sandbox')
myDriver = webdriver.Chrome(chrome_options=chrome_options)
myDriver.get("https://weibo.com/?category=99991")
myDriver.implicitly_wait(10)
#房间名 房间号 主播名 主播号 人气值 印象标签 房间链接 房间封面
#while True:
soup = bs(myDriver.page_source, "html5lib")
print(soup.prettify())
#names = soup.find_all("span", {"class": "common_w-card_views-num"})
div = soup.find_all("div", {"class": "UG_nav"})
print(div)
for child in div:
    print('')
    #print(child.img['src'])
    #print(child.find("span", {"class": "common_w-card_views-num"}).contents[0])
    #print(child.find("p", {"class": "common_w-card_title"}).contents[0])
    #print(child.find("span", {"class": "common_w-card_host-name"}).contents[0])
    #print(child.find("h3", {"class": "list_title_s"}).contents[0])

myDriver.close()
myDriver.quit()
#display.stop()
