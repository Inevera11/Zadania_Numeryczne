import numpy as np
import matplotlib.pyplot as plt

def generate_points(n, func):
    """Generuje punkty siatki oraz wartości funkcji."""
    x = np.array([-1 + 2 * i / n for i in range(n+1)])  # Jednorodna siatka punktów
    y = func(x)                 # Wartości funkcji w punktach siatki
    return x, y

def lagrange_basis(x, j, x_points):
    """Oblicza funkcję bazową Lagrange'a l_j(x)."""
    l_j = 1
    for i in range(len(x_points)):
        if i != j:
            l_j *= (x - x_points[i]) / (x_points[j] - x_points[i])
    return l_j

def lagrange_interpolation(x, x_points, y_points):
    """Oblicza wartość wielomianu interpolacyjnego w punkcie x."""
    P_x = 0
    for j in range(len(x_points)):
        P_x += y_points[j] * lagrange_basis(x, j, x_points)
    return P_x

def calculate_errors(x_plot, y_exact, y_interpolated):
    """Oblicza błędy interpolacji pomiędzy dokładną funkcją a interpolacją."""
    return y_exact - y_interpolated

def polynomial_comparison(n_values, func, func_label):
    """Porównuje interpolacje wielomianowe Lagrange'a dla różnych n na osobnych wykresach."""
    # Punkty do rysowania interpolacji i obliczania błędów
    x_plot = np.linspace(-1, 1, 1000)
    y_exact = func(x_plot)
    
    # Przygotowanie wykresów
    fig, axes = plt.subplots(2, 1, figsize=(8, 10))
    
    # Wykres interpolacji
    axes[0].plot(x_plot, y_exact, label=f'Oryginalna funkcja {func_label}', linewidth=2)
    for n, color in zip(n_values, ['g', 'b', 'orange']):
        x_points, y_points = generate_points(n, func)
        y_interpolated = [lagrange_interpolation(x, x_points, y_points) for x in x_plot]
        axes[0].plot(x_plot, y_interpolated, '--', label=f'Interpolacja Lagrange\'a n={n}', color=color)
        axes[0].scatter(x_points, y_points, color=color, s=20, zorder=5, label=f'Węzły n={n}')
    
    axes[0].set_xlabel('$x$')
    axes[0].set_ylabel('$y$')
    axes[0].set_title('Interpolacja wielomianowa Lagrange\'a')
    axes[0].legend()
    axes[0].grid()
    
    # Wykres błędów
    for n, color in zip(n_values, ['g', 'b', 'orange']):
        x_points, y_points = generate_points(n, func)
        y_interpolated = [lagrange_interpolation(x, x_points, y_points) for x in x_plot]
        errors = calculate_errors(x_plot, y_exact, y_interpolated)
        axes[1].plot(x_plot, errors, label=f'Błąd dla n={n}', color=color)
    
    axes[1].set_xlabel('$x$')
    axes[1].set_ylabel('Błąd')
    axes[1].set_title('Błąd interpolacji wielomianowej Lagrange\'a')
    axes[1].legend()
    axes[1].grid()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    n_values = [5, 10, 15]  # Różne stopnie wielomianu interpolacyjnego
    test_functions = [
        (lambda x: 1 / (1 + 10 * x**2), '$y(x) = \, \, 1 / (1 + 10x^2)$'),
        (lambda x: np.abs(x), '$y(x) = \, \, |x|$')
    ]
    
    for func, label in test_functions:
        polynomial_comparison(n_values, func, label)
