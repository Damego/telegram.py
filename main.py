from telegram.client.bot import Bot

bot = Bot("5558997908:AAGHTZzspej6_Snf8VWjQSyPN7P4TrayuR0")


@bot.on_message()
async def fas(msg):
    print(msg)

bot.run()
