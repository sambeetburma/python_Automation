class A:
    def greet(self):
        print("Hello from class A")


class B:
    def greet(self):
        print("Hello from class B")


class C(B, A):
    pass


class D(A, B):
    pass


obj1 = C()
obj1.greet()

obj2 = D()
obj2.greet()

print(C.mro())
print(D.mro())
