list_number = [1, 2, 3, 4, 5]

square = lambda x: x * x
list_square = []

for i in list_number:
    list_square.append(square(i))

print("By use of for Loop:", list_square)

new_list_square = list(map(lambda x: x*x, list_number))
print("with map function:", new_list_square)
