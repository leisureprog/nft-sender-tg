from g4f.client import Client
import config

prompt = config.GPT_PROMPT

def generate(query):
    try:
        client = Client()
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"{prompt + query}"}],
            web_search=False
        )
        response_text = response.choices[0].message.content

        return response_text

    except Exception as e:
        print(f"Ошибка при обработке текста через g4f: {e}")
        return None
