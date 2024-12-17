import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = cos(x^4)
def f(x):
    return np.cos(x**4)

# Define the first derivative of f(x)
def f_der(x):
    return -4 * x**3 * np.sin(x**4)

# Define the second derivative of f(x)
def f_double_der(x):
    return -16 * x**6 * np.cos(x**4) - 12 * x**2 * np.sin(x**4)

# Compute the derivative using formula (a)
def Dhf_a(f, x, h):
    return (f(x + h) - f(x)) / h

x = 0.2
e_32 = np.float32(1.19e-7)
e_64 = np.float64(2.22e-16)

# Compute the absolute f(x) and f''(x) at the point x
abs_fx = np.abs(f(x))
abs_f_double_prime_x = np.abs(f_double_der(x))

# Compute h using the given formula for float32 and float64
h_opt_32 = 2 * np.sqrt((abs_fx * e_32) / abs_f_double_prime_x)
h_opt_64 = 2 * np.sqrt((abs_fx * e_64) / abs_f_double_prime_x)

h_32 = np.logspace(np.log10(e_32), 1, 400, dtype=np.float32)
h_64 = np.logspace(np.log10(e_64), 1, 400, dtype=np.float64)

# Compute the analytical derivative at x
f_prime_x = f_der(x)

# Compute the error |Dhf(x) - f'(x)| for both formulas and types
error_a_32 = np.abs(Dhf_a(f, x, h_32) - f_prime_x)
error_a_64 = np.abs(Dhf_a(f, x, h_64) - f_prime_x)

# Plot the error for formula a
plt.figure(figsize=(10, 6))

# Plot for formula (a)
plt.subplot(1, 2, 1)
plt.loglog(h_32, error_a_32, label='float32', color='#CA8468')
plt.loglog(h_64, error_a_64, label='float64', color='#0F8B8D')
# Mark the point where h = sqrt(e) for float32
plt.scatter(h_opt_32, np.abs(Dhf_a(f, x, h_opt_32) - f_prime_x), color='#79412A', s=100, marker='o', label=r'$h \approx 2\sqrt{\frac{|f(x)| \cdot e_{32}}{|f''(x)|}}$ = '+ f'{h_opt_32:.1e}' , zorder=5)

# Mark the point where h = sqrt(e) for float64
plt.scatter(h_opt_64, np.abs(Dhf_a(f, x, h_opt_64) - f_prime_x), color='#143642', s=100, marker='o', label=r'$h \approx 2\sqrt{\frac{|f(x)| \cdot e_{64}}{|f''(x)|}}$ = '+ f'{h_opt_64:.1e}', zorder=5)

plt.xlabel('h')
plt.ylabel('|Dhf(x) - f\'(x)|')
plt.title('Error for Formula '+ r'$D_{h}f(x) ≡ \frac{f(x+h)-f(x)}{h}$' + '\n' + ' x = 0.2 ' + r' $f(x) = cos(x^4)$')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
