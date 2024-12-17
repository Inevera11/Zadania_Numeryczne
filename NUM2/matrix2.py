import numpy as np

# Definicja macierzy A2 i wektora b
A2 = np.array([
    [5.4763986379 , 1.6846933459 , 0.3136661779 , -1.0597154562 , 0.0083249547],
    [1.6846933459 , 4.6359087874 ,-0.6108766748 ,2.1930659258 ,0.9091647433],
    [0.3136661779 ,-0.6108766748 ,1.4591897081 ,-1.1804364456 ,0.3985316185],
    [-1.0597154562 ,2.1930659258, -1.1804364456 ,3.3110327980 ,-1.1617171573],
    [0.0083249547, 0.9091647433 ,0.3985316185 ,-1.1617171573, 2.1174700695]
])


b = np.array([-2.8634904630, -4.8216733374, -4.2958468309, -0.0877703331, -2.0223464006])

# Rozwiązywanie A2 * y = b
y = np.linalg.solve(A2, b)

# Generowanie losowego zaburzenia ∆b o małej normie euklidesowej (około 1e-6)
np.random.seed(0)  # Seed dla reprodukowalności
delta_b = np.random.normal(scale=1e-6, size=b.shape)
b_perturbed = b + delta_b

# Rozwiązywanie A2 * y_tilde = b + ∆b
y_tilde = np.linalg.solve(A2, b_perturbed)

# Obliczenie wartości własnych macierzy
eigenvalues = np.linalg.eigvals(A2)

# Obliczenie współczynnika uwarunkowania κ
kappa = np.max(np.abs(eigenvalues)) / np.min(np.abs(eigenvalues))

# Obliczenie błędów względnych
relative_error_y = np.linalg.norm(y_tilde - y) / np.linalg.norm(y)
relative_error_b = np.linalg.norm(delta_b) / np.linalg.norm(b)

# Wyniki
print("b", b)
print("∆b", delta_b)
print("y", y)
print("y_tilde", y_tilde)
print("y - y_tilde", y-y_tilde)
print("Względny błąd wyniku (||y_tilde - y|| / ||y||):", relative_error_y)
print("Względny błąd zaburzenia wektora (||∆b|| / ||b||):", relative_error_b)
print("Współczynnik uwarunkowania κ:", kappa)

