from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from tgbot.keyboards.reply import regions_keyboard
from tgbot.utils.api import get_prayer_tymes
from tgbot.utils.texts import get_regions_names, Text

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    text = """
        Assalomu aleykum. Namoz vaqtlari botga xush kelibsiz. """
    await message.answer(text, reply_markup=regions_keyboard())


@user_router.message(F.text.in_({*get_regions_names()}))
async def region_handler(message: Message):
    times = await get_prayer_tymes(message.text)
    text = f"""
☪️ Namoz vaqtlari:

Bomdod: {times[0]}
Quyosh: {times[1]}
Peshin: {times[2]}
Asr: {times[3]}
Shom: {times[4]}
Xufton: {times[5]}

Manba: namozvaqti.uz

📢@namoz_toshkent1
📢@namoz_vaqtlari_4
🤖@namaz_vaqti_bot"""
    await message.reply(text)


@user_router.message(F.text == Text.today)
async def handler(message: Message):
    await message.answer("Hududni tanlang 👇🏻", reply_markup=regions_keyboard())
