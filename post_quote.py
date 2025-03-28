import os
import json
import random
import telebot

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_ID = "@plato_vibe"

with open("platon_quotes.json", "r", encoding="utf-8") as f:
    all_quotes = json.load(f)

try:
    with open("platon_quotes_used.json", "r", encoding="utf-8") as f:
        used_quotes = json.load(f)
except FileNotFoundError:
    used_quotes = []

used_texts = {q["quote"] for q in used_quotes}
unused_quotes = [q for q in all_quotes if q["quote"] not in used_texts]

if not unused_quotes:
    print("❗ Все цитаты использованы.")
    exit()

quote = random.choice(unused_quotes)
formatted = f"_{quote['quote']}_\n\n**Платон. {quote['source']}**"

bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")
bot.send_message(CHANNEL_ID, formatted)

used_quotes.append(quote)
with open("platon_quotes_used.json", "w", encoding="utf-8") as f:
    json.dump(used_quotes, f, ensure_ascii=False, indent=2)

print("✅ Цитата отправлена")
