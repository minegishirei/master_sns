import requests

url = 'https://d2or2g1md9lrqv.cloudfront.net/api/open_node?page=profile.html&user_id=test'

headers = {
}

def post_only_node(row):
    data = {
        "title": "Apacheライセンス",
        "content": "薬物",
        "secret_id": "JPRNyN3Hz2AzqWqu5M8sASHjHzfm22",
        "page": "profile.html",
        **row
    }
    print(data)
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    print(response.text)
    return response.text
