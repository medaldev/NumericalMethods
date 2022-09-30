import matplotlib.pyplot as plt
from methods.msa import MSA


def plot_result(A, F, X, fr, to, step):
    iterations = [i for i in range(fr, to, step)]
    rs = [MSA(A, F, X, max_itera=i)[2] for i in iterations]
    print("calculated")
    plt.figure(figsize=(10, 8))
    plt.plot(iterations, rs)
    plt.xlabel("Количество итераций")
    plt.ylabel("R")
    plt.title("Cкорость сходимости метода в зависимости от числа итерации")
    plt.show()
