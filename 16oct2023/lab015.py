a = 10
b = 20
c = 23

max_is = None

if a > b and a > c:
    max_is = a
elif b > a and b > c:
    max_is = b
else:
    max_is = c

print("maximum value: ", max_is)
