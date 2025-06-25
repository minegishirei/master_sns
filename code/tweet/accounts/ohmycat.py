import tweepy

def get_tweepy_client():
    # ohmycat
    #Twitter Developer Portalから取得したキーを設定
    CONSUMER_KEY = 'LHqlWvBaUVi3TbALSKZ1Snsg7'
    CONSUMER_SECRET = 'b0IWbRTyDKmr1bg1Cb753ETmRHQLfoBbgWaIyZC2JOtCnGoymj'
    ACCESS_TOKEN = '1266718659671556102-UCUQte7FuhcvungNZovCBVBPyU4DgC'
    ACCESS_SECRET = 'o6r4V2JD5DhH9gIKBw0va3yb89cBddrgYfV9stiYV7iol'
    BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAO9c2gEAAAAAw772Bhonpi%2FyaCf1x10%2BogWwE9w%3D3hBfF1MmoKy7HxBPBPMojxA65IEkRLAZCwBUR19pYoTXhAo0Wn'
    CLIENT = tweepy.Client(
        consumer_key = CONSUMER_KEY,
        consumer_secret = CONSUMER_SECRET,
        access_token = ACCESS_TOKEN,
        access_token_secret = ACCESS_SECRET,
        bearer_token= BEARER_TOKEN
    )
    return CLIENT
