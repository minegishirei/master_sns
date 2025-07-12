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

def get_tweet_prompt(category):
    return f"""
あなたはプロのTwitter広告担当者です。
以下の制約条件と入力文をもとに、ツイート本文のみ出力してください。

制約条件：文字数は100文字以内。制作者は創造性豊かで、世間の話題、ニュース、{category} の情報に精通しており、人々の目を引き付ける魅力的なTwitter投稿文章作成が得意なトップクラスのライターです。
目的と目標:{category}についての関心、興味を引き付け、シェアされやすいTweet投稿文章を作成すること。Twitter高校を通じて依頼者が、SNSで大きな影響力をもち、新規のフォロワーが増加するよう支援、貢献すること。
皮肉や攻撃性を含んでもよいですが、必ずユーモアを交えてください

フォロワーが思わず反応したくなる内容にしてください

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

prog_langs = [
    "Python", "JavaScript", "Java", "C", "C++", "C#", "Go", "Ruby", "PHP", "Swift",
    "Kotlin", "Rust", "TypeScript", "Scala", "Perl", "Lua", "Haskell", "Objective‑C",
    "Dart", "MATLAB", "R", "SQL", "Visual Basic", "Pascal", "Fortran", "Shell",
    "PowerShell", "Groovy", "Elixir", "Erlang", "Julia", "F#", "COBOL", "Assembly",
    "Prolog", "Ada", "Lisp", "Scheme", "OCaml", "Crystal", "VBA", "Delphi", "Bash",
    "Scratch", "SAS", "ABAP", "RPG", "Q#", "LabVIEW", "Logo"
]
aws_services = [
    "EC2", "S3", "EBS", "EFS", "Lambda", "Elastic Beanstalk", "VPC", "Route 53",
    "CloudFront", "RDS", "DynamoDB", "Redshift", "Aurora", "Glue", "CloudFormation",
    "ECS", "EKS", "Fargate", "SQS", "SNS", "SES", "CloudWatch", "CloudTrail",
    "IAM", "KMS", "Athena", "Kinesis", "API Gateway", "Step Functions", "Snowball",
    "Inspector", "Security Hub", "GuardDuty", "AppFlow", "Managed Blockchain",
    "Elasticsearch Service", "QuickSight", "MSK", "Pinpoint", "Device Farm",
    "CodeCommit", "CodePipeline", "CodeDeploy", "Cloud9", "DataSync", "Lake Formation",
    "MQ", "Managed Airflow", "Cognito", "Direct Connect"
]
dev_methods = [
    "ウォーターフォール", "アジャイル", "スクラム", "カンバン", "XP", "リーン開発",
    "DevOps", "CI/CD", "テスト駆動開発（TDD）", "BDD", "ペアプログラミング",
    "コードレビュー", "リファクタリング", "継続的インテグレーション", "継続的デリバリー",
    "継続的デプロイメント", "モブプログラミング", "プロトタイピング", "UAT", "ユースケース駆動開発",
    "ドメイン駆動設計（DDD）", "マイクロサービス", "サーバーレスアーキテクチャ",
    "イベント駆動アーキテクチャ", "SCRUM-ban", "スパイラルモデル", "RAD", "プロジェクトマネジメント",
    "リスク管理", "品質保証（QA）", "バージョン管理", "Gitフロー", "ブランチ戦略", "CIパイプライン",
    "自動テスト", "性能テスト", "負荷テスト", "セキュリティテスト", "コードカバレッジ",
    "ドキュメント駆動開発", "ウォークスルー", "レビュー会議", "設計パターン",
    "アーキテクチャレビュー", "インフラストラクチャ as Code（IaC）", "モニタリング"
]



if __name__ == "__main__":
    # matsuki_no_ukiwaでのツイート
    matsuki_no_ukiwa_word_list = prog_langs + aws_services + dev_methods
    ## Astralでのツイート(1/2で実行)
    keyword = random.choice(matsuki_no_ukiwa_word_list)
    if random.random() < 0.1:
        tweet_content = create_node_from_keyword(keyword,{
            "user_id": "kawadasatoshi",
            "password": "Mine0114!",
        })
        main.create_tweet(
            tweet_content, 
            matsuki_no_ukiwa.get_tweepy_client()
        )
    google_trend_content = googletrends.main.fetch_news(keyword)[0]
    main.create_tweet(
        run_chatgpt(get_tweet_prompt()), 
        matsuki_no_ukiwa.get_tweepy_client()
    )
        
    # ## プロンプトによるツイート
    # tweet_content = run_chatgpt(get_tweet_prompt(random.choice(matsuki_no_ukiwa_word_list)))
    # print(tweet_content)
    # main.create_tweet(
    #     tweet_content,
    #     matsuki_no_ukiwa.get_tweepy_client()
    # )

    # ohmycatでのツイート
    ## Astralでのツイート(1/2で実行)
    if random.random() < 0.1:
        tweet_content = create_node_from_keyword(random.choice(matsuki_no_ukiwa_word_list),{
            "user_id": "ohmycat",
            "password": "Mine0114!",
        })
        main.create_tweet(tweet_content, ohmycat.get_tweepy_client())
    ## プロンプトによるツイート
    tweet_content = run_chatgpt(get_tweet_prompt(random.choice(matsuki_no_ukiwa_word_list)))
    print(tweet_content)
    main.create_tweet(
        tweet_content,
        ohmycat.get_tweepy_client()
    )

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
