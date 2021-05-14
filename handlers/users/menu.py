from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Выберите нужную команду ниже", reply_markup=menu)


@dp.message_handler(text="Добавить ценные бумаги по тикерам")
async def get_tiker(message: types.Message):
    await message.answer("Добавлять ценные бумаги тут")


@dp.message_handler(text="Посмотреть статистику за день")
async def get_dailystat(message: types.Message):
    await message.answer("Статистика за день тут")

@dp.message_handler(text="осмотреть статистику за месяц")
async def get_mounthstat(message: types.Message):
    await message.answer("Статистика за месяц тут",reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="осмотреть статистику за год")
async def get_mounthstat(message: types.Message):
    await message.answer("Статистика за год тут")

