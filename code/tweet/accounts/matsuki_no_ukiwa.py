import tweepy

def get_tweepy_client():
    API_KEY = "dLsHbZeI8F1QOyo7TH63Bt6na"
    API_SECRET = "MdliuIkD6H0ebuUwji7Hq5YiuRdFXjdWYe9i12w9eAGmLns6Kx"
    BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAI1c2gEAAAAAYQPXuZ1CGf%2BVfIeSd49YWxhrDfg%3DeLqjGJLPC6lHdNtNCviItZbGc6cjCqPokYZXBaRYnu9zqe9wiY"
    CLIENT_ID = "U1VjdlV5bVVHNU43ODY3ZXN6dVU6MTpjaQ"
    CLIENT_SECRET = "wbKFCquDK7gbPGzy-P2501r4N1PM16KSTGLKYEdKJQfTjTnvpD"
    CONSUMER_KEY = API_KEY
    CONSUMER_SECRET = API_SECRET
    ACCESS_TOKEN = "968269222525587456-aIa2ADR86BSwMUw2Cd0OWBB77koghHp"
    ACCESS_SECRET ="rQtPX2xTJrCoc7Jxz9e8m4b26ZwC7lI8nD8wjMwPFzdjr"
    client = tweepy.Client(
	    consumer_key = CONSUMER_KEY,
	    consumer_secret = CONSUMER_SECRET,
	    access_token = ACCESS_TOKEN,
	    access_token_secret = ACCESS_SECRET,
	    bearer_token = "AAAAAAAAAAAAAAAAAAAAAI1c2gEAAAAAtn75pEUFmurFgRkesTateJUGumc%3DKGR4OtvWmgEOUDi5m2lzbuHXpTufDXCSvQQQkOB3Uy2pNDzHbi"
    )
    return client
