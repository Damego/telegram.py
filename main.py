from os import environ

from telegram.client.bot import Bot

bot = Bot(environ["TOKEN"])


@bot.on_message()
async def fas(msg):
    print(msg)

bot.run()
