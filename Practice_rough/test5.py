original_str = "naman"
lambda_ref = lambda strr: strr[::-1]

reverse_str = lambda_ref(original_str)

print('original string : ', original_str)
print('reverse string : ', reverse_str)

if original_str == reverse_str:
    print("it's pallindrum")
else:
    print("it's not a pallindrum")
