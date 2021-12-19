import requests
import tweepy
import random
from bs4 import BeautifulSoup
from config import Congfig


# Twitterオブジェクトの生成
class TwitterClient:
  def __init__(self):
    self.auth = tweepy.OAuthHandler(Congfig.CONSUMER_KEY, Congfig.CONSUMER_SECRET)
    self.auth.set_access_token(Congfig.ACCESS_TOKEN_KEY, Congfig.ACCESS_TOKEN_SECRET)
    self.api = tweepy.API(self.auth)
  
  def scraping(self):
    page_number = random.randrange(1, 101)

    programming = "%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0"
    engineer = "%E3%82%A8%E3%83%B3%E3%82%B8%E3%83%8B%E3%82%A2"

    topics = [programming, engineer]
    currentTopic = topics[random.randrange(0,2)]

    qiitaUrl = f"{Congfig.QIITA_URL}/search?page={page_number}&q={currentTopic}&sort=like"

    res = requests.get(qiitaUrl)
    soup = BeautifulSoup(res.text, "html.parser")

    items = soup.find_all(class_="searchResult_main")

    item_number = random.randrange(0, 10)

    title = items[item_number].find(class_="searchResult_itemTitle")
    title_url = title.find("a")
    url = title_url['href']
    text = f'{title.get_text()}\n{Congfig.QIITA_URL}{url}\n\n'
    return text
