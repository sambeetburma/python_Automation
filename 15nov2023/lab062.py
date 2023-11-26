try:
    num1 = int(input("enter your 1st number:"))
    num2 = int(input("enter your 2nd number:"))
    result = num1 / num2
except ValueError:
    print("invalid number")
except ZeroDivisionError:
    print(("You are dividing by zero"))

except Exception as e:
    print("handle all exception")

else:
    print(f"Result is {result}")#if no error this block executes

finally:
    print("If error then please reenter correct value or else ignore this msg")
