from django.db import models
from datetime import datetime


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    button_text = models.CharField(max_length = 20, blank = True)
    write_up = models.CharField(max_length = 10000)
    date = models.DateTimeField(default = datetime.now, blank = True)
    image = models.ImageField(upload_to = "img", blank = True, null = True)
 

class Room(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Messages(models.Model):
    username = models.CharField(max_length=1000)
    room = models.CharField(max_length=1000)
    messages = models.CharField(max_length = 1000)
    date = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.username
    
    
class User(models.Model):
    username = models.CharField(max_length = 30, default = None)
    email = models.CharField(max_length = 100, default = None)


class Students(models.Model):
    name = models.CharField(max_length = 100, default = None)
    age = models.IntegerField()
    description = models.TextField()
    date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
