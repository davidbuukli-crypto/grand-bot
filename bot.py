import os
from flask import Flask
import telebot
from telebot import types
import threading

TOKEN = "8816208555:AAHj3m3qpKjMCCCX65vEbp-XY9O0bqNnyWo"
ADMIN_ID = 5045245352

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Фиктивный сайт, чтобы Render думал, что это веб-сервер и не выключал его
@app.route('/')
def home():
    return "Бот работает!"

# Команда /start
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("👤 Личный кабинет"), types.KeyboardButton("🧮 Калькулятор прибыли"))
    markup.add(types.KeyboardButton("📥 Пополнить"), types.KeyboardButton("📤 Вывести"))
    bot.send_message(message.chat.id, "Привет! Добро пожаловать в инвестиции Grand Mobile.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "👤 Личный кабинет":
        bot.send_message(message.chat.id, "👤 Твой профиль:\nБаланс: 0 виртов\nАктивный вклад: 0 виртов")
    elif message.text == "🧮 Калькулятор прибыли":
        bot.send_message(message.chat.id, "🧮 Прибыль составляет 3% в день. Введи сумму вклада для расчета.")
    elif message.text == "📥 Пополнить":
        bot.send_message(message.chat.id, "📥 Напиши сумму и ник, переведи деньги админу и пришли скриншот.")
        bot.send_message(ADMIN_ID, f"📥 Заявка на ПОПОЛНЕНИЕ от @{message.from_user.username}")
    elif message.text == "📤 Вывести":
        bot.send_message(message.chat.id, "📤 Напиши сумму для вывода и свой ник. Заявка отправлена админу.")
        bot.send_message(ADMIN_ID, f"📥 Заявка на ВЫВОД от @{message.from_user.username}")

# Запуск бота в отдельном потоке
def run_bot():
    bot.infinity_polling()

if __name__ == "__main__":
    # Запускаем телеграм-бота параллельно
    t = threading.Thread(target=run_bot)
    t.start()
    
    # Получаем порт от Render и запускаем веб-сервер
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
