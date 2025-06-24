import tweepy

def get_tweepy_client():
    # ohmycat
    #Twitter Developer Portalから取得したキーを設定
    CONSUMER_KEY = 'SE1MVm9Ta2hRMGdJRmJaYlBhVVI6MTpjaQ'
    CONSUMER_SECRET = 'Lbagx30xH1QSIRnEoZHkVC_9OXvyudi8WjMykuXYE5Eu2R6M6Z'
    ACCESS_TOKEN = '1266718659671556102-UCUQte7FuhcvungNZovCBVBPyU4DgC'
    ACCESS_SECRET = 'o6r4V2JD5DhH9gIKBw0va3yb89cBddrgYfV9stiYV7iol'
    #BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAO9c2gEAAAAAw772Bhonpi%2FyaCf1x10%2BogWwE9w%3D3hBfF1MmoKy7HxBPBPMojxA65IEkRLAZCwBUR19pYoTXhAo0Wn"
    CLIENT = tweepy.Client(
        consumer_key = CONSUMER_KEY,
        consumer_secret = CONSUMER_SECRET,
        access_token = ACCESS_TOKEN,
        access_token_secret = ACCESS_SECRET,
    )
    return CLIENT
