import requests
from bs4 import BeautifulSoup
import json

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
  post_slack(webhook_url, text)