# Generated by Django 4.0.4 on 2022-04-13 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_city_options_alter_collection_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='created',
        ),
        migrations.AddField(
            model_name='collection',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ссылка'),
        ),
    ]
