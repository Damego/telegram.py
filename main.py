from os import environ

from telegram import Bot, Message
from dotenv import load_dotenv
load_dotenv()

bot = Bot(environ["TOKEN"])


@bot.on_message()
async def fas(message: Message):
    await message.reply_text(message.text)

bot.run()
