n = int(input())
suma = 0
while n != 0:
    if n % 2 == 0:
        suma += n
        n = int(input())
    else:
        n = int(input())
print(suma)
