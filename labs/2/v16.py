from lib.main_lib import *
from methods.msa import MSA

A = [[1.67, 7.43, -2.31, 0.99],
    [1.01, -2.34, -7.45, 0.35],
    [2.34, 11.21, 7.15, 6.34],
    [4.39, 17.56, 3.21, 11.28]]

F = [[0.01],
     [11.57],
     [0.34],
     [12.63]]


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