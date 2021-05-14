from aiogram.dispatcher.filters.state import StatesGroup, State

# группа состояний Quotes
class Quotes(StatesGroup):
    portfolio_name = State()
    stock_ticker = State()
    purchase_date = State()
    purchase_price = State()
    quantity = State()
    tax = State()


