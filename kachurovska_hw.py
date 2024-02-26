import math
class Triangle:
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            print("Такого трикутника не існує")
            self.a = self.b = self.c = 0
        else:
            self.a = a
            self.b = b
            self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            print("Ширина та висота повинні бути додатні числа.")
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

class Trapeze:
    def __init__(self, base1, base2, side1, side2):
        if base1 == base2:
            print("Така фігура не є трапецією, оскільки обидві основи мають однакову довжину.")
        elif side1 <= 0 or side2 <= 0:
            print("Така фігура не є трапецією, оскільки одна або обидві бічні сторони мають неправильну довжину.")
        elif abs(base1 - base2) >= side1 + side2:
            print("Така фігура не є трапецією, оскільки різниця між основами більша або рівна сумі бічних сторін.")
        self.base1 = base1
        self.base2 = base2
        self.side1 = side1
        self.side2 = side2

    def perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2

    def height(self):
        if self.base1 != self.base2:  # Перевірка, чи бази трапеції не є однаковими
            return math.sqrt(self.side1 ** 2 - ((self.base2 - self.base1) / 2) ** 2)
        else:
            return 0

    def area(self):
        return ((self.base1 + self.base2) * self.height()) / 2

class Parallelogram:
    def __init__(self, a, b, h) -> None:
        self.a = a
        self.b = b
        self.ha = h

    def perimeter(self):
        return self.a * 2 + self.b * 2

    def area(self):
        return self.a * self.ha

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)


max_area = 0
max_perimeter = 0
max_area_figure = None
max_perimeter_figure = None
figures = []

with open("input.txt", "r") as file_list:
    for filename in file_list:
        filename = filename.strip()
        with open(filename, "r") as file:
            for line in file:
                try:
                    words = line.split()
                    figure_type = words[0]
                    parameters = [float(x) for x in words[1:]]

                    if figure_type == "Triangle":
                        shapes = Triangle(*parameters)
                    elif figure_type == "Rectangle":
                        shapes = Rectangle(*parameters)
                    elif figure_type == "Trapeze":
                        shapes = Trapeze(*parameters)
                    elif figure_type == "Parallelogram":
                        shapes = Parallelogram(*parameters)
                    elif figure_type == "Circle":
                        shapes = Circle(*parameters)

                    figures.append((figure_type, shapes.area(), shapes.perimeter(), parameters))
                except ValueError:
                    print("Неправильний формат даних у файлі:", filename)


for figure_type, area, perimeter, parameters in figures:
    if area is not None:
        if area > max_area:
            max_area = area
            max_area_figure = (figure_type, parameters)

    if perimeter is not None:
        if perimeter > max_perimeter:
            max_perimeter = perimeter
            max_perimeter_figure = (figure_type, parameters)

print("Фігура з максимальною площею:", max_area_figure)
print("Максимальна площа:", max_area)
print("Фігура з максимальним периметром:", max_perimeter_figure)
print("Максимальний периметр:", max_perimeter)