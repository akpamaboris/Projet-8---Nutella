from django.core.management.base import BaseCommand
import requests
from food.models import Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        response = requests.get(
            'https://world.openfoodfacts.org/cgi/search.pl?search_tag=categories&search_terms=Snack&json=1')
        length = len(response.json()['products'])
        count = 0
        while count < length:
            nameOfproduct = response.json()[
                'products'][count]['product_name']

            pictureOfProduct = response.json()[
                'products'][count]['image_url']

            nutriscoreOfProduct = str(response.json()[
                'products'][count]['nutriscore_score'])

            urlOfProduct = response.json()[
                'products'][count]['url']

            newProduct = Product(name_of_product=nameOfproduct, picture_of_product=pictureOfProduct,
                                 nutriscore=nutriscoreOfProduct, url_of_product=urlOfProduct)
            newProduct.save()

            count += 1
