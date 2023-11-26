class car:

    def start_engine(self, carbrand, carname):
        print(self.carbrand, self.carname)


car1 = car()
car2 = car()

car1.start_engine("Toyota", "camry")
car2.start_engine("Honda", "civic")
