import modul_matrix
from modul_matrix import rearrangement_of_row
# матриця для перевірки:
#[1, 2, 3],
#[2, -1, 2],
#[1, 1, 5]

#і ще матриця
#[2, 3, 0, 5],
#[4, -3, -1, 1],
#[2, 5, 1, 3],
#[2, 7, 2, -2]

def max_row_swap(m, col):
    max_el = m[col][col]
    max_row = col
    for i in range(col + 1, len(m)):
        if abs(m[i][col]) > abs(max_el):
            max_el = m[i][col]
            max_row = i
    if max_row != col:
        m = rearrangement_of_row(m, col + 1, max_row + 1)
    return m


def solve_gauss(m):
    n = len(m)              # лише прямий хід Гауса
    for k in range(n - 1):      # знайшла пояснення методу Гауса на форумі, по ньому робила
        max_row_swap(m, k)
        for i in range(k + 1, n):
            div = m[i][k] / m[k][k]
            m[i][-1] -= div * m[k][-1]
            for j in range(k, n):
                m[i][j] -= div * m[k][j]

    for l in range(n):
        if m[l][l] != 1:
            m[l] = modul_matrix.divide_row_by_scalar(m[l], m[l][l])
    return m


def rank_matrix(m):     # ранг матриці
    n = len(m)
    points = 0
    for j in range(n):
        if m[j][j] == 1:
            points += 1
    return points


def determinant(m):    # обчислюю визначник методом Крамера
    det = 0         # використовую тут метод рекурсії
    n = len(m)
    if n == 1:
        return m[0][0]
    elif n == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    else:
        for k in range(n):
            element = m[0][k]
            sign = (-1) ** k
            submatrix = [row[:k] + row[k + 1:] for row in m[1:]]
            submatrix_det = determinant(submatrix)
            det += element * sign * submatrix_det
    return det


dim = int(input('Введіть розмірність матриці: '))
matrix = modul_matrix.input_matrix(dim)

determinant_result = determinant(matrix)

print('Початкова матриця:')
modul_matrix.output_matrix(matrix)

result = solve_gauss(matrix)

print('Матриця після застосування методу Гауса:')
modul_matrix.output_matrix(result)

rank = rank_matrix(matrix)
print('Ранг матриці:', rank)

print('Визначник матриці:', determinant_result)
# довелось викликати функцію для обрахунку детермінанту першою, бо інакше потім в функцію з детермінантом
# відправляється вже матриця, яка обрахована за методом гауса