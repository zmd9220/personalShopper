from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    style_image = models.TextField()
    product_image = models.TextField()
    color = models.CharField(max_length=20)
    season = models.CharField(max_length=2)
    style_products = models.ManyToManyField('self')
    product_description = models.TextField()
    product_type = models.IntegerField()
    price = models.CharField(max_length=10)
    usage = models.CharField(max_length=20)
    product_link = models.TextField()
    location = models.CharField(max_length=1)

