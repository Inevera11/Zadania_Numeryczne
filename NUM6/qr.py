import numpy as np
import matplotlib.pyplot as plt

# Macierz M
M = np.array([
    [9, 2, 0, 0],
    [2, 4, 1, 0],
    [0, 1, 3, 1],
    [0, 0, 1, 2]
])

# Parametry
epsilon = 1e-10  # Warunek stopu
max_iter = 1000  # Maksymalna liczba iteracji

def qr_algorithm(M, epsilon, max_iter):
    """
    Algorytm QR bez przesunięć do znajdowania wartości własnych.
    
    Parametry:
    - M: macierz wejściowa (kwadratowa)
    - epsilon: tolerancja dla warunku stopu
    - max_iter: maksymalna liczba iteracji
    
    Zwraca:
    - wartości własne (diagonalne elementy macierzy trójkątnej górnej)
    - lista macierzy z kolejnych iteracji
    """
    A = M.copy()
    iterations = []
    off_diagonal_norms = []
    for _ in range(max_iter):
        Q, R = np.linalg.qr(A)
        A = R @ Q
        iterations.append(A.copy())

        # Norma elementów POD diagonalą
        lower_triangle = np.tril(A, k=-1)  # Wybieramy elementy poniżej diagonalnej
        off_diagonal_norm = np.linalg.norm(lower_triangle)
        off_diagonal_norms.append(off_diagonal_norm)

        # Sprawdzenie warunku stopu
        if off_diagonal_norm < epsilon:
            break

    return np.diag(A), iterations, off_diagonal_norms

def plot_diagonal_convergence(iterations):
    """
    Wykres ewolucji elementów diagonalnych w kolejnych iteracjach.
    """
    diag_elements = np.array([np.diag(A) for A in iterations])
    for i in range(diag_elements.shape[1]):
        plt.plot(diag_elements[:, i], label=f"λ_{i+1}")
    plt.xlabel("Iteracja")
    plt.ylabel("Elementy diagonalne")
    plt.title("Ewolucja elementów diagonalnych")
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_off_diagonal_norms(off_diagonal_norms):
    """
    Wykres normy elementów pod diagonalą w kolejnych iteracjach.
    """
    plt.plot(off_diagonal_norms, linestyle='dashed')
    plt.xlabel("Iteracja")
    plt.ylabel("Norma elementów poniżej diagonali")
    plt.title("Zbieżność macierzy do postaci trójkątnej górnej")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Uruchomienie algorytmu QR
    eigenvalues, iterations, off_diagonal_norms = qr_algorithm(M, epsilon, max_iter)

    print("A_50: ", iterations[49])
    
    # Wyświetlenie wyników
    print("Wartości własne macierzy M:",eigenvalues)
    
    # Wykres zbieżności wartości własnych
    plot_diagonal_convergence(iterations)
    
    # Wykres zbieżności normy poza diagonalą
    plot_off_diagonal_norms(off_diagonal_norms)
