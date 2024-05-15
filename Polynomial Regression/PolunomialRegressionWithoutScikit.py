import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given data
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([2.1, 7.7, 13.6, 27.2, 40.9, 61.1])

# Define the function for the polynomial fit


def polynomial_func(x, a, b, c):
    return a * x**2 + b * x + c


# Perform the curve fitting
popt, pcov = curve_fit(polynomial_func, x_data, y_data)

# Get the coefficients
a, b, c = popt

# Generate y values from the fitted polynomial
y_fit = polynomial_func(x_data, *popt)

# Calculate R-squared (coefficient of determination)
residuals = y_data - y_fit
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y_data - np.mean(y_data))**2)
r_squared = 1 - (ss_res / ss_tot)

# Calculate standard error
n = len(y_data)
m = len(popt) - 1
std_err = np.sqrt(ss_res / (n - (m+1)))

# Print the coefficients, R-squared, and standard error
print("Coefficients:", a, b, c)
print("Coefficient of determination (R-squared):", r_squared)
print("Standard error (S_y/x):", std_err)

# Plot the original data and the fitted curve
plt.scatter(x_data, y_data, label='Original data')
plt.plot(x_data, y_fit, color='red', label='Fitted curve')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Curve Fitting without scikit-learn')
plt.legend()
plt.show()
