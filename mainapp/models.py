from django.db import models


class ChatUser(models.Model):
    user_id = models.BigIntegerField(verbose_name="ID пользователя")

    def __str__(self):
        return f"{self.user_id}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class City(models.Model):
    name = models.CharField(max_length=200, verbose_name="Город")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Collection(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    order_number = models.IntegerField(null=True, blank=True, verbose_name="Очередь в списке")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"


class Dealer(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    address = models.CharField(max_length=200, verbose_name="Адрес")
    phone = models.CharField(max_length=200, verbose_name="Телефон")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Город")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Дилер"
        verbose_name_plural = "Дилеры"


class SubCollection(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя")
    link = models.CharField(max_length=200, verbose_name="Ссылка")
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name="Категория",
                                   blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"


class Contact(models.Model):
    address = models.CharField(max_length=200, verbose_name="Адрес")
    phone = models.CharField(max_length=200, verbose_name="Телефон")
    site = models.CharField(max_length=200, verbose_name="Интернет сайт")

    def __str__(self):
        return f"{self.address}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
