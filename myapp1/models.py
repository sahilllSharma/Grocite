from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        details = "Type with name {}"
        return details.format(self.name)


class Item(models.Model):
    type = models.ForeignKey(Type, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    product_description = models.TextField(blank=True)
    interested = models.PositiveIntegerField(default=0)

    def topup(self):
        self.stock += 200

    def __str__(self):
        details = "Item with name {}"
        return details.format(self.name)

class Client(User):
    CITY_CHOICES = [('WD', 'Windsor'), ('TO', 'Toronto'), ('CH', 'Chatham'), ('WL', 'Waterloo')]
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='CH')
    interested_in = models.ManyToManyField(Type)
    phone_no = models.CharField(null=True, max_length=30)

    def __str__(self):
        details = "Client: {}"
        return details.format(self.first_name)


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    #no_of_items = models.PositiveIntegerField(default=0)
    STATUS_CHOICES = [('0', 'cancelled order'), ('1', 'placed order'), ('2', 'shipped order'), ('3', 'delivered order')]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='0')
    date = models.DateField(auto_now=True)
    items_ordered = models.PositiveIntegerField(default=0)

    def __str__(self):
        order_details = "Order from city {} whose {} count is {} having status {}"
        return order_details.format(self.client.city, self.item.name, self.no_of_items, self.status)

    def total_price(self):
        return self.item.price * self.no_of_items
