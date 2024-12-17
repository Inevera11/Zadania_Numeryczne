import numpy as np

# Definicja macierzy A1 i wektora b
A1 = np.array([
    [5.8267103432, 1.0419816676, 0.4517861296, -0.2246976350, 0.7150286064],
    [1.0419816676, 5.8150823499, -0.8642832971, 0.6610711416, -0.3874139415],
    [0.4517861296, -0.8642832971, 1.5136472691, -0.8512078774, 0.6771688230],
    [-0.2246976350, 0.6610711416, -0.8512078774, 5.3014166511, 0.5228116055],
    [0.7150286064, -0.3874139415, 0.6771688230, 0.5228116055, 3.5431433879]
])

b = np.array([-2.8634904630, -4.8216733374, -4.2958468309, -0.0877703331, -2.0223464006])

# Rozwiązywanie A1 * y = b
y = np.linalg.solve(A1, b)

# Generowanie losowego zaburzenia ∆b o małej normie euklidesowej (około 1e-6)
np.random.seed(0)  # Seed dla reprodukowalności
delta_b = np.random.normal(scale=1e-6, size=b.shape)
b_perturbed = b + delta_b

# Rozwiązywanie A1 * y_tilde = b + ∆b
y_tilde = np.linalg.solve(A1, b_perturbed)

# Obliczenie wartości własnych macierzy
eigenvalues = np.linalg.eigvals(A1)

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
