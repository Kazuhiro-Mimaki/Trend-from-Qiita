import requests
import json
import settings
import scraping

SLACK_WEB_HOOK = settings.SWH

# slackにpost
try:
  requests.post(SLACK_WEB_HOOK, data = json.dumps({
    'text': scraping.text,
    'unfurl_links': u'true',
    'username': u'Buzzrita',
    'icon_emoji': u':buzzrita:',
  }))
except Exception as e:
  print(e)