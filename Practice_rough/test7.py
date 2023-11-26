class Subject:

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2


obj1 = Subject('Maths','Science')
print("obj1 attribute1:", obj1.attr1)
print("obj1 attribute2:",obj1.attr2)

obj2 = Subject('English', 'Physics')
print("obj2 attribute1:", obj2.attr1)
print("obj2 attribute2:", obj2.attr2)
