import requests
import base64

def image_url_to_base64(url):
    # 画像をダウンロード
    response = requests.get(url)
    
    if response.status_code == 200:
        # 画像のバイナリデータをBase64に変換
        image_base64 = base64.b64encode(response.content).decode('utf-8')
        return image_base64
    else:
        raise Exception(f"画像の取得に失敗しました。ステータスコード: {response.status_code}")


