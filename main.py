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

async def main():
    print('pollingg..')
    await dp.start_polling(bot)

if __name__ =='__main__':
    asyncio.run(main())