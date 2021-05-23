import datetime
import yfinance as yf

from aiogram import types
from aiogram.dispatcher.filters import Command, Text

from loader import dp

@dp.message_handler(Command("present_value"))
async def getting_value(message: types.Message):
    await message.answer("Введите тикер акции")


# @dp.message_handler(Text(ignore_case=False))
# async def get_tiker2(message: types.Message):
#     await message.answer("fuf")



# @dp.message_handler()
# async def get_present_value(message: types.Message):
#     tiker = message.text
#     current_date = datetime.now().date()
#     x = str(current_date)
#     data = yf.download(tiker, x)
#     printstr = data['Adj Close']
#     await message.answer("asdasd")



