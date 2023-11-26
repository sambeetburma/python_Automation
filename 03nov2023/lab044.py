class Car:
    def __init__(self, make, model):
        self.make = make #instance variable
        self.model = model
        print("i will be called first")

    def start_engine(self):
        print("starting a car engine", self.make, self.model)


car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

car1.start_engine()
car2.start_engine()

print(id(car1))
print((id(car2)))
