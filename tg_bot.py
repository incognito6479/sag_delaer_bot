#!/usr/bin/python

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sag.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

import logging
import keyboards as kb
from aiogram import Bot, Dispatcher, executor, types
from environs import Env
from mainapp.models import *

env = Env()
env.read_env()

logging.basicConfig(level=logging.INFO)

bot = Bot(token=env('API_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', ])
async def send_welcome(message: types.Message):
    await message.reply('Вас приветствует Telegram-бот компании SAG Gilamlari', reply_markup=kb.start_kb)


@dp.message_handler()
async def echo(message: types.Message):
    sent_answer = False
    cities = City.objects.all()
    dealers = Dealer.objects.all()
    collections = Collection.objects.all()
    sub_collections = SubCollection.objects.all()
    for collection in collections:
        if message.text == collection.name:
            sent_answer = True
            text = 'Выберите коллекцию ' + collection.name
            await message.answer(text, reply_markup=kb.get_sub_collections_kb(collection.id))
    for sub_collection in sub_collections:
        if message.text == sub_collection.name:
            sent_answer = True
            await message.answer(sub_collection.link)
    for city in cities:
        if message.text in city.name:
            text = ''
            for dealer in dealers:
                if dealer.city_id == city.id:
                    text += dealer.name + '\n📍 Адрес: ' + dealer.address
                    text += '\n☎️ Телефон: ' + dealer.phone + '\n\n'
            sent_answer = True
            await message.answer(text)
    if sent_answer is False:
        if message.text == '🏞 Каталог':
            ChatUser.objects.get_or_create(user_id=message.chat.id)
            await message.answer('Выберите коллекцию', reply_markup=kb.get_collections_kb(message))
        elif message.text == '🏢 Диллеры':
            await message.answer('Выберите Город', reply_markup=kb.get_dealers_kb())
        elif message.text == '📞 Контакты':
            text = '📍 Адрес:\n          ул. Спитаменшох 270 ( Ориентир: Лифтостроительный завод )\n\n'
            text += '☎️ Телефон:\n          +998 (95) 500-72-72\n\n🖥 Сайт:\nhttps://sag.uz'
            await message.answer(text)
        elif message.text == '🏠 Главное Меню':
            await message.answer('Главное меню', reply_markup=kb.start_kb)
        else:
            await message.answer('Используйте меню для пользования ботом', reply_markup=kb.start_kb)


if __name__ == '__main__':
    executor.start_polling(dp)
