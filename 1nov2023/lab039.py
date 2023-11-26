numList = [2,-6,91,10.5,34,-45,10]
def num_greater_10(num):
    return num > 10

list_of_numbers_greater_10 = list(filter(num_greater_10,numList))
print(list_of_numbers_greater_10)

#replace above with lambda
list_of_numbers_greater_10 = list(filter(lambda num: num > 10, numList ))
print(list_of_numbers_greater_10)
