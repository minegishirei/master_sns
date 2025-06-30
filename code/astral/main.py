import requests

url = 'https://d2880sy3aqy51t.cloudfront.net/api/open_node?page=profile.html&user_id=test'

headers = {
    'accept': '*/*',
    'accept-language': 'ja,en-US;q=0.9,en;q=0.8',
    'authorization': 'Bearer eyJraWQiOiJNbnE3VlZJSnpmbjV5S1RmTm45MmM5dzhpS3d2dzVXeW5hZ3lmY0UxeUpRPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiTjlDdWlReWhYSzI4VmxDdnJYWTFqUSIsInN1YiI6IjE3ZjQ1YWQ4LWYwOTEtNzAyNy03NzBiLTFlY2U0ZDE5MzRkZCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAuYXAtbm9ydGhlYXN0LTEuYW1hem9uYXdzLmNvbVwvYXAtbm9ydGhlYXN0LTFfOTJiNG95NnIwIiwiY29nbml0bzp1c2VybmFtZSI6InRlc3QiLCJvcmlnaW5fanRpIjoiNjg5ZmYxNGEtYjhmMy00Zjk2LTgwYTgtMjgxY2JmYjE1YjUxIiwiYXVkIjoiNGE4ZTZ2YTBlNmsxbDhncXA2cjQ4Y2VzZ3UiLCJldmVudF9pZCI6IjhhZDk0MjRmLTAxZDAtNDY1ZC05ZjViLTk3M2ZjMjU1N2E0OCIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNzUxMjUyNTAwLCJleHAiOjE3NTEyOTU3MDAsImlhdCI6MTc1MTI1MjUwMCwianRpIjoiMzM2ZTEzZmYtMDM3Yi00ZjA2LTkyZmEtNzg1NzBkYzJiOWMzIiwiZW1haWwiOiJNaW5lMDExNHlra3lra0BnbWFpbC5jb20ifQ.gkwzP7A_XN2Yb-IW-3YY33o4yws1VPh6k-Y0Q9VkHxT_sZ8lJoE06qOmx0kF7yNWY0TZOPDDZNcF2BnJqxg8BmbsQDqaXYmcaiLqUrNpYX-9URFVhba-m0wgIuIU2Ewt8NT2KPgEkjb4Zlsbhm9XKyiJAjLC3YR_ZdYArh_5iUFfFeedvUMHnGf4_vgYrCaUGurqxGZ0rdsLI8RnWTGAgDkOl6H5ZPZlmX1dzUh7qD_PwiPeVfBwNTlzXx_yGo9bgabra-d3lZL9kpHH1T2xZeGy5lq9ZzO7_ExsGcFYHO6eOhUhZvDyzLq7TTqZOeW5Q9N1tkhPOT87rW1lxhiyLQ',
    'content-type': 'text/plain;charset=UTF-8',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjY1NjM3NjkiLCJhcCI6IjU5NDU3OTg2OSIsImlkIjoiM2Q4MzgxNDI1MjIyZDY5MSIsInRyIjoiMDhlYjYwODQzNGE4MjY0N2MwZmYzY2JlODEwYTg0NWQiLCJ0aSI6MTc1MTI1MjUyNjYyN319',
    'origin': 'https://d2880sy3aqy51t.cloudfront.net',
    'priority': 'u=1, i',
    'referer': 'https://d2880sy3aqy51t.cloudfront.net/dashboard.html?code=44afafd8-cc11-4597-bdee-340e6fba1ee7',
    'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-08eb608434a82647c0ff3cbe810a845d-3d8381425222d691-01',
    'tracestate': '6563769@nr=0-1-6563769-594579869-3d8381425222d691----1751252526627',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36'
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
