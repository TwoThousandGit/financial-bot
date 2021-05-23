from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Работа с инвестиционным портфелем")
        ],
        [
            KeyboardButton(text="Работа с котировками"),
            KeyboardButton(text="Скрыть клавиатуру"),
        ],
    ],
    resize_keyboard=True
)