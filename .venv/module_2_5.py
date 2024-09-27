def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
                matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input('Колличество строк матрицы: '))
m = int(input('Колличество столбцов матрицы: '))
value = int(input('Значение матрицы: '))
matrix = get_matrix(n, m, value)