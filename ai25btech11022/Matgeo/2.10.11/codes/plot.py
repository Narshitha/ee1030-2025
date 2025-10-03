import numpy as np
import matplotlib.pyplot as plt

# Define vectors
u = np.array([1, 1, 2])
v = np.array([1, 2, 1])
B = np.array([1, 1, 1])
A = np.array([0, 1/np.sqrt(2), -1/np.sqrt(2)])

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to plot a vector from origin
def plot_vector(ax, vec, color, label):
    ax.quiver(0, 0, 0, vec[0], vec[1], vec[2],
              color=color, arrow_length_ratio=0.1, linewidth=2, label=label)

# Plot vectors
plot_vector(ax, u, 'blue', 'u = (1,1,2)')
plot_vector(ax, v, 'green', 'v = (1,2,1)')
plot_vector(ax, B, 'orange', 'B = (1,1,1)')
plot_vector(ax, A, 'red', 'Unit vector A')

# Generate a mesh grid for the plane spanned by u and v
s = np.linspace(-1.5, 1.5, 10)
t = np.linspace(-1.5, 1.5, 10)
S, T = np.meshgrid(s, t)

# Parametric equation of the plane: P = s*u + t*v
X = S*u[0] + T*v[0]
Y = S*u[1] + T*v[1]
Z = S*u[2] + T*v[2]

# Plot the plane with transparency
ax.plot_surface(X, Y, Z, alpha=0.3, color='cyan')

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Vectors and Plane spanned by u and v")
ax.legend()

# Equal aspect ratio
max_val = np.max(np.abs([u, v, B, A]))
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])

plt.show()

