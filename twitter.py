import tweepy
import scraping
from scraping import TwitterClient

twitterClient = TwitterClient()

# twitterにpost
try:
  twitterClient.api.update_status(twitterClient.scraping())
except Exception as e:
  print(e)
  raise e