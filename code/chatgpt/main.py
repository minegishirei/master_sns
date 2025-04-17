import os
import groq


def get_client(api_key):
    client = groq.Groq(api_key=api_key)
    return client

def call_groq(client, system_prompt, user_prompt):
    # Set the user prompt
    # Initialize the chat history
    chat_history = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]
    try:
        response = client.chat.completions.create(model="llama3-70b-8192",
                                                    messages=chat_history,
                                                    temperature=0.8)
        return response.choices[0].message.content
    except (groq.APIConnectionError,  groq.RateLimitError):
        return ""

def fetch_file(file_path):
    with open(file_path) as f:
        return f.read()


def get_contents():
    contents = []
    for root, dirs, files in os.walk('/data/psy/blog'):
        md_files = filter(lambda file: ".md" in file, files)
        for md_file in md_files:
            md_file_path = os.path.join(root, md_file)
            content = fetch_file(md_file_path)
            contents.append(
                (md_file_path, content)
            )
    return contents

def contains_two_or_more_keywords(content, keywords, limit):
    count = 0
    hit_words = []
    for keyword in keywords:
        if keyword in content:
            count += 1
            hit_words.append(keyword)
            if count >= limit:
                return True, hit_words
    return False, hit_words



import re
def get_data():
    data = []
    for md_file_path, content in get_contents():
        md_chapters = re.split(r'#### |### |## |# ', content)
        for md_chapter in md_chapters:
            if len(md_chapter) > 50:
                data.append({
                    "md_file_path" : md_file_path,
                    #"hit_words" : hit_words,
                    "md_chapter" : md_chapter
                })
    return data




def run_chatgpt(request):
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    SYSTEM_PROMPT = "あなたは便利な日本人アシスタントです。質問には簡潔に日本語で答えてください。"
    text = call_groq(get_client(GROQ_API_KEY), SYSTEM_PROMPT, request)
    return text
