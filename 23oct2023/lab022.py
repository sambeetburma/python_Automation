#pallindrom
def reverse_string(input_string):
    reverse_str = ""
    for char in input_string:
        reverse_str = char + reverse_str
    return reverse_str  


original_str = "MADAM"
rev_str = reverse_string(original_str)
print(rev_str)

if original_str == rev_str:
    print("It's pallendrom")
else:
    print("Not a pallindrom")

