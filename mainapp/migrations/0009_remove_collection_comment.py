# Generated by Django 4.0.4 on 2022-04-14 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_chatuser_delete_userchatid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='comment',
        ),
    ]
