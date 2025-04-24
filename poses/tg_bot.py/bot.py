import telepot
from telepot.loop import MessageLoop
from openai import OpenAI
import os
client = OpenAI(
    api_key=os.environ["OPENAI_KEY"],
)

def message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    print(content_type, chat_type, chat_id)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            { 
                "role": "system",
                "content": "ти бот,  що можеш відповідати тільки жартами",
            },
            {
                "role": "user",
                "content": msg["text"],
            }
        ]
    )

    bot.sendMessage(chat_id, completion.choices[0].message.content)

bot = telepot.Bot(os.environ["TELEGRAM_KEY"])
MessageLoop(bot, {'chat' : message}).run_forever()