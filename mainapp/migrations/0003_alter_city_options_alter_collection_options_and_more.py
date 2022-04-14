# Generated by Django 4.0.4 on 2022-04-13 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_city_name_alter_collection_has_sub_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категория'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='dealer',
            options={'verbose_name': 'Дилер', 'verbose_name_plural': 'Дилеры'},
        ),
        migrations.AlterModelOptions(
            name='subcollection',
            options={'verbose_name': 'Коллекция', 'verbose_name_plural': 'Коллекции'},
        ),
        migrations.RemoveField(
            model_name='collection',
            name='has_sub',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='link',
        ),
        migrations.AddField(
            model_name='collection',
            name='created',
            field=models.DateTimeField(auto_now=True, verbose_name='Созданный'),
        ),
        migrations.AlterField(
            model_name='subcollection',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.collection', verbose_name='Категория'),
        ),
    ]
