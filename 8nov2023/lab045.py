class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


person_name = Person("sambeet", 37)

print(person_name.get_name())
person_name.set_name("burma")
print(person_name.get_name())
