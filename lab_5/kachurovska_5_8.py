n = int(input())
lst1 = [int(el) for el in input().split()]
max_el = float("inf")
min_el = 0
for i in range(len(lst1)):
    if lst1[i] < max_el:
        max_el = lst1[i]
for el in range(len(lst1)):
    if lst1[el] == max_el:
        min_el = lst1[el]
print(min_el)
