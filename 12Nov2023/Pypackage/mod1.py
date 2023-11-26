def greet(name):
    print("Hi", name)


class Person():
    def __init__(self, name):
        self.name = name

    def intro(self):
        print("Myself", self.name)
