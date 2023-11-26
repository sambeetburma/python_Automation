class Grandparents:
    def grand_parent_property(self):
        return "Grandparent's method"

class Parents(Grandparents):
    def parent_method(self):
        return "Parent's method"

class Child(Parents):
    def child_method(self):
        return "child's method"


child_obj = Child()
print(child_obj.grand_parent_property())
print(child_obj.parent_method())
print(child_obj.child_method())
grandfather_obj = Grandparents()
grandfather_obj.grand_parent_property()#only grandparent property not child property
parent_obj = Parents() #only grantparents and parents properties can be inherited
parent_obj.parent_method()
parent_obj.grand_parent_property()