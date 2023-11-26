from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def eat(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Bow bow"

    def eat(self):
        return "Eates bones"


class Cat(Animal):
    def sound(self):
        return "Meow Meow"

    def eat(self):
        return "Eats fish"


dog = Dog()
print(dog.eat())
print(dog.sound())
print("--------------------")
cat = Cat()
print(cat.eat())
print(cat.sound())

animal = Animal()
print(animal.sound())
