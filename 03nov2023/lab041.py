class Myclass:
    name = None # Not advisable to hardcode the value
    print(name)
    def print_my_name(self):
        print("Your name is -> " + self.name)


sambeet_obj_ref = Myclass()
sambeet_obj_ref.name = "Sambeet burma"
sambeet_obj_ref.print_my_name()