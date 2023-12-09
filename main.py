from bisection_method import bisection_method, plot_function

# Bisection method

# Example usage:
function_str = "x**3-4*x-9"
lower_boundary = 2
upper_boundary = 3
acceptable_error = 0.001



# Compute the root using bisection method
root = bisection_method(function_str, lower_boundary, upper_boundary, acceptable_error)

# Plot the function and the root
plot_function(function_str, lower_boundary, upper_boundary, root)

print(f"The root of the function is {root}")