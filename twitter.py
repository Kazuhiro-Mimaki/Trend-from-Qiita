import tweepy
import scraping

# twitterにpost
try:
  api.update_status(scraping.text)
except Exception as e:
  print(e)