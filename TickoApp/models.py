from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.CharField(max_length=30)
    message=models.TextField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    date=models.DateTimeField()
    depart=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    bus=models.CharField(max_length=20)
    seatno=models.CharField(max_length=20)

    def __str__(self):
        return self.name