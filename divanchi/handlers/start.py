
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("⭕️ Выключение"), KeyboardButton("❌ Отменить выключение"))
    keyboard.add(KeyboardButton("🔄 Перезагрузка"), KeyboardButton("🔒 Заблокировать экран"))
    keyboard.add(KeyboardButton("🖥 Скриншот"))
    keyboard.add(KeyboardButton("🎯 Координаты мыши"))
    keyboard.add(KeyboardButton("🖱 Клик мыши"), KeyboardButton("📍 Переместить мышь"))
    keyboard.add(KeyboardButton("🚬 Пробел"))
    return keyboard

def register(bot):
    @bot.message_handler(commands=['start'])
    async def start_handler(message):
        await bot.send_message(message.chat.id, "управляй пк через телеграм", reply_markup=keyboard())