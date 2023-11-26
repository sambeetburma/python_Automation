#pallindrum slicing mechanism

def is_pallindrum(original_str):
    rev_str = original_str[::-1]
    print(rev_str)
    if original_str == rev_str:
        print("It's pallindrum")
    else:
        print("It's not")

is_pallindrum("haha")

