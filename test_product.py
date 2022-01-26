import pytest


from food.models import Product


@pytest.mark.django_db
def test_django_db():
    test_db = Product.objects.create(
        name_of_product="camembert",
        picture_of_product="",
        nutriscore=5,
        url_of_product="",
        nutriscore_letter="A"
    )
    assert test_db.name_of_product == "camembert"
