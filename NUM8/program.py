import numpy as np
import matplotlib.pyplot as plt


def main(f_1,f_2,f_3,true_a):
    phi_1, title_1 = f_1
    phi_2, title_2 = f_2
    phi_3, title_3 = f_3
    # Generowanie siatki punktów
    n = 20  # Liczba punktów pomiarowych
    sigma = 4  # Odchylenie standardowe zaburzeń
    x = np.linspace(0, 2, n)

    # Prawdziwe współczynniki


    # Generowanie danych pomiarowych
    F_true = true_a[0] * phi_1(x) + true_a[1] * phi_2(x) + true_a[2] * phi_3(x)
    delta_y = np.random.normal(0, sigma, size=n)
    y = F_true + delta_y

    # Aproksymacja metodą najmniejszych kwadratów za pomocą SVD
    A = np.vstack([phi_1(x), phi_2(x), phi_3(x)]).T
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    S_inv = np.diag(1 / S)
    estimated_a = Vt.T @ S_inv @ U.T @ y

    # Obliczenie funkcji aproksymowanej
    F_approx = estimated_a[0] * phi_1(x) + estimated_a[1] * phi_2(x) + estimated_a[2] * phi_3(x)

    # Wizualizacja wyników
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, label="Dane pomiarowe", color="blue")
    plt.plot(x, F_true, label="Prawdziwa funkcja", color="green")
    plt.plot(x, F_approx, label="Aproksymowana funkcja", color="red", linestyle="--")
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Aproksymacja metodą najmniejszych kwadratów f(x) = "+ title_1 + title_2 + title_3)
    plt.grid()
    plt.show()

    # Analiza różnicy współczynników
    for i, (true, est) in enumerate(zip(true_a, estimated_a), 1):
        print(f"Współczynnik a_{i}: Prawdziwy = {true}, Estymowany = {est:.8f}, Różnica = {true - est:.8f}")

if __name__ == "__main__":

    a_1 = [3, 2, 3]
    test_functions_1 = [
        (lambda x: np.sin(2 * x), ' 3sin(2x) '),
        (lambda x: x**3, '+ 2$x^3$'),
        (lambda x: np.exp(x), '+ 3$e^x$'),
    ]
    a_2 = [-3, 3, -2]
    test_functions_2 = [
        (lambda x: np.tan(7 * x), ' -3tan(7x) '),
        (lambda x: np.arctan(-7 * x), '+ 3arctan(-7x)'),
        (lambda x: np.cos(x), ' -2$cos(x)$'),
    ]
    a_3 = [5, 0.2, -2]
    test_functions_3 = [
        (lambda x: np.cos(-4 * x), ' 5cos(-4x) '),
        (lambda x: x, '+ 0.2$x$'),
        (lambda x: np.sin(x), ' -2$sin(x)$'),
    ]
    functions = [test_functions_1,test_functions_2,test_functions_3]
    a = [a_1,a_2,a_3]

    for i in range(len(functions)):
        main(functions[i][0],functions[i][1],functions[i][2],a[i])