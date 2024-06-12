import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Data
# Reshape to make it a column vector
x = np.array([1, 2, 3, 4, 5, 6, 7]).reshape(-1, 1)
y = np.array([7, 23.5, 11, 17, 31, 20, 30])

# Create and fit the model
model = LinearRegression()
model.fit(x, y)

# Calculate predictions
predictions = model.predict(x)

# Print the linear equation
slope = model.coef_[0]
intercept = model.intercept_
print(f'Linear Equation: y = {slope:.2f}x + {intercept:.2f}')

# Plot data and best fit line
plt.scatter(x, y, label='Data')

# Plot best fit line
plt.plot(x, predictions, color='red', linestyle='--', label='Best Fit Line')

# Plot data points
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression with scikit-learn')
plt.legend()
plt.grid(True)

# Show plot
plt.show()
