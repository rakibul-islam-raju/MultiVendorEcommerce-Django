# Generated by Django 3.1.6 on 2021-02-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_category_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.SlugField(blank=True),
        ),
    ]
