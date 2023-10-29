string = input()
word = []
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    if letter not in string:
        pass
    else:
        word.extend([letter] * string.count(letter))
print("".join(map(str, word)))