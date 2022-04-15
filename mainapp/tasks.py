from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests
from environs import Env

from mainapp.models import ChatUser, SubCollection

env = Env()
env.read_env()


@shared_task
def send_sms_to_users_collections(collection_id):
    collection_obj = SubCollection.objects.get(id=collection_id)
    text = f"        ❗️Новая коллекция ❗        \n"
    text += f"\n\nНазвание коллекции: \n        {collection_obj.name}\n"
    text += f"\nСсылка: \n        {collection_obj.link}\n"
    text += f"\n🏞Категория: \n        {collection_obj.collection}\n"
    users = ChatUser.objects.all()
    for user in users:
        requests.get(f"https://api.telegram.org/bot{env('API_TOKEN')}/sendMessage?chat_id={user.user_id}&text={text}")
    return
