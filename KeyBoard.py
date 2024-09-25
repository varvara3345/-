from imghdr import tests

from aiogram import types

main_kb = types.ReplyKeyboardMarkup(
    keyboard=[
    [types.KeyboardButton(text="Список дат")]
],
    resize_keyboard=True
)

test_kb = types.ReplyKeyboardMarkup(
    keyboard=[
    [types.KeyboardButton(text="Тест")]
],
    resize_keyboard=True
)

question1 = types.ReplyKeyboardMarkup(
    keyboard=[
    [types.KeyboardButton(text="Похудеть"),types.KeyboardButton(text="Накачаться")]
],
    resize_keyboard=True
)

question2 = types.ReplyKeyboardMarkup(
    keyboard=[
    [types.KeyboardButton(text="49кг и менее"),types.KeyboardButton(text="50-74кг"),types.KeyboardButton(text="75-99кг"),types.KeyboardButton(text="100кг и более")]
],
    resize_keyboard=True
)

question3 = types.ReplyKeyboardMarkup(
    keyboard=[
    [types.KeyboardButton(text="Женский"),types.KeyboardButton(text="Мужской")]
],
    resize_keyboard=True
)

def date_kb(k):
    return types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text=i)] for i in k],
                                     resize_keyboard=True)
