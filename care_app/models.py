from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class user_reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password= models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50, null=True)
    Image = models.ImageField('images/', null=True)
    status= models.CharField(max_length=100,null=True)

class category(models.Model):
    category = models.CharField(max_length=100,null=True)
    price = models.CharField(max_length=100,null=True)
    details = models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

class ServiceProvider(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categorys = models.ForeignKey(category, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=50,null=True)
    phone = models.CharField(max_length=50,null=True)
    email = models.CharField(max_length=50, null=True)
    Image = models.ImageField('images/', null=True)
    experience = models.CharField(max_length=50, null=True)
    certificate = models.ImageField('images/', null=True)
    status= models.CharField(max_length=50,null=True)

class bookings(models.Model):

    user = models.ForeignKey(user_reg, on_delete=models.CASCADE)
    serviceprovider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    from_date =  models.CharField(max_length=50, null=True)
    to_date = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
    details = models.CharField(max_length=50, null=True)
    payment = models.CharField(max_length=50, null=True)

class Feedback(models.Model):
    user = models.ForeignKey(user_reg, on_delete=models.CASCADE)
    serviceprovider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    feedback =  models.CharField(max_length=50, null=True)
    status =  models.CharField(max_length=50, null=True)

class rating(models.Model):
    user = models.ForeignKey(user_reg, on_delete=models.CASCADE)
    serviceprovider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    rating =  models.CharField(max_length=50, null=True)
    status =  models.CharField(max_length=50, null=True)