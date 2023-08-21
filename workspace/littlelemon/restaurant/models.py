import calendar
from django.db import models

# Create your models here.
class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField(default=0)
    bookingDate = models.DateField(default='2000-01-01')
    
class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'