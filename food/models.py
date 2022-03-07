from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    name_of_product = models.CharField(
        max_length=200, default=None, blank=True, null=True)
    picture_of_product = models.CharField(
        max_length=500, default=None, blank=True, null=True)
    nutriscore = models.CharField(
        max_length=20, default=None, blank=True, null=True)
    url_of_product = models.CharField(
        max_length=500, default=None, blank=True, null=True)
    nutriscore_letter = models.CharField(
        max_length=10, default=None, blank=True, null=True)
    energy_product = models.CharField(
        max_length=500, default=None, blank=True, null=True)
    fat_product = models.CharField(
        max_length=500, default=None, blank=True, null=True)
    proteins_product = models.CharField(
        max_length=500, default=None, blank=True, null=True)
    sugar_product = models.CharField(
        max_length=500, default=None, blank=True, null=True)

    def __str__(self):
        return self.name_of_product

    class Meta:
        verbose_name_plural: 'Product'


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    favorite_object_id = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name_of_product + ' ' + self.user.first_name

    class Meta:
        verbose_name_plural: 'Favorite'
