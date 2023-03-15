
from animal import Animal


class Dog(Animal):

    def __init__(self, dog_name, dog_colour):
        super().__init__(dog_name)
        super().__init__(dog_colour)
        print(super())
        # self._name = dog_name

    def bark(self):
        print("Woof Woof")

    # when using the object in place of a string, it will do this
    def __str__(self):
        return "Woof! My name is " + self._name
