import tweepy
import sys
import datetime
import os
import shutil


#ツイート内容 (本垢)
CONSUMER_KEY = "YnuweXfQMN1WHpxpYZeFVqDRM"
CONSUMER_SECRET = "IMKJRAueZ28Ghp4epL0TT2f1d753x4GocQssFw9Jw2LHaTgU0M"
ACCESS_TOKEN = "1349555933257469955-Bo7TrvVDVIgHRCWmNLJnYnlxv9dHn6"
ACCESS_SECRET = "Eko1yGXwJi0kDnECKbtxMNpvsoBkuGamULGGivIacpW1r"

##オブジェクト作成
#client = tweepy.Client(
#	consumer_key = CONSUMER_KEY,
#	consumer_secret = CONSUMER_SECRET,
#	access_token = ACCESS_TOKEN,
#	access_token_secret = ACCESS_SECRET
#)

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



# ohmycat
#Twitter Developer Portalから取得したキーを設定
CONSUMER_KEY = 'SE1MVm9Ta2hRMGdJRmJaYlBhVVI6MTpjaQ'
CONSUMER_SECRET = 'Lbagx30xH1QSIRnEoZHkVC_9OXvyudi8WjMykuXYE5Eu2R6M6Z'
ACCESS_TOKEN = '1266718659671556102-UCUQte7FuhcvungNZovCBVBPyU4DgC'
ACCESS_SECRET = 'o6r4V2JD5DhH9gIKBw0va3yb89cBddrgYfV9stiYV7iol'
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAO9c2gEAAAAAw772Bhonpi%2FyaCf1x10%2BogWwE9w%3D3hBfF1MmoKy7HxBPBPMojxA65IEkRLAZCwBUR19pYoTXhAo0Wn"
client = tweepy.Client(
	consumer_key = CONSUMER_KEY,
	consumer_secret = CONSUMER_SECRET,
	access_token = ACCESS_TOKEN,
	access_token_secret = ACCESS_SECRET,
	#bearer_token = BEARER_TOKEN
)


def create_tweet(content):
    print(content)
    print("test")
    client.create_tweet(text=content)




def create_draft(content, folderpath):
	dt_now = datetime.datetime.now()
	dt_now = '{:%Y%m%d%H%M%S}'.format(dt_now) 
	with open(folderpath + "/" + dt_now ,"w+" ) as f:
		f.write(content)


def list_files(directory):
    return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        else:
            print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error: {e}")

def move_file(filepath, dest_folder):
	try:
		if os.path.exists(filepath):
			filename = os.path.basename(filepath)
			new_path = os.path.join(dest_folder, filename)
			shutil.move(filepath, new_path)
			print(f"Moved: {filepath} to {new_path}")
		else:
			print(f"File not found: {filepath}")
	except Exception as e:
		print(f"Error: {e}")



def search_go_tweet(folderpath):
	for path in list_files(folderpath):
		content = ""
		with open(path , "r") as f:
			content = f.read()
		if "DONE" in content:
			create_tweet(content.replace("DONE", ""))
			move_file(path, "/done/")
			exit()











