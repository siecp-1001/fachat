from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_response(messages, model="gpt-5.1"):
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.7,
            max_tokens=300,
            presence_penalty=0.4
        )
        return completion.choices[0].message['content']
    except Exception as e:
        return f"⚠️ I'm having trouble responding right now. Error: {str(e)[:200]}"
