class MathUtils:
    def add(self, a, b=0, c=0):
        return a + b+ c

math = MathUtils()
op1 = math.add(1)
print(op1)
op2 = math.add(1,3)
print(op2)
op3 = math.add(2,4,5)
print(op3)
