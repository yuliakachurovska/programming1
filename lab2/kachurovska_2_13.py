a, b, c = [int(d) for d in input().split()]   
if a == b and b == c:
    print("1")
elif a == b and b != c and a != c:
    print("2")
elif a == c and a != b and b != c:
    print("2")
elif b == c and a != b and a != c:
    print("2")
elif a != b and b != c:
    print("3")