from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class my_images(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    img = models.ImageField(default="pic.jpg", upload_to='pics')
    username = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
class Books(models.Model):
    bookID = models.IntegerField()
    title = models.CharField(max_length=120, null=True, blank=True)
    authors = models.CharField(max_length=120)
    average_rating = models.FloatField()
    isbn = models.IntegerField()
    language_code = models.CharField(max_length=120)