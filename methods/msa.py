from lib.main_lib import *


def MSA(A, F, X, eps=None, max_itera=-1):
    A_T = transpose(A)
    A_star = mult_matrix(A_T, A)
    F_star = mult_matrix(A_T, F)

    mu = norm_I(A_star)

    B = diff_matrix(E_matrix(get_shape(A_star)[0]), mult_const_matrix(A_star, 2 / mu))
    G = mult_const_matrix(F_star, 2 / mu)

    R_vector = diff_matrix(F, mult_matrix(A, X))
    R = norm_vector_I(R_vector)

    i = 0

    while eps is None or R > eps:

        if i > max_itera and max_itera > 0:
            break

        X = sum_matrix(mult_matrix(B, X), G)

        R_vector = diff_matrix(F, mult_matrix(A, X))
        R = norm_vector_I(R_vector)

        i += 1

    return X, i, R, R_vector
