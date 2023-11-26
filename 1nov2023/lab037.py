words = ["apple", "banana", "pomogranate", "dates", "mango"]
min_len = 6

def check_len(word):
    return len(word) > min_len
#implement lambda


max1 = list(filter(lambda word: len(word) > min_len, words))
print(max1)

max2 = list(filter(check_len, words))
print(max2)
