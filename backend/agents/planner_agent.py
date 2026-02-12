from openai import OpenAI
from config.settings import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

def plan_user_request(user_query):

    prompt = f"""
    You are a government service planner.
    Break the request into steps.

    Request: {user_query}
    """

    res = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role":"user","content":prompt}]
    )

    return res.choices[0].message.content
