import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1")

resp = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[{"role": "user", "content": "Explain AI agents simply"}]
)
print(resp.choices[0].message.content)
