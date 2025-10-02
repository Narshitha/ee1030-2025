import matplotlib.pyplot as plt
import numpy as np

# Define the three points
points = np.array([[-2,-3], [3, 2], [-1, 8]])

# Extract x and y coordinates
x = points[:, 0]
y = points[:, 1]

# Plot the points
plt.plot(x, y, 'ro')

# Annotate the points
for i, (xi, yi) in enumerate(points):
    plt.text(xi + 0.1, yi, f'({xi},{yi})')

# Draw the triangle by connecting points and closing the loop
triangle = plt.Polygon(points, closed=True, fill=True, color='cyan', alpha=0.3)
plt.gca().add_patch(triangle)

# Set limits
plt.xlim(min(x)-1, max(x)+1)
plt.ylim(min(y)-1, max(y)+1)

# Title and labels
plt.title('Triangle formed by points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
