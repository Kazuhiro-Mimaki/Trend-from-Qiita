import tweepy
import scraping

# twitterにpost
try:
  scraping.api.update_status(scraping.text)
except Exception as e:
  print(e)