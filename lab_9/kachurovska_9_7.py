n = int(input())
cubes = input()
cube_list = str(cubes)
d = {}
for letter in cube_list:
    if letter not in d:
        d[letter] = cube_list.count(letter)
c = 0
for key, value in d.items():
    if value % 2 != 0:
        c += 1
        print(key)
if c == 0:
    print("Ok")