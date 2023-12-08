def quadratic_equation(a, b, c):
    assert a != 0, "Коефіцієнт 'a' не може дорівнювати 0!"

    D = b ** 2 - 4 * a * c
    assert D >= 0, "Рівняння не має розв'язків на множині дійсних чисел"

    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)

    return x1, x2


a, b, c = [int(el) for el in input("Введіть коефіцієнти квадратного рівння a, b, c: ").split()]
result = quadratic_equation(a, b, c)
print("Розв'язки р-ня:", result)
