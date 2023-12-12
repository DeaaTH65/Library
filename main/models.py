from django.db import models
from users.models import CustomUser



# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=250, unique=True)
    author = models.CharField(max_length=250)
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to='books/')
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name


class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reserved_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reservation_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.book.name} - Reserved by {self.reserved_by}"

    class Meta:
        ordering = ['-reservation_date']