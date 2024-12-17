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


def iterate(y_0):
    """
    Implementacja metody potęgowej do znajdowania największej wartości własnej macierzy.
    
    Parametry:
    - y_0: wektor początkowy (niezerowy, losowy)

    Zwraca:
    - iterations: lista wartości log10 normy różnicy kolejnych wektorów własnych (do analizy zbieżności)
    - y: lista zawierająca ostateczny wektor własny (y[0]) oraz największą wartość własną (y[1])
    """
    iterations = []
    diff = float(np.inf)
    y = [y_0/np.linalg.norm(y_0),np.linalg.norm(y_0)]
    i = 0
    while diff>epsilon and i<max_iter:
        z = np.dot(M, y[0])
        # Obliczenie normy (przybliżona wartość własna)
        new_norm = np.linalg.norm(z)
        # Obliczenie nowego wektora własnego (znormalizowanego)
        new_e = z / new_norm
        # Obliczenie różnicy między nowym a poprzednim wektorem własnym
        diff = np.linalg.norm(new_e - y[0])
        y = [new_e,new_norm]
        iterations.append(np.log10(diff) if diff > 0 else -np.inf)
        i+=1
    return iterations, y


def plot_power(iterations):
    """
    Wizualizacja zbieżności metody potęgowej.
    
    Parametry:
    - iterations: lista wartości log10 normy różnic kolejnych wektorów własnych
    """
    plt.plot(iterations, linestyle='dashed', label="Power Method Convergence")
    plt.xlabel("Iteration (k)")
    plt.ylabel("log10(|y_prev - y_next|)")
    plt.title("Power Method Convergence")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Losowy wektor początkowy
    y_0 = np.random.rand(4)
    # Uruchomienie metody potęgowej
    iter, result = iterate(y_0)
    # Wyświetlenie obliczonego wektora własnego
    print("e1 = ",result[0])
    print("||e1|| = ",np.linalg.norm(result[0]))
    # Wyświetlenie największej wartości własnej
    print("lambda1 = ",result[1])
    # Rysowanie wykresu zbieżności
    plot_power(iter)

