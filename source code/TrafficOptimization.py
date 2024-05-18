import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Coefficients for the objective function
c = [1, 1, 1]  # Minimizing the total duration of green lights Z = x1 + x2 + x3

# Inequality constraints matrix (A_ub)
A_ub = [
    [1, 0, 0],  # Constraint for x1
    [0, 1, 0],  # Constraint for x2
    [0, 0, 1],  # Constraint for x3
    [-1, 0, 0], # Lower bound for x1
    [0, -1, 0], # Lower bound for x2
    [0, 0, -1]  # Lower bound for x3
]

b_ub = [60, 50, 40, -30, -25, -20]

# Bounds for each variable
x_bounds = [(30, 60), (25, 50), (20, 40)]

# Initial values set away from the lower bounds
initial_x = [50, 40, 35]  # Mid-upper range of the bounds

# Use linprog to find the optimal solution
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=x_bounds, method='highs')

# Display the results
print("Initial durations:", initial_x)
print("Optimal durations:", result.x)
print("Minimum total waiting time (objective function value):", result.fun)

# Visualization
indices = np.arange(3)
bar_width = 0.35

plt.figure(figsize=(10, 5))
plt.bar(indices, initial_x, bar_width, label='Before Optimization', color='red')
plt.bar(indices + bar_width, result.x, bar_width, label='After Optimization', color='green')
plt.xlabel('Intersections')
plt.ylabel('Green Light Duration (seconds)')
plt.title('Comparison of Green Light Durations: Before vs After Optimization')
plt.xticks(indices + bar_width / 2, ['Intersection A', 'Intersection B', 'Intersection C'])
plt.legend()
plt.show()
