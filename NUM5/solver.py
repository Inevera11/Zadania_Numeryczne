import numpy as np
import matplotlib.pyplot as plt

SIZE = 200

x_0 =  np.ones(SIZE)
k = 100


# Example value for d
d1 = 10  
d2 = 4
d3 = 1.3
d4 = 1

def create_A_and_b(d):
    """Generates the matrix A and vector b for given d."""
    A = np.zeros((5,SIZE))
    for i in range(SIZE):
        if(i<SIZE-2):
            A[0,i] = 0.1 # aii+2
        if(i<SIZE-1):
            A[1,i] = 0.5 # aii+1
        A[2,i] = d # aii
        if(i>0):
            A[3,i] = 0.5 #ai,i-1
        if(i>1):
            A[4,i] = 0.1 #ai,i-2

    b = np.array([x for x in range(1,SIZE+1)])

    return A, b

def get_next_x_jacob(prev_x, A, b):
    next_x = np.zeros(SIZE)
    for i in range(SIZE):
        others = 0
        others += A[0,i] * prev_x[i+2] if i < SIZE-2  else 0
        others += A[1,i] * prev_x[i+1] if i < SIZE-1 else 0
        others += A[3,i] * prev_x[i-1] if i > 0  else 0
        others += A[4,i] * prev_x[i-2] if i > 1 else 0

        next_x[i] = (b[i] - others)/A[2,i]
    return next_x

def get_next_x_gauss(prev_x, A, b):
    next_x = np.zeros(SIZE)
    for i in range(SIZE):
        others = 0
        others += A[0,i] * prev_x[i+2] if i < SIZE-2 else 0
        others += A[1,i] * prev_x[i+1] if i < SIZE-1  else 0
        others += A[3,i] * next_x[i-1] if i > 0 else 0
        others += A[4,i] * next_x[i-2] if i > 1 else 0
        next_x[i] = (b[i] - others)/A[2,i]
    return next_x


def generate_jacob_differences(d):
    A, b = create_A_and_b(d)
    
    # Initial guess for x_0
    x_prev = x_0

    # List to store the log of differences for plotting
    log_differences = []

    # Run the iteration
    for _ in range(k):  # Number of iterations
        x_next = get_next_x_jacob(x_prev, A, b)
        
        # Calculate the absolute difference
        diff = np.abs(x_next - x_prev)
        
        # Take the log10 of the maximum difference
        log_diff = np.log10(np.max(diff)) if np.max(diff) > 0 else -np.inf
        log_differences.append(log_diff)
        
        # Update x_prev for the next iteration
        x_prev = x_next

    return [log_differences,x_prev]

def generate_gauss_differences(d):
    A, b = create_A_and_b(d)
    
    # Initial guess for x_0
    x_prev = x_0

    # List to store the log of differences for plotting
    log_differences = []

    # Run the iteration
    for _ in range(k):  # Number of iterations
        x_next = get_next_x_gauss(x_prev, A, b)
        
        # Calculate the absolute difference
        diff = np.abs(x_next - x_prev)
        
        # Take the log10 of the maximum difference
        log_diff = np.log10(np.max(diff)) if np.max(diff) > 0 else -np.inf
        log_differences.append(log_diff)
        
        # Update x_prev for the next iteration
        x_prev = x_next

    return [log_differences,x_prev]

def plot_jacobi():
    # Plotting the convergence (log10 of |x_prev - x_next|)
    plt.plot(generate_jacob_differences(d1)[0], linestyle='dashed', label=f'd = {d1}' )
    plt.plot(generate_jacob_differences(d2)[0], linestyle='dashed', label=f'd = {d2}' )
    plt.plot(generate_jacob_differences(d3)[0], linestyle='dashed', label=f'd = {d3}' )
    plt.plot(generate_jacob_differences(d4)[0], linestyle='dashed', label=f'd = {d4}' )
    plt.xlabel("Iteration (k)")
    plt.ylabel("log10(|x_prev - x_next|)")
    plt.title("Jacobi's method")
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_gauss():
    # Plotting the convergence (log10 of |x_prev - x_next|)
    plt.plot(generate_gauss_differences(d1)[0], linestyle='dashed', label=f'd = {d1}' )
    plt.plot(generate_gauss_differences(d2)[0], linestyle='dashed', label=f'd = {d2}' )
    plt.plot(generate_gauss_differences(d3)[0], linestyle='dashed', label=f'd = {d3}' )
    plt.plot(generate_gauss_differences(d4)[0], linestyle='dashed', label=f'd = {d4}' )
    plt.xlabel("Iteration (k)")
    plt.ylabel("log10(|x_prev - x_next|)")
    plt.title("Gauss-Seidels's method")
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_gauss_vs_seidel():
    # Plotting the convergence (log10 of |x_prev - x_next|)
    plt.plot(generate_gauss_differences(d1)[0], linestyle='dashed', label=f'gauss-seidel, d = {d1}' )
    plt.plot(generate_jacob_differences(d1)[0], linestyle='dashed', label=f'jacobi, d = {d1}' )
    plt.plot(generate_gauss_differences(d3)[0], linestyle='dashed', label=f'gauss-seidel, d = {d3}' )
    plt.plot(generate_jacob_differences(d3)[0], linestyle='dashed', label=f'jacobi, d = {d3}' )
    plt.plot(generate_gauss_differences(d4)[0], linestyle='dashed', label=f'gauss-seidel, d = {d4}' )
    plt.plot(generate_jacob_differences(d4)[0], linestyle='dashed', label=f'jacobi, d = {d4}' )
    plt.xlabel("Iteration (k)")
    plt.ylabel("log10(|x_prev - x_next|)")
    plt.title("Jacobi's method vs Gauss-Seidels's method")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    jacobi_solution = generate_jacob_differences(d1)[1]
    gauss_solution = generate_gauss_differences(d1)[1]
    print("x as jacobi_solution: ")
    print(jacobi_solution)
    print("x as gauss_solution:")
    print(gauss_solution)
    print("diff:")
    print(jacobi_solution-gauss_solution)
    plot_jacobi()
    plot_gauss()
    plot_gauss_vs_seidel()



