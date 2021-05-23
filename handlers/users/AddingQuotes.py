from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Quotes

portfolioname = []
tiker = []
date = []
price = []
kol = []


@dp.message_handler(Command("addingPortfolio"), state=None) # при вводе команды adding попадает сюда
async def enter_addingportfolio(message: types.Message):
    await message.answer("Введите название портфеля")

    await Quotes.portfolio_name.set()
#await Quotes.first()

@dp.message_handler(state=Quotes.portfolio_name)
async def answer_portfolio_name(message: types.Message, state: FSMContext):
    temp = message.text
    portfolioname.append(temp)
    await state.update_data(portfolio_name=temp)
    #async  with state.proxy() as data:
    #    data["portfolio_name"] = p_name

    await message.answer("Введите тикер акции")
    await Quotes.stock_ticker.set()

@dp.message_handler(state=Quotes.stock_ticker)
async def answer_stock_ticker(message: types.Message, state: FSMContext):
    temp = message.text
    await state.update_data(stock_ticker=temp)
    tiker.append(temp)
    # data = await state.get_data()
    # portfolio_name = data.get("portfolio_name")
    # stock_ticker = message.text

    await message.answer("Введите дату покупки")
    await Quotes.next()

@dp.message_handler(state=Quotes.purchase_date)
async def answer_purchase_date(message: types.Message, state: FSMContext):
    temp = message.text
    await state.update_data(purchase_date=temp)
    date.append(temp)
    # data = await state.get_data()
    # portfolio_name = data.get("portfolio_name")
    # stock_ticker = data.get("stock_ticker")
    # purchase_date = message.text

    await message.answer("Введите цену покупки")
    await Quotes.next()

@dp.message_handler(state=Quotes.purchase_price)
async def answer_purchase_price(message: types.Message, state: FSMContext):
    temp = message.text
    price.append(temp)
    await state.update_data(purchase_price=temp)

    # data = await state.get_data()
    # portfolio_name = data.get("portfolio_name")
    # stock_ticker = data.get("stock_ticker")
    # purchase_date = data.get("purchase_date")
    # purchase_price = message.text

    await message.answer("Введите количество купленных акций")
    await Quotes.next()


@dp.message_handler(state=Quotes.quantity)
async def answer_quantity(message: types.Message, state: FSMContext):
    temp = message.text
    kol.append(temp)
    await state.update_data(quantity=temp)

    data = await state.get_data()
    portfolio_name = data.get("portfolio_name")
    stock_ticker = data.get("stock_ticker")
    purchase_date = data.get("purchase_date")
    purchase_price = data.get("purchase_price")
    quantity = message.text

    await message.answer("Ваши данные:")
    await message.answer(f"Портфель : {portfolio_name}")
    await message.answer(f"Тикер акции : {stock_ticker}")
    await message.answer(f"Дата покупки : {purchase_date}")
    await message.answer(f"Стоимость покупки : {purchase_price}")
    await message.answer(f"Количество : {quantity}")
    #await message.answer(f"списки : {portfolioname}")
    # await message.answer(data) # на этом моменте нужно добавлять в БД


#сбрасываем стате сохраняя дату
    await state.reset_state(with_data=False)













