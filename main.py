import asyncio
import logging

from decouple import config


from aiogram import Bot, Dispatcher, Router, types,F
from aiogram.filters import CommandStart, Command   


TOKEN = config("TOKEN")

dp = Dispatcher() # объект диспетчера (оброботчик событий)
bot = Bot(TOKEN)

# async - асинхронная функция (позволяет не блокировать выполнение кода)
# await - ожидание выполнения асинхронной функции



@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}!")

@dp.message(Command("help"))
async def maybe_help(message: types.Message):
    await message.answer("I can't help you, sorry")
    await message.answer("Можешь відправити мені будь-яке повідомлення...")


@dp.message(F.text == 'hi')
async def hi_handler(message: types.Message):
    await message.answer("Hello, my friend!")
    
    
@dp.message(F.photo)
async def photo_handler(message: types.Message):
    await message.answer("Nice photo!")
    await bot.send_photo(222201019, message.photo[-1].file_id)


@dp.message()
async def echo_handler(message: types.Message):
    print(message)
    print(f'User: {message.from_user.full_name} - {message.from_user.id} | Message: {message.text}')
    await message.answer(message.text)





async def main() -> None:
   
    await dp.start_polling(bot)


if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    asyncio.run(main())