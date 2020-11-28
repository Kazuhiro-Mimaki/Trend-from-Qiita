import requests
from bs4 import BeautifulSoup
import json
import tweepy
import settings
import random

CK_KEY = settings.CK
CS_KEY = settings.CS
AT_KEY = settings.AT
AS_KEY = settings.AS
SLACK_WEB_HOOK = settings.SWH

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK_KEY, CS_KEY)
auth.set_access_token(AT_KEY, AS_KEY)
api = tweepy.API(auth)

# 取得するページ番号
page_number = random.randrange(1, 101)

programming = "%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0"
engineer = "%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2"

topics = [programming, engineer]
currentTopic = topics[random.randrange(0,2)]

qiitaUrl = f"https://qiita.com/search?page={page_number}&q={currentTopic}&sort=like"

res = requests.get(qiitaUrl)
soup = BeautifulSoup(res.text, "html.parser")

items = soup.find_all(class_="searchResult_main")

# 取得する記事の番号
item_number = random.randrange(0, 10)

title = items[item_number].find(class_="searchResult_itemTitle")
title_url = title.find("a")
url = title_url['href']
text = title.get_text() + '\n'
text += 'https://qiita.com' + url + '\n'
text += '\n'

print(text)

# twitterにpost
try:
  api.update_status(text)
except Exception as e:
  print(e)

# slackにpost
try:
  requests.post(SLACK_WEB_HOOK, data = json.dumps({
    'text': text,
    'unfurl_links': u'true',
    'username': u'Buzzrita',
    'icon_emoji': u':buzzrita:',
  }))
except Exception as e:
  print(e)