
from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

import pyautogui

from io import BytesIO
import sys, os, subprocess

from .config import TOKEN

bot = AsyncTeleBot(TOKEN)
users = {}
        
def keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("⏻ Выключение"), KeyboardButton("🔄 Перезагрузка"), KeyboardButton("🔒 Заблокировать экран"))
    keyboard.add(KeyboardButton("🖥 Скриншот"))
    keyboard.add(KeyboardButton("🎯 Координаты мыши"))
    keyboard.add(KeyboardButton("🖱 Клик мыши"), KeyboardButton("📍 Переместить мышь"))
    keyboard.add(KeyboardButton("🚬 Пробел"))
    return keyboard
    
@bot.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id, "управляй пк через телеграм", reply_markup=keyboard())

@bot.message_handler(func=lambda message: message.text == "⏻ Выключение")
async def shutdown(message):
    await bot.send_message(message.chat.id, "пк выключиться через 40 минут")
    os.system(f"shutdown -s -t 2400")

@bot.message_handler(func=lambda message: message.text == "🔄 Перезагрузка")
async def reboot(message):
    await bot.send_message(message.chat.id, "перезагрузка")
    os.system("shutdown /r /t 5")

@bot.message_handler(func=lambda message: message.text == "🔒 Заблокировать экран")
async def lock_screen(message):
    if os.name == "nt":
        os.system("rundll32.exe user32.dll,LockWorkStation")
        
    await bot.send_message(message.chat.id, "экран заблокирован")

@bot.message_handler(func=lambda message: message.text == "🖥 Скриншот")
async def screenshot(message):
    screenshot = pyautogui.screenshot()
    
    bio = BytesIO()
    screenshot.save(bio, format="PNG")
    bio.seek(0)
    
    await bot.send_photo(message.chat.id, bio)

@bot.message_handler(func=lambda message: message.text == "🎯 Координаты мыши")
async def mouse_position(message):
    x, y = pyautogui.position()
    await bot.send_message(message.chat.id, f"курсор сейчас в точке: ({x}, {y})")

@bot.message_handler(func=lambda message: message.text == "🖱 Клик мыши")
async def mouse_click(message):
    pyautogui.click()
    await bot.send_message(message.chat.id, "✅ мышь кликнула")
    
@bot.message_handler(func=lambda message: message.text == "📍 Переместить мышь")
async def ask_mouse_position(message):
    users[message.from_user.id] = True
    await bot.send_message(message.chat.id, "введи координаты X и Y через пробел (пример: 500 300)")

@bot.message_handler(func=lambda message: users.get(message.from_user.id))
async def move_mouse(message):
    try:
        x, y = map(int, message.text.split())
        pyautogui.moveTo(x, y, duration=0.5)
        await bot.send_message(message.chat.id, f"✅ мышь перемещена в ( {x} | {y} )")
    except ValueError:
        await bot.send_message(message.chat.id, "неверный формат")
    finally:
        users.pop(message.from_user.id, None)

@bot.message_handler(func=lambda message: message.text == "🚬 Пробел")
async def space(message):
    pyautogui.press("space")
    await bot.send_message(message.chat.id, "пробел нажат")
