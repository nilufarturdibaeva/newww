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
        [KeyboardButton(text='Menu 🗂️'),KeyboardButton(text="Settings ⚙️"),KeyboardButton(text="Back🔙")]
    ],resize_keyboard=True
)

Help = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Help 🆘'),KeyboardButton(text="Contact 🔎"),KeyboardButton(text="Back 🔙")]
    ],resize_keyboard=True
)

@dp.message(CommandStart())
async def start(m: Message):
    await m.answer(f"Hello {m.from_user.first_name}, how are you? ")

@dp.message(Command('help'))
async def help_command(m: Message):
    await m.answer(f"this is help !", reply_markup=Help)

@dp.message(Command('about'))
async def about_command(m: Message):
    await m.answer(f"this is about !", reply_markup=menu)

@dp.message()
async def menu1(m: Message):
    text = m.text
    if text == "Help 🆘":
        await m.answer(f"This is help!", reply_markup=menu)
    elif text == "Contact 🔎":
        await m.answer(f"This is contact!", reply_markup=menu)
    elif text == "Menu 🗂️":
        await m.answer(f"Here is the menu!", reply_markup=menu)
    elif text == "Settings ⚙️":
        await m.answer(f"Settings are here!", reply_markup=menu)
    elif text == "Back 🔙" or text == "Back🔙":
        await m.answer(f"Going back!", reply_markup=menu)
    else:
        await m.answer(f"I don't understand you.")

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