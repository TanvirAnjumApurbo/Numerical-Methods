import numpy as np

# Define the function


def f(x):
    return 8 + 4 * np.cos(x)

# Trapezoidal Rule


def trapezoidal_rule(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2

# Simpson's 1/3 Rule


def simpson_1_3_rule(f, a, b):
    x0 = a
    x1 = (a + b) / 2
    x2 = b
    return (b - a) * (f(x0) + 4 * f(x1) + f(x2)) / 6

# Simpson's 3/8 Rule


def simpson_3_8_rule(f, a, b):
    x0 = a
    x1 = a + (b - a) / 3
    x2 = a + 2 * (b - a) / 3
    x3 = b
    return (b - a) * (f(x0) + 3 * f(x1) + 3 * f(x2) + f(x3)) / 8


# Integration limits
a = 0
b = np.pi / 2

# Calculate the integrals using the three methods
integral_trapezoidal = trapezoidal_rule(f, a, b)
integral_simpson_1_3 = simpson_1_3_rule(f, a, b)
integral_simpson_3_8 = simpson_3_8_rule(f, a, b)

# Print the results
print(f"Trapezoidal Rule: {integral_trapezoidal}")
print(f"Simpson's 1/3 Rule: {integral_simpson_1_3}")
print(f"Simpson's 3/8 Rule: {integral_simpson_3_8}")
