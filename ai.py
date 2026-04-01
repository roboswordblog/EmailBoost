import openai

client = openai.OpenAI()

def improve(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Improve the user's email to be clearer, more professional, and more effective. Just edit the content. "
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )
    return response.choices[0].message.content

