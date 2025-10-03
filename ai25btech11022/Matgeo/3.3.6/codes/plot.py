import numpy as np
import matplotlib.pyplot as plt

# Given data
B = np.array([0, 0])                # Point B at origin
C = np.array([6, 0])                # Point C at (6,0)
A = np.array([6*(np.sqrt(3)-1), 6*(np.sqrt(3)-1)])  # From LaTeX solution

# Create the triangle
triangle = np.array([A, B, C, A])  # close the triangle

# Plotting
plt.figure(figsize=(6,6))
plt.plot(triangle[:,0], triangle[:,1], 'b-', linewidth=2)
plt.fill(triangle[:,0], triangle[:,1], 'skyblue', alpha=0.3)

# Mark points
plt.scatter(*A, color='red', label='A')
plt.scatter(*B, color='green', label='B')
plt.scatter(*C, color='blue', label='C')

# Annotate points
plt.text(A[0]+0.2, A[1]+0.2, 'A', fontsize=12, color='red')
plt.text(B[0]-0.4, B[1]-0.4, 'B', fontsize=12, color='green')
plt.text(C[0]+0.2, C[1]-0.4, 'C', fontsize=12, color='blue')

# Axes settings
plt.gca().set_aspect('equal', adjustable='box')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle="--", alpha=0.5)
plt.title("Triangle ABC with BC=6, ∠B=45°, ∠A=105°")

plt.legend()
plt.show()
