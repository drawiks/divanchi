
from pyautogui import position, click, moveTo

users = {}

def register(bot):
    @bot.message_handler(func=lambda message: message.text == "🎯 Координаты мыши")
    async def mouse_position_handler(message):
        x, y = position()
        await bot.send_message(message.chat.id, f"курсор сейчас в точке: ({x}, {y})")

    @bot.message_handler(func=lambda message: message.text == "🖱 Клик мыши")
    async def mouse_click_handler(message):
        click()
        await bot.send_message(message.chat.id, "✅ мышь кликнула")
        
    @bot.message_handler(func=lambda message: message.text == "📍 Переместить мышь")
    async def ask_mouse_position_handler(message):
        users[message.from_user.id] = True
        await bot.send_message(message.chat.id, "введи координаты X и Y через пробел (пример: 500 300)")

    @bot.message_handler(func=lambda message: users.get(message.from_user.id))
    async def move_mouse_handler(message):
        try:
            x, y = map(int, message.text.split())
            moveTo(x, y, duration=0.2)
            await bot.send_message(message.chat.id, f"✅ мышь перемещена в ( {x} | {y} )")
        except ValueError:
            await bot.send_message(message.chat.id, "неверный формат")
        finally:
            users.pop(message.from_user.id, None)