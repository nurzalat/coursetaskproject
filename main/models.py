from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, related_name='product_to_user', on_delete=models.CASCADE)
    price = models.FloatField()
