import matplotlib.pyplot as plt
import numpy as np

def bisection_method(func, lower_boundary, upper_boundary, error_accept):
    """
    Bisection method for finding the root of a function.

    Args:
        func (str): The mathematical function in the form of a string, e.g., "x**2 - 4".
        lower_boundary (float): The lower boundary of the interval.
        upper_boundary (float): The upper boundary of the interval.
        error_accept (float): The acceptable error for the result.

    Returns:
        float: The approximate root of the function within the specified error.

    Raises:
        ValueError: If the interval is not valid for the bisection method.
    """
    def f(x):
        return eval(func, {'x': x})

    if f(lower_boundary) * f(upper_boundary) >= 0:
        raise ValueError("No root or multiple roots exist in the given interval; the bisection method cannot be applied.")

    error = abs(upper_boundary - lower_boundary)
    iterations = 0

    while error >= error_accept:
        iterations += 1
        c = (lower_boundary + upper_boundary) / 2

        if f(c) == 0:
            print(f"Found an exact root: {c}")
            return c
        elif f(c) * f(lower_boundary) < 0:
            upper_boundary = c
        elif f(c) * f(upper_boundary) < 0:
            lower_boundary = c
        else:
            raise ValueError("Something went wrong in the bisection method.")

        error = abs(upper_boundary - lower_boundary)

        print(f"Iteration {iterations}: Lower boundary = {lower_boundary}, Upper boundary = {upper_boundary}")

    print(f"The error is {error}")
    print(f"The final lower boundary is {lower_boundary} and the final upper boundary is {upper_boundary}")
    return (lower_boundary + upper_boundary) / 2

# To plot the function 

def plot_function(func, lower_bound, upper_bound, root, num_points=100):
    """
    Plot the given function within the specified range.

    Args:
        func (str): The mathematical function in the form of a string, e.g., "x**2 - 4".
        lower_bound (float): The lower boundary of the plot range.
        upper_bound (float): The upper boundary of the plot range.
        root (float): The computed root of the function.
        num_points (int): The number of points for the plot (default is 100).
    """
    f = lambda x: eval(func, {'x': x})

    x_values = np.linspace(lower_bound, upper_bound, num_points)
    y_values = [f(x) for x in x_values]

    plt.plot(x_values, y_values, label=f'Function: {func}')
    plt.axhline(0, color='black', linestyle='--', linewidth=1)  # Horizontal line at y=0
    plt.axvline(0, color='black', linestyle='--', linewidth=1)  # Vertical line at x=0
    plt.axvline(lower_bound, color='red', linestyle='--', linewidth=1, label='Boundary')  # Line for lower bound
    plt.axvline(upper_bound, color='red', linestyle='--', linewidth=1)  # Line for upper bound
    plt.scatter([root], [0], color='blue', label='Root', marker='o')  # Highlight root
 
    plt.title(f'Plot of the Function: {func}')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()

