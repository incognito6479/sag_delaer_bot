import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sag.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

from aiogram import types
from mainapp.models import *

buttons = {
    'catalog': types.KeyboardButton('🏞 Каталог'),
    'dealers': types.KeyboardButton('🏢 Диллеры'),
    'contacts': types.KeyboardButton('📞 Контакты'),
    'home': types.KeyboardButton('🏠 Главное Меню'),
}

start_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.add(buttons['catalog']).add(buttons['dealers']).add(buttons['contacts'])


def get_collections_kb(message):
    collections_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    collections = Collection.objects.all()
    n = 1
    keyboard = {}
    for collection in collections:
        if n == 1:
            keyboard['first'] = types.KeyboardButton(str(collection.name))
            n = 2
        elif n == 2:
            keyboard['second'] = types.KeyboardButton(str(collection.name))
            n = 3
        else:
            keyboard['third'] = types.KeyboardButton(str(collection.name))
            collections_kb.row(keyboard['first'], keyboard['second'], keyboard['third'])
            keyboard = {}
            n = 1
    if keyboard != {}:
        if 'first' in keyboard:
            if 'second' in keyboard:
                collections_kb.row(keyboard['first'], keyboard['second'], )
            else:
                collections_kb.row(keyboard['first'], )
    collections_kb.add(buttons['home'])
    return collections_kb


def get_sub_collections_kb(collection):
    sub_collections_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sub_collections = SubCollection.objects.all()
    for sub_collection in sub_collections:
        if sub_collection.collection_id == collection:
            sub_collections_kb.add(types.KeyboardButton(str(sub_collection.name)))
    sub_collections_kb.add(buttons['catalog'])
    sub_collections_kb.add(buttons['home'])
    return sub_collections_kb


def get_dealers_kb():
    dealers_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cities = City.objects.all()
    n = 1
    keyboard = {}
    for city in cities:
        if n == 1:
            keyboard['first'] = types.KeyboardButton(str(city.name))
            n = 2
        elif n == 2:
            keyboard['second'] = types.KeyboardButton(str(city.name))
            n = 3
        else:
            keyboard['third'] = types.KeyboardButton(str(city.name))
            dealers_kb.row(keyboard['first'], keyboard['second'], keyboard['third'])
            keyboard = {}
            n = 1
    if keyboard == {}:
        dealers_kb.add(buttons['home'])
        return dealers_kb
    else:
        if 'first' in keyboard:
            if 'second' in keyboard:
                dealers_kb.row(keyboard['first'], keyboard['second'], )
            else:
                dealers_kb.row(keyboard['first'], )
        dealers_kb.add(buttons['home'])
        return dealers_kb


contacts_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
contacts_kb.add(buttons['home'])
