class Animal:

    def sound(self):
        print("some generic animal sound.")


animal = Animal()
print(animal.sound())


class Dog(Animal):
    def sound(self):
        print("Woof!")