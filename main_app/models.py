from django.db import models
from django.urls import reverse

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def get_absolute_url(self):
        return reverse('home')