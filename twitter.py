import requests
from bs4 import BeautifulSoup
import json
import tweepy
import settings

CK_KEY = settings.CK
CS_KEY = settings.CS
AT_KEY = settings.AT
AS_KEY = settings.AS

# Twitterオブジェクトの生成
auth = tweepy.OAuthHandler(CK_KEY, CS_KEY)
auth.set_access_token(AT_KEY, AS_KEY)
api = tweepy.API(auth)

qiitaUrl = "https://qiita.com/"

item_json = []
result = []

res = requests.get(qiitaUrl)

soup = BeautifulSoup(res.text, "html.parser")

items = soup.find_all(class_="tr-Item")

for item in items[0:3]:
  title = item.find(class_="tr-Item_title")
  url = title['href']
  text = title.get_text() + '\n'
  text += url + '\n'
  text += '\n'
  api.update_status(text)