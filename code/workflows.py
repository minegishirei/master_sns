from datetime import datetime
import requests as req
import json
import markdown_to_json
import xmltodict
from chatgpt.main       import run_chatgpt
import markdown
import random
md = markdown.Markdown()
from tweet.main import create_draft, search_go_tweet

HATENA_ID = "minegishirei"
BLOG_DOMAIN = "flamevalue.hatenablog.com"
API_KEY = "u6v0f3440e"

def hatena_create_entry(title, contents, categorys=[], draft=False):
    BASE_URL = f"https://blog.hatena.ne.jp/minegishirei/{BLOG_DOMAIN}/atom/entry"
    updated = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    category = lambda x: "\n".join([f"<category term='{e}' />" for e in x])
    categorys = category(categorys) if category else ""

    xml = f"""<?xml version="1.0" encoding="utf-8"?>
    <entry xmlns="http://www.w3.org/2005/Atom"
          xmlns:app="http://www.w3.org/2007/app">
      <title>{title}</title>
      <author><name>name</name></author>
      {categorys}
      <content type="text/x-markdown">
        {contents}
      </content>
    </entry>""".encode(
        "UTF-8"
    )
    r = req.post(BASE_URL, auth=(HATENA_ID, API_KEY), data=xml)
    return r.text

def hatena_entry(title, contents, entry_id, categorys=[], updated="", draft=False):
    BASE_URL = f"https://blog.hatena.ne.jp/minegishirei/{BLOG_DOMAIN}/atom/entry/{entry_id}"
    updated = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    category = lambda x: "\n".join([f"<category term='{e}' />" for e in x])
    categorys = category(categorys) if category else ""

    xml = f"""<?xml version="1.0" encoding="utf-8"?>
    <entry xmlns="http://www.w3.org/2005/Atom"
          xmlns:app="http://www.w3.org/2007/app">
      <title>{title}</title>
      <author><name>name</name></author>
      {categorys}
      <updated>{updated}</updated>
      <content type="text/x-markdown">
        {contents}
      </content>
    </entry>""".encode(
        "UTF-8"
    )
    r = req.put(BASE_URL, auth=(HATENA_ID, API_KEY), data=xml)
    return r.text



def get_json_markdown(content):
    dictified = markdown_to_json.dictify(content)
    return dictified


def get_page_link_from_markdown(name):
    with open(f"/blog/{name}.md", "r") as f:
        title, categorys, entry_id, *content = f.readlines()
        page_lines = [line for line in content if line.startswith("page:")]
        if len(page_lines) <= 0:
            return "https://flamevalue.hatenablog.com/"
        return page_lines[0].replace("page:","").replace("\n","")

def decorate_FLAMEWORKDICT(FLAMEWORKDICT):
    return list(map(lambda row : {
        **row, 
        "page_link" :get_page_link_from_markdown(row["name"])
    },FLAMEWORKDICT))



def get_tweet_prompt(lang_name):
    return f"""
あなたは、プロのTwitter広告担当者です。
以下の制約条件と入力文をもとに、ツイートの内容を出力してください。

# 制約条件：
・文字数は100文字程度

# 入力文：
ITまたは心理学どちらか選んで、それらの内容の
ツイートを作成してください。

・内容は大喜利系/知識系何でも良いですが、フォロワーが興味を持つような内容にしてください
・皮肉混じりでも攻撃的な内容でも良いですが、あくまでユーモアを交えた内容にしてください
・内容はITまたは心理学に関するもので、特に最近のトレンドや話題に関連していると良いです
"""


if __name__ == "__main__":
    from flamevalue.main import build_param , GEN_FLAMEWORKDICT
    from html_lib.main import get_template, escape_xml
    import sys
    _, arg = sys.argv

    if "tweet" in arg:
        tweet_content = run_chatgpt( get_tweet_prompt( "" ) )
        tweet_content = tweet_content 
        create_draft(tweet_content,"/tweets")
        search_go_tweet("/tweets")
        exit()
