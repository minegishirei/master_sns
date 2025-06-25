
import requests

def get_fox_image_url():
    url = "https://randomfox.ca/floof/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data["image"]
    else:
        raise Exception(f"Error: {response.status_code}")

# 使用例
if __name__ == "__main__":
    image_url = get_fox_image_url()
    print(f"🦊 キツネの画像URL: {image_url}")


