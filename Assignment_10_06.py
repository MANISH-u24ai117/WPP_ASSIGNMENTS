import numpy as np
import matplotlib.pyplot as plt

# Define the polynomial function f(x)
def f(x):
    return x**3 - x - 2  # Example: f(x) = x^3 - x - 2

# Bisection method implementation
def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    updates = []  # List to store updates during the process
    if f(a) * f(b) > 0:
        print("The function must have opposite signs at the endpoints a and b.")
        return None, updates

    for i in range(max_iter):
        c = (a + b) / 2  # Midpoint
        updates.append(c)  # Store the midpoint

        if f(c) == 0 or (b - a) / 2 < tol:
            return c, updates  # Found root or tolerance satisfied

        if f(c) * f(a) < 0:
            b = c  # Narrow the interval to the left
        else:
            a = c  # Narrow the interval to the right

    return (a + b) / 2, updates  # Return the midpoint after max iterations

# Random initial interval (a, b)
np.random.seed(0)  # For reproducibility
a = np.random.uniform(-10, -1)
b = np.random.uniform(1, 10)

# Apply bisection method
root, updates = bisection_method(f, a, b)

# Convert updates to a numpy array for plotting
updates = np.array(updates)

# Plotting the root-finding process
x_vals = np.linspace(a, b, 400)
y_vals = f(x_vals)
plt.plot(x_vals, y_vals, label="f(x)")
plt.axhline(0, color='black',linewidth=0.7)  # x-axis
plt.axvline(root, color='red', linestyle='--', label="Root")
plt.scatter(updates, f(updates), color='orange', zorder=5, label="Midpoints")
plt.title('Bisection Method Root Finding Process')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()