from os import environ

from telegram import Bot, Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
load_dotenv()

bot = Bot(environ["TOKEN"])


@bot.on_message()
async def fas(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="fdas", callback_data="ff")]]
    )
    await message.reply_text(message.text, reply_markup=keyboard)

@bot.on_callback_query()
async def callback(query: CallbackQuery):
    print(query)

bot.run()
