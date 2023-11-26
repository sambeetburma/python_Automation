class Car:
    #color = None
    #model = None

    def car_details(self):
        print("Your car detail is ", self.color, self.model)


#car_color = input("Enter your car color: ")
#car_model = input("Enter the car model: ") \#can remove these two

car_obj_ref = Car()
car_obj_ref.color = input("Enter your car color: ")
car_obj_ref.model = input("Enter the car model: ")
car_obj_ref.car_details()
