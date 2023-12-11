from django.db import models



# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=250, unique=True)
    author = models.CharField(max_length=250)
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to='books/')
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    