from chatgpt.main       import run_chatgpt
import random
from tweet import main
from tweet.accounts import matsuki_no_ukiwa, ohmycat
from tweet import draft

def get_tweet_prompt(lang_name):
    return f"""
あなたはプロのTwitter広告担当者です。
以下の制約条件と入力文をもとに、ツイート本文のみ出力してください。

制約条件：
文字数は50文字程度

大喜利系・知識系どちらでもOK

フォロワーが思わず反応したくなる内容にしてください

皮肉や攻撃性を含んでもよいですが、必ずユーモアを交えてください

ツイート本文だけを出力し、説明や前置き、宣言文（例：「以下のツイートをします」など）は含めないでください
"""


if __name__ == "__main__":
	# ツイート内容のドラフトを作る
    tweet_content = run_chatgpt( get_tweet_prompt( "" ) )
    draft.create_draft(tweet_content,"/tweets")

    # 承認したドラフトから、ツイートする内容を選択。
    tweet_content = draft.fetch_tweet_content_from_draft("/tweets")
    print(tweet_content)

    # アカウントをランダムに二つ選択
    # 選択したアカウントでツイートを行う
    tweet_account = random.choice([ohmycat.get_tweepy_client(),matsuki_no_ukiwa.get_tweepy_client() ])
    main.create_tweet(tweet_content, tweet_account)

