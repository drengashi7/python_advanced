class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("somegeneric animal sound.")

    def description(self):
        print(f"this is an animal named {self.name}.")


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        super().sound()

        print("Woof!")

    def description(self):
        super().description()
        print(f"breed:{self.breed}")

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        super().sound()

        print("meow!")

    def description(self):
        super().description()
        print(f"Color:{self.color}")

animal = Animal("Generic Animal")
print(animal.sound())
print(animal.description())

dog = Dog("rex", "husky")
print(dog.sound())
print(dog.description())


cat= Cat("kiko", "white")
print(cat.sound())
print(cat.description())


