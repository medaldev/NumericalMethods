from lib.main_lib import *
from methods.seidel import seidel

A = [[1, 2, 3, 4],
    [0, 1, 2, 3],
    [0, 0, 1, 2],
    [0, 0, 0, 1]]

F = [[10],
     [6],
     [3],
     [1]]

X = create_random_vector(4, interval=(1, 5))

Eps = 1e-6
res = seidel(A, F, X, eps=Eps, max_itera=1000)

print("Eps =", Eps)
print("Итоговый x: ", res[0])
print("Колличество итераций: ", res[1])
print("max|R_[k]| =", res[2])
print("R", res[3])

Eps = 1e-9
res = seidel(A, F, X, eps=Eps)

print("Eps =", Eps)
print("Итоговый x: ", res[0])
print("Колличество итераций: ", res[1])
print("max|R_[k]| =", res[2])
print("R", res[3])


