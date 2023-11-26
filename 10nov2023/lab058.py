x = int(input("enter a value:"))
y = int(input("enter a value:"))
try:
    result = x/y
    print("result:", result)
    def mul(a,b):
        return a*b

except Exception as error:
    print("Error:", error)


finally:
    print("But print this")


mul = mul(10, 5)
print("multiplication", mul)







