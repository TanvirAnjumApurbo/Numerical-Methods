import numpy as np
import matplotlib.pyplot as plt


def linear_interpolation(x_values, f, x_new):
    # Evaluate f(x) for given x values
    y_values = f(x_values)

    # Perform linear interpolation
    y_new = np.interp(x_new, x_values, y_values)

    # Plot the data points
    plt.plot(x_values, y_values, 'o', label='Original data')

    # Plot the interpolated point
    plt.plot(x_new, y_new, 'rx', label='Interpolated point')

    # Connect the dots for the linear interpolation line
    plt.plot([x_values[0], x_new, x_values[1]], [y_values[0],
             y_new, y_values[1]], 'r--', label='Interpolation line')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.title('Linear Interpolation')
    plt.grid(True)
    plt.show()

    return y_new


# Example usage:
x_values = np.array([0.5, 1.0])
f = np.sin  # function
x_new = 0.632

y_new = linear_interpolation(x_values, f, x_new)
print(f'Interpolated value at x = {x_new}: {y_new}')
