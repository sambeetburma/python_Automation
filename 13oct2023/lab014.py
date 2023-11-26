num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

max_num = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)

print(f'The maximum of three numbers {num1},{num2},{num3} is {max_num}')
