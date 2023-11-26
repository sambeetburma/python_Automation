import copy
original_dict = {'a': 1, 'b': [2, 3]}
copied_dict = copy.deepcopy(original_dict)

copied_dict['b'][0] = 99 # This change will not affect the original dictionary.

print(copied_dict)
print(original_dict)

