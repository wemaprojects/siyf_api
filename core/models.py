from django.db import models
from uuid import uuid4
# Create your models here.

def gen_uuid4_hexed():
    return uuid4().hex

class Feedback(models.Model):
    email = models.EmailField() 
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=1024)


class HeaderNews(models.Model):
    id = models.CharField(max_length=1024, primary_key=True , default=gen_uuid4_hexed)
    image = models.ImageField(default=gen_uuid4_hexed)
    text = models.TextField()
    

class News(models.Model):
    id = models.CharField(max_length=1024, primary_key=True , default=gen_uuid4_hexed)
    image = models.ImageField(default=gen_uuid4_hexed)
    text = models.TextField()

