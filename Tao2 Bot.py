import telegram
import requests
import time
from bs4 import BeautifulSoup
import datetime

url = "https://www.tao2korea.com/mall/m_search.php?ps_mode=search&url=m_mall_list.php&ps_search=%C1%A6%C1%B6%BB%E7&x=0&y=0"
http = requests.get(url).text

soup = BeautifulSoup(http, 'html5lib')
tags = soup.select("body > table > tbody > tr > td > table:nth-of-type(4) > tbody > tr > td:nth-of-type(2) > table:nth-of-type(4) > tbody > tr > td > table > tbody > tr > td > table > tbody > tr > td > b")
tag_old = tags[0]
tag_old = tag_old.text
print(tag_old)


bot = telegram.Bot(token='789952118:AAH3LMKetfaK0Gy4zlSKUUdMLLOIis8tAGI')

me = bot.getMe()
print(me)

chat_id = bot.getUpdates()[-1].message.chat.id
print('user id :', chat_id)
bot.sendMessage(chat_id, '실행')


while True:
    http = requests.get(url).text

    soup = BeautifulSoup(http, 'html5lib')
    tags = soup.select(
        "body > table > tbody > tr > td > table:nth-of-type(4) > tbody > tr > td:nth-of-type(2) > table:nth-of-type(4) > tbody > tr > td > table > tbody > tr > td > table > tbody > tr > td > b")
    tag_new = tags[0]
    tag_new = tag_new.text

    if int(tag_new) == int(tag_old):
        pass
    else:
        bot.sendMessage(chat_id, '사이트 변화 감지')
        break
    time.sleep(600)
