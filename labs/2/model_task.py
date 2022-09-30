from lib.main_lib import *
from methods.msa import MSA

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
res = MSA(A, F, X, eps=Eps)

print("Eps =", Eps)
print("Итоговый x: ", res[0])
print("Колличество итераций: ", res[1])
print("max|R_[k]| =", res[2])
print("||x-x*|| =", norm_vector_I(diff_matrix(X, [[1], [1], [1], [1]])))
print("R", res[3])

Eps = 1e-9
res = MSA(A, F, X, eps=Eps)

print("Eps =", Eps)
print("Итоговый x: ", res[0])
print("Колличество итераций: ", res[1])
print("max|R_[k]| =", res[2])
print("||x-x*|| =", norm_vector_I(diff_matrix(X, [[1], [1], [1], [1]])))
print("R", res[3])


plot_result(A, F, X, fr=10, to=10000, step=50)
