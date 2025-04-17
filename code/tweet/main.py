import tweepy
import sys
import datetime
import os
import shutil


#Twitter Developer Portalから取得したキーを設定
CONSUMER_KEY = 'M8qVyxkSeg8fEfEJb9TjMOGll'
CONSUMER_SECRET = '2qB1l7fs6b837qIetaN9lHSPHI6Awmd3SqWI9NbEyCcMV22OvZ'
ACCESS_TOKEN = '1349555933257469955-2UBWgME3lXUZmw4vmGbWtpcu5UIGXa'
ACCESS_SECRET = 'gSUCGz10sG6U7IRL0PrYSK4DPRhoyXKKWNwypj6iaRea6'

#ツイート内容
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


def create_tweet(content):
    print(content)
    print("test")
    #client.create_tweet(text=content)




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
		if "done" in content:
			create_tweet(content.replace("done", ""))
			move_file(path, "/done/")











