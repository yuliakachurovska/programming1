s = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    s = s.replace(letter, letter * 2)
print(s)