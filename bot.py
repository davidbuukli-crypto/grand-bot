
import telebot
import os
from telebot import types

# Теперь токен берется из настроек Render (Environment Variables)
TOKEN = os.environ.get('TOKEN')
# Вставь свой Telegram ID сюда (цифрами), чтобы заявки на вывод/пополнение шли тебе
ADMIN_ID = 5045245352

bot = telebot.TeleBot(TOKEN)

# Главное меню
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👤 Личный кабинет")
    btn2 = types.KeyboardButton("🧮 Калькулятор прибыли")
    btn3 = types.KeyboardButton("📥 Пополнить")
    btn4 = types.KeyboardButton("📤 Вывести")
    markup.add(btn1, btn2, btn3, btn4)
    
    bot.send_message(message.chat.id, "Привет! Добро пожаловать в инвестиции Grand Mobile.", reply_markup=markup)

# Обработка кнопок
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "👤 Личный кабинет":
        bot.send_message(message.chat.id, "👤 Твой профиль:\nБаланс: 0 виртов\nАктивный вклад: 0 виртов")
    
    elif message.text == "🧮 Калькулятор прибыли":
        bot.send_message(message.chat.id, "🧮 Прибыль составляет 3% в день.\nВведите сумму вклада (например: 5000000), чтобы посчитать доход.")
    
    elif message.text == "📥 Пополнить":
        bot.send_message(message.chat.id, "📥 Чтобы пополнить баланс, напиши сумму и свой ник в игре, а затем передай деньги админу.")
        
    elif message.text == "📤 Вывести":
        bot.send_message(message.chat.id, "📤 Напиши сумму для вывода и свой игровой ник. Заявка отправлена администратору.")
        bot.send_message(ADMIN_ID, f"⚠️ Новая заявка на вывод от @{message.from_user.username} ({message.from_user.id})!")

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()
