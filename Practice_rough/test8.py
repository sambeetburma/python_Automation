class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def s_name(self, name):
        if name == "john":
            print("do not set the name")
        else:
            self.__name = name

    def g_name(self):
        return self.__name


person_name = Person("sambeet", 37)

print(person_name.g_name())
person_name.s_name("john")
print(person_name.g_name())
