import requests
import tweepy
import random
from bs4 import BeautifulSoup
from config import Congfig


# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(Congfig.CONSUMER_KEY, Congfig.CONSUMER_SECRET)
auth.set_access_token(Congfig.ACCESS_TOKEN_KEY, Congfig.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# 取得するページ番号
page_number = random.randrange(1, 101)

programming = "%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0"
engineer = "%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2"

topics = [programming, engineer]
currentTopic = topics[random.randrange(0,2)]

qiitaUrl = f"{Congfig.QIITA_URL}/search?page={page_number}&q={currentTopic}&sort=like"

res = requests.get(qiitaUrl)
soup = BeautifulSoup(res.text, "html.parser")

items = soup.find_all(class_="searchResult_main")

# 取得する記事の番号
item_number = random.randrange(0, 10)

title = items[item_number].find(class_="searchResult_itemTitle")
title_url = title.find("a")
url = title_url['href']
text = title.get_text() + '\n'
text += f'{Congfig.QIITA_URL}{url}\n\n'
