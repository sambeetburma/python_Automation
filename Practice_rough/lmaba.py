
list_number = [1, 2, 3, 4, 5]

new_list_square = list(map(lambda x: x*x, list_number))
print("with map function:", new_list_square)

result = lambda a: a**2
print(result(2))