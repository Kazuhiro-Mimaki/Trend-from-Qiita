# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CK = os.environ.get("CONSUMER_KEY") # 環境変数の値をAPに代入
CS = os.environ.get("CONSUMER_SECRET")
AT = os.environ.get("ACCESS_TOKEN_KEY")
AS = os.environ.get("ACCESS_TOKEN_SECRET")
Slack_web_hook = os.environ.get("SLACK_WEB_HOOK")