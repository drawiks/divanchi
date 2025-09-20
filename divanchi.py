
from src.app import bot
from asyncio import run

if __name__ == "__main__":
    run(bot.polling())