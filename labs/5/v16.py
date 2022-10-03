import sys

sys.path.append("C:\\Users\\sanch\\Desktop\\Лаба\\NumericalMethods")

from lib.main_lib import *
from methods.newton import newton
from math import tan, cos


def f(x, y):
    return [[(y / (cos(x * y - 0.2) ** 2)) - 2 * x, x / (cos(x * y - 0.2) ** 2)], [2 * x, 1.8 * y]]


def F(x, y):
    return [[tan(x * y - 0.2) - x ** 2], [x ** 2 + 0.9*y ** 2 - 1]]


x0 = [[1.03], [0.25]]

for method_type, method_name in zip([False, True], ["Стандартный", "Упрощённый"]):

    print(f"Тип метода Ньютона: " + method_name.upper(), end="\n\n")

    for require_eps in [1e-6, 1e-10]:

        print(f"Зададим точность eps = {require_eps}")
        print("-" * 30)

        x_final, eps_final, itera_final, eps_array,res_f = newton(x0=x0, f=f, F=F, eps=require_eps, max_iter=50000,
                                                            simple=method_type)
        print("Итоговый вектор", x_final)
        print("Итоговая точность", eps_final)
        print("Итоговое кол-во итераций", itera_final)
        print("Результат подстановки x", res_f)
        print("Норма", norm_vector_I(res_f))

        print("\n")

