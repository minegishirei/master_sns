
from GoogleNews import GoogleNews


def fetch_news(keyword):
    googlenews = GoogleNews(lang='ja', region='JP')
    googlenews.get_news(keyword)  # ←空文字で全体トレンドを取得
    results = googlenews.results(sort=True)
    return results

def template(row):
    return f"""{row["title"]}
{row["link"]}
    """
