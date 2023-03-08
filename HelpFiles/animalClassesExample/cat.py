# classes are like blueprints
# capitalise class names
from animal import Animal


# inheriting from the Animal class in animal.py
class Cat(Animal):

    # class variable
    number_of_cats = 0

    # constructor
    def __init__(self, cat_name, cat_colour):

        # calling the super class constructor
        super().__init__(cat_name)

        # attributes / instance variable called _name
        # self._name = cat_name
        # self._colour = cat_colour

        super().__init__(cat_colour)

        # adding one to the class variable (this one acts as a counter)
        Cat.number_of_cats += 1

    # this is a method, not a function, because it belongs to a class
    def purr(self):
        print('purr purr')

    def hunt(self, thing):
        print("Yum yum, I'm hunting a", thing)

    # 'getter' method
    def get_name(self):
        return self._name

    # 'setter' method
    def set_height(self, cat_height):
        print(self._name + " is " + cat_height + "cm tall")

    # overriding
    def make_sound(self):
        return "Meow meow"
