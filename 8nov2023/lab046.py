class Password:
    def __init__(self, password):
        self.__password = password

    def get_password(self, is_auth):
        if is_auth:
            return self.__password
        else:
            print("Error")

    def set_password(self, password):
        if len(password) > 12:
            self.__password = password
        else:
            print("It's weak, password should be more than 12 char")


my_password = Password("sambeet@123")
print(my_password.get_password(True))
my_password.set_password("sambeet")
print("My password has changed to:", my_password.get_password(True))
