import math

n = int(input())
factorial = math.factorial(n)
dig_count = int(math.log10(factorial)) + 1

print(dig_count)