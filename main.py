from os import environ

from telegram import Bot, Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
load_dotenv()

bot = Bot(environ["TOKEN"])


@bot.on_startup()
async def start():
    print(f"logged in as {bot.user.first_name}")


@bot.on_message()
async def fas(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="fdas", callback_data="ff")]]
    )
    await message.reply_text(message.text, reply_markup=keyboard)


@bot.on_callback_query()
async def callback(query: CallbackQuery):
    print(query.message.reply_markup)


@bot.command()
async def test_command():
    print(1)

bot.run()
