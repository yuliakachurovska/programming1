string = input()
k = int(input())
word = []
string_low = string.lower()
for letter in string_low:
    if ord(letter) - k < 97:
        print((chr(ord(letter) - k + 26).upper()), end="")
    else:
        print((chr(ord(letter) - k).upper()), end="")