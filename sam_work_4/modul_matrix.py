def input_matrix(dim):        # ввід матриці
    matrix = []
    for i in range(dim):
        row = []
        for k in range(dim):
            element = int(input('Введіть елемент матриці: '))
            row.append(element)
        matrix.append(row)
    return matrix


def output_matrix(matrix):        # вивід матриці
    for l in matrix:
        print(*l)


def multiply_matrices(mat1, mat2):      # множення матриць
    result = []

    if len(mat1[0]) != len(mat2):
        raise ValueError("Неможливо виконати множення матриць")

    for i in range(len(mat1)):
        result.append([0] * len(mat2[0]))

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result


def multiplication_by_vector(mat, vector):      # множення матриці на вектор
    result1 = []

    if len(mat[0]) != len(vector):
        print("Неможливо виконати множення матриці на вектор")
        return result1

    for i in range(len(mat)):
        element = 0
        for j in range(len(vector)):
            element += mat[i][j] * vector[j]
        result1.append(element)
    return result1

def divide_row_by_scalar(row, scalar):      # додала ще ділення матриці на скаляр
    return [element / scalar for element in row]


def multiplication_vector_by_matrix(vector, mat):       # множення вектора на матрицю
    result = []

    if len(mat[0]) != len(vector):
        raise ValueError(
            "Неможливо виконати множення вектора на матрицю: кількість стовпців матриці не дорівнює кількості елементів у векторі")
    for i in range(len(mat)):
        element = 0
        for j in range(len(vector)):
            element += vector[j] * mat[i][j]
        result.append(element)
    return result


def rearrangement_of_row(matrix, row1, row2):       # перестановка рядків
    row1 -= 1
    row2 -= 1
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
    return matrix


def rearrangement_of_col(matrix, col1, col2):       # перестановка стовпців
    col1 -= 1
    col2 -= 1
    for i in range(len(matrix)):
        matrix[i][col1], matrix[i][col2] = matrix[i][col2], matrix[i][col1]
    return matrix


def getting_row(matrix, num_row):       # отримання певного рядка матриці
    num_row -= 1
    return matrix[num_row]


def multiplicate_vector_by_numb(vector, number):        # множення вектора на число
    new_vector = []
    for i in range(len(vector)):
        new_vector.append(vector[i] * number)
    return new_vector


def subtracting_vector_from_matrix(matrix, vector):     # віднімання вектора від всіх рядків матриці
    result_matrix = []
    for i in range(len(matrix)):
        result_row = []
        for j in range(len(matrix[0])):
            result_row.append(matrix[i][j] - vector[j])
        result_matrix.append(result_row)
    return result_matrix

