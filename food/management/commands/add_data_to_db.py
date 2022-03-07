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
                'products'][count]['product_name_fr']

            pictureOfProduct = response.json()[
                'products'][count]['image_url']

            nutriscoreOfProduct = str(response.json()[
                'products'][count]['nutriscore_score'])

            energyOfProduct = response.json(
            )['products'][count]['nutriments']['energy_100g']
            fatOfProduct = response.json(
            )['products'][count]['nutriments']['fat_100g']
            proteinsOfProduct = response.json(
            )['products'][count]['nutriments']['proteins_100g']
            sugarOfProduct = response.json(
            )['products'][count]['nutriments']['sugars_100g']
            urlOfProduct = response.json()[
                'products'][count]['url']

            nutriscoreLetter = response.json()[
                'products'][count]['nutrition_grade_fr']

            newProduct = Product(name_of_product=nameOfproduct, picture_of_product=pictureOfProduct,
                                 nutriscore=nutriscoreOfProduct, url_of_product=urlOfProduct, nutriscore_letter=nutriscoreLetter,
                                 energy_product=energyOfProduct, fat_product=fatOfProduct, proteins_product=proteinsOfProduct, sugar_product=sugarOfProduct)
            newProduct.save()

            count += 1
