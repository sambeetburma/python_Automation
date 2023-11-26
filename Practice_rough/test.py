original_list = [1, [2, 3]]
copied_list = original_list.copy()

copied_list[1][0] = 99 # This change will affect both lists.

print(copied_list)
print(original_list)