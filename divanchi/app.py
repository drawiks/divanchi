
from telebot.async_telebot import AsyncTeleBot

from .handlers import start, system, mouse, keyboard, screenshot
from .config import TOKEN

bot = AsyncTeleBot(TOKEN)

start.register(bot)
system.register(bot)
mouse.register(bot)
keyboard.register(bot)
screenshot.register(bot)
