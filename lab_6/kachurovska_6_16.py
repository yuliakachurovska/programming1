s = input()
word_3_7_11 = s[2: 11: 4]
word_1_2_last = s[0:1] + s[-2:]
word_1_7 = s[:7]
word_without_first_4 = s[4:]
word_with_odd_indices = ""
for i in range(1, len(s), 2):
    word_with_odd_indices += s[i]
word_with_odd_indices_length = len(word_with_odd_indices)
reversed_s = s[::-1]

print(word_3_7_11)
print(word_1_2_last)
print(word_1_7)
print(word_without_first_4)
print(word_with_odd_indices)
print(word_with_odd_indices_length)
print(reversed_s)