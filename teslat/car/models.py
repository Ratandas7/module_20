from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    brand = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    def __str__(self):
        return self.brand
    

class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.model
    

class Car(models.Model):
    image = models.ImageField(upload_to='car/media/uploads/')
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, null=True, blank=True)
    price = models.IntegerField()
    model = models.OneToOneField(Model, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    quantity = models.IntegerField(default=0)
    date = models.DateField(default=datetime.now)
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='reviews')
    # model = models.OneToOneField(Model, on_delete=models.CASCADE, default=Model)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    comment = models.TextField()
    date = models.DateField(default=datetime.now)
    def __str__(self):
        return self.name
    

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='orders')
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING, related_name='cars')
    order_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.customer.username