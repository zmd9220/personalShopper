from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    barcode = models.IntegerField()
    product_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    style_image = models.TextField()
    product_image = models.TextField()
    color = models.CharField(max_length=20)
    season = models.CharField(max_length=2)
    style_products = models.TextField()
    product_description = models.TextField()
    product_type = models.IntegerField()
    price = models.CharField(max_length=10)
    usage = models.CharField(max_length=20)
    product_link = models.TextField()
    location = models.CharField(max_length=1)


class Recommend(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    week_sale10 = IntegerField()
    month_sale10 = IntegerField()
    visit10 = IntegerField()
    week_sale20 = IntegerField()
    month_sale20 = IntegerField()
    visit20 = IntegerField()
    week_sale30 = IntegerField()
    month_sale30 = IntegerField()
    visit30 = IntegerField()
    week_sale40 = IntegerField()
    month_sale40 = IntegerField()
    visit40 = IntegerField()
    week_sale50 = IntegerField()
    month_sale50 = IntegerField()
    visit50 = IntegerField()
    week_sale60 = IntegerField()
    month_sale60 = IntegerField()
    visit60 = IntegerField()


class Customer(models.Model):
    gender = models.CharField(max_length=1)
    age = models.IntegerField()



class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # size = models.JSONField() # 프론트에서 바꿔준다. ex) 신발 의류 바지 사이즈가 다양하기 떄문
    stock = models.JSONField()
