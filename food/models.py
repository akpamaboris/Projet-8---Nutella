from django.db import models

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

    def __str__(self):
        return self.name_of_product

    class Meta:
        verbose_name_plural: 'Product'
