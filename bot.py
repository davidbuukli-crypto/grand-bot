import telebot
from telebot import types


TOKEN = "8816208555:AAE6vyaGtLXGx5CEBOw18GvrrcOj74jOJNU"
ADMIN_ID = 5045245352

bot = telebot.TeleBot(TOKEN)

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
        bot.send_message(ADMIN_ID, f"📤 Заявка на ВЫВОД от @{message.from_user.username}")

if __name__ == "__main__":
    bot.infinity_polling()
