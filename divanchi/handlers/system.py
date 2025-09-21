
import os

def register(bot):
    @bot.message_handler(func=lambda message: message.text == "⭕️ Выключение")
    async def shutdown_handler(message):
        await bot.send_message(message.chat.id, "пк выключиться через 40 минут")
        os.system(f"shutdown -s -t 2400")

    @bot.message_handler(func=lambda message: message.text == "❌ Отменить выключение")
    async def cancel_shutdown_handler(message):
        await bot.send_message(message.chat.id, "выход из системы отменен")
        os.system(f"shutdown -a")

    @bot.message_handler(func=lambda message: message.text == "🔄 Перезагрузка")
    async def reboot_handler(message):
        await bot.send_message(message.chat.id, "перезагрузка")
        os.system("shutdown /r /t 5")

    @bot.message_handler(func=lambda message: message.text == "🔒 Заблокировать экран")
    async def lock_screen_handler(message):
        if os.name == "nt":
            os.system("rundll32.exe user32.dll,LockWorkStation")
            
        await bot.send_message(message.chat.id, "экран заблокирован")