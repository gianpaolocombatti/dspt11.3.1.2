import random


class Product:
    def __init__(
        self,
        name,
        price=10,
        weight=20,
        flammability=0.5,
        identifier=random.randint(1000000, 9999999),
    ):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        pw_ratio = self.price / self.weight
        if pw_ratio < 0.5:
            return "Not so stealable..."
        elif pw_ratio < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        plode = self.flammability * self.weight
        if plode < 10:
            return "...fizzle."
        elif plode < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    def __init__(
        self,
        name,
        price=10,
        weight=10,
        flammability=0.5,
        identifier=random.randint(1000000, 9999999),
    ):
        super(BoxingGlove, self).__init__(
            name=name,
            price=price,
            weight=weight,
            flammability=flammability,
            identifier=identifier,
        )

    def explode(self):
        print("...it's a glove.")

    def punch(self):
        if self.weight < 5:
            print("That tickles.")
        elif self.weight < 15:
            print("Hey that hurt!")
        else:
            print("OUCH!")
