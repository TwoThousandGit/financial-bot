import datetime
import yfinance as yf

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp

@dp.message_handler(Command("present_value"))
async def show_menu(message: types.Message):
    await message.answer("Введите тикер акции")

    async def get_present_value(message: types.Message):
        tiker = message.text
        current_date = datetime.now().date()
        x = str(current_date)
        data = yf.download(tiker, x)
        printstr = data['Adj Close']
        await message.answer(data['Adj Close'])

