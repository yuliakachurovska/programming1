alphabet = input()
word = input()
sort_alphabet = set(alphabet)
no = 0
for el in word:
    if el not in sort_alphabet:
        no += 1
if no == 0:
    print("Ok")
else:
    print("No")