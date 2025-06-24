import datetime
import shutil
import os

def create_draft(content, folderpath):
	dt_now = datetime.datetime.now()
	dt_now = '{:%Y%m%d%H%M%S}'.format(dt_now) 
	with open(folderpath + "/" + dt_now ,"w+" ) as f:
		f.write(content)

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
        
def fetch_tweet_content_from_draft(folderpath):
	for path in [os.path.join(folderpath, f) for f in os.listdir(folderpath) if os.path.isfile(os.path.join(folderpath, f))]:
		content = ""
		with open(path , "r") as f:
			content = f.read()
		if "DONE" in content:
			move_file(path, "/done/")
			return content.replace("DONE", "")

