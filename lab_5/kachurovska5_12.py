n = int(input())
lst_1 = [int(el) for el in input().split()]
lst_2 = []
for i in range(len(lst_1)):
    el = lst_1[i]
    if el not in lst_2:
        lst_2.append(el)
print(*lst_2)