from django.contrib import admin
from mainapp.models import *


class SubCollectionInline(admin.StackedInline):
    model = SubCollection


@admin.register(Collection)
class CollectionAdminModel(admin.ModelAdmin):
    list_display = ('name', )
    inlines = [SubCollectionInline, ]


@admin.register(SubCollection)
class SubCollectionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'collection')


@admin.register(UserChatId)
class UserModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Dealer)
class DealerModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'city')


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'site')


@admin.register(City)
class CityModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
