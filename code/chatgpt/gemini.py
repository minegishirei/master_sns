



# Used to securely store your API key
import google.generativeai as genai


def run_chatgpt(question):
    # Or use `os.getenv('GEMINI_API_KEY')` to fetch an environment variable.
    GEMINI_API_KEY = "AIzaSyA5HbCA8bI5gCwQwB33v7UV1hseFD31I8I"
    genai.configure(api_key=GEMINI_API_KEY)

    #model = genai.GenerativeModel("gemini-1.5-flash")
    #import pprint
    #for model in genai.list_models():
    #    pprint.pprint(model)
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(question)
    return response.text

