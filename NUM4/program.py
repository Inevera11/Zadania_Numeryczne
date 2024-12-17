import numpy as np
import matplotlib.pyplot as plt
import time

def create_A_and_b(N):
    """Generates the matrix A and vector b for given N."""
    A1 = np.zeros((N, 2))
    for i in range(N):
        A1[i, 0] = 4
        A1[i,1] = 2

    u = np.ones((N, 1))
    v = np.ones((N, 1))
    b = np.full((N, 1), 2)

    return A1, u, v, b

def create_A(N):
    """Generates the matrix A and vector b for given N."""
    A = np.ones((N, N))
    for i in range(N):
        A[i,i] = 5
        if(i == N-1):
            break
        A[i,i+1] = 3

    return A

def backsubstitution(A1, b):
    """Solves Ax = b using back substitution formula."""
    size = len(b)
    x = np.zeros((size, 1))
    for i in range(size-1,-1,-1):
        if(i == size-1):
            x[i] = b[i]/A1[i][0]
        else:
            x[i] = (b[i] - A1[i][1]*x[i+1])/A1[i][0]
    return x



def solve_using_sherman_morrison(A1, u, v, b):
    """Solves Ay = b using the Sherman-Morrison formula."""
    
    # Step 2: Solve A1 z = b
    z = backsubstitution(A1, b)
    
    # Step 3: Solve A1 q = u
    q = backsubstitution(A1, u)
    
    # Step 4: Compute v^T z and v^T q
    vT_z = np.dot(v.T, z)
    vT_q = np.dot(v.T, q)
    
    # Step 5: Compute the result using the Sherman-Morrison formula
    denominator = 1 + vT_q
    y = z - (vT_z / denominator) * q

    return y.flatten()

def measure_execution_time_comparison():
    """Measures execution time for both Sherman-Morrison and numpy.linalg.solve methods."""
    N_values = [i for i in range(10,1001,20)]
    times_sherman = []
    times_library = []

    for N in N_values:
        A1, u, v, b = create_A_and_b(N)
        A = create_A(N)  # Full matrix A for numpy.linalg.solve

        # Measure time for Sherman-Morrison
        start_time = time.time()
        _ = solve_using_sherman_morrison(A1,u, v, b)
        times_sherman.append(time.time() - start_time)

        # Measure time for numpy.linalg.solve
        start_time = time.time()
        _ = np.linalg.solve(A, b)
        times_library.append(time.time() - start_time)

    return N_values, times_sherman, times_library

def plot_execution_time_comparison(N_values, times_sherman, times_library):
    """Plots execution time for both methods as a function of N."""
    plt.figure(figsize=(10, 6))
    plt.plot(N_values, times_sherman, marker='o', linestyle='-', color='b', label='Sherman-Morrison')
    plt.plot(N_values, times_library, marker='s', linestyle='--', color='r', label='numpy.linalg.solve')
    plt.xlabel('Matrix Size N')
    plt.ylabel('Time (seconds)')
    plt.title('Execution Time Comparison: Sherman-Morrison vs numpy.linalg.solve')
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Solve for N = 120 and verify solution
    N = 120
    A1, u, v, b = create_A_and_b(N)
    y = solve_using_sherman_morrison(A1,u, v, b)

    # Verify solution using library function
    A = create_A(N)
    y_lib = np.linalg.solve(A, b).flatten()

    print("Solution computed using Sherman-Morrison formula:")
    print(y)

    print("\nSolution computed using numpy.linalg.solve:")
    print(y_lib)

    # Compare solutions
    print("\nMaximum difference between solutions:", np.max(np.abs(y - y_lib)))

    #Measure execution time for both methods
    N_values, times_sherman, times_library = measure_execution_time_comparison()
    plot_execution_time_comparison(N_values, times_sherman, times_library)