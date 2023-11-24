n = int(input())
lst_1 = [float(el) for el in input().split()]
sum = 0
count = 0
for i in range(len(lst_1)):
    if lst_1[i] > 0:
        sum += lst_1[i]
        count += 1
if count == 0:
    print("Not Found")
else:
    print(format(sum / count, ".2f"))
