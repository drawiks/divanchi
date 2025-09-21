
from pyautogui import press

def register(bot):
    @bot.message_handler(func=lambda message: message.text == "🚬 Пробел")
    async def space_handler(message):
        press("space")
        await bot.send_message(message.chat.id, "пробел нажат")