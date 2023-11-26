original_list = [1, 2, 3, 4]
copy_list = original_list.copy()
print(copy_list) #result [1, 2, 3, 4]
copy_list.append(5)
print(copy_list) #result [1, 2, 3, 4,5]
print(original_list)#result [1, 2, 3, 4]