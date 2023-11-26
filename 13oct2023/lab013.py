num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#result = "Numbers are equal" if num1 == num2 else "Numbers are not equal"
result = "greater than" if num1 > num2 else "less than" if num1 < num2 else "equal to"
print(f"{num1} is {result} {num2}")

