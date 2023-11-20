n = int(input())
positive_digit = [abs(int(el)) for el in input().split()]
sort_positive_digit = set(positive_digit)
print(len(sort_positive_digit))