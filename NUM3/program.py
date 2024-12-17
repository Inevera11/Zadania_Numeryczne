import numpy as np
import time
import matplotlib.pyplot as plt

def create_matrix_H(N):
    H = np.zeros((4, N))
    for i in range(N):
        if i > 1:
            H[0, i - 2] = 0.15 / ((i - 1) ** 3)
        if i > 0:
            H[1, i - 1] = 0.2 / i
        H[2, i] = 1.01
        if i < N - 1:
            H[3, i + 1] = 0.3
    return H

def lu_decomposition(H, N):

    for i in range(1, N):
        # li+1,i
        H[3,i] = H[3, i] / H[2, i - 1]
        # uii
        H[2, i] = H[2, i] - H[3,i] * H[1, i - 1]
        # ui,i+1
        if i < N - 1:
            H[1, i] = H[1, i] - H[3,i]*H[0,i-1]

def solve_LU(H, N):
    # Step 1: LU decomposition
    lu_decomposition(H, N)
    
    # Step 2: Solve Lz = x (forward substitution)
    x = np.arange(1, N + 1)
    z = np.zeros(N)
    z[0] = x[0]
    for i in range(1, N):
        z[i] = x[i] - H[3,i] * z[i - 1]
    
    # Step 3: Solve Uy = z (backward substitution)
    y = np.zeros(N)
    y[N-1] = z[N-1] / H[2, N-1]
    y[N - 2] = (z[N - 2] - H[1,N-2]*y[N-1]) / H[2, N-2]
    for i in range(N - 3, -1, -1):
        y[i] = (z[i] - H[0,i]*y[i+2] - H[1,i]*y[i+1]) / H[2, i]
    return y

# calculate det(A)
def calculate_determinant(H):
    det = np.prod(H[2, :])
    print("Determinant of A:", det)
    return det

def solve_for_300():
    N = 300
    H = create_matrix_H(N)
    lu_decomposition(H, N)
    y = solve_LU(H, N)
    print("y vector for N = 300:", y)
    calculate_determinant(H)

solve_for_300()

def measure_time(N_values):
    times = []
    for N in N_values:
        H = create_matrix_H(N)
        
        start_time = time.time()
        solve_LU(H, N)
        end_time = time.time()

        times.append(end_time - start_time)
    
    return times

N_values = np.arange(100, 801, 100)
times = measure_time(N_values)

# Wykres zależności czasu działania od rozmiaru N
plt.plot(N_values, times, label="Czas działania")
plt.xlabel("N")
plt.ylabel("Czas [s]")
plt.title("Zależność czasu działania od rozmiaru N")
plt.legend()
plt.grid(True)
plt.show()

