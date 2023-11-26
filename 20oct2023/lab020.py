number = int(input("Enter a number: \n"))
if number < 0:
    print("Factorial is not possible!")
else:
    fact = 1
    for i in range(1, number+1): #(range starts from 0 so assigned 1,
        fact = fact * i              # number-1 in range so added 1)

    print("Factorial of number is>>>>>", fact)

