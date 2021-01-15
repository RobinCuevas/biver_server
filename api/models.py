from django.db import models

# Create your models here.

class Invoice(models.Model):
    marketplace = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    restaurant = models.CharField(max_length=100)
    price = models.FloatField(max_length=100)
    order = models.CharField(max_length=1000)
    date = models.DateField()
    client_address = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    deliveryperson = models.CharField(max_length=100)
    expiration_date = models.DateField()
    client_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100,default="pending")


    def __str__(self):
        return self.client_name

class Local(models.Model):
    restaurant = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.restaurant
