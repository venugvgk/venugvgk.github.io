import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

fig, ax = plt.subplots()

sides = 6
outer_radius = 20
layers = 6

# Create 5 nested polygons with decreasing radius
for i in range(layers):
    r = outer_radius * (layers - i) / layers
    theta = 2 * np.pi / sides
    vertices = []

    for j in range(sides):
        angle = j * theta
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        vertices.append((x, y))

    polygon = Polygon(vertices, closed=True, facecolor='none', edgecolor='black', linewidth=1.5)
    ax.add_patch(polygon)

# Set the figure area square
ax.set_aspect(1)

# Set axes limits
ax.set_xlim(-outer_radius, outer_radius)
ax.set_ylim(-outer_radius, outer_radius)

# Hide axes labels
ax.set_xticks([])
ax.set_yticks([])

# Remove the border
for spine in ax.spines.values():
    spine.set_visible(False)

plt.show()

