n, k = [int(m) for m in input().split()]
array = [int(el) for el in input().split()]

i = len(array) - 1
while i > 0:
    for j in range(0, i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
    i -= 1
print(array[k - 1])