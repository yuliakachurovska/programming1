def count_ones_in_range(a, b):
    total_ones = 0
    for i in range(a, b + 1):
        binary_repres = bin(i)[2:]  # Перетворення у бінарне представлення
        ones_count = binary_repres.count('1')  # Підрахунок одиниць
        total_ones += ones_count

    return total_ones

a, b = [int(i) for i in input().split()]
result = count_ones_in_range(a, b)
print(result)
