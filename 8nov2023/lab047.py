class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("Bow Bow")

call_dog = Dog()
call_dog.speak()
