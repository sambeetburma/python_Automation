square = [1,2,3]
l1 = square
l2 = square.copy()

square.append(44)

print('original:', square,'reference:', l1 ,'copied', l2 )
print(id(square))
print(id(l1))
print(id(l2))