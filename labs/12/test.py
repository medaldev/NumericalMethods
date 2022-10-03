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
    h = (b - a) / n
    xs = arange(a, b, h)
    result = 0

    result += func(xs[0]) + func(xs[n])

    for i in range(1, n, 2):
        result += 4 * (func(xs[i]))

    for i in range(2, n - 1, 2):
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



