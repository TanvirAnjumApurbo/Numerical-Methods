import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Given data
x_data = np.array([0, 1, 2, 3, 4, 5]).reshape(-1, 1)
y_data = np.array([2.1, 7.7, 13.6, 27.2, 40.9, 61.1])

# Define the degree of the polynomial
degree = 2

# Generate polynomial features
poly_features = PolynomialFeatures(degree=degree)
x_poly = poly_features.fit_transform(x_data)

# Perform linear regression
model = LinearRegression()
model.fit(x_poly, y_data)

# Get the coefficients
a = model.coef_[2]
b = model.coef_[1]
c = model.intercept_

# Generate y values from the fitted polynomial
y_fit = model.predict(x_poly)

# Calculate R-squared (coefficient of determination)
ss_res = np.sum((y_data - y_fit)**2)
ss_tot = np.sum((y_data - np.mean(y_data))**2)
r_squared = 1 - (ss_res / ss_tot)

# Calculate standard error
n = len(y_data)
m = degree
std_err = np.sqrt(ss_res / (n - (m + 1)))

# Print the coefficients, R-squared, and standard error
print("Coefficients:", a, b, c)
print("Coefficient of determination (R-squared):", r_squared)
print("Standard error (S_y/x):", std_err)

# Plot the original data and the fitted curve
plt.scatter(x_data, y_data, label='Original data')
plt.plot(x_data, y_fit, color='red', label='Fitted curve')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Polynomial Curve Fitting with scikit-learn')
plt.legend()
plt.show()
