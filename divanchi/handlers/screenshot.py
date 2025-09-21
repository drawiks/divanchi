
from io import BytesIO
import pyautogui

def register(bot):
    @bot.message_handler(func=lambda message: message.text == "🖥 Скриншот")
    async def screenshot_handler(message):
        screenshot = pyautogui.screenshot()
        
        bio = BytesIO()
        screenshot.save(bio, format="PNG")
        bio.seek(0)
        
        await bot.send_photo(message.chat.id, bio)