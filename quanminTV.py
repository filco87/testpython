from bs4 import BeautifulSoup as bs
import urllib.request
import ssl
from selenium import webdriver
#ssl._create_default_https_context = ssl._create_unverified_context
#browser = webdriver.chromedriver()

#myDriver = webdriver.Firefox()
myDriver = webdriver.Chrome()
#myDriver.get("https://www.douyu.com/kpl")
myDriver.get("https://www.quanmin.tv/game/juediqiusheng")

#房间名 房间号 主播名 主播号 人气值 印象标签 房间链接 房间封面
#while True:
soup = bs(myDriver.page_source, "lxml")
#names = soup.find_all("span", {"class": "common_w-card_views-num"})
div = soup.find_all("div", {"class": "common_w-card"})
for child in div:
    print(child.a['href'])
    print(child.img['src'])
    print(child.find("span", {"class": "common_w-card_views-num"}).contents[0])
    print(child.find("p", {"class": "common_w-card_title"}).contents[0])
    print(child.find("span", {"class": "common_w-card_host-name"}).contents[0])
