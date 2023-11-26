class Myclass:
    #name = None # Not advisable to hardcode the value
    #print(name)
    def print_my_name_with_last_name(self, name, last_name, age):
        print("Your name is -> " + name + last_name + age)


sambeet_obj_ref = Myclass()
#sambeet_obj_ref.name = "Sambeet burma"
#sambeet_obj_ref.name = "sambeet"
sambeet_obj_ref.print_my_name_with_last_name\
    (name="Sambeet", last_name="Burma", age = "37")
#sambeet_obj_ref.print_my_name_with_last_name("Burma")
#sambeet_obj_ref.print_my_name_with_last_name("37")
#ambeet_obj_ref.print_my_name_with_last_name("Company")