# Generated by Django 3.2.5 on 2021-07-27 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('style_image', models.TextField()),
                ('product_image', models.TextField()),
                ('color', models.CharField(max_length=20)),
                ('season', models.CharField(max_length=2)),
                ('product_description', models.TextField()),
                ('product_type', models.IntegerField()),
                ('price', models.CharField(max_length=10)),
                ('usage', models.CharField(max_length=20)),
                ('product_link', models.TextField()),
                ('location', models.CharField(max_length=1)),
                ('style_products', models.ManyToManyField(related_name='_products_product_style_products_+', to='products.Product')),
            ],
        ),
    ]
