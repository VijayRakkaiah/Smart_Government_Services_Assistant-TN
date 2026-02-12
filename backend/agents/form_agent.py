from openai import OpenAI
from config.settings import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_application_form(user_input, scheme_info):

    prompt = f"""
    Create a simple filled application draft.

    User Info: {user_input}
    Scheme Info: {scheme_info}
    """

    res = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role":"user","content":prompt}]
    )

    return res.choices[0].message.content
