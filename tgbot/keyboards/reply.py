from itertools import chain

from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def regions_keyboard():
    keyboard = ReplyKeyboardBuilder()
    buttons = [
        ['Toshkent', 'Fargona', 'Andijon'],
        ['Buxoro', 'Guliston', 'Samarqand'],
        ['Namangan', 'Navoiy', 'Jizzax'],
        ['Nukus', 'Qarshi', 'Xiva'],
        ['Qoqon']
    ]
    keyboard.row(*[KeyboardButton(text=i) for i in chain(*buttons)], width=3)
    return keyboard.as_markup(resize_keyboard=True)
