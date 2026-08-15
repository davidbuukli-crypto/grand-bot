import telebot
from telebot import types

TOKEN = "8943143101:AAGoHQXQ8XEpaVGfYGWDv3utZfeBwYyA4KA"
ADMIN_ID = 5045245352

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👤 Личный кабинет")
    btn2 = types.KeyboardButton("🧮 Калькулятор прибыли")
    btn3 = types.KeyboardButton("📥 Пополнить")
    btn4 = types.KeyboardButton("📤 Вывести")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, "Привет! Добро пожаловать в инвестиции Grand Mobile.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "👤 Личный кабинет":
        bot.send_message(message.chat.id, "👤 Твой профиль:\nБаланс: 0 виртов\nАктивный вклад: 0 виртов")
    elif message.text == "🧮 Калькулятор прибыли":
        bot.send_message(message.chat.id, "🧮 Прибыль составляет 3% в день.")
    elif message.text == "📥 Пополнить":
        bot.send_message(message.chat.id, "📥 Чтобы пополнить баланс, напиши сумму и свой ник администратору.")
    elif message.text == "📤 Вывести":
        bot.send_message(message.chat.id, "📤 Заявка на вывод отправлена.")

if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()
