from chatgpt.main       import run_chatgpt
from chatgpt.gemini     import run_chatgpt
import random
from tweet import main
from tweet.accounts import matsuki_no_ukiwa, ohmycat
from tweet import draft
import fox.main
import astral.main
import googletrends.main
import json
import lib.image

def get_tweet_prompt(lang_name):
    return f"""
あなたはプロのTwitter広告担当者です。
以下の制約条件と入力文をもとに、ツイート本文のみ出力してください。

制約条件：
文字数は120文字以内

大喜利系・知識系どちらでもOK

フォロワーが思わず反応したくなる内容にしてください

皮肉や攻撃性を含んでもよいですが、必ずユーモアを交えてください

ツイート本文だけを出力し、説明や前置き、宣言文（例：「以下のツイートをします」など）は含めないでください
"""


def create_node_from_keyword(keyword,user):
    def create_title(title):
        return f"""
    あなたはプロのTwitter広告担当者です。
    以下の制約条件と入力文をもとに、タイトルをのみを出力してください。

    制約条件:
    30文字以内

    ネタ:
    {title}

    タイトル本文だけを出力し、説明や前置き、宣言文（例：「以下のタイトルを出力します」など）は含めないでください
    """
    content = googletrends.main.fetch_news(keyword)[0]
    print(content)
    node_data = {
        "title" : keyword +"->-" +run_chatgpt( create_title(content["title"]) ),
        "content" : (content["title"] + content["link"]),
        "image" : lib.image.image_url_to_base64(content["img"]),
        **user
    }
    print(node_data)
    response = astral.main.post_only_node(node_data)
    print(response)
    new_node_dict = list(json.loads(response).values())[0] 
    node_id = new_node_dict["node_id"]
    print(node_id)
    return f"""{content["title"]}
https://d2or2g1md9lrqv.cloudfront.net/dashboard.html?node_id={new_node_dict["node_id"]}
"""



if __name__ == "__main__":
	# ツイート内容のドラフトを作る
    tweet_content_draft = run_chatgpt( get_tweet_prompt( "" ) )
    draft.create_draft(tweet_content_draft,"/tweets")
    print(tweet_content_draft)

    tweet_content = create_node_from_keyword(random.choice(["今だけ","知らなきゃ損","9割が知らない","するだけ","〇選","裏ワザ","最新版","一瞬で","たった1分で","衝撃の事実","バレた","なぜ なのか？","しないでください","【保存版】","本当は教えたくない","○○の真実","無料でできる","専門家が教える","今すぐチェック","した結果…",]),{
        "user_id": "kawadasatoshi",
        "password": "Mine0114!",
    })
    main.create_tweet(tweet_content, matsuki_no_ukiwa.get_tweepy_client())

    tweet_content = create_node_from_keyword(random.choice(["", "ゲーム", "統計データ","心理学", "エンジニア", "プログラミング", "AI"]),{
        "user_id": "ohmycat",
        "password": "Mine0114!",
    })
    main.create_tweet(tweet_content, ohmycat.get_tweepy_client())

    # # 承認したドラフトから、ツイートする内容を選択。
    # tweet_content = draft.fetch_tweet_content_from_draft("/tweets")
    # print(tweet_content)
    # # アカウントをランダムに二つ選択
    # # 選択したアカウントでツイートを行う
    # tweet_account = random.choice([ohmycat.get_tweepy_client(),matsuki_no_ukiwa.get_tweepy_client() ])
    # try:
    #     main.create_tweet(tweet_content, tweet_account)
    # except Exception as e:
    #     import traceback
    #     error_msg = traceback.format_exc()
    #     print("例外が発生しました:")
    #     print(error_msg)
