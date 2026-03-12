import asyncio
from aiogram import Bot,Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart,Command

TOKEN = "8763458886:AAGyOxXkqNa__6dHh-dBkeKmK8fX2KEpxHI"
bot = Bot(token=TOKEN)
dp = Dispatcher()
@dp.message(CommandStart)
async def start(message:Message):
    await message.answer(f"Assalawmu alikum {message.from_user.first_name}")

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer(f'qanday jardem kerek')

@dp.message(Command('about'))
async def help(message: Message):
    await message.answer(f'test bot')


async def main():
    print('pollingg..')
    await dp.start_polling(bot)

if __name__ =='__main__':
    asyncio.run(main())