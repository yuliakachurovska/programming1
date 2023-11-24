n = int(input())
lst1 = [int(m) for m in input().split()]
n1 = int(input())
lst2 = [int(k) for k in input().split()]
lst3 =[ ]
for i in lst1:
    if i not in lst2:
        lst3.append(i)
print(len(lst3))
print(" ".join(str(lst3[j]) for j in range(len(lst3))))