from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Выберите нужную команду ниже", reply_markup=menu)


@dp.message_handler(text="Работа с инвестиционным портфелем")
async def get_tiker(message: types.Message):
    await message.answer("Для добавления ценных бумаг нажмите сюда -/addingPortfolio")
    await message.answer("Для просмотра доходности, нажмите сюда - ")



@dp.message_handler(text="Работа с котировками")
async def get_dailystat(message: types.Message):
    await message.answer("Чтобы узнать текущую стоимость, нажмите сюда -  /present_value")
    await message.answer("Чтобы посотреть график изменений, нажмите сюда -  ")

@dp.message_handler(text="Скрыть клавиатуру")
async def get_mounthstat(message: types.Message):
    await message.answer("Для того чтобы открыть меню заново, нажмите сюда - /menu",reply_markup=ReplyKeyboardRemove())


