import pytest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


def test_default_product_price():
    prod = Product("Test Product")
    assert prod.price == 10


def test_create_product():
    name = "test a"
    price = 10
    flammability = 0.3
    weight = 20
    identifier = 1000000
    test_product = Product(
        name=name,
        price=price,
        flammability=flammability,
        weight=weight,
        identifier=identifier,
    )
    assert (
        type(test_product) == Product
        and test_product.name == name
        and test_product.price == price
        and test_product.weight == weight
        and test_product.identifier == identifier
        and test_product.flammability == flammability
    )


def test_methods_product():
    name = "test a"
    price = 10
    flammability = 0.5
    weight = 20
    identifier = 1000000
    test_product = Product(
        name=name,
        price=price,
        flammability=flammability,
        weight=weight,
        identifier=identifier,
    )
    assert (
        test_product.stealability() == "Kinda stealable."
        and test_product.explode() == "...boom!"
    )


def test_default_num_products():
    x = generate_products()
    assert len(x) == 30


def test_legal_names():
    products = generate_products()
    for i in products:
        a, b = i.name.split()
        assert a in ADJECTIVES and b in NOUNS
