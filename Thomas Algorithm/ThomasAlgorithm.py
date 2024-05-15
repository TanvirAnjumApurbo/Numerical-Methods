import numpy as np


def thomas_algorithm(n, e, f, g, constant):
    """
    Thomas algorithm for solving a tridiagonal matrix equation.

    Parameters:
        n (int): Size of the matrix.
        e (array): Lower diagonal elements (length n-1).
        f (array): Diagonal elements (length n).
        g (array): Upper diagonal elements (length n-1).
        constant (array): Constants on the right-hand side (length n).

    Returns:
        x (array): Solution of the tridiagonal system.
    """
    # Forward elimination
    for i in range(1, n):
        factor = e[i-1] / f[i-1]
        f[i] -= factor * g[i-1]
        constant[i] -= factor * constant[i-1]

    # Backward substitution
    x = np.zeros(n)
    x[-1] = constant[-1] / f[-1]
    for i in range(n-2, -1, -1):
        x[i] = (constant[i] - g[i] * x[i+1]) / f[i]

    return x


# Example usage
n = int(input("Enter the size of the matrix: "))
e = np.array([float(input("Enter element e{}: ".format(i+2)))
             for i in range(n-1)])
f = np.array([float(input("Enter element f{}: ".format(i+1)))
             for i in range(n)])
g = np.array([float(input("Enter element g{}: ".format(i+1)))
             for i in range(n-1)])
constant = np.array(
    [float(input("Enter constant {}: ".format(i+1))) for i in range(n)])

solution = thomas_algorithm(n, e, f, g, constant)
print("Solution:", solution)
