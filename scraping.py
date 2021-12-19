import requests
import tweepy
import random
from bs4 import BeautifulSoup
from config import Congfig
from urllib.parse import quote

keyword_list = ["プログラミング", "エンジニア"]
url_encoded_keyword_list = [quote(keyword) for keyword in keyword_list]

class ScrapingClient:
  def __init__(self):
    self.auth = tweepy.OAuthHandler(Congfig.CONSUMER_KEY, Congfig.CONSUMER_SECRET)
    self.auth.set_access_token(Congfig.ACCESS_TOKEN_KEY, Congfig.ACCESS_TOKEN_SECRET)
    self.api = tweepy.API(self.auth)

  def scraping(self):
    page_number = random.randrange(1, 101)
    currentTopic = url_encoded_keyword_list[random.randrange(0,2)]
    qiitaUrl = f"{Congfig.QIITA_URL}/search?page={page_number}&q={currentTopic}&sort=like"
    try:
      res = requests.get(qiitaUrl)
      soup = BeautifulSoup(res.text, "html.parser")
      items = soup.find_all(class_="searchResult_main")
      return self.parse(items)
    except Exception as e:
      print(e)
      raise e
  
  def parse(self, items):
    item_number = random.randrange(0, 10)
    title = items[item_number].find(class_="searchResult_itemTitle")
    title_url = title.find("a")
    url = title_url['href']
    return f'{title.get_text()}\n{Congfig.QIITA_URL}{url}\n\n'