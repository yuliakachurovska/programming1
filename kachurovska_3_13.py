n = int(input())
i = 1
factorial = 1
while factorial < n:
    i += 1
    factorial *= i
if factorial == n:
    print(i)
else:
    exit(0)