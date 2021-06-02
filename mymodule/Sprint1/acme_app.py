from acme import Product
from acme import BoxingGlove

prod = Product("A Cool Toy")
glove = BoxingGlove("Punchy the Third")

print(prod.name)
print(prod.price)
print(prod.weight)
print(prod.flammability)
print(prod.identifier)
prod.stealability()
prod.explode()
print(glove.price)
print(glove.weight)
glove.punch()
glove.explode()
