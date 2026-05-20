import telebot
import requests

# ВСТАВЬ СВОЙ ТОКЕН СЮДА
bot = telebot.TeleBot("8895018394:AAHvnjjT3UV665PV8K2Xmai5MXbVwKD9vWI")

AI_URL = "https://api.aiproxy.io/api/v1/chat/completions"

def ask_ai(message):
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "Ты — умный ассистент Веры. Пиши ясно, дружелюбно, по делу."},
            {"role": "user", "content": message}
        ]
    }
    r = requests.post(AI_URL, json=payload)
    return r.json()["choices"][0]["message"]["content"]

@bot.message_handler(func=lambda m: True)
def reply(message):
    try:
        answer = ask_ai(message.text)
        bot.send_message(message.chat.id, answer)
    except Exception as e:
        bot.send_message(message.chat.id, "Ошибка, попробуй ещё раз.")

bot.polling()
