'''def is_pallindrum(original_str):
    rev_str = original_str[::-1]
    print(rev_str)
    if original_str == rev_str:
        print("It's pallindrum")
    else:
        print("It's not")

is_pallindrum("haha")'''

#Implement Lambda

original_str = "naman"
reverse_str = lambda original_str: original_str[::-1] #store as object
print('reverser string:', reverse_str)

if original_str == reverse_str("naman"):
    print("it's pallindrum")
else:
    print("it's not a pallindrum")


