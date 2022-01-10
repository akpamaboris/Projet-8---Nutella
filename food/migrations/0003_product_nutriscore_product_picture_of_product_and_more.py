# Generated by Django 4.0 on 2022-01-09 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_remove_product_nutriscore_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='nutriscore',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='picture_of_product',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='url_of_product',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name_of_product',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
