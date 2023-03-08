
# Using Cat class from cat.py
from cat import Cat
from dog import Dog

# Instantiating a class
# Creating a new object (instance) using the Cat class
catObj = Cat("Agnes", "Grey")
catObj2 = Cat("Bentley", "Black and white")

catObj.purr()
catObj.hunt('mouse')

print(catObj.get_name())
print(catObj2.get_name())

catObj.set_height('40')
catObj2.set_height('45')

print(Cat.number_of_cats)

dogObj = Dog("Fletcher", "Black and brown")
dogObj.bark()

print(dogObj.make_sound())
print(catObj.make_sound())

print(catObj.sleep())
print(dogObj)
