from lib.main_lib import *


def newton(x0, f, F, eps=None, max_iter=-1, simple=False):
    i = 0

    x = copy_matrix(x0)

    f_inv = inv_matrix(f(*x[0], *x[1]))

    eps_values = []

    while True:

        if not simple:
            f_inv = inv_matrix(f(*x[0], *x[1]))

        x_diff = mult_matrix(f_inv, F(*x[0], *x[1]))
        eps_local = norm_I(x_diff)
        x = diff_matrix(x, x_diff)
        i += 1

        eps_values.append(eps_local)

        if i >= max_iter > 0:
            break
        if eps is not None:
            if eps_local <= eps:
                break

    return x, eps_local, i, eps_values, F(*x[0], *x[1])
