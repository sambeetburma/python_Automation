original_dict = {'name': 'abc', 'age': '27', 'place': 'india'}
copy_dict = original_dict.copy()
print(copy_dict) # same as original
copy_dict.pop('age')
print(copy_dict)#{'name': 'abc', 'place': 'india'}
