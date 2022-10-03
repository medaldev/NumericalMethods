from random import randint


# -----------------------------------------------------------------------------
# Матричные функции
# -----------------------------------------------------------------------------

def E_matrix(m):
    return [[1 if i == j else 0 for j in range(m)] for i in range(m)]


def create_zero_matrix(m, n):
    return create_matrix(m, n, iter([0 for _ in range(m * n)]))


def create_random_matrix(m, n, interval):
    a, b = interval
    return create_matrix(m, n, iter([randint(a, b) for _ in range(m * n)]))


def create_matrix(m, n, data):
    return [[next(data) for j in range(n)] for i in range(m)]


def create_random_vector(m, interval):
    return create_random_matrix(m, 1, interval)


def print_matrix(matrix):
    print(*matrix, sep="\n", end="\n\n")


def mult_matrix(M1, M2):
    (m1, n1), (m2, n2) = get_shape(M1), get_shape(M2)
    assert n1 == m2
    M3 = create_zero_matrix(m1, n2)
    for i in range(m1):
        for j in range(n2):
            for k in range(n1):
                M3[i][j] += M1[i][k] * M2[k][j]
    return M3


def mult_const_matrix(M1, a):
    (m1, n1) = get_shape(M1)
    M2 = create_zero_matrix(m1, n1)
    for i in range(m1):
        for j in range(n1):
            M2[i][j] = M1[i][j] * a
    return M2


def sum_matrix(M1, M2):
    (m1, n1), (m2, n2) = get_shape(M1), get_shape(M2)
    assert m1 == m2 and n1 == n2
    M3 = create_zero_matrix(m1, n1)
    for i in range(m1):
        for j in range(n1):
            M3[i][j] = M1[i][j] + M2[i][j]
    return M3


def diff_matrix(M1, M2):
    (m1, n1), (m2, n2) = get_shape(M1), get_shape(M2)
    assert m1 == m2 and n1 == n2
    M3 = create_zero_matrix(m1, n1)
    for i in range(m1):
        for j in range(n1):
            M3[i][j] = M1[i][j] - M2[i][j]
    return M3


def get_shape(M1):
    if not len(M1): return (0, 0)
    return (len(M1), len(M1[0]))


def transpose(M1):
    (m1, n1) = get_shape(M1)
    M2 = create_zero_matrix(n1, m1)
    for i in range(n1):
        for j in range(m1):
            M2[i][j] = M1[j][i]
    return M2


# -----------------------------------------------------------------------------
# Нормы над матрицами
# -----------------------------------------------------------------------------

def norm_III(M1):
    res = 0
    (m1, n1) = get_shape(M1)
    for i in range(m1):
        for j in range(n1):
            res += M1[i][j] ** 2
    return res


def norm_II(M1):
    res = 0
    (m1, n1) = get_shape(M1)
    for i in range(m1):
        for j in range(n1):
            res += abs(M1[i][j])

    return res


def norm_I(M1):
    res = 0
    (m1, n1) = get_shape(M1)
    for i in range(m1):
        for j in range(n1):
            res += M1[i][j] ** 2
    res = res ** 0.5
    return res


# -----------------------------------------------------------------------------
# Нормы над векторами
# -----------------------------------------------------------------------------

def norm_vector_I(V):
    return max([abs(V[i][0]) for i in range(len(V))])


def norm_vector_II(V):
    return sum([abs(V[i][0]) for i in range(len(V))])


def norm_vector_III(V):
    return sum([(V[i][0]) ** 2 for i in range(len(V))]) ** 0.5


# Lb 5


def copy_matrix(M1):
    (m1, n1) = get_shape(M1)
    M2 = create_zero_matrix(m1, n1)
    for i in range(m1):
        for j in range(n1):
            M2[i][j] = M1[i][j]
    return M2


def union_matrix(M1):
    (m1, n1) = get_shape(M1)
    M2 = create_zero_matrix(n1, m1)
    for i in range(n1):
        for j in range(m1):
            M2[i][j] = algebraic_addition(M1, j, i)
    return M2


def inv_matrix(M1):
    M_det = det(M1)
    if M_det == 0:
        raise Exception("Для построения обратной матрицы детерминант должен быть отличен от нуля")
    return mult_const_matrix(M1=union_matrix(M1), a=1 / M_det)


def algebraic_addition(M1, i, j):
    (m1, n1) = get_shape(M1)
    sign = (-1) ** (i + j + 2)
    res = sign * det([row[:j] + row[j + 1:] for ir, row in enumerate(M1) if ir != i])
    return res


def det(M1):
    res = 0
    (m1, n1) = get_shape(M1)

    assert m1 == n1

    if m1 == n1 == 1:
        return M1[0][0]

    if m1 == n1 == 2:
        return M1[0][0] * M1[1][1] - M1[0][1] * M1[1][0]

    M2 = M1[1:]
    for i in range(n1):
        # sign = (-1) ** (i + 2)

        # res += M1[0][i] * sign * det([row[:i] + row[i+1:] for row in M2])
        res += M1[0][i] * algebraic_addition(M1, 0, i)

    return res

def left_low_triangle(M1):
    (m1, n1) = get_shape(M1)
    M2 = create_zero_matrix(n1, m1)
    for i in range(n1):
        for j in range(m1):
            M2[i][j] = M1[i][j] if j < i else 0
    return M2

def right_top_triangle(M1):
    (m1, n1) = get_shape(M1)
    M2 = create_zero_matrix(n1, m1)
    for i in range(n1):
        for j in range(m1):
            M2[i][j] = M1[i][j] if j >= i else 0
    return M2