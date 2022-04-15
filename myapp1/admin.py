from django.contrib import admin
from django.db import models
from .models import Type, Item, Client, OrderItem

@admin.action(description='FIRSTNAMECAPS')
def firstnameupper(obj):
    return obj.first_name.upper()

class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name']


# Register your models here.
admin.site.register(Type)
admin.site.register(Item)
admin.site.register(Client,ClientAdmin)
admin.site.register(OrderItem)