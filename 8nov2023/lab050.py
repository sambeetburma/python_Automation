class GrandFather:
    def method_grantfather(self):
        return "Grandfather method"


class Father(GrandFather):
    def method_father(self):
        return "father method"


class Mother(GrandFather):
    def method_mother(self):
        return "mother method"


class Son(Father, Mother, GrandFather):
    def method_son(self):
        return "son method" 


son_obj = Son()
print(son_obj.method_grantfather())
print(son_obj.method_father())
print(son_obj.method_mother())
