import telebot
import time
import threading
from flask import Flask
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# --- Flask Web Server Setup (Sleep theke bachanor jonno) ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running makhon er moto bro!"

def run_web():
    # Port 8080 te web server cholbe background e
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = threading.Thread(target=run_web)
    t.start()
# -----------------------------------------------------------

# Tomar Notun Telegram Bot Setup
API_TOKEN = '8729596702:AAGQcI0IdilmvLjYjOeCvLm7YzbpIXQkZBk'
bot = telebot.TeleBot(API_TOKEN)
MY_USER_ID = 5124729477

def get_time_keyboard():
    markup = ReplyKeyboardMarkup(row_width=4, resize_keyboard=True, one_time_keyboard=False)
    markup.add(
        KeyboardButton('M1'), 
        KeyboardButton('M2'), 
        KeyboardButton('M3'), 
        KeyboardButton('M5')
    )
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.chat.id != MY_USER_ID:
        return
    bot.send_message(
        message.chat.id,
        "Tomar Trade neyar time select koro",
        reply_markup=get_time_keyboard()
    )

@bot.message_handler(func=lambda message: message.text in ['M1', 'M2', 'M3', 'M5'])
def handle_time_selection(message):
    if message.chat.id != MY_USER_ID:
        return

    text = message.text
    # 'M1' theke 1, 'M5' theke 5 ber kore niye aschi
    minutes = int(text.replace('M', ''))

    bot.send_message(message.chat.id, f"✅ {text} Select kora hoyeche. Wait koro...")
    
    # Bot ke wait korano hocche (minutes * 60 seconds)
    time.sleep(minutes * 60)

    bot.send_message(message.chat.id, "tomar trade nea hoyeche..")
    
    bot.send_message(
        message.chat.id,
        "Tomar Trade neyar time select koro",
        reply_markup=get_time_keyboard()
    )

if __name__ == "__main__":
    print("Web server chalu hocche jate bot na ghumay...")
    keep_alive()  # Web server ta background e chalu kore dilam
    print("Bot chalu hoyeche bro! Telegram e giye /start dao...")
    bot.infinity_polling()
