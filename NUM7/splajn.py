import numpy as np
import matplotlib.pyplot as plt

def generate_points(n):
    """Generuje jednolitą siatkę punktów."""
    return np.array([-1 + 2 * i / n for i in range(n + 1)])

def cholesky_decomposition(n):
    """Faktoryzacja Cholesky'ego potrzebna do interpolacji splajnami."""
    n = n - 1
    C = []
    C.append([0] * n)
    C.append([0] * n)

    for i in range(n):
        if i == 0:
            C[1][i] = 2
        else:
            C[0][i] = 1 / C[1][i - 1]
            C[1][i] = np.sqrt(4 - C[0][i - 1] ** 2)

    return C

def cubic_spline_interpolation(n, x_plot,fun):
    """Interpolacja metodą splajnów kubicznych."""
    x = generate_points(n)
    y = fun(x)
    h = 2 / n
    E = [0] * (n + 1)
    C = cholesky_decomposition(n)

    # Podstawianie w przód
    c = 6 / (h**2)
    E[1] = c * (y[0] - 2 * y[1] + y[2]) / C[1][0]
    for i in range(2, n):
        E[i] = (c * (y[i - 1] - 2 * y[i] + y[i + 1]) - C[0][i - 1] * E[i - 1]) / C[1][i - 1]

    # Podstawianie w tył
    E[n - 1] = E[n - 1] / C[1][n - 2]
    for i in range(n - 2, 0, -1):
        E[i] = (E[i] - C[0][i] * E[i + 1]) / C[1][i - 1]

    y_new = []
    for a in x_plot:
        a = round(a, 14)
        for i in range(n):
            if x[i] <= a <= x[i + 1]:
                s = (
                    E[i] * ((x[i + 1] - a) ** 3) / (6 * h)
                    + E[i + 1] * ((a - x[i]) ** 3) / (6 * h)
                    + (a - x[i]) * ((y[i + 1] - y[i]) / h - h * (E[i + 1] - E[i]) / 6)
                    + y[i]
                    - (E[i] * (h**2)) / 6
                )
                y_new.append(s)
                break

    return y_new

def plot_interpolation(x_plot, n_values, test_functions):
    """Wykres interpolacji dla różnych ilości węzłów i funkcji."""
    for func, label in test_functions:
        plt.figure(figsize=(8, 8))
        plt.title(f'Interpolacja splajnami kubicznymi\n{label}')
        plt.plot(x_plot, func(x_plot), 'r', label='Oryginalna funkcja')
        for n, color in zip(n_values, ['g', 'b', 'orange']):
            plt.plot(x_plot, cubic_spline_interpolation(n, x_plot,func), color, label=f'$S_{{{n}}}(x)$')
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        plt.legend()
        plt.grid()
        plt.show()

def plot_error(x_plot, n_values, test_functions):
    """Wykres błędu interpolacji dla różnych funkcji na jednym wykresie."""
    for func, label in test_functions:
        plt.figure(figsize=(8, 6))
        plt.title(f'Błąd interpolacji splajnami kubicznymi\n{label}')
        for n, color in zip(n_values, ['g', 'b', 'orange']):
            x_nodes = generate_points(n)
            y_exact = func(x_plot)
            y_interp = cubic_spline_interpolation(n, x_plot, func)
            error = abs(y_exact - y_interp)
            plt.plot(x_plot, error, color, label=f'$n = {n}$')
            plt.scatter(x_nodes, [0] * len(x_nodes), color=color, s=10, marker='o')  # Węzły interpolacji
        plt.xlabel('$x$')
        plt.ylabel('Błąd $|f(x) - S(x)|$')
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    x_plot = np.linspace(-1, 1, 1000)
    n_values = [5, 10, 15]  # Różne ilości węzłów
    test_functions = [
        (lambda x: 1 / (1 + 10 * x**2), r'$f(x) = \frac{1}{1 + 10x^2}$'),
        (lambda x: np.abs(x), r'$f(x) = |x|$')
    ]
    plot_interpolation(x_plot, n_values, test_functions)
    plot_error(x_plot, n_values, test_functions)
