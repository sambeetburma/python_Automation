class Grandfather:
    def cycle(self):
        return "only ride cycle"


class Father(Grandfather):
    def car(self):
        return "This is my car."

    def bike(self):
        return "This is my bike"


class Son(Father):
    pass


class Daughter(Father):
    pass


# father oject
father_obj = Father()
print("father", father_obj.cycle())
print("father", father_obj.car())
print("father", father_obj.bike())

# son object
son_obj = Son()
print("son", son_obj.bike())
print("son", son_obj.car())

# daughter object
daughter_obj = Daughter()
print("daughter", daughter_obj.car())
