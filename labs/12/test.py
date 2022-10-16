from lib.main_lib import *


def arange(a, b, h):
    res = []
    i = a
    while i < b:
        res.append(i)
        i += h
    return res


def trapeze(func, a, b, n):
    h = (b - a) / n
    xs = arange(a, b, h)
    result = 0
    for i in range(len(xs) - 1):
        result += (h / 2) * (func(xs[i]) + func(xs[i + 1]))
    return result


def simpson(func, a, b, n):
    if n % 2 != 0:
        raise Exception("n должно быть чётным в ф-ле Симпсона")
    m = n // 2
    h = (b - a) / (2 * m)
    xs = arange(a, b, h)
    result = 0

    result += func(xs[0]) + func(xs[(2 * m - 1)])

    for i in range(1, (2 * m), 2):
        result += 4 * (func(xs[i]))

    for i in range(2, (2 * m) - 1, 2):
        result += 2 * (func(xs[i]))

    result = (h / 3) * result

    return result


def newton(func, a, b, n):
    if n % 3 != 0:
        raise Exception(f"n должно делиться на 3 ")
    h = (b - a) / n
    xs = arange(a, b, h)
    result = 0

    for i in range(n - 3):
        result += (3 * h / 8) * (func(xs[i]) + 3 * func(xs[i + 1]) + 3 * func(xs[i + 2]) + func(xs[i + 3]))

    return result


def chebishev(func, A, B, m):
    ts = [-0.883862, -0.529657, -0.323912, 0, 0.323912, 0.529657, 0.883862]
    n = len(ts)
    h = (B - A) / m
    xs = arange(A, B, h)

    result = 0

    for j in range(m - 1):

        a, b = xs[j], xs[j + 1]

        for i in range(len(ts)):
            result += func(((b + a) / 2) + ((b - a) / 2) * ts[i])

        result *= ((b - a) / 2)

    return result


from methods.msa import MSA


def gauss(func, A, B, m, eps):
    ts = [-0.883862, -0.529657, -0.323912, 0, 0.323912, 0.529657, 0.883862]
    n = len(ts)
    h = (B - A) / m
    xs = arange(A, B, h)

    t_left = [[ts[j] ** i for j in range(n)] for i in range(0, n)]
    t_right = [(2 / (k + 1)) if k % 2 == 0 else 0 for k in range(0, n)]

    A_coefs = MSA(A=t_left, F=list_to_vector(t_right), X=create_random_vector(n, (1, 5)), eps=eps, max_itera=10000)[0]

    result = 0

    for j in range(m - 1):

        a, b = xs[j], xs[j + 1]

        for i in range(n):
            result += A_coefs[i][0] * func(((b + a) / 2) + ((b - a) / 2) * ts[i])

        result *= ((b - a) / 2)

    return result


def list_to_vector(lst):
    return [[el] for el in lst]


ifunc = lambda x: x * 2

fr = 1
to = 4

segments = 18

print(trapeze(ifunc, fr, to, segments))
print(simpson(ifunc, fr, to, segments))
print(newton(ifunc, fr, to, segments))
print(chebishev(ifunc, fr, to, segments))
print(gauss(ifunc, fr, to, segments, 1e-3))
