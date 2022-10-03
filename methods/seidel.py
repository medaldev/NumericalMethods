from lib.main_lib import *


def seidel(A, F, X, eps=None, max_itera=-1):
    A_T = transpose(A)
    A_star = mult_matrix(A_T, A)
    F_star = mult_matrix(A_T, F)

    mu = norm_I(A_star)

    B = diff_matrix(E_matrix(get_shape(A_star)[0]), mult_const_matrix(A_star, 2 / mu))
    G = mult_const_matrix(F_star, 2 / mu)

    M = left_low_triangle(B)
    N = right_top_triangle(B)

    E_M_inv = inv_matrix(diff_matrix(E_matrix(get_shape(M)[0]), M))

    print_matrix(M)
    print_matrix(N)
    print_matrix(E_M_inv)

    exit()

    R_vector = diff_matrix(F, mult_matrix(A, X))
    R = norm_vector_I(R_vector)

    i = 0

    while eps is None or R > eps:

        if i > max_itera and max_itera > 0:
            break

        X = sum_matrix(mult_matrix(mult_matrix(E_M_inv, N), X), mult_matrix(E_M_inv, G))

        R_vector = diff_matrix(F, mult_matrix(A, X))
        R = norm_vector_I(R_vector)

        i += 1

    return X, i, R, R_vector
