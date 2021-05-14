from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Добавить ценные бумаги по тикерам")
        ],
        [
            KeyboardButton(text="Посмотреть статистику за день"),
            KeyboardButton(text="Посмотреть статистику за месяц"),
            KeyboardButton(text="Посмотреть статистику за месяц"),
        ],
    ],
    resize_keyboard=True
)