import asyncio
from aiogram import Bot,Dispatcher
from aiogram.types import Message,ReplyKeyboardMarkup,KeyboardButton
from aiogram.filters import CommandStart,Command
import os

from dotenv import load_dotenv
load_dotenv()

Token = os.getenv('TOKEN')
bot = Bot(token=Token)
dp = Dispatcher()
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Menu 🗂'),
            KeyboardButton(text="Settings ⚙️"),
            KeyboardButton(text="Back 🔙")
        ]
    ],
    resize_keyboard=True
)

Help = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Help 🆘'),
            KeyboardButton(text="Contact 🔎"),
            KeyboardButton(text="Back 🔙")
        ]
    ],
    resize_keyboard=True
)
@dp.message(CommandStart)
async def start(message:Message):
    await message.answer(f"Hello {message.from_user.first_name}!")

# /menu
@dp.message(Command("menu"))
async def menu_command(message: Message):
    await message.answer("📂 This is menu", reply_markup=menu)

# /help
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("🆘 Choose help option")

# /settings
@dp.message(Command("settings"))
async def settings_command(message: Message):
    await message.answer("⚙️ Settings section")

# /contact
@dp.message(Command("contact"))
async def contact_command(message: Message):
    await message.answer("📩 Contact: @your_username")

@dp.message()
async def buttons(message: Message):
    text = message.text

    if text == "Menu 🗂":
        await message.answer("📂 You opened menu")

    elif text == "Settings ⚙️":
        await message.answer("⚙️ Settings menu")

    elif text == "Help 🆘":
        await message.answer("🆘 Help section")

    elif text == "Contact 🔎":
        await message.answer("📩 Contact: @your_username")

@dp.message()
async def main():
    print('pollingg..')
    await dp.start_polling(bot)

if __name__ =='__main__':
    asyncio.run(main())