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
    collection = Collection.objects.filter(name__exact=str(message.text))
    if collection:
        collection = collection.first()
        sent_answer = True
        text = 'Выберите коллекцию ' + collection.name
        await message.answer(text, reply_markup=kb.get_sub_collections_kb(collection.id))
    sub_collection = SubCollection.objects.filter(name__exact=str(message.text))
    if sub_collection:
        sub_collection = sub_collection.first()
        sent_answer = True
        await message.answer(sub_collection.link)
    city = City.objects.filter(name__exact=str(message.text))
    if city:
        city = city.first()
        text = ''
        dealer = Dealer.objects.filter(city_id=city.id)
        if dealer:
            dealer = dealer.first()
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
