from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from handlers.users.AddingQuotes import portfolioname, tiker, date, price, kol
from loader import dp
from states import Quotes


@dp.message_handler(Command("list"))
async def showlists(message: types.Message):
    await message.answer(f"списки : {portfolioname},{tiker},{date},{price},{kol}")