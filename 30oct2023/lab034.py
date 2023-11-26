my_dict = {"name": "sambeet", "age": '37', 'weight': '79', 'ismale': True}
my_keys = my_dict.keys()
my_values = my_dict.values()
print("show me all keys", my_keys, "\nshow me all values", my_values)
print(type(my_keys))
my_keys = list(my_keys)
print(type(my_keys))
print(my_keys)
print(my_keys[0])

copy_my_dict = my_dict
print('copied dict : ', copy_my_dict)
print('my dict :', my_dict)
copy_my_dict.pop('ismale')
print('my copied : ', copy_my_dict)
print("my dict : ", my_dict)
