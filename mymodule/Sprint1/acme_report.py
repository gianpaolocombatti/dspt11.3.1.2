import random
import statistics
import numpy as np
from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ["Awesome", "Shiny", "Impressive", "Portable", "Improved"]
NOUNS = ["Anvil", "Catapult", "Disguise", "Mousetrap", "???"]


def generate_products(x=30):
    products = []
    for i in range(x):
        adjectives = np.random.choice(ADJECTIVES)
        nouns = np.random.choice(NOUNS)
        price = np.random.randint(5, 101)
        weight = np.random.randint(5, 101)
        flammability = round(random.uniform(0.0, 2.6), 1)
        full_name = adjectives + " " + nouns
        product = Product(
            name=full_name, price=price, weight=weight, flammability=flammability
        )
        products.append(product)
    return products


def inventory_report(products):
    unique_1 = []
    for i in products:
        unique_1.append(i.name)
    unique_2 = set(unique_1)

    unique_3 = len(unique_2)

    prices = [i.price for i in products]
    price_mean = statistics.mean(prices)
    weight = [i.weight for i in products]
    weight_mean = statistics.mean(weight)
    flammability = [i.flammability for i in products]
    flammability_mean = statistics.mean(flammability)

    print(
        f"ACME CORPORATION OFFICIAL INVENTORY REPORT\n"
        f"Number of unique product names: {unique_3}\n"
        f"Average price: {price_mean}\n"
        f"Average weight: {weight_mean}\n"
        f"Average flammability: {flammability_mean}"
    )


if __name__ == "__main__":
    inventory_report(generate_products())
