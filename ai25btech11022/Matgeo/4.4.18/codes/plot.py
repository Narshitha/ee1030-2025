import numpy as np
import matplotlib.pyplot as plt

# Given points
B = np.array([3, 6])
C = np.array([-3, 4])

# Equation of line: x - 3y + 15 = 0 -> y = (x + 15)/3
x_vals = np.linspace(-10, 10, 400)
y_vals = (x_vals + 15) / 3

# Plot the line
plt.plot(x_vals, y_vals, label=r"$x - 3y + 15 = 0$", color='blue')

# Plot given points
plt.scatter(B[0], B[1], color='red', label='B(3,6)')
plt.scatter(C[0], C[1], color='green', label='C(-3,4)')

# Optional: Choose A on the line to verify collinearity
A_x = 0
A_y = (A_x + 15) / 3
plt.scatter(A_x, A_y, color='purple', label=f'A({A_x},{A_y})')

# Formatting
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Collinearity of A, B, and C')
plt.legend()
plt.grid(True)
plt.show()

