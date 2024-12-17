import numpy as np
import matplotlib.pyplot as plt

# Define the first function f(x) = sin(x^3)
def f1(x):
    return np.sin(x**3)

# Define the first derivative for f1(x)
def f1_der(x):
    return 3 * x**2 * np.cos(x**3)

# Define the second function f(x) = cos(x^4)
def f2(x):
    return np.cos(x**4)

# Define the first derivative for f2(x)
def f2_der(x):
    return -4 * x**3 * np.sin(x**4)

# Define the central difference approximation
def Dhf_b(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

x = 0.2
e_32 = np.float32(1.19e-7)
e_64 = np.float64(2.22e-16)

h_32 = np.logspace(np.log10(e_32), 1, 400, dtype=np.float32)
h_64 = np.logspace(np.log10(e_64), 1, 400, dtype=np.float64)

# Analytical derivatives at x for both functions
f1_prime_x = f1_der(x)
f2_prime_x = f2_der(x)

# Compute the error |Dhf(x) - f'(x)| for f1(x) = sin(x^3)
error_f1_32 = np.abs(Dhf_b(f1, x, h_32) - f1_prime_x)
error_f1_64 = np.abs(Dhf_b(f1, x, h_64) - f1_prime_x)

# Compute the error |Dhf(x) - f'(x)| for f2(x) = cos(x^4)
error_f2_32 = np.abs(Dhf_b(f2, x, h_32) - f2_prime_x)
error_f2_64 = np.abs(Dhf_b(f2, x, h_64) - f2_prime_x)

# Plot the errors for both functions
plt.figure(figsize=(12, 6))

# Plot for f1(x) = sin(x^3)
plt.subplot(1, 2, 1)
plt.loglog(h_32, error_f1_32, label='float32', color='#CA8468')
plt.loglog(h_64, error_f1_64, label='float64', color='#0F8B8D')
plt.xlabel('h')
plt.ylabel('|Dhf(x) - f\'(x)|')
plt.title('Error for Formula '+ r'$D_{h}f(x) ≡ \frac{f(x+h)-f(x-h)}{2h}$' + '\n' + ' x = 0.2 ' + r' $f(x) = sin(x^3)$')
plt.legend()
plt.grid(True)

# Plot for f2(x) = cos(x^4)
plt.subplot(1, 2, 2)
plt.loglog(h_32, error_f2_32, label='float32', color='#CA8468')
plt.loglog(h_64, error_f2_64, label='float64', color='#0F8B8D')
plt.xlabel('h')
plt.ylabel('|Dhf(x) - f\'(x)|')
plt.title('Error for Formula '+ r'$D_{h}f(x) ≡ \frac{f(x+h)-f(x-h)}{2h}$' + '\n' + ' x = 0.2 ' + r' $f(x) = cos(x^4)$')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
