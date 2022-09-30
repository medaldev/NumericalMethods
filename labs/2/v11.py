from lib.main_lib import *
from methods.msa import MSA

A = [[1.26, 1.15, 2.46, 28.15],
    [-0.43, -15.13, 1.24, 17.43],
    [23.16, -1.12, 1.15, -10.16],
    [0.13, 21.22, 1.46, 7.15]]

F = [[1.16],
     [-2.51],
     [1.17],
     [8.46]]

X = create_random_vector(4, interval=(1, 5))

Eps = 1e-6
res = MSA(A, F, X, eps=Eps)

print("Eps =", Eps)
print("Итоговый x: ", res[0])
print("Колличество итераций: ", res[1])
print("max|R_[k]| =", res[2])
print("R", res[3])

Eps = 1e-9
res = MSA(A, F, X, eps=Eps)

print("Eps =", Eps)
print("Итоговый x: ", res[0])
print("Колличество итераций: ", res[1])
print("max|R_[k]| =", res[2])
print("R", res[3])


plot_result(A, F, X, fr=10, to=10000, step=50)