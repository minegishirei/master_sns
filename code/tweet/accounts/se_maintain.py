import tweepy

def get_tweepy_client():
    #ツイート内容 (本垢)
    CONSUMER_KEY = "YnuweXfQMN1WHpxpYZeFVqDRM"
    CONSUMER_SECRET = "IMKJRAueZ28Ghp4epL0TT2f1d753x4GocQssFw9Jw2LHaTgU0M"
    ACCESS_TOKEN = "1349555933257469955-Bo7TrvVDVIgHRCWmNLJnYnlxv9dHn6"
    ACCESS_SECRET = "Eko1yGXwJi0kDnECKbtxMNpvsoBkuGamULGGivIacpW1r"

    #オブジェクト作成
    client = tweepy.Client(
    	consumer_key = CONSUMER_KEY,
    	consumer_secret = CONSUMER_SECRET,
    	access_token = ACCESS_TOKEN,
    	access_token_secret = ACCESS_SECRET
    )
    return client

